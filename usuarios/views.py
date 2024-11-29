from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm, registroForm
from .models import Usuario
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import datetime
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q

# Create your views here.
@login_required
def create_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form=UsuarioForm()
    return render(request, 'usuarios/usuario_form.html',{'form':form})

def usuario_list(request):
    query= request.GET.get("q")
    if query:
        usuarios = Usuario.objects.filter(
            Q(nombre__icontains=query) | Q(apellidos__icontains=query)
        )
    else:
        usuarios=Usuario.objects.all()
    return render(request, 'usuarios/usuario_list.html',{'usuarios':usuarios})

@login_required
def update_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=usuario )
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/usuario_form.html', {'form':form, 'usuario':usuario})

@login_required
def delete_usuario(request, pk):
    usuario=get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuarios/usuario_confirm_delete.html', {'usuario':usuario})

def generar_pdf_usuario(request):
    response = HttpResponse(content_type='application/pdf') 
    #abrir = inline, descargar = attachment
    response['Content-Disposition'] = 'inline; filename="usuarios.pdf"'
    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.setTitle("Reporte de Usuarios")
    width, height = letter

    fecha_generacion= datetime.datetime.today().strftime("%d-%m-%Y")
    pagina_num = 1

    def agregar_pie_pag(pdf, pagina_num):
        pdf.setFont("Helvetica", 10)
        pdf.drawString(30,20, f"Fecha de generacion: {fecha_generacion}")
        pdf.drawString(width-100, 20, f"Pagina num. {pagina_num}")

    #CONTENIDO DEL PDF

    #Imagen
    image_path = os.path.join(settings.MEDIA_ROOT, 'img/Logo.png')
    if os.path.exists(image_path): # Si el archivo de imagen existe
        pdf.drawImage(image_path, 40, height - 50, width=72, height=35)
    else:
        print(f"Error: No se encuentra la imagen en {image_path}")

    #Titulo
    pdf.setFont("Helvetica-Bold", 14)
    texto="LISTA DE USUARIOS"
    ancho_texto = pdf.stringWidth(texto)
    x=(width-ancho_texto)/2
    pdf.drawString(x, height-40, texto)

    #Encabezado de la tabla 
    pdf.setFont("Helvetica-Bold", 12)
    encabezados = ["Nombre","Apellidos","Fecha de nac.","Usuario","Contraseña"]
    x_inicial=40
    y = height-80

    for i, encabezado in enumerate(encabezados):
        pdf.drawString(x_inicial + i * 110, y, encabezado)
    
    y-=10
    pdf.line(40, y, width-40, y)

    y-=20
    pdf.setFont("Helvetica", 12)
    query= request.GET.get("q")
    if query:
        usuarios = Usuario.objects.filter(
            Q(nombre__icontains=query) | Q(apellidos__icontains=query)
        )
    else:
        usuarios=Usuario.objects.all()
        
    for usuario in usuarios:
        pdf.drawString(40, y, usuario.nombre)
        pdf.drawString(150, y, usuario.apellidos)
        pdf.drawString(260, y, usuario.fecha_nac.strftime("%d-%m-%Y"))
        pdf.drawString(370, y, usuario.usuario)
        pdf.drawString(480, y, usuario.password)
        y-=20

        if y<=50:
            agregar_pie_pag(pdf, pagina_num)
            pdf.showPage()
            pdf.setFont("Helvetica",12)
            y = height-80
            for i, encabezado in enumerate(encabezados):
                pdf.drawString(x_inicial + i * 110, y, encabezado)
                y-=10
                pdf.line(40, y, width-40, y)
                y-=20
            pagina_num+=1


    y-=20
    agregar_pie_pag(pdf, pagina_num)

    pdf.showPage()
    pdf.save()
    return response

def register(request):
    if request.method == 'POST':
        form = registroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = registroForm()
    return render(request, 'registration/register.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')