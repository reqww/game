function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function send(val){
  $.ajax({
    type: "POST",
    url: "/game/play/",
    data: {
      csrfmiddlewaretoken: getCookie('csrftoken'),
      "rate": val,
    },
    dataType: "text",

    success: function(data){
      if (data)
      {
        arr = data.split(";")
        console.log(arr[0], arr[1], arr[2])
        $("#result").html(arr[0])
        document.getElementById(arr[1]).className += " chosen-two";
        document.querySelector('.countdown__vs').style.display += 'block';
        document.querySelector('.countdown').style.display += 'none';

        if (!document.querySelector('.choose-button').classList.contains("chosen")) {
          paperDefault();
        }
        coins = Number(document.getElementById("coins_hidden").value)
        if (arr[2] == "win") {
          var win = coins + val 
          $("#coins").html(win)
          document.getElementById("coins_hidden").value = win
          $("#result").css("color", "green");
        }
        else
          if (arr[2] == "lose") {
            var lose = coins - val
            $("#coins").html(lose)
            document.getElementById("coins_hidden").value = lose
            $("#result").css("color", "red"); 
          } else {
            $("#result").css("color", "black"); 
          }
        page_reebot(arr[1])
      }
      else
        document.location.href = "/game/error"
    }
  });
}

function paperDefault() {
  document.getElementById('paper').className += " chosen"
  document.getElementById('rock').disabled = true;
  document.getElementById('scissors').disabled = true;
}

function getTimeRemaining(endtime) {
  var t = Date.parse(endtime) - Date.parse(new Date());
  var seconds = Math.floor((t / 1000) % 60);
  return {
    total: t,
    seconds: seconds
  };
}

function initializeClock(id, endtime) {
  var clock = document.getElementById(id);
  var secondsSpan = clock.querySelector('.seconds');

  function updateClock() {
    var t = getTimeRemaining(endtime);
    secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

    if (t.total <= 0)
      clearInterval(timeinterval);
  }
  updateClock();
  var timeinterval = setInterval(updateClock, 1000);
}

function light_send(str){
  $.ajax({
    type: "POST",
    url: "/game/calculate/",
    data: {
      csrfmiddlewaretoken: getCookie('csrftoken'),
      "choice": str,
    },
    dataType: "text",
  })
}

$("#paper").click(function(){
  document.getElementById('paper').className += " chosen"
  document.getElementById('rock').disabled = true;
  document.getElementById('scissors').disabled = true;
  light_send("Бумага")
})

$("#rock").click(function(){
  document.getElementById('rock').className += " chosen"
  document.getElementById('paper').disabled = true;
  document.getElementById('scissors').disabled = true;
  light_send("Камень")
})

$("#scissors").click(function(){
  document.getElementById('scissors').className += " chosen"
  document.getElementById('rock').disabled = true;
  document.getElementById('paper').disabled = true;
  light_send("Ножницы")
})

document.getElementById('scissors').disabled = true;
document.getElementById('rock').disabled = true;
document.getElementById('paper').disabled = true;
document.getElementById('Ножницы-2').disabled = true;
document.getElementById('Камень-2').disabled = true;
document.getElementById('Бумага-2').disabled = true;

$("#play__start").click(function(){
  if (document.querySelector('.chosen-two')) {
    document.querySelector('.chosen-two').className = "choose-button";
  }  

  document.querySelector('.countdown').style.display = 'none';  
  document.querySelector('.play-player__img__new').style.display = 'none'; // иконка соперника
  document.getElementById('Ножницы-2').disabled = true;
  document.getElementById('Камень-2').disabled = true;
  document.getElementById('Бумага-2').disabled = true;

  $("#result").html("")
  document.getElementById('play__start').disabled = true;

  if (document.querySelector('.chosen')) {
    document.querySelector('.chosen').disabled = true;
    document.querySelector('.chosen').className = "choose-button";
  }  

  document.querySelector('.loader__wrapper').style.display = 'block';
  document.querySelector('.play-player__img__last').style.display = 'none';
  document.querySelector('.play-player__name__last').innerHTML = "Поиск соперника ..."

  document.getElementById('radio-1').disabled = true;
  document.getElementById('radio-2').disabled = true;
  document.getElementById('radio-3').disabled = true;
  document.getElementById('radio-4').disabled = true;

  setTimeout(function(){
    document.getElementById('scissors').disabled = false;
    document.getElementById('rock').disabled = false;
    document.getElementById('paper').disabled = false;

    document.querySelector('.loader__wrapper').style.display = 'none';
    document.querySelector('.play-player__img__new').style.display = 'block'; // иконка соперника
    document.querySelector('.play-player__name__last').innerHTML = "neverpickmee" // ник противника

    document.querySelector('.countdown__wrapper').style.display = 'flex';
    document.querySelector('.countdown').style.display = 'inline-block';
    document.querySelector('.countdown__vs').style.display = 'none';
    var deadline = new Date(Date.parse(new Date()) + 5 * 1000); // for endless timer
    var rate = Number($('input[name=radio]:checked').val())
    send(rate)
    initializeClock('countdown', deadline);
  }, Math.random() * 10000) // Время поиска игрока
})

$( document ).ready(function() {
 coins = Number(document.getElementById("coins").innerHTML)
 check_validness(coins)
});

function check_validness(coins)
{
  if (coins < 10)
  {
    document.getElementById("header").innerHTML = "Пополните счет!"
    document.getElementById('radio-1').disabled = true;
    document.getElementById('radio-2').disabled = true;
    document.getElementById('radio-3').disabled = true;
    document.getElementById('radio-4').disabled = true;
    document.getElementById('play__start').disabled = true;
  }
  else
    if (coins < 50)
    {
      document.getElementById('radio-2').disabled = true;
      document.getElementById('radio-3').disabled = true;
      document.getElementById('radio-4').disabled = true;
    }
    else
      if (coins < 100)
      {
        document.getElementById('radio-3').disabled = true;
        document.getElementById('radio-4').disabled = true;
      }
      else
        if (coins < 500)
          document.getElementById('radio-4').disabled = true;
}

function page_reebot(remove_blue)
{
  document.getElementById('radio-1').disabled = false;
  document.getElementById('radio-2').disabled = false;
  document.getElementById('radio-3').disabled = false;
  document.getElementById('radio-4').disabled = false;
  document.getElementById('play__start').disabled = false;
  coins = Number(document.getElementById("coins").innerHTML)
  check_validness(coins)  
}


