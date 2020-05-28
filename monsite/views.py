from django.http import HttpResponse

def accueil(request):
    return HttpResponse("Bonjour, vous êtes dans la page d'accueil de PhotosHyperboliques.")