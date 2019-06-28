from django.db import models
from rest_framework.reverse import reverse as api_reverse


class Question(models.Model):
    description      = models.CharField(max_length=500)
    diagram          = models.ImageField(upload_to='diagrams/questions',null=True)               #TODO : setup the upload folders and what not
    answers          = models.CharField(max_length=600)  #TODO : research a better approach
    correct_answer   = models.CharField(max_length=500)  #TODO : research a better approach
    created_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question_{self.pk}"
    
    def get_api_url(self,request=None):
        return api_reverse('questions-details',kwargs={'pk':self.pk },request=request)
    
    def mark_question(self,selected_answer): #TODO : find more cleaner way to get an answer from user, perhaps a select answer method
        if self.correct_answer == selected_answer :
            return True
        return False

