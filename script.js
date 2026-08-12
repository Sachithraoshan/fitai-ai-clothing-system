function recommend() {

    const type =
        document.getElementById("type").value;

    const size =
        document.getElementById("size").value;

    const color =
        document.getElementById("color").value;

    const style =
        document.getElementById("style").value;

    const budget =
        Number(document.getElementById("budget").value);


    let scoredProducts = [];


    products.forEach(product => {

        if (!product.stock)
            return;


        let score = 0;


        // Size is very important

        if (product.size === size)
            score += 30;


        // Clothing type

        if (product.type === type)
            score += 25;


        // Style

        if (product.style === style)
            score += 20;


        // Color

        if (product.color === color)
            score += 15;


        // Budget

        if (product.price <= budget)
            score += 10;


        scoredProducts.push({

            ...product,

            score: score

        });

    });


    // Highest score first

    scoredProducts.sort(
        (a, b) => b.score - a.score
    );


    // Only show top 3

    const recommendations =
        scoredProducts.slice(0, 3);


    displayProducts(recommendations);
}



function displayProducts(products) {

    const results =
        document.getElementById("results");


    if (products.length === 0) {

        results.innerHTML = `

        <div class="no-results">

            <h3>No suitable products found</h3>

            <p>
                Try changing your preferences.
            </p>

        </div>
        `;

        return;
    }


    let output = "";


    products.forEach(product => {

        output += `

        <div class="product-card">

            <img
                src="${product.image}"
                class="product-image"
                alt="${product.name}"
            >

            <div class="product-info">

                <span class="match">
                    ${product.score}% Match
                </span>

                <h3>
                    ${product.name}
                </h3>

                <div class="price">
                    Rs. ${product.price.toLocaleString()}
                </div>

                <div class="details">

                    Size: ${product.size}<br>

                    Color: ${product.color}<br>

                    Style: ${product.style}

                </div>


                <div class="card-buttons">

                    <button
                        class="try-button"
                        onclick="tryAI(${product.id})">

                        ✨ AI Try-On

                    </button>


                    <button
                        class="cart-button"
                        onclick="addCart(${product.id})">

                        Add Cart

                    </button>

                </div>

            </div>

        </div>

        `;

    });


    results.innerHTML = output;

}



function tryAI(productID) {

    const selectedProduct = products.find(
        product => product.id === productID
    );

    localStorage.setItem(
        "selectedProduct",
        JSON.stringify(selectedProduct)
    );

    window.location.href = "tryon.html";
}
function addCart(productID) {
    alert("Product added to cart!");
}
