
var butt = document.querySelector("#b");
console.log(butt);
butt.addEventListener('click',clearBoard)

var cells = document.querySelectorAll("td");
console.log(cells);
console.log(cells.length);

for (var i = 0; i < cells.length; i++) {cells[i].addEventListener("click", changeMarker)};

function changeMarker() {
    if (this.innerHTML == '<img src="empty.png" alt="">') {this.innerHTML = '<img src="circle.png" alt="">';console.log("enteryng loop");}
    else if (this.innerHTML == '<img src="circle.png" alt="">') {this.innerHTML = '<img src="cross.png" alt="">';}
    else if (this.innerHTML == '<img src="cross.png" alt="">') {this.innerHTML = '<img src="empty.png" alt="">';}
  };

function clearBoard () {for (var i = 0; i < cells.length; i++) {cells[i].innerHTML = '<img src="empty.png" alt="">'; console.log("clearing cells");}
};
