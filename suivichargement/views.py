from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .models import FormulaireChargement

# Create your views here.
ALLOWED_USERS = ['C', 'A', 'M']


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    user = request.user

    if user.user_role in ALLOWED_USERS:

        return render(request, 'suivichargement/home.html')


@login_required(login_url='/login/')
def consult(request, parametre):
    if request.user.user_role in ALLOWED_USERS:

        if parametre == "chargement":
            latest = FormulaireChargement.objects.all().order_by('-date')
            if len(latest) > 10:
                latest = latest[:10]

            context = {
                'latest': latest
            }

            return render(request, 'suivichargement/charg-listing.html', context)


@login_required(login_url='/login/')
def submit(request, parametre):
    user = request.user
    context = {}
    if user.user_role in ALLOWED_USERS:
        controleur = user

        if parametre == "chargement" and request.method == "POST":

            vehicule = request.POST["vehicule"]
            bon_de_livraison = request.POST["bon_de_livraison"]
            sacs_sortis = request.POST["sacs_sortis"]

            bonus = False
            if request.POST["bonus"] != '':
                sent = request.POST["bonus"]
                if sent == 'True':
                    bonus = True
            
            if "element_id" in request.POST:
                
                element_id = request.POST["element_id"]                 
                current_element = FormulaireChargement.objects.get(id=element_id)
                try:       
                    current_element.vehicule = vehicule                       
                    current_element.bon_de_livraison = bon_de_livraison
                    current_element.sacs_sortis = sacs_sortis 
                    current_element.bonus = bonus 
                    current_element.save()                                            
                except :
                    
                    context["error"] = """Une erreur s'est produite lors de
                        la validation du formulaire.
                        Veuillez réessayer SVP."""

                    return render(request, "notification.html", context)
                
                context["success"] = "Les données ont bien été enregistrées."                        
                return render(request, "notification.html", context)

            else:
                
                new = FormulaireChargement(
                    controleur = controleur,
                    vehicule = vehicule,
                    bon_de_livraison = bon_de_livraison,
                    sacs_sortis = sacs_sortis,
                    bonus = bonus
                )
                
                try:
                    new.save()
                    
                except :
                    
                    context["error"] = """Une erreur s'est produite lors de
                        la validation du formulaire.
                        Veuillez réessayer SVP."""

                    return render(request, "notification.html", context)

            context["success"] = "Les données ont bien été enregistrées."                           
            return render(request, "notification.html", context)
