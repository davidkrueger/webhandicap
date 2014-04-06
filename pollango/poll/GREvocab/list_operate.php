<?

// connect to the mysql database



// don't allow browsers to cache the contents of this page because it may change
header('Cache-Control: no-cache, must-revalidate');
header('Pragma: no-cache'); // for HTTP/1.0
header('Expires: Thu, 01 Jan 1970 00:00:00 GMT');

// request for a new id
if (isset($_GET['getid'])&& isset($_GET['url']) && isset($_GET['title'])) {
  // insert a new empty note and return it's id
  $url = strtolower($_GET['url']);
  $title = $_GET['title'];
  if (mysql_query("INSERT INTO list_info (text,user_email,title) VALUES('$url','$email','$title')")) {
    echo mysql_insert_id();
  } else {
    echo 0; // the insert somehow failed (should add more error handling)
  }
}

// init the list with all current notes
else if (isset($_GET['init']) ) {
  // first do a cleanup of the notes list (remove notes which are added but not edited)
  mysql_query("DELETE FROM list_info WHERE text = '' AND user_email='$email'");
 
  $query = "
    SELECT *
    FROM list_info WHERE user_email='$email'
   ";
  $result = @mysql_query($query);

  @header('Content-type: text/javascript');
 
  while ($row = mysql_fetch_assoc($result)) {
    $text = addslashes($row['text']);
	
   $title = addslashes($row['title']);

    // we are returning javascript code which will call the addnote function
    echo "addnote({$row['id']}, '$title', '$text'); \n";
  }
}

// delete a note
else if (isset($_GET['del']) &&
         is_numeric($_GET['del'])) {
  @mysql_query('DELETE FROM list_info WHERE id = '.$_GET['del']);
}

// update the contents of a note
else if (isset($_POST['id']) &&
         is_numeric($_POST['id'])) {
  // strip the tags from the note text
  $text = strip_tags($_POST['text']);
	$email = $_COOKIE['web2phone_email'];
  $query = "
    UPDATE list_info
    SET text = '$text', user_email = '$email'
    WHERE id = {$_POST['id']}
   ";
  mysql_query($query);
}

?>