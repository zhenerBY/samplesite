from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Bb
from .models import Rubric
from .forms import BbForm


# ZHE вывыдим просто текст
# def index(request):
#     s = 'Список объявлений\n\n\n'
#     for bb in Bb.objects.order_by('-published'):
#         s += bb.title + '\n' + bb.content + '\n\n'
#     return HttpResponse(s, content_type='text/plain; charset=utf-8')

# ZHE рендерим низкоуровневыми инструментами
# def index(request):
#     template = loader.get_template('bboard/index.html')
#     bbs = Bb.objects.order_by('-published')
#     context = {'bbs': bbs}
#     return HttpResponse(template.render(context, request))

# ZHE рендер на основе сокращений
def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', {'bbs': bbs})


# ZHE вывод рубрик (1,2 и т.д.)
def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    # success_url = '/bboard/'
    #ZHE не указывать путь прямым способом
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.all()
        return context
