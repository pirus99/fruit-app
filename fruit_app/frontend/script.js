async function getFruits() {
    let response = await fetch('http://127.0.0.1:8000/fruit_app/');
    let data = await response.json();
    console.log(data);
    return data;
}

getFruits()
    .then(fruits => {
        const fruitList = document.getElementById('fruitList');
        if (fruitList) {
            fruitList.innerHTML = '';
            fruits.forEach(fruit => {
                fruitList.innerHTML += `<li>${fruit.name} - Color: ${fruit.color}, Weight: ${fruit.weight}g</li>`;
            });
        } else {
            console.error("Element with id 'fruitList' not found in the DOM.");
        }
    })
    .catch(error => {
        console.error("Failed to fetch fruits:", error);
    });