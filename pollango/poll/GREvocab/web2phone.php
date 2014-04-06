<?php
header('Cache-Control: no-cache, must-revalidate');
header('Pragma: no-cache'); // for HTTP/1.0
header('Expires: Thu, 01 Jan 1970 00:00:00 GMT');
$email = $_GET['email_password'];
$password = $_GET['password'];
if(isset($_GET['version'])){
	$version = $_GET['version'];
	include_once('web2phone_db_functions.php');
	echo fetch_multiple_urls($email, $password);
	increment_hits($email, 'app_hits');
}
else {
	include_once('web2phone_db_functions.php');
	echo fetch_url($email, $password);
	increment_hits($email, 'app_hits');
}
?>