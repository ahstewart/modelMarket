from django.shortcuts import render
from django.http import HttpResponse
from .models import NNmodel
from django.template import loader

# main model list view - view all models you have access to
def models_hp(request):
    model_list = NNmodel.objects.all()
    template = loader.get_template("mods/index.html")
    context = {
        "model_list": model_list
    }
    return HttpResponse(template.render(context, request))

def model_details(request, model_id):
    the_model = NNmodel.objects.get(pk=model_id)
    return HttpResponse(f"I'll put the model details for {the_model.model_name} here")