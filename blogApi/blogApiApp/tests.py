from django.test import TestCase
import requests

request = requests.get('http://localhost:8080')

print(request.json())
