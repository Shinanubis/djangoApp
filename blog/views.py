from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Article


def index(req):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    context = {'latest_article_list': latest_article_list}
    return render(req, 'blog/index.html', context)
    return HttpResponse(template.render(context, req))

def detail(req, article_id):
    return HttpResponse("You're looking at article %s." % article_id)