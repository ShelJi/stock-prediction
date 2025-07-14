from rest_framework import response

def home(request):
    return response.Response({"message": "Welcome to the Stock Prediction API!"})