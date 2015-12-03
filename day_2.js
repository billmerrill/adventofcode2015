var input = document.getElementsByTagName("pre")[0].textContent;
var presents_re = /([0-9]+)x([0-9]+)x([0-9]+)/g;
var presents = presents_re.exec(input)

var area = 0;

function cmp_number(a, b) {
  return a - b;
}

var p;
// wrapping paper for boxes, total area + 1 extra smallest side.
while ( (p = presents_re.exec(input)) !== null) {
    var d = [Number(p[1]), Number(p[2]), Number(p[3])]
    var sides = [d[0] * d[1], d[1] * d[2], d[0] * d[2]]
    sides = sides.sort(cmp_number);
    area += sides[0] * 3 + sides[1] * 2 + sides[2] * 2;
}
console.log('total area');
console.log(area);
