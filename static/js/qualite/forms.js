document.addEventListener("DOMContentLoaded", () => {
    let pcFormBtn = document.querySelector("#show-pc-form")
    let microFormBtn = document.querySelector("#show-micro-form")
    let metroFormBtn = document.querySelector("#show-metro-form")
    let prodFormBtn = document.querySelector("#show-prod-form")

    pcFormBtn.addEventListener('click', togglePcForm)
    microFormBtn.addEventListener('click', toggleMicroForm)
    metroFormBtn.addEventListener('click', toggleMetroForm)
    prodFormBtn.addEventListener('click', toggleProdForm)
})

function togglePcForm(event) {
    let pcForm = document.querySelector("#form-pc")
    
    if (pcForm.style.display == 'none' || pcForm.style.display == '') {
        pcForm.style.display = 'block'

        let pcAnnulerBtn = document.querySelector(".annuler-pc")
        pcAnnulerBtn.addEventListener('click', togglePcForm)
    } else {
        pcForm.style.display = 'none'
    }
}

function toggleMetroForm(event) {
    let metroForm = document.querySelector("#form-metro")
    
    if (metroForm.style.display == 'none' || metroForm.style.display == '') {
        metroForm.style.display = 'block'

        let metroAnnulerBtn = document.querySelector(".annuler-metro")
        metroAnnulerBtn.addEventListener('click', toggleMetroForm)
    } else {
        metroForm.style.display = 'none'
    }
}

function toggleMicroForm(event) {
    let microForm = document.querySelector("#form-micro")
    
    if (microForm.style.display == 'none' || microForm.style.display == '') {
        microForm.style.display = 'block'

        let microAnnulerBtn = document.querySelector(".annuler-micro")
        microAnnulerBtn.addEventListener('click', toggleMicroForm)
    } else {
        microForm.style.display = 'none'
    }
}

function toggleProdForm(event) {
    let prodForm = document.querySelector("#form-prod")
    
    if (prodForm.style.display == 'none' || prodForm.style.display == '') {
        prodForm.style.display = 'block'

        let prodAnnulerBtn = document.querySelector(".annuler-prod")
        prodAnnulerBtn.addEventListener('click', toggleprodForm)
    } else {
        prodForm.style.display = 'none'
    }
}