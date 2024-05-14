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



// // Get the search input field and button
// const searchInput = document.getElementById('search-input');
// const searchBtn = document.getElementById('search-btn');
//
// // Get all movie and TV show cards
// const movieCards = document.querySelectorAll('.movies-card');
//
// // Add event listener to the search button
// searchBtn.addEventListener('click', searchMoviesAndTVShows);
//
// // Function to search movies and TV shows
// function searchMoviesAndTVShows() {
//     const searchTerm = searchInput.value.trim().toLowerCase();
//     movieCards.forEach((card) => {
//         const title = card.querySelector('h5').textContent.toLowerCase();
//         if (title.includes(searchTerm)) {
//             card.style.display = 'block';
//         } else {
//             card.style.display = 'none';
//         }
//     });
// }

// Search function
// function searchMovies() {
//     var input, filter, movies, cards, title, i;
//     input = document.getElementById('searchInput');
//     filter = input.value.toUpperCase();
//     movies = document.querySelectorAll('.movies-card');
//
//     movies.forEach(function(movie) {
//         title = movie.querySelector('h5');
//         if (title.innerText.toUpperCase().indexOf(filter) > -1) {
//             movie.classList.add('show');
//         } else {
//             movie.classList.remove('show');
//         }
//     });
// }
//
// // Add event listener
// document.getElementById('searchInput').addEventListener('input', searchMovies);

//
// $('#search-input').keyup(function(){
//     var searchText = $(this).val().toLowerCase();
//     $('#LatestMovie tbody tr').each(function(){
//         var rowData = $(this).find('td:first-child').text().toLowerCase();
//         if(rowData.indexOf(searchText) !== -1) {
//             $(this).show();
//         } else {
//             $(this).hide();
//         }
//     });
// });
