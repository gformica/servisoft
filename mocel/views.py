# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from registroForm import loginForm
from mocel.models import *
from django.shortcuts import render as Render, redirect, get_object_or_404 as get404

@login_required(login_url='/mocel/login')
def index(request):
    usuario = request.user
    cliente = get404(Cliente, user=usuario)
    lista_productos = Producto.objects.filter(id_cliente=cliente)
    lista_afilia_prepago = Afilia.objects.filter(id_producto__in=lista_productos, vigente_afilia=True, id_plan__tipo_plan="prepago")
   
    lista_afilia_postpago = Afilia.objects.filter(id_producto__in=lista_productos, vigente_afilia=True, id_plan__tipo_plan="postpago")
    print lista_afilia_postpago
    print lista_productos
    lista_producto_postpago = []
    for afilia in lista_afilia_postpago:
	lista_producto_postpago.append(afilia.id_producto)
    lista_factura = Factura.objects.filter(id_producto__in=lista_producto_postpago) 	
    
	
    print "HOLA"	
    print lista_factura

#    for afilia in lista_afilia_postpago:
#	factura = Factura.objects.filter(id_producto__in=lista_afilia_postpago)
    
    #print lista_productos
    return Render(request, 'mocel/index.html', locals())

def login(request):
    print "Estoy en login"
    if not request.user.is_authenticated():
    	print "no estoy autenticado"
        if request.method == "POST":
            form = loginForm(request.POST)
	    print request.POST
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
                if user is not None:
		    print "holis"
                    if user.is_active:
                        auth_login(request, user)
                        return redirect('/index')
                else:
                    return Render(request,'mocel/inicioSesion.html',{'auth_err':'si',})
            else:
                return Render(request,'mocel/inicioSesion.html',{'auth_err':'si',})
        else:
            return Render(request,'mocel/inicioSesion.html',{})
    else:
	print request.user
        return Render(request,'mocel/inicioSesion.html',{'auth_usuario':request.user.first_name})

def logout(request):
	auth_logout(request)
	return redirect('/login')

