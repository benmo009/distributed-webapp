from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

import json
from .models import CountProcess

@csrf_protect
def index(request):
    return render(request, "counter/index.html")

def new_counter(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        max_count = int(request_body['max_count'])
        counter = CountProcess.objects.create(max_count=max_count)

        data = {
            "counter_url": counter.get_absolute_url()
        }
        return JsonResponse(data=data)
    else:
        return render(request, "counter/index.html")

def counter_log(request, counter_id):
    counter = CountProcess.objects.get(id=counter_id)
    context = {
        "counter": counter
    }
    return render(request, 'counter/counter.html', context=context)
