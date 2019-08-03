<html>
<head>
<meta name="viewport" content="width=device-width" />
<title>LED Control</title>
</head>
        <body>
        WEB PAGE ON PHP BASED GPIO Control:
        <form method="get" action="gpio.php">
                <input type="submit" value="ON" name="on">
                <input type="submit" value="OFF" name="off">
        </form>
        <?php
        
        if(isset($_GET['on'])){
                system ('gpio write 1 1');
                echo "LED is on";
        }
        else if(isset($_GET['off'])){
                system ('gpio write 1 0');
                echo "LED is off";
        }

        ?>
        </body>
</html>