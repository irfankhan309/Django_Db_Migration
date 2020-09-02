from django.shortcuts import render
from django.template import RequestContext


def handler404(request,exception):
    template = 'testApp/404.html'
    # response = render_to_response(template, {},
    #                               context_instance=RequestContext(request))
    # response.status_code = 404
    # return response

    return render(request, template, status=404)


def handler500(request):
    template = 'testApp/500.html'
    return render(request, template, status=500)



def index_Veiw(request):
    template = 'testApp/index.html'
    return render(request, template)
