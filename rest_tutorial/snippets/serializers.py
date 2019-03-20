from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

"""
Clase serializador Snippets
"""

"""
VVV --- CON LA CLASE SERIALIZER --- VVV

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    titulo = serializers.CharField(required = False, allow_blank = True, max_length=100)
    codigo = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required = False)
    lenguaje = serializers.ChoiceField(choices = LANGUAGE_CHOICES, default='python')
    estilo = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        Crea y devuelve una nueva instancia de 'Snippet', con la información validada.
   
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Actualiza y devuelve una instancia existente de 'Snippet', con la información validada.
   
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.codigo = validated_data.get('codigo', instance.codigo)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.lenguaje = validated_data.get('lenguaje', instance.lenguaje)
        instance.estilo = validated_data.get('estilo', instance.estilo)
        instance.save()
        return instance
"""

"""
VVV --- UTILIZANDO CLASE MODELSERIALIZER --- VVV

class SnippetSerializer(serializers.ModelSerializer):
    
    autor = serializers.ReadOnlyField(source = 'autor.username')

    class Meta:
        model = Snippet

        fields = ('id', 'titulo', 'codigo', 'linenos', 'lenguaje', 'estilo', 'autor', )

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta: 
        model = User
        fields = ('id', 'username', 'snippets')
"""

"""
VVV --- UTILIZANDO CLASE HYPERLINKEDMODELSERIALIZER --- VVV

"""
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    
    autor = serializers.ReadOnlyField(source = 'autor.username')
    remarcado = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet

        fields = ('url', 'id', 'titulo', 'codigo', 'linenos', 'lenguaje', 'estilo', 'autor', 'remarcado',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta: 
        model = User
        fields = ('url', 'id', 'username', 'snippets')

