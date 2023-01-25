from django.views.generic.edit import FormView
from main import forms

class ViewFaleConosco(FormView):
    template_name = "fale_conosco.html"
    form_class = forms.FormFaleConosco
    success_url = "/"

    def form_valid(self, form):
        form.enviar_mensagem_por_email()
        return super().form_valid(form)
    
    # if request.method == 'POST':
     #   meu_campo = rquest.POST.get('meu_campo')
      #  formulario = forms.FormFaleConosco(request.POST)
       # nome = formulario['nome'].value() # Primeira forma, acessando por chave
       # nome = formulario.data['nome'] # Segunda forma, por chave
#
 #       if formulario.is_valid():
            #nome = formulario.cleaned_data['nome'] # Primeira forma
            #nome = formulario.instance.nome # Segunda forma