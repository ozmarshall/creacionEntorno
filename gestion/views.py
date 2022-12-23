from rest_framework.decorators import api_view

@api_view(http_method_names=['GET', 'POST'])
def inicio(request):

    return{
        'message' : 'Bienvenido a mi Api de agenda'
    }