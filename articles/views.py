from django.shortcuts import render
from articles.models import Article

# Create your views here.


def article_search_view(request):
    query_dict = request.GET
    try:
        query = int(query_dict.get("q"))  # q is the name of the input field.
    except:
        query = None

    article_object = None
    if query is not None:
        article_object = Article.objects.get(id=query)

    context = {
        "detail_object": article_object
    }

    return render(request, "articles/search.html", context)


def article_detail_view(request, id):
    if id is not None:
        article_detail_obj = Article.objects.get(id=id)

    context = {
        "detail_object": article_detail_obj
    }

    return render(request, "articles/detail.html", context)
