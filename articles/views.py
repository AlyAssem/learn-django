from django.shortcuts import render
from articles.models import Article

# Create your views here.


def article_create_view(request):
    # this method runs on both post and get for the given url
    context = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article_to_add = Article.objects.create(title=title, content=content)

        context['article_obj'] = article_to_add
        context['created'] = True

    return render(request, "articles/create.html", context)


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
