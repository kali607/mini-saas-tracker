from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def get_user_info(request):
    user = request.user
    return JsonResponse({
        "id": user.id,
        "email": user.email,
        "username": user.username,
    })
