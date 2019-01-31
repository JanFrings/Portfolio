from django.views.generic import TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

class ProjectsView(TemplateView):
    template_name = 'projects.html'

class TestView(TemplateView):
    template_name = 'registration/test.html'

class ThanksView(TemplateView):
    template_name = 'registration/thanks.html'
