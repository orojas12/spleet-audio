"use strict";

const inputFile = document.querySelector('#input_file');
const btnSubmit = document.querySelector('#submit');
const form = document.querySelector('#upload')

const postData = async function(url, data={}) {
    const response = await fetch(url, {
        method: 'POST',
        body: data
    })
    return response;
}

form.addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = new FormData(form);

    // set loading wheel
    
    const response = await postData('http://127.0.0.1:5000/spleet', formData);

    // remove loading wheel

    console.log(response)
})