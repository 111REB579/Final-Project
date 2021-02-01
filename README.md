## Uzstādīšana un iestatīšana

Virtuālās vides izveide/aktivizēšana. Visu nepieciešamo pakešu uzstādīšana.
```python
virtualenv .virtual
source .virtual/bin/activate
sudo apt install python3-django
sudo pip install djangorestframework
sudo pip install djangorestframework-simplejw
```

Django palaišana.
```python
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


## API

### Lietotāju autentifikācija un tālāka autorizācija.
```bash
post http://127.0.0.1:8000/auth/token/ '{username:test_username, password:test_password}'
```
Pieprasījuma atbildē sagaidāmi divi tokeni. Turpmākai autorizācijai tiks norādīts `access` tokens.

```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDU4OTkxOTgsImp0aSI6IjMyNmM5YzUxMTk2ZjQ4NGU4OTYwZTFhYmMxOTgwMDk0IiwidG9rZW5fdHlwZSI6ImFjY2VzcyIsInVzZXJfaWQiOjF9.t5b2kqUVprbizNQrowMD50b1s0bVk98qfwvlzDBEjag",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDU5ODUyOTgsImp0aSI6ImFlZTdiMzY3NTc2NjQwMjE5NzZiMTE4NDA5OWUzNjJiIiwidG9rZW5fdHlwZSI6InJlZnJlc2giLCJ1c2VyX2lkIjoxfQ.PCySDorBpCswLmz6E2s_xcgWndbSIAZ1zbrDVrayckc"
}
```


### Administratora API  `/api/administrator/`.
Aptaujas izveide ar diviem jautājumiem un vairākiem atbilžu izvēles variantiem.

```bash
# Send data to server with http header
post http://127.0.0.1:8000/api/administrator/surveys/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDU4OTkxOTgsImp0aSI6IjMyNmM5YzUxMTk2ZjQ4NGU4OTYwZTFhYmMxOTgwMDk0IiwidG9rZW5fdHlwZSI6ImFjY2VzcyIsInVzZXJfaWQiOjF9.t5b2kqUVprbizNQrowMD50b1s0bVk98qfwvlzDBEjag"
```
```json
# POST data
{
    "name": "Aptauja. Strādājoši studenti.",
    "description": "Detalizēts aptaujas apraksts",
    "datetime_start": "2021-01-31 10:00",
    "datetime_end": "2021-01-31 10:00",
    "questions": [{
        "text": "Pirmais jautājums. Cik ilgu laiku strādājat algotu darbu?",
        "choices": [
            {
                "choice_text": "Līdz gadam"
            },
            {
                "choice_text": "1-5 gadi"
            },
            {
                "choice_text": "5-20 gadi"
            }
        ]
    },{
        "text": "Otrais jautājums. Kādas slodzes darbu strādājat?",
        "choices": [
            {
                "choice_text": "Pilnas slodzes"
            },
            {
                "choice_text": "Pusslodzes"
            }
        ]
    }]
}
```

### Atbilde uz jautājumu.
Atbildes uz jautājumiem. Visi dati tiek saglabāti konkrētam indentifikatoram. 
**selected_choices** - saraksts **id** modelis **ChoiceOptionModel**. Lietotāja izvēlētie varianti.
```bash
# Send data to server
post http://127.0.0.1:8000/api/answers/?identifier=12345
```
```json
# POST data
{
    "question": 4,
    "text": "Piemērs ar paplašinātu atbildi uz kādu no jautājumiem.",
    "selected_choices": [
        3,
        5
    ]
}
```

### Informācija par API.

```bash
# Get all surveys
get http://127.0.0.1:8000/api/administrator/surveys/ "Authorization: Bearer ..."

# Create new survey
post http://127.0.0.1:8000/api/administrator/surveys/ "Authorization: Bearer ..."

# Show detail survey
get http://127.0.0.1:8000/api/administrator/surveys/<id>/ "Authorization: Bearer ..."

# Delete survey
delete http://127.0.0.1:8000/api/administrator/surveys/<id>/ "Authorization: Bearer ..."
```

```bash
# Get all questions
get http://127.0.0.1:8000/api/administrator/questions/ "Authorization: Bearer ..."

# Update question
put http://127.0.0.1:8000/api/administrator/questions/<id>/ "Authorization: Bearer ..."

# Show detail question
get http://127.0.0.1:8000/api/administrator/questions/<id>/ "Authorization: Bearer ..."

# Delete question
delete http://127.0.0.1:8000/api/administrator/questions/<id>/ "Authorization: Bearer ..."
```

API Lietotājiem

```bash
# Get all surveys for users
get http://127.0.0.1:8000/api/list-active-surveys/
```

```bash
# Get all answers for users by identifier
get http://127.0.0.1:8000/api/answers/?identifier=12345
```

```bash
# Get all answered surveys by identifier
get http://127.0.0.1:8000/api/answered-surveys/?identifier=12345
```
```json
1: {
    "name": "Aptauja. Strādājoši studenti.",
    "description": "Detalizēts aptaujas apraksts",
    "info": "Start survey 31 January 2021 (11:11). End 31 January 2021 (11:11)",
    "questions": [
        {
            "text": "Pirmais jautājums. Cik ilgu laiku strādājat algotu darbu?",
            "choices": [
                "1-5 gadi"
            ]
        }, {
            "text": "Otrais jautājums. Kādā vecumā sākāt strādāt algotu darbu?",
            "answer_text": "14 gadu vecumā",
        }
    ]
}
```


### Atsauces
https://docs.djangoproject.com/en/2.2/topics/http/urls/
https://docs.djangoproject.com/en/2.2/topics/settings/
https://docs.djangoproject.com/en/2.2/ref/settings/
https://docs.djangoproject.com/en/2.2/ref/settings/#databases
https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
https://docs.djangoproject.com/en/2.2/topics/i18n/
https://docs.djangoproject.com/en/2.2/howto/static-files/
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#date
https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#date

**GitHub users:** smendes, karthikbgl, smirolo

