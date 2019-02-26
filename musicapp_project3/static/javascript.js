// Buttons - Show/Hide Modals
window.onclick = function(event) {
  var b = document.querySelectorAll(".button1");
  var m = document.querySelectorAll('#modal');
  var c = document.querySelectorAll('#close');

  function hideAllButtons(){
    if(b.length > 0){
      for(var i=0; i < b.length; i++){
        b[i].style.visibility = "hidden";
      }
    }
  }

  function showAllButtons(){
    if(b.length > 0){
      for(var i=0; i < b.length; i++){
        b[i].style.visibility = "visible";
      }
    }
  }

  // when a button is pressed, hide all buttons and open corresponding modal
  // check all buttons to see if it was the event target
  for(var i=0; i < b.length; i++){
    if(b[i] == event.target)
    {
      m[i].style.display="block";
      hideAllButtons();
    }
  }
  // when the close button is pressed, hide open modal and show all buttons
  // check all close buttons to see if it was the event target
  for(var i=0; i < c.length; i++){
    if(c[i] == event.target)
    {
      m[i].style.display="none";
      showAllButtons();
    }
  }

}

// form focus styling

// form
var loginform = document.getElementById("loginform");

// Focus
loginform.addEventListener("focus", function( event ) {
  event.target.style.background = "grey";
}, true);

// Blur
loginform.addEventListener("blur", function( event ) {
  event.target.style.background = "";
}, true);
