from django.shortcuts import render

def client_dashboard(request):
    return render(request, 'client_dashboard.html', {})
