from django.shortcuts import render
from contact.forms import RegisterForm

def register(request):
    return render(
        form = RegisterForm()
        request,
        'contact/registe.html',
        {
            'form': form
        }
    )
