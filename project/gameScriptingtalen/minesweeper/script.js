class Game {

    constructor() {
        this.board = [];
        this.score = 0;
        this.message = '';
    }

    // hulp methode
    setboard(value) {
        $("#board").empty();
        $.each(value, function (index, value) {
            $.each(value, function (index2, value) {
                $("#board").append("<div id='" + index + index2 + "' class='board-element " + value + "' ></div>")
            });
            $("#board").append("<br/>")
        });
    }

    setmoves(moves) {
        $("#moves").empty();
        $.each(moves, function (index, value) {
            $("#moves").append("<option value='" + value + "'>" + value + "</option>");
        });
    }

    setScore(score) {
        $("#score").html("aantal gevonden mijnen: " + score)
    }

    update(zet, plaats) {
        let self = this;
        $.ajax({
            url: "/cgibin/minesweeperDoMove.py",
            cache: false,
            method: 'POST',
            data: {
                'status': JSON.stringify({'board': self.board, 'score': self.score}),
                'zet': JSON.stringify(zet),
                'plaats': JSON.stringify(plaats)
            },
            dataType: 'json',
            error: function () {
                if ($("#board p").length === 0) {
                    $("#board").append("<br><p>An error occured, couldn't update the board.</p>")
                }
            },
            success: function (result) {

                self.board = result.board;
                self.score = result.score;
                self.message = result.message;
                $.each(result.board, function (index, value) {
                    self.setboard(value);
                });
                $.each(result.moves, function (index, value) {
                    self.setmoves(value);
                });
                self.setScore(result.score);
                if (result.hasOwnProperty('message')) {
                    $("#myModal").css("display", "block");
                    $("#message").html(result.message);
                }
            }
        });
    }

    newGame() {
        let self = this;
        $("#board").fadeOut(400, function () {
            $.ajax({
                url: "/cgibin/minesweeper.py",
                cache: false,
                dataType: 'json',
                error: function () {
                    $("#board").html("<p>An error occured, couldn't start a new game</p>").fadeIn(400)
                },
                success: function (result) {
                    self.board = result.board;
                    self.score = result.score;
                    self.message = result.message;
                    $.each(result.board, function (index, value) {
                        self.setboard(value);
                    });
                    $.each(result.moves, function (index, value) {
                        self.setmoves(value);
                    });
                    self.setScore(result.score);
                    $("#board").fadeIn(400)
                }
            });
        })
    }

}




