from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #here we are importing the user model present in the django
#each class will be out table and every variable is attribute
from django.urls import reverse 
class Post(models.Model):
      title = models.CharField(max_length = 100)
      content = models.TextField()
      date_posted = models.DateTimeField(default = timezone.now)
      author = models.ForeignKey(User, on_delete = models.CASCADE) #here we are making relationship between author and post
      #"on_delete =  models.CASCADE" deltets all the posts created by author if author is got deleted 

      def __str__(self):
            return self.title

      def get_absolute_url(self):
            return reverse('post-detail', kwargs={'pk': self.pk})