from django.shortcuts import render

def aa(request):
    context={}

    login_session = request.session.get('login_session','')
    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] =True

    return render(request, 'home/aa.html', context)



def favorites(request):
    return render(request,'home/favorites.html')
def about(request):
    return render(request,'home/about.html')
def contact(request):
    return render(request,'home/contact.html')