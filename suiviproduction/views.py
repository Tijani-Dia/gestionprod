from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import (
    FormulaireProduction, 
    get_latest_by_date_and_quart,
    FormulaireCasse
)


ALLOWED_USERS = ['P', 'A', 'M']

CASSE_PARAMS = [
    'casses_recues',
    'casses_traitees',
    'dotation_commerciaux',
    'dotation_personnel',
    'retour_commerciaux',
    'casse_reelle'
]


@login_required(login_url='/login/')
def index(request):
    user = request.user

    if user.user_role in ALLOWED_USERS:

        return render(request, 'suiviproduction/home.html')


@login_required(login_url='/login/')
def consult(request, parametre):
    if request.user.user_role in ALLOWED_USERS:

        if parametre == "production":
            context = {
                'latest': get_latest_by_date_and_quart()
            }

            return render(request, 'suiviproduction/prod-listing.html', context)

        elif parametre == "casse":
            latest = FormulaireCasse.objects.all().order_by('-date')
            if len(latest) > 10:
                latest = latest[:10]

            context = {
                'latest': latest
            }

            return render(request, 'suiviproduction/casse-listing.html', context)

    
@login_required(login_url='/login/')
def submit(request, parametre):
    user = request.user
    context = {}
    if user.user_role in ALLOWED_USERS:
        controleur = user

        if parametre == "production":
            if request.method == "POST":

                quart = request.POST["quart"]
                tickets = 0
                if "tickets" in request.POST:
                    tickets = int(request.POST["tickets"])

                sacs = 0
                if request.POST["sacs"] != '':
                    sacs = int(request.POST["sacs"])

                sacs_produits = sacs + (tickets * 50)
                
                if "element_id" in request.POST:
                    
                    element_id = request.POST["element_id"]                 
                    current_element = FormulaireProduction.objects.get(id=element_id)
                    try:       
                        current_element.quart_de_production = quart                       
                        current_element.sacs_produits = sacs_produits
                        
                        current_element.save()                                            
                    except :
                        
                        context["error"] = """Une erreur s'est produite lors de
                            la validation du formulaire.
                            Veuillez réessayer SVP."""

                        return render(request, "notification.html", context)

                else:
                    
                    new = FormulaireProduction(
                        controleur = controleur,
                        quart_de_production = quart,
                        sacs_produits = sacs_produits
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

        elif parametre in CASSE_PARAMS and request.method == 'POST':
            # Check if a casse form exists for the day
            if "element_id" in request.POST:
                current = FormulaireCasse.objects.get(id=request.POST["element_id"])

                try:
                    current_value = getattr(current, parametre) 
                    current_value += int(request.POST["{}".format(parametre)])
                    setattr(current, parametre, current_value)
                    current.save()
                except Exception as e:
                    context["error"] = e
                    return render(request, "notification.html", context)


                context["success"] = "Les données ont bien été enregistrées."
                return render(request, "notification.html", context)

            else :
                new = FormulaireCasse(controleur=controleur)
                try:
                    setattr(new, parametre, int(request.POST["{}".format(parametre)]))
                    new.save()
                except Exception as e:
                    context["error"] = e
                    return render(request, "notification.html", context)

                context["success"] = "Les données ont bien été enregistrées."
                return render(request, "notification.html", context)
                



