# views.py
from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
from .model_utils import prediction_model # Import your model and scaler
import pickle
import sklearn

def predict(request):
    if request.method == 'POST':
        runs = int(request.POST.get('runs'))
        wickets = int(request.POST.get('wickets'))
        overs = float(request.POST.get('overs'))
        striker = int(request.POST.get('striker'))
        non_striker = int(request.POST.get('non_striker'))
        prediction = prediction_model(runs,wickets, overs, striker, non_striker)
        prediction = int(prediction)
        return JsonResponse({'prediction': prediction})
    return render(request, 'model.html')
