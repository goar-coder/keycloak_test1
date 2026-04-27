from django.contrib.auth.middleware import RemoteUserMiddleware

class XForwardedUserMiddleware(RemoteUserMiddleware):
    # header = 'HTTP_X_FORWARDED_EMAIL'  # ← email, no user (que es el UUID)
    header = 'HTTP_X_FORWARDED_PREFERRED_USERNAME'  # ← django_user
    # header = 'HTTP_X_FORWARDED_USER'
