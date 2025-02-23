from django.db import models

# DB model for main NN models
class NNmodel(models.Model):
    model_owner = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    model_description = models.TextField()
    model_version = models.IntegerField(default=0)

    def __str__(self):
        return self.model_name
