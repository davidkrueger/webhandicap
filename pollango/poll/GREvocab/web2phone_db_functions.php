<?php
	function connect_to_db(){
		$hostname="web2phone.db.7448163.hostedresource.com";
                $username="web2phone";
                $password="Lgrowing1!";
                mysql_connect($hostname,$username, $password) or die ("fail");
                mysql_select_db($username);
	}
	function login($email, $password){
		connect_to_db();
			$qry="SELECT * FROM user WHERE email='".$email."' AND password='".$password."'";
			$result=mysql_query($qry);
		if (mysql_num_rows($result)>0){
			return "success";
		}
		else {
			return $qry;
		}
	}
	
	function fetch_url($email, $password){
		connect_to_db();
		$qry="SELECT * FROM list_info WHERE user_email='".$email."'";
		$result=mysql_query($qry);
		
		if (mysql_num_rows($result)>0){
			$array = mysql_fetch_assoc($result);
			$url = $array['text'];
			if(substr($url,0,7) != "http://" && substr($url,0,8) != "https://" && substr($url,0,7) != "HTTP://" && substr($url,0,8) != "HTTPS://"){
				if($url != ""){
					$url = "http://".$url;
				}
			}
			return $url;
		}
		else {
			return "fail";
		}	}	
		function fetch_multiple_urls($email, $password){
		connect_to_db();
		//validate p/w
		$qry="SELECT * FROM user WHERE email='$email' AND password='$password'";
		$result=mysql_query($qry);
		if (mysql_num_rows($result) <= 0){
		
			return "fail";
		}
		$qry="SELECT * FROM list_info WHERE user_email='$email'";
		$result=mysql_query($qry);
		if (mysql_num_rows($result)>0){
			$url = "";
			while($row = mysql_fetch_array($result, MYSQL_ASSOC)){
				if($row['text'] != ""){
					$url_temp = $row['text']."\n";
					if(substr($url_temp,0,7) != "http://" && substr($url_temp,0,8) != "https://" && substr($url_temp,0,7) != "HTTP://" && substr($url_temp,0,8) != "HTTPS://"){
							$url_temp = "http://".$url_temp;
					}
					$title = $row['title'];
					if($title == ""){
						$title = $row['text'];
					}
					$url .= $title."\n".$url_temp;
				}
			}
			return $url;
		}
		else {
			return "Go to theapparchitect.com/web2phone to start using bookmarks\nhttp://theapparchitect.com/web2phone";
		}
	}	
	function validate_login(){
		if(isset($_COOKIE['web2phone_email']) && isset($_COOKIE['web2phone_password'])){
			connect_to_db();
			$qry="SELECT email FROM user WHERE email='".$_COOKIE['web2phone_email']."' AND password='".$_COOKIE['web2phone_password']."'";
			$result=mysql_query($qry);
			if (mysql_num_rows($result)!=0){
				return 1;
			}
			else {
				return 0;
			}
		}
		else {
			return 0;
		}
	}
	function get_url(){
		connect_to_db();
			$qry="SELECT website FROM user WHERE email='".$_COOKIE['email']."' AND password='".$_COOKIE['password']."'";
			$result=mysql_query($qry);
			if (mysql_num_rows($result)!=0){
				$array = mysql_fetch_assoc($result);
				return $array['website'];
			}
			else {
				return '';
			}
	}
	
	function increment_hits($email, $field){
		connect_to_db();
		$qry="UPDATE `user` SET `$field` = $field+1 WHERE `user`.`email` = '$email';";
		$result=mysql_query($qry);
	}
	
	function get_app_hits($email){
		connect_to_db();
		$qry="SELECT `app_hits` FROM `user` WHERE `user`.`email` = '$email';";
		$result=mysql_query($qry);
		$array = mysql_fetch_assoc($result);
		return $array['app_hits'];
	}
?>