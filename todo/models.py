from django.db import models

# Create your models here.
class Todo(models.Model):
    PRIORITY = (
        (1, 'Hight'),
        (2, 'Medium'),
        (3, 'Low')
    )
    task = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    prioirty = models.SmallIntegerField(choices=PRIORITY, default=3)
    is_done = models.BooleanField(default=False)
    updated_data = models.DateTimeField(auto_now=True)
    created_data = models.DateTimeField(created_now_add=True)


    def __str__(self):
        return self.task
