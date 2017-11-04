# @Author: 魏巍
# @Date:   2017-11-02T10:48:18+08:00
# @Email:  524314430@qq.com
# @Last modified by:   魏巍
# @Last modified time: 2017-11-04T14:56:16+08:00



from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Article
from .forms import NameForm,ArticleForm


def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'polls/index.html', context)

def detail(request, article_id,pk='id'):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'polls/detail.html', {'article': article})


def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArticleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArticleForm()

    return render(request, 'polls/article.html', {'form': form})
