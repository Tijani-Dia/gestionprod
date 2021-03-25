from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import (
    ParametresPhysicoChimiques,
    ParametresMicrobiologiques,
    ParametresMetrologiques,
    MachineEnsacheuse,
    get_latest_by_date_and_quart
)

from datetime import date


ALLOWED_USERS = ['Q', 'A', 'M']


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    user = request.user

    if user.user_role in ALLOWED_USERS:

        return render(request, 'suiviqualite/home.html')


@login_required(login_url='/login/')
def consult(request, parametre):
    if request.user.user_role in ALLOWED_USERS:

        ### PARAMETRES PHYSICO-CHIMIQUES ####
        if parametre == "physicochimique":
            latest = ParametresPhysicoChimiques.objects.all().order_by('-date')
            if len(latest) > 10:
                latest = latest[:10]

            context = {
                'latest': latest
            }

            return render(request, 'suiviqualite/pc-listing.html', context)


        ### PARAMETRES MICROBIOLOGIQUES ####
        elif parametre == "microbiologique":
            latest = ParametresMicrobiologiques.objects.all().order_by('-date')
            if len(latest) > 10:
                latest = latest[:10]

            context = {
                'latest': latest
            }

            return render(request, 'suiviqualite/micro-listing.html', context)


        ### PARAMETRES METROLOGIQUES ####
        elif parametre == "metrologique":

            context = {
                'latest': get_latest_by_date_and_quart()
            }

            return render(request, 'suiviqualite/metro-listing.html', context)

        


@login_required(login_url='/login/')
def submit(request, parametre):
    user = request.user
    context = {}
    if user.user_role in ALLOWED_USERS:
        controleur = user

        ### PARAMETRES PHYSICO-CHIMIQUES ####
        if parametre == "physicochimique":
            if request.method == "POST":
                
                chlore_libre = float(request.POST["chlore_libre"])
                chlore_total = float(request.POST["chlore_total"])
                turbidite = float(request.POST["turbidite"])
                ph = float(request.POST["ph"])
                durete = float(request.POST["durete"])
                nitrate = 0
                if request.POST["nitrate"]:
                    nitrate = float(request.POST["nitrate"])
                observation = request.POST["observation"]
                
                if "element_id" in request.POST:
                    element_id = request.POST["element_id"]                 
                    current_element = ParametresPhysicoChimiques.objects.get(id=element_id)
                    try:       
                        current_element.chlore_libre = chlore_libre                       
                        current_element.chlore_total = chlore_total                       
                        current_element.turbidite = turbidite
                        current_element.ph = ph
                        current_element.durete = durete
                        current_element.nitrate = nitrate
                        current_element.observation = observation
                        
                        current_element.save()                                            
                    except :
                        
                        context["error"] = """Une erreur s'est produite lors de
                            la validation du formulaire.
                            Veuillez réessayer SVP."""

                        return render(request, "notification.html", context)

                else:
                    
                    new = ParametresPhysicoChimiques(
                        controleur = controleur,
                        chlore_libre = chlore_libre,
                        chlore_total = chlore_total,
                        turbidite = turbidite,
                        ph = ph,
                        durete = durete,
                        nitrate = nitrate,
                        observation = observation
                    )

                    try:
                        new.save()
                        
                    except Exception as e :
                        context["error"] = "{}".format(e)

                        
                        return render(request, "notification.html", context)

                context["success"] = "Les données ont bien été enregistrées." 
                              
                return render(request, "notification.html", context)



        #### PARAMETRES MICROBIOLOGIQUES ####
        elif parametre == "microbiologique":
            if request.method == "POST":

                microorganismes_22 = float(request.POST["microorganismes_22"])
                microorganismes_36 = float(request.POST["microorganismes_36"])
                microorganismes_44 = float(request.POST["microorganismes_44"])
                coliformes_fecaux = float(request.POST["coliformes_fecaux"])
                coliformes_totaux = float(request.POST["coliformes_totaux"])
                e_coli = float(request.POST["e_coli"])
                pseudomonas = request.POST["pseudomonas"]
                observation = request.POST["observation"]

                if "element_id" in request.POST:
                    element_id = request.POST["element_id"]                 
                    current_element = ParametresMicrobiologiques.objects.get(id=element_id)
                    try:       
                        current_element.microorganismes_22 = microorganismes_22                       
                        current_element.microorganismes_36 = microorganismes_36                       
                        current_element.microorganismes_44 = microorganismes_44
                        current_element.coliformes_totaux = coliformes_totaux
                        current_element.coliformes_fecaux = coliformes_fecaux
                        current_element.e_coli = e_coli
                        current_element.pseudomonas = pseudomonas
                        current_element.observation = observation
                        
                        current_element.save()                                            
                    except :
                        
                        context["error"] = """Une erreur s'est produite lors de
                            la validation du formulaire.
                            Veuillez réessayer SVP."""

                        return render(request, "notification.html", context)
                
                else:
                    new = ParametresMicrobiologiques(
                        controleur = controleur,
                        microorganismes_22 = microorganismes_22,
                        microorganismes_36 = microorganismes_36,
                        microorganismes_44 = microorganismes_44,
                        coliformes_totaux = coliformes_totaux,
                        coliformes_fecaux = coliformes_fecaux,
                        e_coli = e_coli,
                        pseudomonas = pseudomonas,
                        observation = observation
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


        #### PARAMETRES METROLOGIQUES ###    
        elif parametre == "metrologique":
            if request.method == "POST":

                poids = float(request.POST["poids"])
                machine_code = request.POST["machine"]
                machine = MachineEnsacheuse.objects.filter(machine_code=machine_code)[0]
                quart = request.POST["quart"]
                observation = request.POST["observation"]

                if "element_id" in request.POST:
                    element_id = request.POST["element_id"]                 
                    current_element = ParametresMetrologiques.objects.get(id=element_id)
                    try:       
                        current_element.poids = poids                       
                        current_element.machine = machine                       
                        current_element.quart = quart
                        current_element.observation = observation
                        
                        current_element.save()                                            
                    except :
                        
                        context["error"] = """Une erreur s'est produite lors de
                            la validation du formulaire.
                            Veuillez réessayer SVP."""

                        return render(request, "notification.html", context)
                
                else:

                    new = ParametresMetrologiques(
                        controleur = controleur,
                        poids = poids,
                        machine = machine,
                        quart = quart,
                        observation = observation
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

                        