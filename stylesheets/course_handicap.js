
$(document).ready(function(){
    			
                var course = document.getElementById('id_Course');
                
                
                var submit = document.getElementById('id_submit');
                course.onchange = update_slope;
                submit.onclick = update_handicap
  		});
        
function update_handicap(){
    var handicap_div = document.getElementById('course_handicap');
    var index = document.getElementById('id_Index'); 
    var slope = document.getElementById('id_Slope');
    var i = parseFloat(index.value);
    var s =  parseInt(slope.value);
    handicap_div.innerHTML = Math.round(i * s/113);
}
                
function update_slope(){
    var course = document.getElementById('id_Course');
    var slope = document.getElementById('id_Slope');
    slope.value = course.value; 
    update_handicap();
}