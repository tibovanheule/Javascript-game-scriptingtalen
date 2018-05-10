class Game {

    constructor() {
        this.board = [];
        this.score = 0;
        this.message = '';
    }

    // hulp methode
    setboard(value) {
        $.each(value, function (index, value) {
            $.each(value, function (index2, value) {
                $("#board").append("<div id='" + index + index2 + "' class='dot " + value + "' ></div>")
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
        $("#score").html("aantal stappen: " + score)
    }

    update(zet, plaats) {
        let self = this;
        $.ajax({
            url: "/cgibin/doMove.py",
            cache: false,
            method: 'POST',
            data: {
                'status': JSON.stringify({'board': self.board, 'score': self.score}),
                'zet': JSON.stringify(zet),
                'plaats': JSON.stringify(plaats)
            },
            dataType: 'json',
            success: function (result) {

                self.board = result.board;
                self.score = result.score;
                self.message = result.message;
                $("#board").empty();
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
        $.ajax({
            url: "/cgibin/gekleurde druppels.py", cache: false, dataType: 'json', success: function (result) {
                self.board = result.board;
                self.score = result.score;
                self.message = result.message;

                $("#board").empty();
                $.each(result.board, function (index, value) {
                    self.setboard(value);
                });
                $.each(result.moves, function (index, value) {
                    self.setmoves(value);
                });
                self.setScore(result.score)
            }
        });
    }

}




