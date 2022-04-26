from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.models import usuarios # tabla en base de datos
from users.forms import formularioRegistro, formularioLogin, filesForm # formulario para crear html
from django.core.mail import send_mail # envio de correos
from django.conf import settings # datos para el envio de correos
from django.core.files.storage import FileSystemStorage
import re
#import analizador as a

# Create your views here.

##################################################
class File_reading: # Lectura de archivo de texto extensión ".p2"
    def __init__(self):
        self.texto = []

    def lectura(self,name):
        if name[len(name) - 2:len(name)] == 'p2':
            file = open(name,'r')
            text = [line.split() for line in file]
            file.close()
            if len(text) == 1:
                self.texto = text[0]
            else:
                for i in range(len(text)):
                    self.texto += text[i]
            return self.texto		# Devuelve una lista con elementos como las palabras.
        else:
            print('Tipo de archivo no aceptado.')


class Analizador:
    def __init__(self):
        self.fechas = '-?\d+[/-]\d+[/-]\d+\.?\d*'	# fechas, aceptadas en ambos formatos, guiones y slash.
        self.enteros = '^\d+$'	# enteros.
        self.reales = '^\d+[.]\d+$'	# reales.
        self.cientificas = '^(\d+[.]\d+|\d+)[E]-?\d+$'	# notación científica aceptada con la "E"
        self.complejos = '^(\d+[.]\d+|\d+)[+-](\d+[.]\d+|\d+)[i]$'	# números complejos en notación z = a + bi
        self.palabras_clave = '(^|.)(Teorema|Matemática|Matemático|Hilbert|Turing|Análisis|Euler|Fermat|Pitágoras|Autómata|Boole|Cantor|Perelman|Experimentación|Físico|Física|Astronomía|Mecánica|Newton|Einstein|Galileo|Modelo|Tesla|Dinámica|Partículas)($|.)'	# Palabras clave a buscar relacionadas con física y matemática.


    def analizar(self,texto_splitted):
        if type(texto_splitted) == list:
            texto_fechas = [] # para almacenar el texto con fechas analizadas
            for i in range(len(texto_splitted)):
                fecha = re.match(self.fechas, texto_splitted[i])
                if fecha != None: # si encuentra una fecha le añade el código
                    texto_fechas.append('<font color="orange">' + texto_splitted[i] + '</font>')
                else: # sino, simplemente añade la palabra
                    texto_fechas.append(texto_splitted[i])
		# esto se realiza para cada expresión regular.
            texto_enteros = []
            for i in range(len(texto_fechas)):
                entero = re.match(self.enteros,texto_fechas[i])
                if entero != None:
                    texto_enteros.append('<font color="blue">' + texto_fechas[i] + '</font>')
                else:
                    texto_enteros.append(texto_fechas[i])

            texto_reales = []
            for i in range(len(texto_enteros)):
                real = re.match(self.reales,texto_enteros[i])
                if real != None:
                    texto_reales.append('<font color="green">' + texto_enteros[i] + '</font>')
                else:
                    texto_reales.append(texto_enteros[i])

            texto_cientificas = []
            for i in range(len(texto_reales)):
                cientific = re.match(self.cientificas,texto_reales[i])
                if cientific != None:
                    texto_cientificas.append('<font color="purple">' + texto_reales[i] + '</font>')
                else:
                    texto_cientificas.append(texto_reales[i])

            texto_complejos = []
            for i in range(len(texto_cientificas)):
                complex = re.match(self.complejos,texto_cientificas[i])
                if complex != None:
                    texto_complejos.append('<font color="red">' + texto_cientificas[i] + '</font>')
                else:
                    texto_complejos.append(texto_cientificas[i])

            texto_palabras_clave = []
            for i in range(len(texto_complejos)):
                keywords = re.match(self.palabras_clave,texto_complejos[i],re.IGNORECASE)
                if keywords:
                    texto_palabras_clave.append('<font color="gray">' + texto_complejos[i] + '</font>')
                else:
                    texto_palabras_clave.append(texto_complejos[i])
            return ' '.join(texto_palabras_clave)
        else:
            print('Objeto no analizable')
            return
##################################################

def inicio(request):
    return render(request, 'inicio.html')


def registro(request):
    if request.method == 'POST':
        formulario = formularioRegistro(request.POST)
        if formulario.is_valid(): # validar la informacion ingresada en el formulario
            infFormulario = formulario.cleaned_data # crear un diccionario con dicha informacion

            if email_existence(infFormulario) or nickname_existence(infFormulario): # si ya existen
                return render(request, 'registro.html',{'form':formulario}) # regreso a la pagina de registro
            elif (infFormulario['password'] == infFormulario['confPassword']):
                # ingreso de datos en base de datos
                user = usuarios(email = infFormulario['email'], nickname = infFormulario['nickname'],CUI = infFormulario['CUI'], carrera = infFormulario['carrera'], password = infFormulario['password'])
                user.save() # guardado

                print('Ok')
                # Envío de confirmacion de registro (PROBLEMAS CON GMAIL)
                ### send_mail('Registro','Su registro ha sido aprobado correctamente.', 'dsarceno69@gmail.com',[infFormulario['email']],fail_silently = False,)
                return redirect('/login/') # corroboracion de ingreso correcto
            else:
                return render(request, 'registro.html',{'form':formulario}) # regreso a la pagina de registro

    else:
        formulario = formularioRegistro()
    return render(request, 'registro.html',{'form':formulario}) # al ingresar al servidor, lleva a la pagina de registro

# Funciones ayuda
def email_existence(dict): # false si no existe ningun email igual en la base de datos
    y_n = True
    try:
        usuarios.objects.get(email = dict['email'])
    except usuarios.MultipleObjectsReturned:
        return y_n
    except usuarios.DoesNotExist:
        y_n = False
        return y_n
    return y_n


def nickname_existence(dict): # false si no existe ningun usuario con el mismo nickname
    y_n = True
    try:
        usuarios.objects.get(nickname = dict['nickname'])
    except usuarios.MultipleObjectsReturned:
        return y_n
    except usuarios.DoesNotExist:
        y_n = False
        return y_n
    return y_n

def password_existence(dict): # Como es poco probable que existan contraseñas iguales, se validará de esta forma
    y_n = True
    try:
        usuarios.objects.get(password = dict['password'])
    except usuarios.MultipleObjectsReturned:
        return y_n
    except usuarios.DoesNotExist:
        y_n = False
        return y_n
    return y_n


def login(request):
    if request.method == 'POST':
        formulario = formularioLogin(request.POST)
        if formulario.is_valid(): # validar la informacion ingresada en el formulario
            infFormulario = formulario.cleaned_data # crear un diccionario con dicha informacion
            print(email_existence(infFormulario), nickname_existence(infFormulario), password_existence(infFormulario))
            if email_existence(infFormulario) and nickname_existence(infFormulario) and password_existence(infFormulario): # si ya existen
                nickname = infFormulario['nickname']
                return redirect(f'/{nickname}/') # aceptacion del ingreso
            else:
                return render(request, 'ingreso.html',{'form':formulario}) # regreso a la pagina de ingreso

    else:
        formulario = formularioLogin()
    return render(request, 'ingreso.html',{'form':formulario}) # al ingresar al servidor, lleva a la pagina de ingreso




def upload(request, nickname):
    if request.method == 'POST':
        formulario = filesForm(request.POST, request.FILES)
        if formulario.is_valid():
            directory = '/home/diego/Documents/TrabajosSemestre5/Semestre5/Programación2/Trabajos/Practica3/Practica3/media/archivos/'

            formulario.save()
            infFormulario = formulario.cleaned_data
            nickname = infFormulario['nickname']
            uploaded_file = infFormulario['file']
            #print(uploaded_file)
            file_name = directory + uploaded_file.name

            readed = File_reading().lectura(file_name)
            print(readed)
            analyzed = Analizador().analizar(readed)

            file_analizado = f'<!DOCTYPE html> \n \
            <html lang="es" dir="ltr"> \n \
              <head> \n \
                <meta charset="utf-8"> \n \
                <title>Analizado</title> \n \
              </head> \n \
              <body> \n \
                <div style="text-align:center"> \n \
                    <h1>Texto Analizado</h1> \n \
                    <h5>Usuario {nickname}</h5> \n \
                      <table style="margin: 0 auto;"> \n \
                        {analyzed} \n \
                      </table> \n \
                    <a href="/{nickname}/">Subir Otro Archivo</a> \n \
                </div> \n \
              </body> \n \
            </html>'
            html_file = open('/home/diego/Documents/Trabajos/Semestre7/ProgramacionMatematica2/Practica3/Practica3/users/templates/texto_analizado_real.html','w')
            html_file.write(file_analizado)
            html_file.close()

            return render(request, 'texto_analizado_real.html')
    else:
        formulario = filesForm()
    return render(request, 'upload.html', {'form':formulario})



























# END
