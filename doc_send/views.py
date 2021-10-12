from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from doc_send.forms import *
import datetime
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_protect

@csrf_protect
@login_required
def Send(request):
    query_results = doc_request.objects.all()
    form = doc_request_form()
    if request.is_ajax():
        if request.POST.get('data') == "history":
            html = render(request, '../templates/right_menu/history_requests.html', {'query_results': query_results,'user':str(request.user)})
            return HttpResponse(html)
        else:
            html = render(request, '../templates/right_menu/doc_request.html', {'query_results': query_results, 'form': form})
            return HttpResponse(html)
    elif not request.is_ajax():
        if request.POST:
            form = doc_request_form(request.POST, request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = request.user
                data.text = 'В обработке'
                data.date = datetime.datetime.now()
                data.status = 'Выполняются работы по заявлению'
                data.result = 'Обработка инфы'
                data.save()
                return render(request, 'home.html', {'query_results': query_results})
    return render(request, 'home.html', {'query_results': query_results})

def logout(request):
    auth_logout(request)
    return redirect('accounts/login');

