"""
Renders html pages to the browser
"""
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
    """
    takes in a request
    returns Html response
    """

    # the query set can be filtered and has many other functionalities from a normal list.
    article_queryset = Article.objects.all()

    context = {
        "articles": article_queryset,
    }

    HOME_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HOME_STRING)
