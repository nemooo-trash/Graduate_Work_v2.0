import json

from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from .models import *
from RRIT.views import get_sidebar, get_settings, get_search
from django.core.serializers import serialize

def incidents_all(request):
    if request.GET.get('search'):
        return incidents_search(request)
    else:
        app_models = get_sidebar()
        function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_settings(Incidents)
        return render(request, 'RRIT/view_all.html',
                      {'function_name': function_name,
                       'breadcrumb_ru': breadcrumb_ru,
                       'app_models': app_models,
                       'action_model': action_model,
                       'eddit_name': eddit_name,
                       'action_models_s': action_models_s,
                       'array_of_data': array_of_data,
                       'array_of_th': array_of_th,
                       'count': count,
                       })


def incidents_id(request, IncidentId):
    #print(request.GET)
    #здесь вывод 1-го

    incident = Incidents.objects.filter(pk=IncidentId).values('description', 'latitude', 'longitude')
    list_data_json = json.dumps(list(incident))
    #serialized_data = serialize("json", incident)
    #incidents_result = json.loads(serialized_data)
    return render(request, 'Incidents/index.html', {'data': list_data_json})


def incidents_search(request):
    arg = request.GET.get('search')
    function_name, breadcrumb_ru, action_model, action_models_s, eddit_name, array_of_data, count, array_of_th = get_search(
        Incidents, arg)
    app_models = get_sidebar()
    return render(request, 'RRIT/view_all.html',
                  {'function_name': function_name,
                   'breadcrumb_ru': breadcrumb_ru,
                   'app_models': app_models,
                   'action_model': action_model,
                   'eddit_name': eddit_name,
                   'action_models_s': action_models_s,
                   'array_of_data': array_of_data,
                   'array_of_th': array_of_th,
                   'count': count,
                   })
def incidents_add(request):
    return render(request, 'Incidents/add.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница инцидентов не найдена')
