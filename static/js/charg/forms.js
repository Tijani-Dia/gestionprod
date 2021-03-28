document.addEventListener("DOMContentLoaded", () => {
    let chargFormBtn = document.querySelector("#show-charg-form")
    chargFormBtn.addEventListener('click', toggleChargForm)

    let chargementForm = document.forms["chargement"]
    chargementForm.addEventListener('submit', submitForm)
})

async function submitForm(event) {
    event.preventDefault()
    let chargementForm = document.forms["chargement"]
    let chargementFormData = new FormData(chargementForm)
    
    let response = await fetch("soumettre/chargement/", {
        method: 'POST',
        body: chargementFormData
    });

    if (response.status == 201) {
        let result = await response.json()

        displayNotification(result["detail"], 'success')

        chargementForm.vehicule.value = ""
        chargementForm.bon_de_livraison.value = ""
        chargementForm.sacs_sortis.value = ""
        chargementForm.observation.value = ""
        window.scrollTo(0, 0)
    } else {
        let result = await response.json()
        displayNotification(result["detail"], 'error')
    }
}

function displayNotification(msg, selector) {
    let notifDiv = document.querySelector(`#${selector}`)
    let notifMsg = document.createElement("p")
    notifMsg.innerHTML = msg
    notifDiv.appendChild(notifMsg)

    setTimeout(() => {
        notifMsg.remove()
    }, 3000)
}



function toggleChargForm(event) {
    let chargForm = document.querySelector("#form-charg")
    
    if (chargForm.style.display == 'none' || chargForm.style.display == '') {
        chargForm.style.display = 'block'

        let chargAnnulerBtn = document.querySelector(".annuler-charg")
        chargAnnulerBtn.addEventListener('click', toggleChargForm)
    } else {
        chargForm.style.display = 'none'
    }
}