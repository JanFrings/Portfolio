from django.views.generic import TemplateView
from django.http import HttpResponse
from wsgiref.util import FileWrapper

from django.http import FileResponse
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

class ProjectsView(TemplateView):
    template_name = 'projects.html'

class PortfolioView(TemplateView):
    template_name='portfolio.html'

class TestView(TemplateView):
    template_name = 'registration/test.html'

class ThanksView(TemplateView):
    template_name = 'registration/thanks.html'

def resume_download(request):
    response = FileResponse(open('static/documents/Frings_Resume.pdf', 'rb'), as_attachment=True)
    return response
