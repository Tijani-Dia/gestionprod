document.addEventListener("DOMContentLoaded", () => {
    let casseListingBtn = document.querySelectorAll(".show-casse-fixture")

    casseListingBtn.forEach(btn => {
        btn.addEventListener('click', toggleCasseListing)
    });
})

function toggleCasseListing(event) {
    let clicked = event.currentTarget
    let casseListing = clicked.parentElement.parentElement.nextElementSibling 

    casseListing.style.display = 'block'

    let casseAnnulerBtn = casseListing.querySelector(".hide-fixture")
    casseAnnulerBtn.addEventListener('click', hideCasseListing)
}

function hideCasseListing(event) {
    let clicked = event.currentTarget
    let casseListing = clicked.parentElement.parentElement
    casseListing.style.display = 'none'
}