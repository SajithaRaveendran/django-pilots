from django.db import models


class Students(models.Model):
    register_id = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    name = models.CharField(max_length=255)
    roll_no = models.IntegerField()
    _class  = models.IntegerField()
    parent = models.CharField(max_length=255)

    class Meta:
        verbose_name = ('Students')
        verbose_name_plural = ('Students')

    def __str__(self):
        return self.name


class Parent(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    occupation = models.CharField(max_length=255)

    class Meta:
            verbose_name = ('Parent')
            verbose_name_plural = ('Parent')

    def __str__(self):
        return self.name


class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    division = models.CharField(max_length=255)
    class_teacher = models.CharField(max_length=255)

    class Meta:
            verbose_name = ('Class')
            verbose_name_plural = ('Class')

    def __str__(self):
        return self.class_teacher


class Subjects(models.Model):
    name = models.CharField(max_length=255)
    hours_per_week = models.FloatField()

    class Meta:
            verbose_name = ('Subjects')
            verbose_name_plural = ('Subjects')

    def __str__(self):
        return self.name


class ClassTeacher(models.Model):
    phone_no =  models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    subject_handled = models.CharField(max_length=255)

    class Meta:
            verbose_name = ('Class Teacher')
            verbose_name_plural = ('Class Teacher')

    def __str__(self):
        return self.name

    


