from django.shortcuts import render
from .forms import ImagemForm
from .reconhecimento import analisar_imagem
from django.contrib import messages

# Create your views here.

def salvar_imagem(request):
    form = ImagemForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            imagem = form.save(commit=False)
            imagem.save()
            valor = analisar_imagem()
            print(valor)
            if valor == True:
                messages.success(request, 'Uma Face foi reconhecida com sucesso nesta imagem.')
            elif valor == False:
                messages.error(request,"Não foi detectada nenhuma face nesta imagem.")

    return render(request,'index.html',{'form':form})


