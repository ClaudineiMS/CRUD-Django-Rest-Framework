from django.shortcuts import ( render, get_object_or_404, redirect, HttpResponseRedirect ) 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Grupos
from .models import Usuarios
from .forms import GruposForm
from .forms import UsuariosForm
from .forms import GruposFormEdit
from .forms import UsuariosFormEdit

def home(request):
    return render(request, 'home.html')

def usuarios_create(request):
    form = UsuariosForm

    if(request.method == 'POST'):

        form = UsuariosForm(request.POST)

        if(form.is_valid()):
            usuarios_nome_completo = form.cleaned_data['nome_completo']
            usuarios_idade = form.cleaned_data['idade']
            usuarios_sexo = form.cleaned_data['sexo']
            usuarios_email = form.cleaned_data['email']
            usuarios_telefone = form.cleaned_data['telefone']
            usuarios_pais = form.cleaned_data['pais']
            usuarios_estado = form.cleaned_data['estado']
            usuarios_cidade = form.cleaned_data['cidade']
            usuarios_bairro = form.cleaned_data['bairro']
            usuarios_logradouro = form.cleaned_data['logradouro']
            usuarios_status = form.cleaned_data['status']
            usuarios_grupos = form.cleaned_data['grupo']

            new_post = Usuarios(nome_completo = usuarios_nome_completo, idade = usuarios_idade, sexo = usuarios_sexo,
            email = usuarios_email, telefone = usuarios_telefone, pais = usuarios_pais, estado = usuarios_estado,
            cidade = usuarios_cidade, bairro = usuarios_bairro, logradouro = usuarios_logradouro, status = usuarios_status, 
            grupo = usuarios_grupos)
            new_post.save()

            return redirect('home')

        #elif(request.method == 'GET'):
    return render(request, 'cadastro_usuario.html', {'form': form})

def grupos_create(request):

    form = GruposForm()

    if(request.method == 'POST'):

        form = GruposForm(request.POST)

        if(form.is_valid()):
            grupos_nome = form.cleaned_data['titulo']
            grupos_descricao = form.cleaned_data['descricao']
            grupos_status = form.cleaned_data['status']
            grupos_criado = form.cleaned_data['criado']


            new_post = Grupos(titulo = grupos_nome, descricao = grupos_descricao, status = grupos_status, criado = grupos_criado)
            new_post.save()
            

            return redirect('home')

        #elif(request.method == 'GET'):
    return render(request,  'cadastra_grupo.html', {'form': form})


def grupos_consulta(request):
    if ( request.method == 'GET'):
        lista ={}
        lista["dataset"] = Grupos.objects.all()
        return render(request, 'consulta_gupo.html', lista)
   
def usuarios_consulta(request):
    if ( request.method == 'GET'):
        lista ={}
        lista["dataset"] = Usuarios.objects.all()
        return render(request, 'consulta_usuario.html', lista)


def grupo_deletar(request,id):
    #lista = {}
    #lista["dataset"] = Grupos.objects.all()
    obj = get_object_or_404(Grupos, id_grupo = id)
    #if request.method =="POST":
    obj.delete()
    return redirect('grupos_consulta_excluir')
    #return render(request, "excluir_grupo.html")


def usuario_deletar(request,id):
    #lista = {}
    #lista["dataset"] = Usuarios.objects.all()
    obj = get_object_or_404(Usuarios, id_user = id)
    #if request.method =="POST":
    obj.delete()
    return redirect('usuarios_consulta_excluir')
    #return render(request, "excluir_usuario.html", lista)


def detail_view(request, id):
    context ={}
    context["data"] = Grupos.objects.get(id_grupo = id)
    return render(request, "detail_view.html", context)


def update_view(request, id):
    context ={}
    obj = get_object_or_404(Grupos, id_grupo = id)
    form = GruposFormEdit(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('grupos_consulta_edit')
    context["form"] = form
 
    return render(request, "update_view.html", context)


def update_view_user(request, id):
    context ={}
    obj = get_object_or_404(Usuarios, id_user = id)
    form = UsuariosFormEdit(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('usuarios_consulta_edit')
    context["form"] = form
 
    return render(request, 'update_view_user.html', context)


def grupos_consulta_edit(request):
    lista ={}
    lista["dataset"] = Grupos.objects.all()
    return render(request, 'editar_grupo.html', lista)

   
def usuarios_consulta_edit(request):
    lista ={}
    lista["dataset"] = Usuarios.objects.all()
    return render(request, 'editar_usuario.html', lista)


def grupos_consulta_excluir(request):
    lista ={}
    lista["dataset"] = Grupos.objects.all()
    return render(request, 'excluir_grupo.html', lista)


   
def usuarios_consulta_excluir(request):
    lista ={}
    lista["dataset"] = Usuarios.objects.all()
    return render(request, 'excluir_usuario.html', lista)