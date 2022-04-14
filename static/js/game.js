
function addLetter(){
	var table_row = document.getElementById("queso")
	var formElement = document.createElement("select");
	var white = document.createElement("option");
	var red = document.createElement("option");
	var green = document.createElement("option");
	formElement.appendChild(white);
	formElement.appendChild(red);
	formElement.appendChild(green);
	table_row.appendChild(formElement);
}

function removeLetter(){
	var table_row = document.getElementById("queso");
	if(table_row.children.length > 1){
		table_row.removeChild(table_row.lastElementChild);
	}
}

addLetter()