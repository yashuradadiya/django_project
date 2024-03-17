from django.shortcuts import render,redirect
from admin_ultras.models import *
from UltrasApp.models import *

# Create your views here.
def about(request):
    return render (request, 'about.html')
def blog_masonny(request):
    return render (request, 'blog-masonny.html')
def blog_sidebar(request):
    return render (request, 'blog-sidebar.html')
def blog(request):
    return render (request, 'blog.html')
def cart(request):
    if 'admin_id' not in request.session:
        return redirect('/login')
    data = Cart.objects.filter(user_id=request.session['admin_id'])
    if 'save' in request.POST:
        quantity = request.POST['quantity']
        pdt_id = request.POST['pdt_id']
        cart = Cart.objects.filter(id=pdt_id).get()
        before = cart.qty
        cart.qty = quantity
        cart_price = int(cart.price)
        cart.amount = int(quantity) * cart_price
        product = Product.objects.filter(id=cart.product_id.id).get()
        product.quantity= int(product.quantity)-(int(quantity)-before)
        product.save()
        cart.save()
    total_data = Cart.objects.filter(user_id=request.session['admin_id']).values('amount')
    total=0
    for t in total_data:
        total = total+ int(t['amount'])
    return render (request, 'cart.html',{'rows':data,'total':total})
def add_cart(request,product_id):
    if 'admin_id' not in request.session:
        return redirect('/login')
    try:
        cart = Cart.objects.get(user_id=request.session['admin_id'], product_id=product_id)
        return redirect('/cart')
    except Cart.DoesNotExist:
        profile = Profile.objects.filter(id=request.session['admin_id']).get()
        product = Product.objects.filter(id=product_id).get()
        if product.quantity >= 1 :
            obj = Cart(
                user_id = profile,
                product_id = product,
                qty = 1,
                price = product.price,
                amount = product.price
            )
            obj.save()
            product.quantity = product.quantity-1
            product.save()
            return redirect ('/cart')
        else:
            return redirect ('/single_product/'+str(product_id))
def cancle_cart(request,cart_id):
    cart = Cart.objects.filter(id=int(cart_id)).get()
    product = Product.objects.get(id=cart.product_id.id)
    product.quantity = product.quantity + cart.qty
    product.save()
    cart.delete()
    return redirect('/cart')
def checkout(request):
    return render (request, 'checkout.html')
def coming_soon(request):
    return render (request, 'coming-soon.html')
def contact(request):
    return render (request, 'contact.html')
def error(request):
    return render (request, 'error.html')
def faqs(request):
    return render (request, 'faqs.html')
# ---------------- index -------------------
def index(request):
    data = Slider.objects.all()
    cats = Category.objects.all()
    product = Product.objects.all()
    return render (request, 'index.html',{'rows':data,'cats':cats,'product':product})
# -------------- login ---------------------
def login(request):
    if 'admin_id' in request.session:
        return redirect ('/profiles')
    msg = ""
    fromobj = UserForm()
    if 'submit' in request.POST:
        fromobj = UserForm(request.POST)
        fromobj.save()
        return redirect('/login')
    if 'save' in request.POST:
        g_email = request.POST['email']
        g_password = request.POST['password']
        obj = User.objects.filter(email=g_email,password=g_password)
        if obj.count()==1:
            row = obj.get()
            if row.status == 'active':
                request.session['admin_id'] = row.id
                return redirect ('/profiles')
            else:
                msg = "Your account is Blocked"
        else :
            msg = "Please Enter Valid Email Or Password"
    return render (request, 'login.html',{'data':fromobj,'msg':msg})
# --------------- profiles -------------------
def profiles(request):
    con_id = request.session['admin_id']
    data = User.objects.filter(id=con_id).get()
    obj = UserForm(instance=data)
    if 'submit' in request.POST:
        obj = UserForm(request.POST,instance=data)
        obj.save()
        return redirect ('/profiles') 
    return render (request, 'profiles.html',{'row':data,'data':obj})
# ----------------- logout -------------------
def logouts(request):
    del request.session['admin_id']
    return redirect ('/index')
def shop_grid(request):
    return render (request, 'shop-grid.html')
def shop_list(request):
    return render (request, 'shop-list.html')
def shop_slider(request):
    return render (request, 'shop-slider.html')
# -------------- shop -----------------
def shop(request):
    category = Category.objects.all()
    product = Product.objects.all()
    tag = Tag.objects.all()
    brand = Brand.objects.all()
    return render (request, 'shop.html',{'category':category,'product':product,'tag':tag})
def single_post(request):
    return render (request, 'single-post.html')
# ------------------ single product -----------------
def single_product(request,product_id):
    product = Product.objects.filter(id=product_id).get()
    return render (request, 'single-product.html',{'product':product})
def buy(request,product_id):
    user = User.objects.filter(id=request.session['admin_id']).get()
    user_data = Users_Form(instance=user)
    if 'submit' in request.POST:
        user_data = Users_Form(request.POST,instance=User)
        user_data.save()
    return render (request, 'checkout.html',{'data':user_data})
def styles(request):
    return render (request, 'styles.html')
def thank_you(request):
    return render (request, 'thank-you.html')
# ------------------  Wishlist --------------------
def wishlist(request):
    if 'admin_id' not in request.session:
        return redirect('/login')
    user_id = request.session['admin_id']
    profile = Profile.objects.filter(id=user_id).get()
    wishlist = Wishlist.objects.filter(user_id=profile)
    return render (request, 'wishlist.html',{'data':wishlist})
def add_wishlist(request,product_id):
    product = Product.objects.filter(id=product_id).get()
    user = Profile.objects.filter(id=request.session['admin_id']).get()
    wishlist =Wishlist(
        wishlist = product,
        user_id = user
    )
    wishlist.save()
    return redirect('/wishlist')
def cancle_wishlist(request,wishlist_id):
    Wishlist.objects.filter(id=wishlist_id).delete()
    return redirect ('/wishlist')
