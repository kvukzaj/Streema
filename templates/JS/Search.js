// Search function
function searchTitles() {
    // Get input value
    var input = document.getElementById("searchBar").value.toLowerCase();
    // Get all movie cards
    var cards = document.querySelectorAll(".movies-card");

    cards.forEach(function(card) {
        // Get title of each card
        var title = card.querySelector("h5").innerText.toLowerCase();
        // Check if title matches search input
        if (title.includes(input)) {
            card.style.display = "block"; // Show the card
        } else {
            card.style.display = "none"; // Hide the card
        }
    });
}

// Fetch movie titles from other pages
$(document).ready(function() {
    // Fetch titles from movies.html
    $.get("movies.html", function(data) {
        var titles = $(data).find("#movieSection h5").map(function() {
            return $(this).text().toLowerCase();
        }).get();
        sessionStorage.setItem("movieTitles", JSON.stringify(titles));
    });

    // Fetch titles from series.html
    $.get("series.html", function(data) {
        var titles = $(data).find("#movieSection h5").map(function() {
            return $(this).text().toLowerCase();
        }).get();
        sessionStorage.setItem("seriesTitles", JSON.stringify(titles));
    });
});
