from rest_framework import serializers

from users.models import CustomUser


class ReadOnlyUserSerializer(serializers.ModelSerializer):
    ''' Сериалайзер для получения данных из модели CustomUser.

    Используем только необходимые поля.

    '''
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'is_active',
            'last_login',
            'is_superuser'
        ]


class WriteOnlyUserSerializer(serializers.ModelSerializer):
    '''Сериалайзер для записи данных в модель CustomUser.

    Используем только необходимые поля.

    '''
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'is_active'
            ]
