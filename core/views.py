from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterForm, ContactForm

from .models import Newsletter

from django.http import JsonResponse

# def newsletter_signup(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         if email:
#             if not Newsletter.objects.filter(email=email).exists():
#                 Newsletter.objects.create(email=email)
#                 return JsonResponse({'status': 'success', 'message': 'Vous êtes inscrit à la newsletter!'})
#             else:
#                 return JsonResponse({'status': 'info', 'message': 'Cet email est déjà inscrit à la newsletter.'})
#         else:
#             return JsonResponse({'status': 'error', 'message': 'Veuillez fournir une adresse email valide.'})
#     return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée'}, status=405)

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # Vérifiez si l'email existe déjà
            if not Newsletter.objects.filter(email=email).exists():
                Newsletter.objects.create(email=email)
                messages.success(request, 'Vous êtes inscrit à la newsletter!')
            else:
                messages.info(request, 'Cet email est déjà inscrit à la newsletter.')
        else:
            messages.error(request, 'Veuillez fournir une adresse email valide.')
        return redirect('core:home')  # ou toute autre page où vous voulez rediriger l'utilisateur
    return redirect('core:home')  # Si quelqu'un accède à cette URL directement sans POST



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a été envoyé!')
            return redirect('core:home')  # Assurez-vous d'avoir une vue 'home'
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})



def homeView(request):
    return render(request, 'core/home.html')
