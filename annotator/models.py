from django.db import models
from multiselectfield import MultiSelectField

class survey(models.Model):
    name = models.CharField(max_length=250 , null= True)
    document = models.FileField(upload_to='documents/', null= True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name

class Page1(models.Model):

    MY_CHOICES = (('item_key1', 'Item title 1.1'),
                  ('item_key2', 'Item title 1.2'),
                  ('item_key3', 'Item title 1.3'))


    SET_OF_CHOICES = (('choice1', 'choice1'),
        ('choice2', 'choice2'),
        ('choice3', 'choice3'),
    )
    name = models.ForeignKey('survey', on_delete=models.CASCADE, null=True)
    p1q1= models.CharField(max_length=250, choices=SET_OF_CHOICES, null=True)
    p1q2 = MultiSelectField(choices=MY_CHOICES, max_choices=3, null = True)
    p1q3 = models.CharField(max_length=250, null = True)
    p1q4 = models.CharField(max_length=20, null = True)
    anno = models.CharField(max_length=10000, null=True)

    def __str__(self):
        return self.name.name


class Page2(models.Model):

    MY_CHOICES = (('item_key1', 'Item title 1.1'),
                  ('item_key2', 'Item title 1.2'),
                  ('item_key3', 'Item title 1.3'))


    SET_OF_CHOICES = (('choice1', 'choice1'),
        ('choice2', 'choice2'),
        ('choice3', 'choice3'),
    )
    name = models.ForeignKey('survey', on_delete=models.CASCADE, null=True)
    p2q1 = models.CharField(max_length=250, choices=SET_OF_CHOICES, null=True)
    p2q2 = MultiSelectField(choices=MY_CHOICES, max_choices=3, null = True)
    p2q3 = models.CharField(max_length=250, null = True)
    p2q4 = models.CharField(max_length=20, null = True)

    def __str__(self):
        return self.name.name

class Page3(models.Model):

    MY_CHOICES = (('item_key1', 'Item title 1.1'),
                  ('item_key2', 'Item title 1.2'),
                  ('item_key3', 'Item title 1.3'))


    SET_OF_CHOICES = (('choice1', 'choice1'),
        ('choice2', 'choice2'),
        ('choice3', 'choice3'),
    )
    name = models.ForeignKey('survey', on_delete=models.CASCADE, null=True)
    p3q1 = models.CharField(max_length=250, choices=SET_OF_CHOICES, null=True)
    p3q2 = MultiSelectField(choices=MY_CHOICES, max_choices=3, null = True)
    p3q3 = models.CharField(max_length=250, null = True)
    p3q4 = models.CharField(max_length=20, null = True)

    def __str__(self):
        return self.name.name

class Page4(models.Model):

    MY_CHOICES = (('item_key1', 'Item title 1.1'),
                  ('item_key2', 'Item title 1.2'),
                  ('item_key3', 'Item title 1.3'))


    SET_OF_CHOICES = (('choice1', 'choice1'),
        ('choice2', 'choice2'),
        ('choice3', 'choice3'),
    )
    name = models.ForeignKey('survey', on_delete=models.CASCADE, null=True)
    p4q1 = models.CharField(max_length=250, choices=SET_OF_CHOICES, null=True)
    p4q2 = MultiSelectField(choices=MY_CHOICES, max_choices=3, null = True)
    p4q3 = models.CharField(max_length=250, null = True)
    p4q4 = models.CharField(max_length=20, null = True)

    def __str__(self):
        return self.name.name

class Page5(models.Model):

    MY_CHOICES = (('item_key1', 'Item title 1.1'),
                  ('item_key2', 'Item title 1.2'),
                  ('item_key3', 'Item title 1.3'))


    SET_OF_CHOICES = (('choice1', 'choice1'),
        ('choice2', 'choice2'),
        ('choice3', 'choice3'),
    )
    name = models.ForeignKey('survey', on_delete=models.CASCADE, null=True)
    p5q1 = models.CharField(max_length=250, choices=SET_OF_CHOICES, null=True)
    p5q2 = MultiSelectField(choices=MY_CHOICES, max_choices=3, null = True)
    p5q3 = models.CharField(max_length=250, null = True)
    p5q4 = models.CharField(max_length=20, null = True)

    def __str__(self):
        return self.name.name
