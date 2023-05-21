let clickCount = 0;

function showRecipes() {
    clickCount++;
    const element1 = document.getElementById("rec-1");
    const element2 = document.getElementById("rec-2");
    const element3 = document.getElementById("rec-3");

    if (clickCount === 1) {
        console.log("Hello");
        const element1DisplayStyle = getComputedStyle(element1).display;
        if (element1DisplayStyle === "none") {
            element1.style.display = "block";
        } else {
            element1.style.display = "none";
        }
    } else if (clickCount === 2) {
        const element2DisplayStyle = getComputedStyle(element2).display;
        if (element2DisplayStyle === "none") {
            element2.style.display = "block";
        } else {
            element2.style.display = "none";
        }
    } else if (clickCount === 3) {
        const element3DisplayStyle = getComputedStyle(element3).display;
        if (element3DisplayStyle === "none") {
            element3.style.display = "block";
        } else {
            element3.style.display = "none";
        }
    } else if (clickCount < 1 || clickCount > 3) {
        clickCount = 0;
        element1.style.display = "none";
        element2.style.display = "none";
        element3.style.display = "none";
    }
}


function togglePopup_1() {
    document.getElementById("popup-1").classList.toggle("active");
    document.querySelector("body").classList.toggle("popup-active");

    if (popup.classList.contains("active")) {
        const rect = popup.getBoundingClientRect();
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const left = window.innerWidth / 2 - rect.width / 2;
        const top = rect.top + scrollTop + rect.height / 2;
        popup.style.transform = `translate(${left}px, ${top}px) scale(1)`;
    } else {
        popup.style.transform = "translate(-50%, -50%) scale(0)";
    }
}

function togglePopup_2() {
    document.getElementById("popup-2").classList.toggle("active");
    document.querySelector("body").classList.toggle("popup-active");

    if (popup.classList.contains("active")) {
        const rect = popup.getBoundingClientRect();
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const left = window.innerWidth / 2 - rect.width / 2;
        const top = rect.top + scrollTop + rect.height / 2;
        popup.style.transform = `translate(${left}px, ${top}px) scale(1)`;
    } else {
        popup.style.transform = "translate(-50%, -50%) scale(0)";
    }
}

function togglePopup_3() {
    document.getElementById("popup-3").classList.toggle("active");
    document.querySelector("body").classList.toggle("popup-active");

    if (popup.classList.contains("active")) {
        const rect = popup.getBoundingClientRect();
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const left = window.innerWidth / 2 - rect.width / 2;
        const top = rect.top + scrollTop + rect.height / 2;
        popup.style.transform = `translate(${left}px, ${top}px) scale(1)`;
    } else {
        popup.style.transform = "translate(-50%, -50%) scale(0)";
    }
}

// function updateRecipeInformation(recipeNumber, recipeName, ingredients, instructions) {
//     // Update the recipe name
//     document.getElementById(`recipeName${recipeNumber}`).textContent = recipeName;

//     // Update the ingredients list
//     const ingredientsList = document.getElementById(`ingredientsList${recipeNumber}`);
//     ingredientsList.innerHTML = '';
//     ingredients.forEach(function (ingredient) {
//         const li = document.createElement('li');
//         li.textContent = ingredient;
//         ingredientsList.appendChild(li);
//     });

//     // Update the instructions list
//     const instructionsList = document.getElementById(`instructionsList${recipeNumber}`);
//     instructionsList.innerHTML = '';
//     instructions.forEach(function (instruction) {
//         const li = document.createElement('li');
//         li.textContent = instruction;
//         instructionsList.appendChild(li);
//     });
// }

// // Example of handling the fetch response
// fetch('/', {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/x-www-form-urlencoded'
//     },
//     body: 'ingredients=' + encodeURIComponent(ingredients)
// })
//     .then(response => response.json())
//     .then(data => {
//         // Update the recipe information in the HTML
//         updateRecipeInformation(1, data.recipeName, data.ingredients, data.instructions);
//     })
//     .catch(error => {
//         // Handle any errors
//         console.error('Error:', error);
//     });


