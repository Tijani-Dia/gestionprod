document.addEventListener("DOMContentLoaded", () => {
    let showPriseBtn = document.querySelectorAll(".show-prise")
    showPriseBtn.forEach(btn => {
        btn.addEventListener('click', togglePrise)
    });

    let showQuartBtn = document.querySelectorAll(".show-quart")
    showQuartBtn.forEach(btn => {
        btn.addEventListener('click', toggleQuart)
    });

    let showResultFormBtn = document.querySelectorAll(".modify-result")
    showResultFormBtn.forEach(btn => {
        btn.addEventListener('click', toggleResultForm)
    });

    let hideResultFormBtn = document.querySelectorAll(".annuler-metro")
    hideResultFormBtn.forEach(btn => {
        btn.addEventListener('click', hideResultForm)
    });
})

function togglePrise(event) {
    let clicked = event.currentTarget
    let priseBody = clicked.parentElement.nextElementSibling
    priseBody.style.display = 'block'

    let hidePriseBtn = priseBody.querySelector(".hide-prise")
    hidePriseBtn.addEventListener('click', hidePrise)
}

function hidePrise(event) {
    let clicked = event.currentTarget
    let priseBody = clicked.parentElement
    priseBody.style.display = 'none'
}

function toggleQuart(event) {
    let clicked = event.currentTarget
    let quartContainer = clicked.parentElement.nextElementSibling
    quartContainer.style.display = 'block'

    let hideQuartBtn = quartContainer.querySelector(".hide-quart")
    hideQuartBtn.addEventListener('click', hideQuart)
}

function hideQuart(event) {
    let clicked = event.currentTarget
    let quartContainer = clicked.parentElement
    quartContainer.style.display = 'none'
}

function toggleResultForm(event) {
    let clicked = event.currentTarget
    let resultForm = clicked.parentElement.nextElementSibling
    clicked.style.display = 'none'
    resultForm.style.display = 'block'
}

function hideResultForm(event) {
    let clicked = event.currentTarget
    let resultForm = clicked.parentElement.parentElement.parentElement
    resultForm.previousElementSibling.querySelector('.modify-result').style.display = 'block'
    resultForm.style.display = 'none'
}