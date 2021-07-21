const pixelCanvas = document.querySelector("#pixelCanvas");
const sizePicker = document.querySelector('#sizePicker');

function makeGrid(height, width) {
	pixelCanvas.innerHTML = null; // reset the grid to a blank state
	// nested for loop to generate the rows and cells
	for (let i = 0; i < height; i++) {
		var tableRow = pixelCanvas.insertRow(i);
		for (let j = 0; j < width; j++) {
			var tableCell = tableRow.insertCell(j);
			tableCell.addEventListener('click', function(event) {
				const colorPicker = document.getElementById('colorPicker').value;
				event.target.style.backgroundColor = colorPicker;
			});
		}
	}
}
// When size is submitted by the user, call makeGrid()
sizePicker.addEventListener('submit', function(event) {
	event.preventDefault();
	var height = sizePicker.height.value;
	var width = sizePicker.width.value;
	makeGrid(height, width); // hoisting
})
