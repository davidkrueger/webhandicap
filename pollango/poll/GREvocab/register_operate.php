<?php
include_once("web2phone_db_functions.php");
connect_to_db();

$email = strtolower($_POST['email']);
$password = $_POST['password'];

if($email == "" || $password == ""){
	header("register.php");	
	exit();
}

$email = mysql_real_escape_string($email);
$password = mysql_real_escape_string($password);

$qry="SELECT email FROM user WHERE email='$email'";
$result=mysql_query($qry);

if (mysql_num_rows($result)!=0){
	#already in DB, please log in
	header("location: register.php?regerror=1");
}
else {
	#add person to database, then log them in
	$sql = "INSERT INTO user (email,password) VALUES ('$email','$password')";
	$result = mysql_query($sql);
	include "login_operate.php";
}


#update a field in the DB
#$sql = "UPDATE person SET first='mark2' WHERE email='test@gmail.com'";
#$result = mysql_query($sql);

#delete a record from db
#$sql = "DELETE FROM person WHERE first='Mark2'";
#$result = mysql_query($sql);

#check password
#$qry="SELECT email FROM person WHERE email='davidckrueger@gmail.com' AND password='test1'";
#$result=mysql_query($qry);
#echo $result;
#if (mysql_num_rows($result)<=0){
#	echo "incorrect password/email combination";

#}
#else{
#$result = mysql_query("SELECT * FROM person");
#


#	while($row = mysql_fetch_assoc($result)){

#		echo "email:".$row["email"]."<br>";
	
#	}
#}
?>