<?php
include_once("web2phone_db_functions.php");
if(!validate_login()){
	header("location: web_login.php");
	exit();
	}

include('generic_header.php');
echo "refer:".$_SERVER['HTTP_REFERER'];
?>
<script>
alert(document.referrer) 
</script>
<a href="one_click_add.php">test</a>
<table>
	<tr>
		<td>
			<form name="update_form" id="web2phone_add_bookmark_form" class="form" action="" onsubmit="" method="post">
			<table>
				<tr>
					<td>
						<labelwide>Add a new bookmarks:</labelwide>
						<br/>
						Note: Need web2phone App version 1.2 or later to use multiple bookmarks
						<br/>
					</td>
				</tr>
				</tr>
				<tr>
					<td><labelwide for="title">Bookmark Name:</labelwide><br/>(e.g. "Yahoo")<br/>
						<input type="text" name="title" id="title" />
					</td>
				</tr>
				<tr>
					<td>
						<labelwide for="url">Web Address:</labelwide><br/>(e.g. "www.yahoo.com")<br/>
						<input type="text" name="url" id="url" />
					</td>
				</tr>
				<tr>
					<td>
						<input type="hidden" id="getid" value="1">
						<input type="submit" value="Submit" class="submit" />
					</td>
				</tr>
			</table>
			</div>
		</td>
	</tr>
	<tr>
		<td>Click the <img src="dele.gif"/> to delete. Click the text to follow a bookmark.
			<div class="list2">
			  <ol id="list">
			  </ol>
			</div>
		</td>
	</tr>
</table>
<?php
	include_once('generic_footer.php');
?>