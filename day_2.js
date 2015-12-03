var input = document.getElementsByTagName("pre")[0].textContent;
var presents_re = /([0-9]+)x([0-9]+)x([0-9]+)/g;

var wrapping_paper_area = 0;
var ribbon_length = 0;


function cmp_number(a, b) {
  return a - b;
}

var p;
// wrapping paper for boxes, total wrapping_paper_area + 1 extra smallest side.
while ( (p = presents_re.exec(input)) !== null) {
    // dimensions
    var d = [Number(p[1]), Number(p[2]), Number(p[3])];
    d = d.sort(cmp_number);
    // side areas
    var sides = [d[0] * d[1], d[1] * d[2], d[0] * d[2]];
    sides = sides.sort(cmp_number);

    wrapping_paper_area += (sides[0] * 3) + (sides[1] * 2) + (sides[2] * 2);
    ribbon_length += (2 * d[0]) + (2 * d[1]) + (d[0] * d[1] * d[2]);
}
console.log('total wrapping paper area');
console.log(wrapping_paper_area);
console.log('total ribbon length');
console.log(ribbon_length);


/*
total wrapping paper area
2015-12-03 12:30:27.652 VM1849:27 1606483
2015-12-03 12:30:27.652 VM1849:28 total ribbon length
2015-12-03 12:30:27.652 VM1849:29 3842356
undefined
*/
