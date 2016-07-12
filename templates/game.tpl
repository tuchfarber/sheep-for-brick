<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <script src="/static/js/jquery.min.js"></script>
        <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.min.css">
        <script src="/static/js/bootstrap.min.js"></script>
        <link rel="stylesheet" type="text/css" href="/static/css/game.css">
        <script src="/static/js/game.js"></script>
        <title>Game</title>
    </head>
    <body>
        <div id="playerbar">
            <div id="player1box" class="player">
                Player 1: <br>
                Cards:0 VP:0
                {{num_players}}
            </div>
            <div id="player2box" class="player">
                Player 2: <br>
                Cards:0 VP:0
            </div>
            <div id="player3box" class="player">
                Player 3: <br>
                Cards:0 VP:0
            </div>
            <div id="player4box" class="player">
                Player 4: <br>
                Cards:0 VP:0
            </div>
            % short_hash = hash[0:8]
            <div id="gameinfo" class="toptile">
                <span title="{{hash}}">Welcome, {{user}}<br>Game: {{short_hash}}</span>
            </div>
        </div>
        <div id="boardarea"></div><div id="inventory"></div>
        <div id="actionbar"></div>
        
    </body>
</html>