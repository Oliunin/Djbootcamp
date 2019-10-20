function sleepIn(weekday, vacation) {
  console.log('weekday: ',weekday, "vacation: ",vacation);
  return (!wd || vac) }

var week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
var weekday = prompt("what day is it today?");
var vacation = prompt('are we on vacation? yes/no');

console.log(week);
if (week.includes(weekday))
  {wd = true}
  else {wd=false};
if (vacation == 'yes')
  {vac=true}
  else {vac=false};

if (sleepIn(wd,vac) == true) {alert('Go to slepp')}
else {alert('Go for a work, bitch')}
