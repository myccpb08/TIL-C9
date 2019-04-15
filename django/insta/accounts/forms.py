from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm): # UserChangeForm 을 상속받아서 custom 하겠다
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name','last_name',] #수정 하고 싶은 4가지