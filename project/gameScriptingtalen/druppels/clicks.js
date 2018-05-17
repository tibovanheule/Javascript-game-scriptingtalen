const game = new Game;
$("#newgame").click(function () {
    game.newGame();
    //I don't won't to spam the server with CGI processes.
    //that is why I disable the button for 1 seconds, so users can make only 1 request per second.
    let btn = $(this);
    btn.prop('disabled', true);
    setTimeout(function () {
        btn.prop('disabled', false);
    }, 1000);
});

$(document).on('click', '.board-element', function () {
    game.update($("#moves").val(), [$(this).data("x"), $(this).data("y")]);
});

$("#close").click(function () {
    $("#myModal").css("display", "none");
    game.newGame();
});

game.newGame();