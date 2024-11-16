from django.db import models

class Carousel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    button =models.CharField(max_length=100)

    def __str__(self):
        return self.title


class About(models.Model):
    content = models.TextField(max_length=1000)
    list_1 = models.TextField(max_length=1000)
    list_2 = models.TextField(max_length=1000)
    list_3 = models.TextField(max_length=1000)
    explanation = models.TextField(max_length=1000)


class Box(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    explanation = models.TextField(max_length=1000)
    discussion = models.TextField(max_length=1000)
    list_1 = models.TextField(max_length=1000)
    list_2 = models.TextField(max_length=1000)
    list_3 = models.TextField(max_length=1000)
    list_4 = models.TextField(max_length=1000)
    conclusion = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Action(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    button =models.CharField(max_length=100)


class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)

class Portfolio(models.Model):
    link =models.CharField(max_length=1000)
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    image_3 = models.ImageField(upload_to='images/')
    image_4 = models.ImageField(upload_to='images/')
    image_5 = models.ImageField(upload_to='images/')
    image_6 = models.ImageField(upload_to='images/')
    image_7 = models.ImageField(upload_to='images/')
    image_8 = models.ImageField(upload_to='images/')
    image_9 = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    image = models.ImageField(upload_to='images/')
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.full_name

class Pricing(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    list_1 = models.TextField(max_length=1000)
    list_2 = models.TextField(max_length=1000)
    list_3 = models.TextField(max_length=1000)
    list_4 = models.TextField(max_length=1000)
    list_5 = models.TextField(max_length=1000)
    list_6 = models.TextField(max_length=1000)
    button =models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Faq(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)


class Team(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    twitter_url = models.URLField(max_length=1000)
    facebook_url = models.URLField(max_length=1000)
    instagram_url = models.URLField(max_length=1000)
    linkedin_url = models.URLField(max_length=1000)

    def __str__(self):
        return self.full_name

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    full_name = models.CharField(max_length=100)
    date = models.DateField()
    profile_pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name

class Contact(models.Model):
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.address

class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()








# Create your models here.
