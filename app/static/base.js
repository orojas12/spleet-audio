"use strict";

const form = document.querySelector('#formUpload');
const btnSubmit = document.querySelector('#btnSubmit');
const spinner = document.querySelector('#spinner');

form.addEventListener('submit', function(e) {
    btnSubmit.classList.add('visually-hidden');
    spinner.classList.remove('visually-hidden');
})