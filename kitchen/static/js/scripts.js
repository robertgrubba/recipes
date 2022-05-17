/*!
* Start Bootstrap - Business Casual v7.0.8 (https://startbootstrap.com/theme/business-casual)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-casual/blob/master/LICENSE)
*/
// Highlights current date on contact page
window.addEventListener('DOMContentLoaded', event => {
    const listHoursArray = document.body.querySelectorAll('.list-hours li');
    listHoursArray[new Date().getDay()].classList.add(('today'));
})

$("bookmark").click(function(e){
    e.preventDefault(); // this will prevent the anchor tag from going the user off to the link
    var bookmarkUrl = "http://eatinghealthyis.fun";
    var bookmarkTitle = "Eating Healthy is Fun!";

    if (window.sidebar) { // For Mozilla Firefox Bookmark
	window.sidebar.addPanel(bookmarkTitle, bookmarkUrl,"");
    } else if( window.external || document.all) { // For IE Favorite
	window.external.AddFavorite( bookmarkUrl, bookmarkTitle);
    } else { // for other browsers which does not support
	 alert('Your browser does not support this bookmark action');
	 return false;
    }
  });
