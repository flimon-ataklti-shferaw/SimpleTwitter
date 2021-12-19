from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class UserLoginForm(forms.Form):
    email = forms.EmailField(label='email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        #method 1 of using authentication
        user_obj = User.objects.filter(email=email).first()
        if not user_obj:
            raise forms.ValidationError("Invalid Credentials -- invalid email")
        else:
            if not user_obj.check_password(password):
                raise forms.ValidationError("Invalid Credentials --  invalid password")
        # method 2 of using authentication
        # the_user = authenticate(email=email, password=password)
        # if not the_user:
        #     raise forms.ValidationError("Invalid Credentials")

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('name', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'is_active', 'is_staff', 'is_admin')
