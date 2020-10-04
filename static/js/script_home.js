var video = document.getElementById("myVideo");
var btn = document.getElementById("myBtn");

function myFunction() {
  if (video.paused) {
    video.play();
    btn.innerHTML = "Pause";
  } else {
    video.pause();
    btn.innerHTML = "Play";
  }
}
function showPosition() {
      if(navigator.geolocation ){
          navigator.geolocation.getCurrentPosition(function(position) {
              var positionInfo = "posizione (" + "Latitudine: " + position.coords.latitude + ", " + "Longitudine: " + position.coords.longitude + ")";
              document.getElementById("result").innerHTML = positionInfo;
          });
      } else {
          alert("niente geolocalizzazione");
      }
  }