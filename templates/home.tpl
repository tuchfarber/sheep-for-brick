<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <script src="static/js/jquery.min.js"></script>
        <link rel="stylesheet" type="text/css" href="static/css/bootstrap.min.css">
        <script src="static/js/bootstrap.min.js"></script>
        <link rel="stylesheet" type="text/css" href="static/css/login.css">
        <script src="static/js/login.js"></script>
        <title>Login</title>
    </head>
    <body>
        <img src="static/img/logo.png">
        <div id="loginbox">
            <div>
                <button class="tab" id="login">Login</button><button class="tab" id="signup">Sign-up</button>
            </div>
            <form action="/login" method="post">
                <div>
                    <input type="text" placeholder="Username" name="username"><br>
                    <input class="error" type="password" placeholder="Password" name="password"><br>
                </div>
            </form>
            <button id="form_btn">Submit</button>
            <span id="error_line"></span>
        </div>
    </body>
</html>