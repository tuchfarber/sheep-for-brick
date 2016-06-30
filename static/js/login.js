$(document).ready(function(){
    $('#login').toggleClass('form_btn_selected',true)
    $('.tab').click(function(){flipTab(this)})
    $('#form_btn').click(function(){
        console.log('test')
        $('#error_line').html('')
        $.each($('form input'),function(index,result){
            if(result.value.length < 1 && index == 0){$('#error_line').html('Please enter username');return false}
            if(result.value.length < 1 && index == 1){$('#error_line').html('Please enter password');return false}
        })
        $.post($('form').attr('action'), $('form').serialize(),loginSuccess)
    })
})

function loginSuccess(data){
    console.log(data);
}
function flipTab(tab){
        $('form').attr('action','/'+tab.id)
        var submit_text = tab.id == 'login' ? 'Sign In' : 'Register';
        $('input[type="submit"]').attr('value',submit_text)
        $('#'+ tab.id).toggleClass('form_btn_selected',true)
        var otherbtn;
        tab.id == "login" ? otherbtn = 'signup' : otherbtn = 'login';
        $('#'+ otherbtn).toggleClass('form_btn_selected',false); 
}