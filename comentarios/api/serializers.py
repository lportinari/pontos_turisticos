from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario


class ComentarioSeralizer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('usuario', 'comentario', 'data', 'aprovado')