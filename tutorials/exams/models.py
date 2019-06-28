from django.db import models
from questions.models import Question
from random import sample
from django.db.models.signals import post_save

GRADE_CHOICES = [
    ("pass","pass"),
    ("fail","fail")
]


class Exam(models.Model):
    description      = models.CharField(max_length=500,blank=True)
    score            = models.IntegerField(blank=True,null=True)
    questions        = models.ManyToManyField(Question, related_name='exams') #TODO : Not sure about the related_name
    grade            = models.CharField(max_length=5,choices=GRADE_CHOICES,null=True,blank="True")
    created_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question_{self.pk}"

    
    def increment_score(self):
        '''increments the score if the question was marked correct'''
        self.score += 1
        self.save()

    
    def set_grade(self):
        '''sets the grade of the test after the test was commplete'''
        if self.score >=23:
           self.grade = 'pass'
           self.save()
        else:
            self.grade = 'fail'
            self.save()
           

    
def add_questions(instance,sender,*args,**kwargs):

    questionIndices = sample(range(1, Question.objects.count()), 3) #TODO : change 3 to 25
    qs = Question.objects.filter(pk__in=questionIndices)
    instance.questions.set(qs)

post_save.connect(add_questions,sender=Exam)
        




