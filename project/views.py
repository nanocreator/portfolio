from django.views.generic import ListView, DetailView
from .models import Projet, Category


class ListeProjetsView(ListView):
    model = Projet
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class DetailProjetView(DetailView):
    model = Projet
    template_name = 'project/project_detail.html'
    context_object_name = 'project'

