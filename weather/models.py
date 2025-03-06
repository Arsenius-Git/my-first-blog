from django.db import models

# Create your models here.

class ToDoList(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.namefr

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

class ExpensesTrack(models.Model):
    description = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description}: ${self.amount}"