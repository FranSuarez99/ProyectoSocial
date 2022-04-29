window.onload = function () {

    /* event listener */
    document.getElementsByName("sonidos")[0].addEventListener('change', doThing);
    console.log("a");

    /* function */
    function doThing(){
        var table_row = document.getElementById("new_word_table");
        table_row.innerHTML = "";
        var number = document.getElementById("sonidos").value
		console.log("a")

        
        
        for (let i = 0; i < number; i++) {
            table_row.innerHTML = "<select id='intento' style='width: 200px;'><option data-img_src= ../static/images/white.png></option></select>"  
        }
        
    }

}



$(document).ready(function () {
    function custom_template(obj){
        var data = $(obj.element).data();
        var text = $(obj.element).text();
        if(data && data['img_src']){
            img_src = data['img_src'];
            template = $("<div><img src=\"" + img_src + "\" style=\"width:100%;height:150px;\"/><p style=\"font-weight: 700;font-size:14pt;text-align:center;\">" + text + "</p></div>");
            return template;
        }
    }
    var options = {
    'templateSelection': custom_template,
    'templateResult': custom_template,
    }
    $('#intento').select2(options);
    $('.select2-container--default .select2-selection--single').css({'height': '220px'});
    
  });