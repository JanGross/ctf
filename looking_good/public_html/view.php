
<!--





There's no flag in the source code ;)
























































































































-->
<?php
    if ($_POST['username'] != "factory_admin" || $_POST['password'] != 'CHANGE_THIS_BEFORE_SHIPPING!') {
        echo "Invalid Credentials!";
        die();
    }
    setcookie("show_viewer_hint", 0, time()+3600, "/", "sketchfab.com", false);
?>
<!DOCTYPE HTML>
<html>
<head>
    <meta challenge_chk_view />
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Camera Feed</title>

    <!-- Insert this script -->
    <script type="text/javascript" src="/sketchfab-viewer-1.2.1.js"></script>
</head>

<body>
    <style>
        body {
            background-color: black;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: white;
        }
        .topbox {
            position: absolute;
            top:0px;
            left: 50%;
            height: 50px;
            background-color: black;
            width: 810px;
            z-index:2;
            transform: translateX(-50%);

        }
        .bottombox {
            position: absolute;
            top: 550px;
            left: 50%;
            height: 60px;
            background-color: black;
            width: 810px;
            z-index:2px;
            transform: translateX(-50%);

        }
        .loading-box {
            position: absolute;
            top: 300px;
            text-align: center;
            left: 50%;
            height: 60px;
            background-color: black;
            width: 810px;
            z-index:-2px;
            transform: translateX(-50%);

        }
        .bottombox>p {
            color:white;
        }
        #api-frame {
            left:50%;
            transform: translateX(-50%);
            z-index: -1;
            position: absolute;
            top:0px;
        }
    </style>
    
    <div class="topbox">Logged in as "factory_admin"</div>
    <div class="bottombox"><p>Control camera movement by dragging the screen!<br>Control zoom using your mousewheel!</p></div>
    <!-- Insert an empty iframe -->
    <iframe style="display:none; border:none; width:800px; height:600px;" src="" id="api-frame" allow="autoplay;"></iframe>
    <div class="loading-box" id="loadingbox">Loading camera feed...</div>
    <!-- Initialize the viewer -->
    <script type="text/javascript">
    var iframe = document.getElementById( 'api-frame' );
    var urlid = '31a3cdd73b4344f1a836c4cf364a22ae';

    var client = new Sketchfab( iframe );


    client.init( urlid, {
        preload: 1,
        camera: 0,
        ui_hint: 0,
        success: function onSuccess( api ){
            api.start();
            api.addEventListener( 'viewerready', function() {

                // API is ready to use
                // Insert your code here
                console.log( 'Viewer is ready' );
                document.getElementById("api-frame").style.display = "block";
                document.getElementById("loadingbox").style.display = "none";
            } );
        },
        error: function onError() {
            console.log( 'Viewer error' );
        }
    } );
    </script>
</body>
</html>