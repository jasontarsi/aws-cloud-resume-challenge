const counter = document.querySelector(".counter-number");
async function updateCounter() {
    let response = await fetch("https://80xkmr79r7.execute-api.us-east-1.amazonaws.com/dev");
    let data = await response.json();
    counter.innerHTML = `This page has ${data} Views!`;
}

updateCounter();