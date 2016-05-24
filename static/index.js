console.log("begin");

$("#login").click(function login(){
    $(".left").fadeIn(1000);
    $(".right").fadeOut(1000);
});

$("#signup").click(function signup(){
    $(".left").fadeOut(1000);
    $(".right").fadeIn(1000);
});

console.log("end");