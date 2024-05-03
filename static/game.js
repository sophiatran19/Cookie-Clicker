var width = $('#game').width()
var height = $('#game').height()
var start = $('#object').position()

if($.cookie('backcol') != undefined){
  $('body').css('background-color',$.cookie('backcol'))
  $('#game').css('background-color',$.cookie('gamecol'))
  $('#object')[0].src = $.cookie('objecturl') 
  $('body').css('color', $.cookie('fontcol'))
}

$(window).resize(function(){
  width = $('#game').width()
  height = $('#game').height()
})

$('#object').click(function(){
    var xhr = new XMLHttpRequest();
     xhr.open('POST', `/score`)
    xhr.onreadystatechange = function(){
      if(xhr.readyState == 4){
        $('#score').html('Score: '+ xhr.response)
      }
    }
    xhr.send()
  })

setInterval(function(){
  $('#object').offset({top: Math.random()* height + start.top, left: Math.random()* width + start.left/2})
}, 1000)