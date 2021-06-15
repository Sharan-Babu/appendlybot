# Appendly Bot
Website FAQ Bot built using Flask and Wit.ai. Part of the Appendly website which was submitted for the Dr.Chrono Hackathon 2021.

## Using the API
```
import requests
import json

url = "https://appendlybot.herokuapp.com."
data = {'input':'what is your name'}

send_request = requests.post(url,files=data).json()
print(send_request)
```

_Procfile_ is used to declare process type. It instructs Heroku on how to use various parts of your app.
_app.py_ contains the chatbot logic.
_requirements.txt_ has the libraries/dependencies to be installed.
