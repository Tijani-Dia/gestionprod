document.addEventListener("DOMContentLoaded", () => {
    let microListingBtn = document.querySelectorAll(".show-micro-fixture")
    let microFormBtn = document.querySelectorAll(".show-micro-fixture-form")

    microListingBtn.forEach(btn => {
        btn.addEventListener('click', toggleMicroListing)
    });

    microFormBtn.forEach(btn => {
        btn.addEventListener('click', toggleMicroForm)
    });
})

function toggleMicroListing(event) {
    let clicked = event.currentTarget
    let microListing = clicked.parentElement.parentElement.nextElementSibling 
    let microForm = microListing.nextElementSibling
    
    if (microForm.style.display != 'none') {
        microForm.style.display = 'none'
    }

    microListing.style.display = 'block'

    let microAnnulerBtn = microListing.querySelector(".hide-fixture")
    microAnnulerBtn.addEventListener('click', hidemicroListing)

    let modifyListingBtn = microListing.querySelector(".modify-fixture")
    modifyListingBtn.addEventListener('click', modifymicroForm)
}

function hidemicroListing(event) {
    let clicked = event.currentTarget
    let microListing = clicked.parentElement.parentElement
    microListing.style.display = 'none'
}

function toggleMicroForm(event) {
    let clicked = event.currentTarget
    let microListing = clicked.parentElement.parentElement.nextElementSibling 
    let microForm = microListing.nextElementSibling
    
    if (microListing.style.display != 'none') {
        microListing.style.display = 'none'
    }
    
    microForm.style.display = 'block'

    let microAnnulerBtn = microForm.querySelector(".annuler-micro")
    microAnnulerBtn.addEventListener('click', hidemicroForm)
}

function hidemicroForm(event) {
    let clicked = event.currentTarget
    let microForm = clicked.parentElement.parentElement.parentElement
    microForm.style.display = 'none'
}

function modifymicroForm(event) {
    let clicked = event.currentTarget
    let microListing = clicked.parentElement.parentElement
    let microForm = microListing.nextElementSibling
    
    if (microListing.style.display != 'none') {
        microListing.style.display = 'none'
    }
    
    microForm.style.display = 'block'

    let microAnnulerBtn = microForm.querySelector(".annuler-micro")
    microAnnulerBtn.addEventListener('click', hidemicroForm)
}