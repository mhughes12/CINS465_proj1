function initBoard() {
  document.getElementById("r1c3").firstChild.focus();
}

function newGame() {
  let table = document.getElementById("t1");
  let inputs = table.getElementsByTagName("input");
  for (let i=0; i < inputs.length; i++) {
    if (!inputs[i].disabled) {
      inputs[i].value = "";
    }
  }
  initBoard();
}

function checkCellValid(cell) {
  let value = parseInt(cell.value);
  let isValid = (Number.isInteger(value) && value >= 1 && value <=9);
  if (isValid) {
    cell.style.color = "green";
    cell.blur();
  }
  else
  cell.value = "";
  return isValid;
}
