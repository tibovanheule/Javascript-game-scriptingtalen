var board;
var score;
var message;

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
            board = result.board;
            score = result.score;
            message = result.message;
            $("#board").empty();
            $.each(result.board, function (index, value) {
                setboard(value);
            });
            $.each(result.moves, function (index, value) {
                setmoves(value);
            });
            setScore(result.score)
        }
    });
}

function setboard(value) {
    $.each(value, function (index, value) {
        $.each(value, function (index2, value) {
            $("#board").append("<div id='" + index + index2 + "' class='dot " + value + "' ></div>")
        });
        $("#board").append("<br/>")
    });
}

function setmoves(moves) {
    $("#moves").empty();
    $.each(moves, function (index, value) {
        $("#moves").append("<option value='" + value + "'>" + value + "</option>");
    });
}

function setScore(score) {
    $("#score").html("aantal stappen: " + score)
}

newGame();

$(document).on('click', '.dot', function () {
    update($("#moves").val(), [this.id.charAt(0), this.id.charAt(1)]);
});

$("#close").click(function () {

    $("#myModal").css("display", "none");
    newGame();
});


function update(zet, plaats) {
    $.ajax({
        url: "/cgibin/doMove.py",
        cache: false,
        method: 'POST',
        data: {
            'status': JSON.stringify({'board': board, 'score': score}),
            'zet': JSON.stringify(zet),
            'plaats': JSON.stringify(plaats)
        },
        dataType: 'json',
        success: function (result) {

            board = result.board;
            score = result.score;
            message = result.message;
            $("#board").empty();
            $.each(result.board, function (index, value) {
                setboard(value);
            });
            $.each(result.moves, function (index, value) {
                setmoves(value);
            });
            setScore(result.score);
            if (result.hasOwnProperty('message')) {
                $("#myModal").css("display", "block");
                $("#message").html(result.message);
            }
        }
    });
}



