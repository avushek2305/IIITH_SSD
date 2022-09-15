



function userValid(){
    
   
    document.getElementById("is uvalid").innerHTML = "valid";
   

}

function passValid(){
    let x = document.forms["myForm"]["Password"].value;
  let y = document.forms["myForm"]["CPassword"].value;
  if(x == y)
    document.getElementById("is valid").innerHTML = "valid";
 else
 document.getElementById("is valid").innerHTML = "notvalid";
}
function validateForm() {
  let x = document.forms["myForm"]["Password"].value;
  let y = document.forms["myForm"]["CPassword"].value;
  if (x != y) {
    alert("Password is not matched");
    return false;
  }
  else{
    let a = document.forms["myForm"]["name"].value;
    let b = document.forms["myForm"]["email"].value;
    let c = document.forms["myForm"]["userName"].value;
    // let d = document.forms["myForm"]["Lead"].value;
    let e = document.forms["myForm"]["Team Members"].value;
    var myKeyVals = {"Name": a, "email": b, "userName" :c," Member" : e};
    alert( JSON.stringify(myKeyVals,null,4));
  }
}

