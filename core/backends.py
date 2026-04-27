from django.contrib.auth.backends import RemoteUserBackend

class KeycloakRemoteUserBackend(RemoteUserBackend):
    def authenticate(self, request, remote_user):
        user = super().authenticate(request, remote_user)
        if user and request:
            email = request.META.get('HTTP_X_FORWARDED_EMAIL', '')
            if email and not user.email:
                user.email = email
                user.save(update_fields=['email'])
        return user