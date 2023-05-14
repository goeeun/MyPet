from django.shortcuts import render

def index(request):
    context={}

    login_session = request.session.get('login_session','')
    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] =True

    return render(request, 'index/index.html', context)



def favorites(request):
    return render(request,'index/favorites.html')
def about(request):
    return render(request,'index/about.html')
def contact(request):
    return render(request,'index/contact.html')