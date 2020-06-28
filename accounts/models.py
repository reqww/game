from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to="user_avatars/%Y/%m/%d", blank=True)

	def __str__(self):
		return "Профиль пользователя %s" % self.user.username 

	def get_url(self):
		try:
			return self.avatar.url
		except ValueError:
			return None

