from django.shortcuts import render


# Function-based view for the homepage using a template
def home(request):
    return render(request, "home.html")
