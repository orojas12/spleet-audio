"use strict";

const prediction = document.querySelector('#prediction');
const predictionId = prediction.dataset['predictionId'];

prediction.addEventListener('click', (e) => {
  const file = e.target.dataset['name'];
  console.log(file);
})
