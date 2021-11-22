// we create three separate, but very similar, functions that enable us to save information related to every item

function ladder() {
  document.getElementById("nameOfItem").innerHTML = "LADDER";
  // we change the inner HTML paragraph with the given ID to say the name of the relevant item clicked on
  document.getElementById("itemName").value = "Ladder";
  // we change the value of the thing with ID itenName to the relevant item, which we can save for Python database work
  openForm();
  // we call our function to open the form
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
    // by default our form is closed, so this opens it by making it visible
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
  }