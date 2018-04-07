from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	is_specialist = models.BooleanField(default=False)
	skills = models.ManyToMany(Skill, verbose_name='list of skills')

class Skill(models.Model):
	tag = models.CharField(max_length=50)

class Chat(models.Model):
	user_instructor = models.ForeignKey(User)
	user_student = models.ForeignKey(User)

class Question(models.Model):
	question = models.TextField()
	skills = models.ManyToMany(Skill, verbose_name='question skills')
