# ~*~ coding: utf-8 ~*~
import time

from django.conf import settings
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from django.views.generic.edit import FormView

from authentication.mixins import PasswordEncryptionViewMixin, AuthMixin
from authentication import errors

from common.utils import get_logger
from ... import forms
from ...utils import (
    get_user_or_pre_auth_user,
)

__all__ = ['UserVerifyPasswordView']

logger = get_logger(__name__)


class UserVerifyPasswordView(AuthMixin, FormView):
    template_name = 'users/user_password_verify.html'
    form_class = forms.UserCheckPasswordForm

    def form_valid(self, form):
        user = get_user_or_pre_auth_user(self.request)
        if user is None:
            return redirect('authentication:login')

        try:
            password = self.get_decrypted_password(username=user.username)
        except errors.AuthFailedError as e:
            form.add_error("password", _(f"Password invalid") + f'({e.msg})')
            return self.form_invalid(form)

        user = authenticate(request=self.request, username=user.username, password=password)
        if not user:
            form.add_error("password", _("Password invalid"))
            return self.form_invalid(form)

        self.mark_password_ok(user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        referer = self.request.META.get('HTTP_REFERER')
        next_url = self.request.GET.get("next")
        if next_url:
            return next_url
        else:
            return referer

    def get_context_data(self, **kwargs):
        context = {
            'user': get_user_or_pre_auth_user(self.request)
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)