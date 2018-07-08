<!DOCTYPE html>
<html>
<head>
    <meta challenge_chk_login />
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>SECURE REMOTE CAMERA LOGIN</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
</head>
<body>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding-top: 5%;
            padding-left: 15%;
            padding-right: 15%;
            background-color: wheat;
        }
        .container {
            box-shadow: 3px 3px 2px gray;
            width: 50%;
            margin: 0 auto;
            height: 250px;
            position: relative;
            text-align: center;
            padding: 5%;
            background-color: rgb(167, 167, 155);
        }
        .container.heading {
            height: 20px;
            padding-top: 5px;
        }
        button {
            padding: 10px 20px;
            font-size: 18px;
            margin-top: 15px;
            color:whitesmoke;
            background-color:rgba(0, 0, 0, 0.85);
            border-radius: 2px;
            border: none;
            box-shadow: 3px 3px 2px gray;
        }
        form {
            z-index: 999;
            position: relative;
        }
        form label {
            font-weight: bold;
            font-size: 18px;
        }
        .lock {
            z-index: -0;
            font-size: 20em;
            position: absolute;
            top: 50%;
            transform: translate(-50%, -50%);
            left: 50%;
            text-shadow: 0px 0px 5px rgba(0, 0, 0, 0.35);
            font-family: 'Times New Roman', Times, serif;
            color: rgba(0, 0, 0, 0.15);
        }
    </style>
    <div class="container heading"><h1>Remote Camera Login</h1></div>
    <div class="container">
        <form action="/view.php" method="POST">
            <label>Username<br>
                <input name="username" type="text"></label><br>
            <label>Password<br>
                <input name="password" type="password"></label><br>
            <button type="submit">Login</button>
        </form>
        <span class="lock">🔒</span>
    </div>
</body>
</html>