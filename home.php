<!DOCTYPE html>
<html lang="de" dir="ltr">
    <head>
        <meta charset="utf-8"/>
        <title>Grenzweg</title>
        <meta http-equiv="refresh" content="1"/>
        <meta http-equiv="cache-control" content="no cache"/>
        <link rel="stylesheet" type="text/css" href="home.css" charset="utf-8"/>
    </head>
    <body>
        <div class="AllContentWrapper">
            <div class="login">
                <?php 
                    echo "Benutzername:". $_POST['UserName'];
                    echo "Passwort:". $_POST['Password'];        
                 ?>
                 <form action="home.php" method="post">
                    <h1>Benutzername</h1>
                    <input type="text" name="UserName"/>
                    <h1>Password</h1>
                    <input type="password" name="Password"/>
                    <input type="submit" value="absenden"/>
                 </form>
            </div>
        </div>
    </body>
</html>