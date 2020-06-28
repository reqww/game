$(document).ready(function()
{
  $('#open-button').on('click', function(event) {
    event.preventDefault();
    $('#modal').css("display", "block");
    console.log("123");
 		$('#modal-overlay').css("display", "block");
  });
  $('#open-button2').on('click', function(event) {
    event.preventDefault();
    $('#modal').css("display", "block");
    console.log("123");
    $('#modal-overlay').css("display", "block");
  });

  $('#close-button').on('click', function() {
    $('#modal').css("display", "none");
 		 $('#modal-overlay').css("display", "none");
  });

  $('#modal-overlay').on('click', function() {
    $('#modal').css("display", "none");
 		$(this).css("display", "none");

    $(".drower").addClass("close");
    $(".header__menu-toggle").removeClass("open");
    $(".open-img").css("display", "block");
    $(".close-img").css("display", "none");
    $('#modal-overlay').css("display", "none");
  });


  $('.open-img').on('click', function() {
    $(".drower").removeClass("close");
    $(".header__menu-toggle").addClass("open");
    $(".open-img").css("display", "none");
    $(".close-img").css("display", "block");
    $('#modal-overlay').css("display", "block");
  });

  $('.close-img').on('click', function() {
    $(".drower").addClass("close");
    $(".header__menu-toggle").removeClass("open");
    $(".open-img").css("display", "block");
    $(".close-img").css("display", "none");
    $('#modal-overlay').css("display", "none");
  });


});