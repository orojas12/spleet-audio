"use strict";

const btnSubmit = document.querySelector('#btnSubmit');
const spinner = document.querySelector('#spinner');

btnSubmit.addEventListener('click', function(e) {
    btnSubmit.classList.add('visually-hidden');
    spinner.classList.remove('visually-hidden');
})