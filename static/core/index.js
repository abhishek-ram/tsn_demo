// Get the star rating for the page
var starRating = Number(
    document.querySelector(".stars-outer").getAttribute("data-rating"));

// Set the number of stars using the rating
document.querySelector(".stars-inner").style.width = ((starRating / 5) * 100) + '%';