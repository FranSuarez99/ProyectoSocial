
var letters = 10; //Max number of letters in a word

var table_row = document.getElementById("div_select"); // selects container
var formElement = document.getElementById("select0"); // select to copy
var letter = document.getElementById("select0_letter"); // input where the value will be saved
for(var i=1;i<letters;i++){ //Adds the letters (Copy and paste the selects)
    var aux_form = formElement.cloneNode(true);
    var aux_letter = letter.cloneNode(true);
    aux_form.id = "select"+i;
    aux_letter.id = "select"+i+"_letter";
    aux_letter.name = "select"+i+"_letter";
    table_row.appendChild(aux_letter);
    table_row.appendChild(aux_form);
}

for(var i=0;i<letters;i++){ //Transforms each select to a div using Slick jQuery plugin
	$("#select"+i).ddslick({
        width:"100%",
        imagePosition:"left",
        selectedText:"test¿",
        onSelected: function(data){
        	$(("#"+data.original.context.id+"_letter")).html(data.selectedData.value);
        }
	});
	document.getElementById("select"+i).hidden = true;
}
document.getElementById("select0").hidden = false;

function addLetter(){ // show the last hidden select
	var letterNum = document.getElementById("letterNum");
	var aux = parseInt(letterNum.value);
	if(aux < letters){
		document.getElementById("select"+aux).hidden = false;
		letterNum.value = aux+1;
	}
}

function removeLetter(){ // hide the last shown select 
	var letterNum = document.getElementById("letterNum");
	var aux = parseInt(letterNum.value);
	if(aux > 1){
		document.getElementById("select"+(aux-1)).hidden = true;
		letterNum.value = aux-1;
	}
}
