from rest_framework import serializers
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta :
        model = Question
        fields = [
            'url',
            'description',
            'diagram',
            'answers',
            'correct_answer',
            'created_at'



        ]
    def get_url(self,obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
