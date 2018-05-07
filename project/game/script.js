
$("#newgame").click(function(){
    newGame();
    //I don't won't to spam the server with CGI processes.
    //that is why I disabled the button for 1 seconds, so users can make only 1 request per second.
    var btn = $(this);
    btn.prop('disabled', true);
    setTimeout(function(){
        btn.prop('disabled', false);
    }, 1000);
});

function newGame() {
    $.ajax({url: "/cgibin/gekleurde druppels.py",cache: false,dataType: 'json', success: function(result){
        console.log(result);
        $("#board").html("");
        $.each(result.board.valueOf(), function (index, value) {
            setboard(value);
        });
    }});
}

function setboard(value) {
    $.each(value,function (index,value) {
        $.each(value,function (index, value) {
            $("#board").append("<div class='dot "+value+"'></div>")
        });
        $("#board").append("</br>")
    })
}

newGame();