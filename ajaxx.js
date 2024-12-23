
let demo = document.getElementById("demo");
demo.addEventListener('click', loadDoc)



function loadDoc() {
    console.log("hello")
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'neww.txt', true);

    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 300) {
            // variable named textData(which the string is assigned as a object) , converts string to Js objects , recieves data from tnhe api as a string.
            var textData = JSON.parse(xhr.responseText);
            // Update the DOM with the quote
            document.getElementById('quote-container').innerHTML = '<p>"' + textData.content;
        } else {
            // Handle errors
            document.getElementById('quote-container').innerHTML = '<p>Failed to fetch quote. Please try again later.</p>';
        }
    };

    // Sending the request
    xhr.send(); 
}