// ran in console from input page
var input = document.getElementsByTagName("pre")[0].textContent;

// part one, final floor, answer 280
var final_floor = input.match(/\(/g).length - input.match(/\)/g).length

// part two, when basement
function part_two_first_basement(input) {
	var current_floor = 0;
	for (var step in input) {
		if (input[step] == '(') {
			current_floor++;
		} else {
			current_floor--;
		}

		if (current_floor == -1) {
			return Number(step)+1;
		}
	}
}

part_two_first_basement(input);
// answer 1797
