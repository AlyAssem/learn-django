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
    x = Article.objects.get(id=1)

    context = {
        "id": x.id,
        "title": x.title,
        "content": x.content
    }

    HOME_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HOME_STRING)
