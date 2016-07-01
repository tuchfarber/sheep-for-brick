$(document).ready(function(){
    populateList()
    setKeyBindings();
});
function setKeyBindings(){
    $('button').click(function(){joinGame()});
}
function joinGame(){

}
function populateList(){
    $.get('/allgames', listSuccess)
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