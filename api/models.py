from django.db import models

# Create your models here.

# class Poll(models.Model):
#     question = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

class Category(models.Model):
	name = models.CharField(max_length=50, null=False, blank=False)
	description = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)
	description = models.TextField(null=True, blank=True)
	category = models.ForeignKey('Category', null=False, blank=False, related_name='items')
	rating = models.DecimalField(max_digits=2, decimal_places=4, null=False, blank=False, default=0)

	def __unicode__(self):
		return self.name

class Voter(models.Model):
	email = models.EmailField(unique=True, null=False, blank=False)
	suggestion = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.email

class Rating(models.Model):
	item = models.ForeignKey('Item', null=False, blank=False, related_name='ratings')
	rating = models.IntegerField(min_value=1, max_value=10)
	voter = models.ForeignKey('Voter', null=False, blank=False, related_name='user_ratings')
	suggestion = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.item + " - " + self.rating