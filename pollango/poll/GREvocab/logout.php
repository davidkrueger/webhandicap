<?php 
setcookie("web2phone_email", "");
setcookie("web2phone_password","");
header("location: web.php");
#echo "
"<script type='text/javascript'>
document.cookie = 'email' +'=; expires=Thu, 01-Jan-70 00:00:01 GMT;';
document.cookie = 'password' +'=; expires=Thu, 01-Jan-70 00:00:01 GMT;';
document.cookie = 'appid' +'=; expires=Thu, 01-Jan-70 00:00:01 GMT;';

window.location = 'web_login.php';
</script>
";
exit();
?>