document.addEventListener("DOMContentLoaded", () => {
    let prodFormBtn = document.querySelector("#show-prod-form")
    let showCasseBtn = document.querySelectorAll(".show-casse")

    prodFormBtn.addEventListener('click', toggleProdForm)
    showCasseBtn.forEach(btn => {
        btn.addEventListener('click', toggleCasseForm)
    });
})



function toggleProdForm(event) {
    let prodForm = document.querySelector("#form-prod")
    
    if (prodForm.style.display == 'none' || prodForm.style.display == '') {
        prodForm.style.display = 'block'

        let prodAnnulerBtn = document.querySelector(".annuler-prod")
        prodAnnulerBtn.addEventListener('click', toggleProdForm)
    } else {
        prodForm.style.display = 'none'
    }
}

function toggleCasseForm(event) {
    let clicked = event.currentTarget
    let casseForm = clicked.parentElement.nextElementSibling
    clicked.style.display = 'none'
    casseForm.style.display = 'block'

    let casseAnnulerBtn = casseForm.querySelector(".annuler-casse")
    casseAnnulerBtn.addEventListener('click', hideCasseForm)
}

function hideCasseForm(event) {
    let clicked = event.currentTarget
    let casseForm = clicked.parentElement.parentElement.parentElement
    let showCasseBtn = casseForm.previousElementSibling.querySelector('.show-casse')
    casseForm.style.display = 'none'
    showCasseBtn.style.display = 'block'

}