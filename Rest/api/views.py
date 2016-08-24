


# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

#from Rest.api.serializers import TiendaSerializer
#from Rest.api.serializers import ProductoSerializer

from Rest.models import sucursal, cliente, factura
from Rest.models import productos

#class Tienda(APIView):
 #   serializer_class=TiendaSerializer
  #  serializer_class=ProductoSerializer
   # def get(self, request, format=None):

#        tiendas= sucursal.objects.all()
 #       producto=productos.objects.all()

#        response=self.serializer_class(sucursal,many=True)
 #       return Response(response.data)
#tien=Tienda.as_view()

from Rest.models import sucursal
from rest_framework import viewsets
from .serializers import sucursalSerializer, productoSerializer, clienteSerializer, facturaSerializer



from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .permissions import IsOwnerOrReadOnly




class SucursalViewSet(viewsets.ModelViewSet):
    queryset = sucursal.objects.all()
    serializer_class=sucursalSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = productos.objects.all()
    serializer_class = productoSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class =clienteSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user
class FacturaViewSet(viewsets.ModelViewSet):
    queryset = factura.objects.all()
    serializer_class = facturaSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

