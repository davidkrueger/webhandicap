<div id="wrapper">
<?php if(isset($_GET["regerror"])){
		$regerror = $_GET["regerror"];
	
		if ($regerror == 1){
			echo "This e-mail is already registered. Please log-in";	
		}
		if ($regerror ==2) {
			echo "Please fill in all fields";	
		}

	}
?>
  <form name="register_form" id="register_form" class="form" action="register_operate.php" onsubmit="return web2phone_register_validate(this)" method="post">
    <ul class="list4">

  </ul>
  </form>
  <em><b>Already registered?</b></em><br>
  <a href="web_login.php"><em><b>Log-in here.</b></em></a><br><br>

</div>

