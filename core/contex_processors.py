from .models import Salon


def categories(request):
    return {
        'salons': Salon.objects.all()
    }