function displayProducts() {

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

                <h3>${product.name}</h3>

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
                        class="cart-button"
                        onclick="addCart(${product.id})"
                    >
                        Add to Cart
                    </button>

                </div>

            </div>

        </div>
        `;
    });

    document.getElementById("normalResults").innerHTML = output;
}


function addCart(productID) {

    alert("Product added to cart!");

}


displayProducts();
