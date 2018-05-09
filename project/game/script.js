var result = {};


$("#newgame").click(function () {
    newGame();
    //I don't won't to spam the server with CGI processes.
    //that is why I disabled the button for 1 seconds, so users can make only 1 request per second.
    var btn = $(this);
    btn.prop('disabled', true);
    setTimeout(function () {
        btn.prop('disabled', false);
    }, 1000);
});

function newGame() {
    $.ajax({
        url: "/cgibin/gekleurde druppels.py", cache: false, dataType: 'json', success: function (result) {
            console.log(result);
            game = result;
            console.log(result.board);
            $("#board").html("");
            $.each(result.board, function (index, value) {
                setboard(value);
            });
            $.each(result.moves, function (index, value) {
                setmoves(value);
            })
        }
    });
}

function setboard(value) {
    $.each(value, function (index, value) {
        $.each(value, function (index2, value) {
            $("#board").append("<div id='" + index + index2 + "' class='dot " + value + "' ></div>")
        });
        $("#board").append("</br>")
    })
}

function setmoves(moves) {
    $("#moves").html("");
    $.each(moves, function (index, value) {
        $("#moves").append("<option value='"+value+"'>"+value+"</option>");
    });


}

newGame();

$(document).on('click', '.dot', function () {
    var zet = $("#moves").val();
    console.log(zet);
    update(game,zet, [this.id.charAt(0), this.id.charAt(1)]);
});


function update(board, zet, plaats) {
    $.ajax({
        url: "/cgibin/doMove.py",
        cache: false,
        method: 'POST',
        data: {'board': JSON.stringify(board.board), 'zet': JSON.stringify(zet), 'plaats': JSON.stringify(plaats)},
        dataType: 'json',
        success: function (result) {
            game = result;
            $("#board").html("");
            $.each(result.board, function (index, value) {
                setboard(value);
            });
            $.each(result.moves, function (index, value) {
                setmoves(value);
            })
        }
    });
}

