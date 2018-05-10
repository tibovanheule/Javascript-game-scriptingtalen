# Javascript-game-scriptingtalen

working example:
https://tibovanheule.space/gameScriptingtalen/

## Some notes

first i have used my own server to test out the sricpt.
the server has a content security policy in place so a few changes have been made.

first there is a jquery class that handles all communication to the python scripts.
I use a second script to handle all clicks and to update the board.
that script can be placed inline if you run it on a server without csp(otherwise it will block it)

for the same reason, I color the dots with a class defined in a css file and not
with an inline style="background-color:white;"

