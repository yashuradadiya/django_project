from django.shortcuts import render,redirect
from admin_ultras.models import *
from UltrasApp.models import *

# Create your views here.
# -------------------- login admin user ------------------------------------
def a_index(request):
    if 'user_id' in request.session:
        return redirect ('/myadmin/home')
    msg = ""
    if 'save' in request.POST:
        g_email = request.POST['email']
        g_password = request.POST['password']
        obj = Profile.objects.filter(email=g_email,password=g_password)
        if obj.count()==1:
            row = obj.get()
            request.session['user_id'] = row.id
            return redirect ('/myadmin/home')
        else :
            msg = "Please Enter Valid Email Or Password"
    return render (request, 'index1.html',{'msg':msg})

# -------------------------- register admin user ---------------------------------
def register(request):
    if 'save' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        object = Profile(
            name = name,
            email = email,
            password = password
        )
        object.save()
        return redirect ('/myadmin')
    return render (request, 'register.html')

# ------------------------------ Home page --------------------------
def home(request):
    if 'user_id' not in request.session:
        return redirect ('/myadmin')
    con_id = request.session['user_id']
    user = Profile.objects.filter(id=con_id).get()
    request.session['user_name'] = user.name
    user_image = user.image
    request.session['user_image'] = str(user_image)
    request.session['user_skill'] = user.skills
    return render (request, 'home.html',{'user_name':request.session['user_name'],'user_id':con_id,'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

#  ----------------------------- User Profile -----------------------------
def profile(request):
    con_id = request.session['user_id']
    data = Profile.objects.filter(id=con_id).get()
    return render (request, 'profile.html',{'rows':data,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def view_admin(request):
    return render (request, 'view_admin.html')

def setting(request):
    user_id = request.session['user_id']
    Frmobj = Profile.objects.filter(id = user_id).get()
    obj = ProfileForm(instance=Frmobj)
    if 'save' in request.POST:
        obj = ProfileForm(request.POST,request.FILES,instance=Frmobj)
        obj.save()
        return redirect ('/myadmin/home') 
    return render (request, 'setting.html',{'Cdata':obj , 'user_name':request.session['user_name'],'user_id':user_id,'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

# --------------------------- Slider --------------------------------
def view_slider(request):
    data = Slider.objects.all()
    return render (request, 'view_slider.html',{'rows':data,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def add_slider(request):
    fromobj = SliderFrom()
    if 'save' in request.POST:
        fromobj = SliderFrom(request.POST,request.FILES)
        fromobj.save()
        return redirect('/myadmin/view_slider')
    return render (request, 'add_slider.html',{'data':fromobj,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def edit_slider(request,edit_id):
    Frmobj = Slider.objects.filter(id = edit_id).get()
    obj = SliderFrom(instance=Frmobj)
    if 'save' in request.POST:
        obj = SliderFrom(request.POST,request.FILES,instance=Frmobj)
        obj.save()
        return redirect ('/myadmin/view_slider') 
    return render (request, 'add_slider.html',{'data':obj,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def delete_slider(request,del_id):
    Slider.objects.filter(id=del_id).delete()
    return redirect ('/myadmin/view_slider')

# ----------------------------- Category ----------------------------------
def view_category(request):
    data = Category.objects.all()
    return render (request, 'view_category.html',{'rows':data,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def add_category(request):
    fromobj = CategoryForm()
    if 'save' in request.POST:
        fromobj = CategoryForm(request.POST,request.FILES)
        fromobj.save()
        return redirect('/myadmin/view_category')
    return render (request, 'add_category.html',{'data':fromobj,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def edit_category(request,edit_id):
    Frmobj = Category.objects.filter(id = edit_id).get()
    obj = CategoryForm(instance=Frmobj)
    if 'save' in request.POST:
        obj = CategoryForm(request.POST,request.FILES,instance=Frmobj)
        obj.save()
        return redirect ('/myadmin/view_category') 
    return render (request, 'add_category.html',{'data':obj,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def delete_category(request,del_id):
    Category.objects.filter(id=del_id).delete()
    return redirect ('/myadmin/view_category')

# -------------------------------- Tag ---------------------------------------
def view_tag(request):
    data = Tag.objects.all()
    return render (request, 'view_tag.html',{'rows':data,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def add_tag(request):
    fromobj = TagForm()
    if 'save' in request.POST:
        fromobj = TagForm(request.POST)
        fromobj.save()
        return redirect('/myadmin/view_tag')
    return render (request, 'add_tag.html',{'data':fromobj,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def edit_tag(request,edit_id):
    Frmobj = Tag.objects.filter(id = edit_id).get()
    obj = TagForm(instance=Frmobj)
    if 'save' in request.POST:
        obj = TagForm(request.POST,instance=Frmobj)
        obj.save()
        return redirect ('/myadmin/view_tag') 
    return render (request, 'add_tag.html',{'data':obj,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def delete_tag(request,del_id):
    Tag.objects.filter(id=del_id).delete()
    return redirect ('/myadmin/view_tag')

# ------------------------ Brand -------------------------------------
def view_brand(request):
    data = Brand.objects.all()
    return render (request, 'view_brand.html',{'rows':data,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def add_brand(request):
    fromobj = BrandForm()
    if 'save' in request.POST:
        fromobj = BrandForm(request.POST)
        fromobj.save()
        return redirect('/myadmin/view_brand')
    return render (request, 'add_brand.html',{'data':fromobj,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def edit_brand(request,edit_id):
    Frmobj = Brand.objects.filter(id = edit_id).get()
    obj = BrandForm(instance=Frmobj)
    if 'save' in request.POST:
        obj = BrandForm(request.POST,instance=Frmobj)
        obj.save()
        return redirect ('/myadmin/view_brand') 
    return render (request, 'add_brand.html',{'data':obj,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def delete_brand(request,del_id):
    Brand.objects.filter(id=del_id).delete()
    return redirect ('/myadmin/view_brand')
    
# ---------------------- Product --------------------
def view_product(request):
    data = Product.objects.all()
    return render (request, 'view_product.html',{'rows':data,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def add_product(request):
    fromobj = ProductForm()
    cats = Category.objects.all()
    tags = Tag.objects.all()
    brands = Brand.objects.all()
    if 'save' in request.POST:
        fromobj = ProductForm(request.POST,request.FILES)
        fromobj.save()
        return redirect('/myadmin/view_product')
    return render (request, 'add_product.html',{'data':fromobj,'cats':cats,'tags':tags,'brands':brands,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def edit_product(request,edit_id):
    cats = Category.objects.all()
    tags = Tag.objects.all()
    brands = Brand.objects.all()
    Frmobj = Product.objects.filter(id = edit_id).get()
    obj = ProductForm(instance=Frmobj)
    if 'save' in request.POST:
        obj = ProductForm(request.POST,request.FILES,instance=Frmobj)
        price = request.POST['price']
        cart_entries = Cart.objects.filter(product_id=edit_id)
        for entry in cart_entries:
            entry.price = price
            qty = int(entry.qty)
            entry.amount = qty * int(price)
            entry.save()
        obj.save()
        return redirect ('/myadmin/view_product') 
    return render (request, 'add_product.html',{'data':obj,'cats':cats,'tags':tags,'brands':brands,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def delete_product(request,del_id):
    Product.objects.filter(id=del_id).delete()
    return redirect ('/myadmin/view_product')

# ----------------------- view Frontend user ----------------------
def view_user(request):
    data = User.objects.all()
    return render (request,'view_user.html',{'rows':data,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def edit_user(request,edit_id,status):
    data = User.objects.filter(id=edit_id).get()
    data.status = status
    data.save()
    return redirect ('/myadmin/view_user')

def view_cart(request):
    data = Cart.objects.all()
    return render (request,'view_cart.html',{'rows':data,'user_name':request.session['user_name'],'user_id':request.session['user_id'],'user_image':request.session['user_image'],'user_skill':request.session['user_skill']})

def logout(request):
    del request.session['user_id']
    return redirect ('/myadmin')


  