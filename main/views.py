from events.models import Event

input_example = [
    {
        'campagin_id': 'campaign_id1',
        'type': 'CLICK',
        'channel': 'LinkedInChannel',
        'action': 'connect',
        'prospects': [
            'prospect_id1',
            'prospect_id2'
        ]
    },
    {
        'campaign': 'campaign_id1',
        'type': 'OPEN',
        'rule': 'count()>2',
        'channel': 'EmailChannel',
        'action': 'cold_email',
        'prospects': ['prospect_id1']
    }
]


def run(request):
    for e in input_example:
        event = Event(owner=request.user.id)
        for k, v in e.items():
            if hasattr(event, k):
                setattr(event, k, v)
        event.save()
