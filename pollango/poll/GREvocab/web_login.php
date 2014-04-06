<?php
	if(isset($_COOKIE['web2phone_email']) && isset($_COOKIE['web2phone_password'])){
		//echo $_COOKIE['email'];
		header("location: web.php");
		//echo "failure";
		exit();
	}
	include("generic_header.php");
	?>
	<ul class="list3">
		<li>
			<br/><em><b>New User?</b></em><br>
								<a href="register.php"><em><b>Register here.</b></em></a>
									<h3>Log in to update your web2phone bookmark</h3>
									<?php include("login_form.php");?>
		</li>
		<li class="alt">

									<img src="web2phone_app_example.png" height=500px>
		</li>
	</ul>
<?php
include("generic_footer.php");?>
