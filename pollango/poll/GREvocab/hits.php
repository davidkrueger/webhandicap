<?php

include("web2phone_db_functions.php");
connect_to_db();

$qry="SELECT `id` FROM user";

$result = mysql_query($qry);

//check if app name already exists
if(mysql_num_rows($result)>0){
	$total = 0;
     while($row=mysql_fetch_assoc($result)){
				$total +=1;
			}
	echo $total."<br/>";

	
}

?>
