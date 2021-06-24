let toggle = true;

function ToggleNav(){
  if (toggle){
    openNav();
  }else{
    closeNav();
  }
}

function openNav() {
    document.getElementById("mySidenav").style.width = "300px";
    toggle = false;
  }
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  toggle = true;
}



