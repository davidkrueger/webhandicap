<div id="wrapper">
<?php if(isset($loginerror)) {
	if($loginerror==1){
		echo "Incorrect email/password combination. Please try again or register.";
	}
	if($loginerror==2){
		echo "Please enter an e-mail and password.";
	}
	if($loginerror==3){
		echo "Please log-in.";
	}
}
?>

  <form name="login_form" id="login_form" class="form" action="login_operate.php" onsubmit="" method="post">
  <ul class="list4">
	<li>
    <label for="email">E-mail:</label>
    <input type="text" name="email" id="email" />
	</li>
	<li>
    <label for="password">Password:</label>
    <input type="password" name="password" id="password" />
	<li>
	<li>
    <input type="submit" value="Submit" class="submit" />
	</li>
  </ul>
  </form>
</div>

