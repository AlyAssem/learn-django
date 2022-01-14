"""
Renders html pages to the browser
"""
from django.http import HttpResponse

HOME_STRING = """
<h1>hello world</h1>
"""


def home_view(request):
    """
    takes in a request
    returns Html response
    """

    return HttpResponse(HOME_STRING)
