from django.shortcuts import render

# Create your views here.

def exchange(request):
    name = "Rustam"

    context = {
        'name':name,
    }

    return render(request=request, template_name='currerter_app/index.html', context=context)
