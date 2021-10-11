from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from doc_send.forms import *
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout

@staff_member_required
def Send(request):
    query_results = doc_request.objects.all()
    if request.is_ajax():
        if request.POST.get('data') == "applications":
            html = render(request, '../templates/right_menu/applications.html', {'query_results': query_results})
            return HttpResponse(html)
        elif request.POST.get('data') == "reg_app":
            html = render(request, '../templates/right_menu/reg_app.html', {'query_results': query_results})
            return HttpResponse(html)
        elif request.POST.get('data') == "PopUpShow":
            form = registred_docs_form(request.POST, request.FILES)
            html = render(request, '../templates/app_edit/create_app.html', {'query_results': query_results, 'form': form})
            return HttpResponse(html)
    return render(request, 'home_moder.html', {'query_results': query_results})

def logout(request):
    auth_logout(request)
    return redirect('accounts/login');