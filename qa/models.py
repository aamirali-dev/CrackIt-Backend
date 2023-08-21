from django.db import models

class QuestionCategory(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.name 

class Question(models.Model):
    category = models.ForeignKey(QuestionCategory, on_delete=models.PROTECT, related_name='questions')
    description = models.TextField(null=False, blank=False)

    def __str__(self) -> str:
        return self.description

class Solution(models.Model):
    data = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self) -> str:
        print(self.data)
        if self.data is None:
            return ''
        return self.data

