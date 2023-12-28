from django.db import models
from django.contrib.auth.models import User
from google.cloud import firestore
import json
from datetime import datetime

class UserSelection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def save_to_firestore(self):
        key_path= 'C:/Users/mgkco/OneDrive/job/Internship/sigaram tech/Admin panel/main/creadentials/adminpanel-409509-65f29fa144c6.json'
        db = firestore.Client.from_service_account_json(key_path)
        collection_ref = db.collection('sigaram_test_collection')

        data = {
            'user_id': self.user.id,
            'country': self.country,
            'language': self.language,
            'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        collection_ref.add(data)