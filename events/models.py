from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

from channels.views import LinkedInChannel, EmailChanel
from main.models import Prospect, Campaign


# TODO - find a more elegant solution for the channel types
channel_types = {
    'EmailChanel': EmailChanel,
    'LinkedInChannel': LinkedInChannel
}


class EventStatus(models.IntegerChoices):
    FAILED = 0
    SUCCESS = 1
    PRE_RUN = 2
    PROCESSING = 3


class EventType(models.TextChoices):
    CLICK = 'CLICK'
    OPEN = 'OPEN'


class Event(models.Model):

    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    status = models.IntegerField(choices=EventStatus.choices, default=EventStatus.PRE_RUN)
    """
    in theory campaign and channel should be set to null=False, 
    but this creates more issues than solving them a lot of the times 
    """
    campaign = models.ForeignKey(Campaign, null=True, on_delete=models.SET_NULL)
    channel = models.CharField(max_length=20, choices=tuple(channel_types.items()))
    """
    TODO - Currently and as in the requirements sheet, the rule will be executed using eval() to the string.
     this is very unsafe and should be changed in the design 
    """
    rule = models.JSONField()
    execution_time = models.DateTimeField(default=now, editable=True)
    next_event = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    """
    TODO - change action to be a choice field that updates based on the function names that the different channels
    hold
    """
    action = models.CharField(max_length=10)
    # params should include content template
    params = models.JSONField()
    prospects = models.ManyToManyField(Prospect, related_name='events')
    type = models.CharField(max_length=10, choices=EventType.choices)


@receiver(post_save, sender=Event, dispatch_uid="run_event_on_insert")
def run_event(sender, instance, **kwargs):
    instance.status = EventStatus.PROCESSING
    instance.save()
    channel_cls = channel_types[instance.channel]
    # TODO - remove eval in the code - very dangerous and a horrible practice
    if eval(instance.rule):
        channel_cls.execute_all(instance)
    instance.status = EventStatus.SUCCESS
    instance.save()
