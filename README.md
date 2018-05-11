# Javascript-game-scriptingtalen

- working example: https://tibovanheule.space/gameScriptingtalen/
- mail: tibo.vanheule@ugent.be

## Some notes

I have used my own server to test out the sricpts.
The server has a content security policy in place, so the code a written with that restriction in mind.

first there is a jquery class that handles all communication to the python scripts.
I use a second script to handle all clicks and to update the board.
that script can be placed inline if you run it on a server without csp(otherwise it will block it)

for the same reason, I color the dots with a class defined in a css file and not
with an inline style="background-color:white;"

## file structure

### root
- hulpbestanden (contains the task)
- project (project files)
- .travis.yml (For Travis CI to test out the python scripts, when i commit to my github repo)
- readme.md

### project

- cgibin (python scripts)
- gameScriptingtalen (html and js files)

### cgibin

- gekleurde druppel.py (new game functie)
- doMove.py (do move functie)
- test.py (implements some functions of doMove.py and see if it works. for Travis CI )

### gameScriptingtalen

- clicks.js  (contains the onclick functions to start the correct method in script.js)
- clicks.min.js (minified version)
- game.css (css for the dots ,controls and popup)
- game.min.css (minified version)
- index.html (game page)
- loader.gif (for when the game is loading)
- script.js (Jquery class game, for visualisation.)
- script.min.js (minified version)


