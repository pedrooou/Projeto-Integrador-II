#o roteiro do jogo esta presente nesse arquivo

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image bg praça3poderes = "images/praça3poderes.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg praça3poderes

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

    "... Confesso que aqui é bem bonito mesmo \n(dá pra ver os principais prédios, bem como o vô disse)"

    "Entao... vamos aonde primeiro?"

    # This ends the game.

    return
