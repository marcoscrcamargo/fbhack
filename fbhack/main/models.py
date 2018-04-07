from django.db import models

# Create your models here.
class Skill(models.Model):
	tag = models.CharField(max_length=50)

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	is_specialist = models.BooleanField(default=False)
	skills = models.ManyToManyField(Skill, verbose_name='list of skills')

class Question(models.Model):
	question = models.TextField()
	skills = models.ManyToManyField(Skill, verbose_name='question skills')

class Chat(models.Model):
	user_instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructor')
	user_student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
