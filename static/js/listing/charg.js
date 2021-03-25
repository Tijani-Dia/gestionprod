document.addEventListener("DOMContentLoaded", () => {
    let chargListingBtn = document.querySelectorAll(".show-charg-fixture")
    let chargFormBtn = document.querySelectorAll(".show-charg-fixture-form")

    chargListingBtn.forEach(btn => {
        btn.addEventListener('click', toggleChargListing)
    });

    chargFormBtn.forEach(btn => {
        btn.addEventListener('click', toggleChargForm)
    });
})

function toggleChargListing(event) {
    let clicked = event.currentTarget
    let chargListing = clicked.parentElement.parentElement.nextElementSibling 
    let chargForm = chargListing.nextElementSibling
    
    if (chargForm.style.display != 'none') {
        chargForm.style.display = 'none'
    }

    chargListing.style.display = 'block'

    let chargAnnulerBtn = chargListing.querySelector(".hide-fixture")
    chargAnnulerBtn.addEventListener('click', hidechargListing)

    let modifyListingBtn = chargListing.querySelector(".modify-fixture")
    modifyListingBtn.addEventListener('click', modifychargForm)
}

function hidechargListing(event) {
    let clicked = event.currentTarget
    let chargListing = clicked.parentElement.parentElement
    chargListing.style.display = 'none'
}

function toggleChargForm(event) {
    let clicked = event.currentTarget
    let chargListing = clicked.parentElement.parentElement.nextElementSibling 
    let chargForm = chargListing.nextElementSibling
    
    if (chargListing.style.display != 'none') {
        chargListing.style.display = 'none'
    }
    
    chargForm.style.display = 'block'

    let chargAnnulerBtn = chargForm.querySelector(".annuler-charg")
    chargAnnulerBtn.addEventListener('click', hidechargForm)
}

function hidechargForm(event) {
    let clicked = event.currentTarget
    let chargForm = clicked.parentElement.parentElement.parentElement
    chargForm.style.display = 'none'
}

function modifychargForm(event) {
    let clicked = event.currentTarget
    let chargListing = clicked.parentElement.parentElement
    let chargForm = chargListing.nextElementSibling
    
    if (chargListing.style.display != 'none') {
        chargListing.style.display = 'none'
    }
    
    chargForm.style.display = 'block'

    let chargAnnulerBtn = chargForm.querySelector(".annuler-charg")
    chargAnnulerBtn.addEventListener('click', hidechargForm)
}