from django.shortcuts import render,redirect 
from Contacts.models import User,UserForm,Contact,ContactForm

# Create your views here.
def index (request):
    if 'user_id' in request.session:
        return redirect ('/home')
    if 'save' in request.POST:
        g_email = request.POST['email']
        g_password = request.POST['password']
        obj = User.objects.filter(email=g_email,password=g_password)
        if obj.count()==1:
            row = obj.get()
            request.session['user_id'] = row.id
            return redirect ('/home')
    return render (request, 'index.html')

def home (request):
    if 'user_id' not in request.session:
        return redirect ('/index')
    con_id = request.session['user_id']
    user = User.objects.filter(id=con_id).get()
    request.session['user_name'] = user.name
    data = Contact.objects.filter(user_id=con_id)
    return render (request, 'home.html',{'rows':data, 'user_name':request.session['user_name'] , 'user_id':con_id })

def register (request):
    CFormObj = UserForm()
    if 'save' in request.POST:
        CFormObj = UserForm(request.POST)
        CFormObj.save()
        return redirect ('/index')
    return render (request, 'register.html', {'data':CFormObj})
     
def add_contact (request):
    CFormObj = ContactForm()
    user_id = request.session['user_id']
    if 'save' in request.POST:
        CFormObj = ContactForm(request.POST)
        CFormObj.save()
        return redirect ('/home')
    return render (request, 'add_contact.html', {'Cdata':CFormObj , 'user_name':request.session['user_name'] , 'user_id':user_id})

def delete(request,del_id):
    Contact.objects.filter(id=del_id).delete()
    return redirect ('/home')

def edit_data(request ,edit_id):
    Frmobj = Contact.objects.filter(id = edit_id).get()
    obj = ContactForm(instance=Frmobj)
    if 'save' in request.POST:
        obj = ContactForm(request.POST ,instance=Frmobj)
        obj.save()
        return redirect ('/home') 
    return render (request, 'add_contact.html',{'Cdata':obj , 'user_name':request.session['user_name'] })

def logout(request):
    del request.session['user_id']
    return redirect ('/index')

def edit_profile(request ,edit_id):
    Frmobj = User.objects.filter(id = edit_id).get()
    obj = UserForm(instance=Frmobj)
    if 'save' in request.POST:
        obj = UserForm(request.POST ,instance=Frmobj)
        obj.save()
        return redirect ('/home') 
    return render (request, 'edit_profile.html',{'data':obj , 'user_name':request.session['user_name'] })
