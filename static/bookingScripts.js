function ladder() {
  document.getElementById("nameOfItem").innerHTML = "LADDER";
  document.getElementById("itemName").value = "Ladder";
  openForm();
}

function drill() {
  document.getElementById("nameOfItem").innerHTML = "DRILL";
  document.getElementById("itemName").value = "Drill";
  openForm();
}

function chairs() {
  document.getElementById("nameOfItem").innerHTML = "CHAIRS";
  document.getElementById("itemName").value = "Chairs";
  openForm();
}

function openForm() {
    document.getElementById("myForm").style.display = "block";
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
  }