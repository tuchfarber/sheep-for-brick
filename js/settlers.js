$().ready(function() {
    buildClickTiles()
});

function buildClickTiles(){
    var retHTML = "";
    for(var i=0;i<19;i++){
        switch(i){
            case 0:
                retHTML += '<div class="three">';
                break;
            case 3:
                retHTML += '</div><div class="four">';
                break;
            case 7:
                retHTML += '</div><div class="five">';
                break;
            case 12:
                retHTML += '</div><div class="four">';
                break;
            case 16:
                retHTML += '</div><div class="three">';
                break;
            }
        retHTML += '<div class="tilebtn" onclick="tileclick(' + i + ')"></div>';
    }
    retHTML += '</div>';
    $('#click_tile_area').html(retHTML);
}
function tileclick(tile_no){
    console.log(tile_no);
}