<?php
include_once("web2phone_db_functions.php");
connect_to_db();

if(isset($_POST['email']) && isset($_POST['password'])){
	$email = $_POST['email'];
	$password = $_POST['password'];
}
else {
	header("location: login.php?loginerror=2");
	exit();
}

$email = mysql_real_escape_string($email);
$password = mysql_real_escape_string($password);

$qry="SELECT * FROM user WHERE email='$email' AND password='$password'";
$result=mysql_query($qry);


if (mysql_num_rows($result)>0){

	$member=mysql_fetch_assoc($result);


	#$_SESSION['email']=$member['email'];
	#$_SESSION['first']=$member['first'];
	#$_SESSION['last']=$member['last'];
	#$_SESSION['id']=$member['id'];
	setcookie('web2phone_email',strtolower($member['email']), time()+60*60*3);
	setcookie('web2phone_password', ($member['password']), time()+60*60*3);
	//Write session to disc
	#session_write_close();
	header("location: web.php");
	exit();

}
else {
echo "nothing found";

	#$_SET["error"] = 1;
	header("location: web_login.php");
	exit();
}
?>