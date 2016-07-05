$(document).ready(function(){
    populateList()
    setKeyBindings();
});
function setKeyBindings(){
    $('#join').click(function(){joinGame()});
    $('#new').click(function(){newGame()});
}
function joinGame(){
    window.location = '/game/' + $('#games').val()
}
function newGame(){
    $.get('/game/new', newSuccess)
}
function populateList(){
    $.get('/allgames', listSuccess)
}

function newSuccess(data){
    window.location = '/game/' + data;
}

function listSuccess(data){
    var retHTML = "";
    games = data.allgames;
    $.each(games,function(index,result){
        retHTML += '<option value="' + result + '">' + result + '</option>'
        console.log(result);
    });
    $('#games').html(retHTML);
}