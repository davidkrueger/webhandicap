<?php

include("web2phone_db_functions.php");
connect_to_db();

$qry="SELECT * FROM user";

$result = mysql_query($qry);

//check if app name already exists
if(mysql_num_rows($result)>0){
	$total = 0;
	$array;
	$installed = 0;
     while($row=mysql_fetch_assoc($result)){
				$total +=1;
				$id = $row['id'];
				if (strlen($row['id']) <2){
					$id = '0'.$id;
				}
				$array[$total]= $id.": ".$row['web_hits']." ".$row['app_hits']." ".$row['notes_app_hits']." ".$row['notes_web_hits'];
				if($row['notes_app_hits'] != '0'){
					$installed+=1;
				}
			}
	sort($array);
	foreach ($array as $item){
		echo $item."<br/>";
	}
	echo $total;
	echo "<br/>".$installed;
}

?>
