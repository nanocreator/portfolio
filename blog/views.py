from django.views.generic import ListView, DetailView
from .models import Category, Articles


class ArticleListView(ListView):
    model = Articles
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'
