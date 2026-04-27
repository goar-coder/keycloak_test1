from django.http import HttpResponse

def test_view(request):
    # Debug temporal — borrar después
    import logging
    logger = logging.getLogger(__name__)
    logger.warning(f"HEADERS: { {k:v for k,v in request.META.items() if 'USER' in k or 'FORWARD' in k} }")
    
    if request.user.is_authenticated:
        user_info = f"""
            <h1>¡Funciona!</h1>
            <p>Estás logueado como: <strong>{request.user.username}</strong></p>
            <p>Email: {request.user.email}</p>
            <hr>
            <p>Este usuario fue autenticado por Keycloak y reconocido por Django.</p>
        """
    else:
        user_info = "<h1>No estás autenticado</h1>"
    
    return HttpResponse(user_info)