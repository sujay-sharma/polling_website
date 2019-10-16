# We are importing the base model class we want our 
  # model to extend
from django.db import models

# Any model we create is going to be a class
class Question(models.Model):
    # Specify fields 
    # models have many different data types
    # It will create an id automatically which will be our 
      # primary key which will auto increment
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # When questions and choices are added in the admin area, it will just say 
      # 'question object', we want to diaplay the question text and the choice text
    def __str__(self):  
      return self.question_text

class Choice(models.Model):
    # Want to link the foreign key to the primary key 
        # of the Question table
    # If there is a question that is deleted, all 
      # of its choices will also be deleted   
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):  
      return self.choice_text
