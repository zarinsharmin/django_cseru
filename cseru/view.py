from django.http import HttpResponse

def index(req):
    #return HttpResponse('Hello World')
    html_code = """
                    <h1> This is my First Django project </h1>
                    <p> This is paragraph tag... </p>
                """
    return HttpResponse(html_code)