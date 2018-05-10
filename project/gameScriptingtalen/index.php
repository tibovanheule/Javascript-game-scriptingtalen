<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <link rel="apple-touch-icon" sizes="180x180" href="/resources/favicon/apple-touch-icon.png"/>
    <link rel="icon" type="image/png" href="/resources/favicon/favicon-32x32.png" sizes="32x32"/>
    <link rel="icon" type="image/png" href="/resources/favicon/favicon-16x16.png" sizes="16x16"/>

    <link rel="stylesheet" href="https://tibovanheule.space/newstyle.min.css" integrity="sha384-bR/ZFfqZWIuQQkSNOn3Q0W0Ui6ejQqPK3l/biTTqQgeGgI6Cu2aNUTmA+wsilw1b" crossorigin="anonymous">
    <link rel="stylesheet" href="game.min.css" >
    <!-- zonder SRI
    <link rel="stylesheet" type="text/css" href="/newstyle.min.css"/>
    -->
    <meta name="theme-color" content="#ffffff"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <meta name="description"
          content="Gekleurde druppels, an implementation of a game in python and javascript for the course scripting Languages Ugent.">
    <title>Home</title>
    <script
            src="https://code.jquery.com/jquery-3.3.1.min.js"
            integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
            crossorigin="anonymous"></script>
    <script async src="script.min.js"></script>
    <script async src="clicks.min.js"></script>
</head>
<body class="home">
<div class="content">
    <div class="logo">
        <img src="../resources/images/logo.png" alt="logo"/><br/>
    </div>
    <h1>GEKLEURDE DRUPPELS</h1>
    <div id="myModal" class="modal">
        <div class="modal-content controls">
                <p id="message"></p>
                <button id="close">New Game</button>
        </div>
    </div>
    <div class="controls">
        <button id="newgame">New Game</button>
        <label for="moves">kleuren: </label>
        <select id="moves">
        </select>
        <p id="score">Loading ...</p>
    </div>
    <div id="board">

    </div>


    <div class="footer">
        <p>Created with &hearts;<br>COPYRIGHT TIBO VANHUELE 2015-<?php echo date('Y'); ?> <br/><a
                    href="../policies/cookies.php">COOKIE POLICY</a> <a href="../policies/terms.php">TERMS OF USE</a> <a
                    href="../policies/disclaimer.php">DISCLAIMER</a></p>
        <img src="../resources/images/footer.jpg" alt="footer">
    </div>
</div>
</body>
</html>


