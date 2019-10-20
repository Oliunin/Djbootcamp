var commands = ['add','remove','display','quit']
var roster = [];

function addstud() {
  var student = prompt('what is the name of a student?')
  roster.push(student)
}
function remstud() {
  var student = prompt('what is the name of a student you want to remove?')
  var stpos = roster.indexOf(student);
  roster.splice(stpos,1)
}


var start = prompt('start app? y/n');
var command = 'none';

if (start = "y") {
  while (command !== "quit") {
    var command = prompt('what do you wanna do with roster?');
      if (command == "add") {addstud()
      }else if (command == "remove") {remstud()
      }else if (command == "display") {console.log(roster)
      }
    }
  }

alert('Bye bye');
