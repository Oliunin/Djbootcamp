var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  // Add a method called nameLength that prints out thelength of the employees name to the console.
  nameLength: function() {console.log(this.name.length)},
  //Alert: Name is John Smith, Job is Programmer, Age is 31 if age is > 30
  agealert: function() {
    if (this.age >=30) {
      alert("Name: "+this.name+" Job is: "+this.job+" Age: "+this.age);
    }
  },
  // Add a method called lastName that prints out the employee's last name to the console.
  lastname: function() {
    var str = this.name;
    var res = str.split(" ");
    var lastname = res[1];
    console.log(lastname);
  }
}
