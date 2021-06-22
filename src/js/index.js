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
   // document.getElementById("main").style.marginLeft = "250px";
  }
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  toggle = true;
//  document.getElementById("main").style.marginLeft= "0";
}