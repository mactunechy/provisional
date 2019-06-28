from django.db import models
from questions.models import Question
class Notes(models.Model):
    description  =    models.CharField(max_length=500)
    diagram      =    models.ImageField(null=True, upload_to="diagrams/notes")  #TODO : setup upload path and stuff 
    created_at   =    models.DateTimeField(auto_now_add=True)
    examples     =    models.ManyToManyField(Question,related_name="notes")

    def __str__(self):
        return f"notes_{self.pk}"
