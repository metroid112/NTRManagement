from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Design


def index(request):
    return HttpResponse('Hello, world!')


def design_list(request):
    designs = Design.objects.order_by('-date')
    template = loader.get_template('design/design_list.html')
    context = {
        'designs': designs
    }
    return HttpResponse(template.render(context, request))


def design_detail(request, design_id):
    return HttpResponse(f'Design ID: {design_id}')
