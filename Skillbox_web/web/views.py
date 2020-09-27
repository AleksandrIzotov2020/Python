from datetime import datetime
from django.shortcuts import render, redirect
from mysite import settings


def index(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html')

def status(request):
    return render(request, 'status.html')

publications_data = []

def publications(request):
    return render(request, 'publications.html', {
        'publications': publications_data
    })


def publication(request, id):
    if id < len(publications_data):
        return render(request, 'publication.html', publications_data[id])
    else:
        return redirect('/')

def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    else:
        secret = request.POST['secret']
        name = request.POST['name']
        text = request.POST['text']
        redirect('/publications')

        if secret != settings.SECRET_KEY:
            return render(request, 'publish.html', {
                'error': 'Неправильный Secret Key'
            })
        if len(name) == 0:
            return render(request, 'publish.html', {
                'error': 'Пустое имя'
            })
        if len(text) == 0:
            return render(request, 'publish.html', {
                'error': 'Пустой text'
            })

        publications_data.append({
            'id': len(publications_data),
            'name': name,
            'date': datetime.now(),
            'text': text.replace('\n', '<br />')
        })