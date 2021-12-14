# rightbound

The project is based on python with the Django framework as I found it easier to implement this way and I believe it can show the way of thinking relatively easily. 


prerequisites:

 * Python3.8
 * Pipenv

Installation:

```
git clone git@github.com:NotSoShaby/rightbound.git 
cd rightbound
pipenv install
```

Activate virtual environment:

```
pipenv shell
```

Create local db:

```
python manage.py migrate
```

Create a superuser (follow the steps after the command):

```
python manage.py createsuperuser
```

Run the server:

```
python manage.py runserver
```

Access the admin console at `http://localhost:8000/admin/` and log in using the superuser you have created to look at the db in the UI (optional -not much to see).


Key things to explore in the project:
  * `main/views.py` loook at the `run` function. 
  * `run_event` function which is located in the `events/models.py` file and is a hook that is being runned after saving an event instance
  * All the models and db structure
