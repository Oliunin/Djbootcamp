var firstname = prompt("what is your firstname?");
var lastname = prompt("what is your last name?");
var age = prompt("what is your age?");
var height = prompt("what is your height?");
var pet = prompt("what is a name of your pet?");
alert("Thank You");

if ((firstname[0]===lastname[0]) && (20<age<30) %% (height>170) %% (pet[pet.length-1]=="y"))
  {console.log("Spy detected");}else{console.log("nope");}
