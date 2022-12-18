
import os
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.shortcuts import render
from .models import Badanie
from .forms import BadanieForm
from wsgiref.util import FileWrapper
import pandas as pd
from io import StringIO


# Create your views here.


def new_sample(request):
    if request.method == "POST":
        form = BadanieForm(request.POST)
        if form.is_valid():
            data = request.POST.dict()
            data.pop('csrfmiddlewaretoken')
            data['oznakowanie'] = int(data['oznakowanie'])

            for key, val in {**data}.items():
                if not val:
                    data.pop(key)

            for key, val in {**data}.items():
                try:
                    numval = float(val)
                except:
                    numval = val
                data[key] = numval

            #print(data)
            new_badanie = Badanie(**data)
            new_badanie.save()
            return HttpResponseRedirect('new')

    else:
        form = BadanieForm()
        return render(request, 'grunty/new.html', context={'form': form})


def table(request):
    if request.method == "POST":
        id = int(request.POST.get('del_id'))
        Badanie.objects.filter(pk=id).delete()


    badania = Badanie.objects.all()
    fields = list(map(lambda field: field.verbose_name, Badanie._meta.fields))
    fields[0] = 'Nr_prob'
    return render(request, 'grunty/table.html', context={'badania': badania, 'fields': fields})


def download_csv(request):
    data = Badanie.objects.all()
    data_serial = serializers.serialize("python", data)
    for ds in data_serial:
        ds['fields']['id'] = ds['pk']
    data_serial = [ds['fields'] for ds in data_serial]

    for ds in data_serial:
        for key, val in {**ds}.items():
            new_key = Badanie._meta.get_field(key).verbose_name
            ds[new_key] = ds.pop(key)

    print('DATA', data_serial)

    try:
        df = pd.DataFrame(data_serial)
        df.rename(columns={'ID': 'Nr_prob'}, inplace=True)
        df.set_index('Nr_prob', inplace=True)

        buffer = StringIO()
        df.to_csv(buffer)
        buffer.seek(0)



        content = FileWrapper(buffer)
        response = HttpResponse(content, content_type='application/csv')

        #response['Content-Length'] = os.path.getsize(buffer)
        response['Content-Disposition'] = 'attachment; filename=%s' % 'badania_gleby.csv'
        return response
    except:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

