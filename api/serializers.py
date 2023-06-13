from rest_framework.serializers import Serializer


class MySerializer(Serializer):
    class Meta:
        model = 'MyModel'
        field = '__all__'
