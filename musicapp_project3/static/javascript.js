// Buttons - Show/Hide Modals
window.onclick = function(event) {
  var btn = document.querySelectorAll(".button1");
  var modal = document.querySelectorAll('#modal');
  var c = document.querySelectorAll('#close');
  var m = [modal[0], modal[1], modal[2]];
  var b = [btn[0], btn[1], btn[2]];

  function hideB(){
    for(var i=0; i < b.length; i++){
        b[i].style.visibility = "hidden";
    }
  }
  function showB(){
    for(var i=0; i < b.length; i++){
        b[i].style.visibility = "";
    }
  }
  if (event.target == btn[0] ) {
      m[0].style.display='block';
      hideB();
    }
  if (event.target == btn[1] ) {
      m[1].style.display='block';
      hideB();
    }
  if (event.target == btn[2] ) {
      m[2].style.display='block';
      hideB();
    }
  if (event.target == c[0] ) {
      m[0].style.display='none';
      showB();
    }
  if (event.target == c[1] ) {
      m[1].style.display='none';
      showB();
    }
  if (event.target == c[2] ) {
      m[2].style.display='none';
      showB();
    }
  if (event.target == m[0] ) {
      m[0].style.display='none';
      showB();
    }
  if (event.target == m[1] ) {
      m[1].style.display='none';
      showB();
    }
  if (event.target == m[2] ) {
      m[2].style.display='none';
      showB();
    }

}

// form
var loginform = document.getElementById("loginform");
// Focus
loginform.addEventListener("focus", function( event ) {
  event.target.style.background = "";
}, true);

// Blur
loginform.addEventListener("blur", function( event ) {
  event.target.style.background = "";
}, true);
