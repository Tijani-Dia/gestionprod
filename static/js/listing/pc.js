document.addEventListener("DOMContentLoaded", () => {
    let pcListingBtn = document.querySelectorAll(".show-pc-fixture")
    let pcFormBtn = document.querySelectorAll(".show-pc-fixture-form")

    pcListingBtn.forEach(btn => {
        btn.addEventListener('click', togglePcListing)
    });

    pcFormBtn.forEach(btn => {
        btn.addEventListener('click', togglePcForm)
    });
})

function togglePcListing(event) {
    let clicked = event.currentTarget
    let pcListing = clicked.parentElement.parentElement.nextElementSibling 
    let pcForm = pcListing.nextElementSibling
    
    if (pcForm.style.display != 'none') {
        pcForm.style.display = 'none'
    }

    pcListing.style.display = 'block'

    let pcAnnulerBtn = pcListing.querySelector(".hide-fixture")
    pcAnnulerBtn.addEventListener('click', hidePcListing)

    let modifyListingBtn = pcListing.querySelector(".modify-fixture")
    modifyListingBtn.addEventListener('click', modifyPcForm)
}

function hidePcListing(event) {
    let clicked = event.currentTarget
    let pcListing = clicked.parentElement.parentElement
    pcListing.style.display = 'none'
}

function togglePcForm(event) {
    let clicked = event.currentTarget
    let pcListing = clicked.parentElement.parentElement.nextElementSibling 
    let pcForm = pcListing.nextElementSibling
    
    if (pcListing.style.display != 'none') {
        pcListing.style.display = 'none'
    }
    
    pcForm.style.display = 'block'

    let pcAnnulerBtn = pcForm.querySelector(".annuler-pc")
    pcAnnulerBtn.addEventListener('click', hidePcForm)
}

function hidePcForm(event) {
    let clicked = event.currentTarget
    let pcForm = clicked.parentElement.parentElement.parentElement
    pcForm.style.display = 'none'
}

function modifyPcForm(event) {
    let clicked = event.currentTarget
    let pcListing = clicked.parentElement.parentElement
    let pcForm = pcListing.nextElementSibling
    
    if (pcListing.style.display != 'none') {
        pcListing.style.display = 'none'
    }
    
    pcForm.style.display = 'block'

    let pcAnnulerBtn = pcForm.querySelector(".annuler-pc")
    pcAnnulerBtn.addEventListener('click', hidePcForm)
}