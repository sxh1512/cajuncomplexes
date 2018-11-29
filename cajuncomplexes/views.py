from django.http import HttpResponseRedirect

def redirect_to_app(request):
    return HttpResponseRedirect('/aptman/')