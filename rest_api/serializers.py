from rest_framework import serializers
from myapp.models import Categoria, Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['producto_id','nombre', 'categoria_id', 'precio']


class Categoria(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre']

        