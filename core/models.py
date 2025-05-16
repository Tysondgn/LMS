from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()
    
    def __str__(self):
        return self.name

class Student(models.Model):
    enrollment_number = models.CharField(max_length=50, primary_key=True, default='EN001')  # Unique ID with default
    name = models.CharField(max_length=100, null=False, default='')
    class_name = models.CharField(max_length=50, null=False, default='')
    email = models.EmailField(unique=True, null=False, default='')
    date_of_birth = models.DateField(null=False, default='2000-01-01')
    enrollment_date = models.DateField(null=False, default='2000-01-01')
    password = models.CharField(max_length=100, null=False, default='')
    
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # students = models.ManyToManyField(Student, related_name='courses')  # Removed for migration
    
    def __str__(self):
        return self.title

class StudyMaterial(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='materials/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    upload_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    total_marks = models.IntegerField()
    date = models.DateField()
    
    def __str__(self):
        return self.title
