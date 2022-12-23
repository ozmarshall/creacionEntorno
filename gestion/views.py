from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView

@api_view(http_method_names=['GET', 'POST'])
def inicio(request : Request):

    print(request.method)
    print(request)

    if request.method == 'GET':

        return Response(data={
            'message' : 'Bienvenido a mi Api de agenda'
        })

    elif request.method == 'POST':
        return Response(data={
            'message' : 'Hiciste un post'
        },status=201)

class pruebaApiView(ListAPIView):
    serializer_class = None
