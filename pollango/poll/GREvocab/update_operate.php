
<?php

include_once("web2phone_db_functions.php");
connect_to_db();

if(isset($_POST['website'])){
	$website = $_POST['website'];
}
else {

	header("location: web2phone.php");
	exit();
}
$email = $_COOKIE['web2phone_email'];
$password = $_COOKIE['web2phone_password'];
$url = mysql_real_escape_string($website);
$qry="SELECT * FROM user WHERE email='$email' AND password='$password'";
$result=mysql_query($qry);


if (mysql_num_rows($result)>0){
	$qry="UPDATE `user` SET `website` = '".$url."' WHERE `user`.`email` = '".$email."';";
	
	$result=mysql_query($qry);
	$qry="SELECT `website` FROM `user` WHERE `user`.`email` = '".$email."';";

	$result=mysql_query($qry);
	$array = mysql_fetch_assoc($result);
	echo "Current bookmark is:<br/><label>".$array['website']."</label>";

	exit();

}
else {
echo "nothing found";

	#$_SET["error"] = 1;
	header("location: login.php?loginerror=1");
	exit();
}
?>