import os
import shutil

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config,view_defaults
import transaction
from .models import User, Session, Product
from random import randint


@view_config(route_name='home', renderer='templates/index.pt')
def home(request):
    return {}
@view_config(route_name='adminPanel', renderer='templates/adminPanel.pt')
def adminPanel(request):
    return{}
@view_config(route_name='productInsert', renderer='templates/productInsert.pt')
def productInsert(request):
#       ##Get from DB
    if 'submitProduct' in request.params:
        Pname = request.params['Pname']
        description = request.params['tozihat']
        price = request.params['price']
        state = request.params['state']
        # pic = request.params['state']
        p = Session.query(Product.product_id).count()
        p+=randint(0, 10000)
        x= "aks"+str(p)+".jpg"
        filename = request.POST['aks'].filename
        input_file = request.POST['aks'].file
        file_path = os.path.join('tutorial/templates/img/up/',x)
        y="tutorial:templates/img/up/"+x;
        aks=y
        temp_file_path = file_path + '~'
        input_file.seek(0)
        with open(temp_file_path, 'wb') as output_file:
            shutil.copyfileobj(input_file, output_file)
        os.rename(temp_file_path, file_path)
        Session.add(Product(Pname=Pname,description=description,pic=aks,price=price,state=state))
        transaction.commit()
        return HTTPFound('/productList')
    return dict()

@view_config(route_name='productList', renderer='templates/productList.pt')
def productList(request):
    ProductList = Session.query(Product).all()
    return dict(ProductList=ProductList)

@view_config(route_name='reg', renderer='templates/forms/reg/index.pt')
def reg(request):
    if 'form.submitted' in request.params:
        name = request.params['name']
        lname = request.params['lname']
        jensiyat = request.params['jensiyat']
        phone = request.params['phone']
        email = request.params['email']
        address = request.params['address']
        username = request.params['username']
        password = request.params['password']
        Session.add(User(name=name, lname=lname, jensiyat=jensiyat, phone=phone, email=email, address=address,
                         username=username, password=password))
        transaction.commit()
        return HTTPFound('/login')
    return dict()
@view_config(route_name='productList', renderer='templates/productList.pt')
def productList(request):
    ProductList = Session.query(Product).all()
    return dict(ProductList=ProductList)

def __init__(request):
        logged_in = request.authenticated_userid


@view_config(route_name='reg', renderer='templates/forms/reg/index.pt')
def reg(request):
    if 'form.submitted' in request.params:
        name = request.params['name']
        lname = request.params['lname']
        jensiyat = request.params['jensiyat']
        phone = request.params['phone']
        email = request.params['email']
        address = request.params['address']
        username = request.params['username']
        password = request.params['password']
        Session.add(User(name=name, lname=lname, jensiyat=jensiyat, phone=phone, email=email, address=address,
                         username=username, password=password))
        transaction.commit()
        return HTTPFound('/login')
    return dict()


@view_config(route_name='login', renderer='templates/forms/login/index.pt')
def login(request):
    login_url = request.route_url('login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/'  # never use login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    message = ''
    login = ''
    password = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        if check_password(password, USERS.get(login)):
            headers = remember(request, login)
            return HTTPFound(location=came_from,
                             headers=headers)
        message = 'Failed login'

    return dict(
        name='Login',
        message=message,
        url=request.application_url + '/login',
        came_from=came_from,
        login=login,
        password=password,
    )

#
# @view_config(route_name='logout')
# def logout(request):
#     request = request
#     headers = forget(request)
#     url = request.route_url('home')
#     return HTTPFound(location=url,
#                      headers=headers)  # @view_config(route_name='logout')
# def logout(request):
# headers = forget(request)
#     loginpage = route_url('login', request)
#     return HTTPFound(location=loginpage, headers=headers)
