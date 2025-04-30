from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUBMITTED', 'Submitted'),
        ('LATE', 'Late'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"{self.title} ({self.student.name})"
