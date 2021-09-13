from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=250, null=True)
    discription = models.TextField(null=True, )
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title


class Board(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=True)
    sequence = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title


class Card(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, )
    title = models.CharField(max_length=50, null=True, )
    discription = models.TextField(null=True, )
    due_date = models.DateTimeField()
    sequence = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title
