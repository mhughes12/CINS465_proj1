

function newGame() {
  let table = document.getElementById("t1");
  let inputs = table.getElementsByTagName("input");
  for (let i=0; i < inputs.length; i++) {
    if (!inputs[i].disabled) {
      inputs[i].value = "";
    }
  }
}



function move(){
  var originLoc = document.getElementById('origin').value;
  var destinationLoc = document.getElementById('destination').value;

  var originPiece = document.getElementById(originLoc).innerHTML;

  if(originPiece.includes("&nbsp;")){
    return;

  }

else if(originPiece.includes("<sub>" && "<sup>")){
    document.getElementById(destinationLoc).innerHTML = "&#9814";

    document.getElementById(originLoc).innerHTML = "<sup>1</sup> &nbsp<sub>A</sub>";

  }

  else if(originPiece.includes("<sup>")){

    var n = originPiece.lastIndexOf(">");
    var cut = originPiece.slice(0, n+1);
    var piece = originPiece.slice(n+1,originPiece.length);
    document.getElementById(destinationLoc).innerHTML = piece;

    document.getElementById(originLoc).innerHTML = cut;

  }

  else if(originPiece.includes("<sub>")){

    var n = originPiece.indexOf("<");
    var cut = originPiece.slice(n, originPiece.length);
    var piece = originPiece.slice(0,n);
    document.getElementById(destinationLoc).innerHTML = piece;

    document.getElementById(originLoc).innerHTML = "&nbsp"+cut ;

  }




  else if(!originPiece.includes("&nbsp;")){
    document.getElementById(destinationLoc).innerHTML = originPiece;

    document.getElementById(originLoc).innerHTML = "";

  }









  }
