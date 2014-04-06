<?php
include_once("web2phone_db_functions.php");
if(!validate_login()){
	header("location: web_login.php");
	exit();
	}

include('generic_header.php');
?>
										
									  <form name="update_form" id="update_form" class="form" action="" onsubmit="" method="post">
									  <table>
										<tr>
											<td>
												<label for="website">Bookmark URL:</label>
												
											</td>
										</tr>
										<tr>
											<td>
												
												(e.g. www.yahoo.com)
											</td>
										</tr>
										<tr>
											<td>
												<input type="text" name="website" id="website" />
											</td>
										</tr>
										<tr>
											<td>
												<input type="submit" value="Submit" class="submit" />
											</td>
										</tr>
									  <tr>
											<td>
												<div id="loading">
														<img src="ajax-loader.gif"></img>  Updating...
													</div>
												<div id="update_content">
													
						
													<?php	
													
														include_once("web2phone_db_functions.php");
														$url = get_url();
														
														if ($url != "") {
															echo "Current bookmark is:<br/>";
															echo "<label>".$url."</label>";
														}


													?>
												
												
												</div>
											</td>
										</tr>					
									</table>
									</form>
