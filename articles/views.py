from django.shortcuts import render
from articles.models import Article

# Create your views here.


def article_detail_view(request, id):
    if id is not None:
        article_detail_obj = Article.objects.get(id=id)

    context = {
        "detail_object": article_detail_obj
    }

    return render(request, "articles/detail.html", context)
