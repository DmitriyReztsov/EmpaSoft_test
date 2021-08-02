from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ''' Переопределяем стандартный класс User
    на случай необходимости внесения изменений

    '''
    pass
