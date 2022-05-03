var selected = null;

var aux = document.getElementById("wordsContainer").style;
function selector(div){
	if(!selected){
		selected = div.id;
	}
	div.style.backgroundColor = "#66A9D9";
	if(selected != div.id){
		document.getElementById(selected).style = aux;
		selected = div.id;
	}
}