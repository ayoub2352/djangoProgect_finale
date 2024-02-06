function togglePopup(){
    document.getElementById("pop-up1").classList.toggle("active");
    document.body.style.overflow="hidden";
    document.getElementById('logBlock').remove()
    $(window).scrollTop(0);
}
