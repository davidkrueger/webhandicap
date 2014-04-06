function update_note_text() {
    var ret = "";
    
	$.ajax({
		url : "./ajax_test_do_something",
		success : function(data){
			ret =  "5";
		}
		});
     return ret;
}