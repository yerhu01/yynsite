/* Toggle between adding and removing the "responsive" class to navbar when the user clicks on the icon */
function openHamburgerMenu() {
    var x = document.getElementById("myNavBar");
    if (x.className === "navbar") {
      x.className += " responsive";
    } else {
      x.className = "navbar";
    }
  }