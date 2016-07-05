<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <script src="static/js/jquery.min.js"></script>
        <link rel="stylesheet" type="text/css" href="static/css/bootstrap.min.css">
        <script src="static/js/bootstrap.min.js"></script>
        <link rel="stylesheet" type="text/css" href="static/css/lobby.css">
        <script src="static/js/lobby.js"></script>
        <title>Lobby</title>
    </head>
    <body>
        <img class="center" src="static/img/logo.png">
        <div>
            <div>
                <label>Click a game below to join!</label>
                <div>
                    <select id="games" class="form-control" size="8">
                    </select>
                    <div id="buttons">
                        <button id="join">Join Game</button>
                        <button id="new">New Game</button>
                    </div>                    
                </div>
            </div>
        </div>
    </body>
</html>