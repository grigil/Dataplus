from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from doc_send.forms import *
from django import forms
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.forms.models import model_to_dict


@staff_member_required
def Send(request):
    query_results = doc_request.objects.all()
    query_results2 = registred_docs.objects.all()
    if request.is_ajax():
        if request.POST.get('data') == "applications":
            html = render(request, '../templates/right_menu/applications.html', {'query_results': query_results})
            return HttpResponse(html)
        elif request.POST.get('data') == "reg_app":
            html = render(request, '../templates/right_menu/reg_app.html', {'query_results': query_results2})
            return HttpResponse(html)
        elif request.POST.get('data') == "PopUpShow":
            form = registred_docs_form(request.POST)
            bunch = doc_request.objects.get(id=form.data['hidden_id'])
            # print("-"*50)
            # print(bunch.file)
            # print(form.data)
            # print("-" * 50)
            html = render(request, '../templates/app_edit/create_app.html', {'query_results': query_results, 'form': form, 'file':bunch.file})
            return HttpResponse(html)
    elif not request.is_ajax():
        if request.POST:
            form = registred_docs_form(request.POST)
            print("8"*70)
            print(form.data)
            print("8" * 70)
            if form.data['CRUD_app'] == 'Удалить заявление':
                p = registred_docs.objects.get(id=form.data['hidden_id'])
                p.delete()
                return render(request, 'home_moder.html', {'query_results': query_results})
            if form.is_valid():
                data = form.save(commit=False)
                print(form.data['hidden_id'])
                bunch = doc_request.objects.get(id=form.data['hidden_id'])
                try:
                    registred_docs.objects.update_or_create(text=data.text,
                                                            status=data.status,
                                                            result=data.result,
                                                            user=bunch.user,
                                                            id=bunch.id,
                                                            name=bunch.name,
                                                            date=bunch.date,
                                                            file=bunch.file)
                    record = doc_request.objects.get(id=bunch.id)
                    record.text = data.text
                    record.status = data.status
                    record.result = data.result
                    record.save()
                except:
                    record = registred_docs.objects.get(id=bunch.id)
                    record.text = data.text
                    record.status = data.status
                    record.result = data.result
                    record.user = bunch.user
                    record.id = bunch.id
                    record.name = bunch.name
                    record.date = bunch.date
                    record.file = bunch.file
                    record.save()

                    record2 = doc_request.objects.get(id=bunch.id)
                    record2.text = data.text
                    record2.status = data.status
                    record2.result = data.result
                    record2.save()
                return render(request, 'home_moder.html', {'query_results': query_results})
    return render(request, 'home_moder.html', {'query_results': query_results})

def logout(request):
    auth_logout(request)
    return redirect('accounts/login');