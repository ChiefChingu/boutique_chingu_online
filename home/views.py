from django.shortcuts import render

# Create your views here.

# 3.1 Add a view to render the home template
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

