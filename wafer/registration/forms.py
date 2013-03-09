from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RegistrationFormHelper(FormHelper):
    form_method = 'post'
    form_action = reverse('registration_register')

    def __init__(self, *args, **kwargs):
        super(RegistrationFormHelper, self).__init__(*args, **kwargs)
        self.add_input(Submit('submit', 'Register'))


class LoginFormHelper(FormHelper):
    form_method = 'post'
    form_action = reverse('django.contrib.auth.views.login')

    def __init__(self, *args, **kwargs):
        super(LoginFormHelper, self).__init__(*args, **kwargs)
        # TODO: next field
        self.add_input(Submit('submit', 'Log in'))
