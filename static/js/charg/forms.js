document.addEventListener("DOMContentLoaded", () => {
    let chargFormBtn = document.querySelector("#show-charg-form")
    chargFormBtn.addEventListener('click', toggleChargForm)
})



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