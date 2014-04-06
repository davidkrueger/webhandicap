<?php
	echo "<li><a href='about.php'><em><b>About Web2Phone</b></em></a></li>";
	if(isset($_COOKIE['web2phone_email']) && $_COOKIE['web2phone_email'] != 'a'){
		echo  "<li><a href='logout.php'><em><b>Logout</b></em></a></li><li><a href='web.php'><em><b>Manage Bookmarks</b></em></a></li>"."<li><em>Logged in as ".$_COOKIE['web2phone_email']."</em></li>";
	}
	else {
		echo "<li><a href='web_login.php'><em><b>Log-in</b></em></a></li>";
		echo "<li><a href='register.php'><em><b>Register</b></em></a></li>";
	}
	
?>
