from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from app.forms import NotaForm
from app.models import Nota


class NotaCreateView(CreateView):
    model = Nota
    form_class = NotaForm
    template_name = 'notas/notas.html'
    success_url = reverse_lazy('asys:nota_list')

    def form_valid(self, form):
        # Si necesitas hacer algo adicional antes de guardar la nota, hazlo aquí.
        return super().form_valid(form)

class NotaListView(LoginRequiredMixin, generic.ListView):
    model = Nota
    template_name = 'notas/lista.html'
    context_object_name = 'notas'
    ordering = ['-fecha_creacion']

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = [i.toJSON() for i in Nota.objects.all()]
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Servicio'
        context['create_url'] = reverse_lazy('asys:servicio_create')
        context['list_url'] = reverse_lazy('service_list')
        context['entity'] = 'Nota'
        return context