"use strict";

const inputFile = document.querySelector('#input_file');
const btnSubmit = document.querySelector('#submit');

btnSubmit.addEventListener('click', async function(e) {
    const file = inputFile.files[0];
    const data = new FormData();

    data.append('song', file, file.name);
    console.log(data.get('song'))
    // set loading wheel

    const response = await postData('http://127.0.0.1:5000/split', data);

    // remove loading wheel

    console.log(response)
})

const postData = async function(url, data={}) {
    const response = await fetch(url, {
        method: 'POST',
        body: data
    })
    return response;
}