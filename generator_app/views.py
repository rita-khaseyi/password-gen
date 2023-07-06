from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import random
import string

def generate_password(request):
    if request.method == 'POST':
        length = int(request.POST.get('length'))
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        return render(request, 'generator_app/password.html', {'password': password})
    return render(request, 'generator_app/generate.html')

