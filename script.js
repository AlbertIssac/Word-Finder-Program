// Function to capitalize input letters
function capitalizeInput(event) {
    event.target.value = event.target.value.toUpperCase();
}

// Attach the capitalize function to each input field on page load
window.onload = function() {
    // Get all input fields by name attribute
    let inputFields = document.querySelectorAll("input[name^='letter']");

    inputFields.forEach(function(input) {
        input.addEventListener("input", capitalizeInput);
    });
};

// Function to remove the placeholder text when typing begins
const letterInputs = document.querySelectorAll('input[type="text"]');

letterInputs.forEach(input => {
    input.addEventListener('focus', function() {
        // Only clear placeholder if the field is empty
        if (this.value === "") {
            this.placeholder = "";
        }
    });

    input.addEventListener('blur', function() {
        // Restore the placeholder when the field is empty and loses focus
        if (this.value === "") {
            const letterIndex = this.getAttribute('name').replace('letter', '');
            const suffix = ['st', 'nd', 'rd', 'th'][letterIndex - 1] || 'th';
            this.placeholder = `${letterIndex}${suffix}`;
        }
    });
});

const boxes = document.querySelectorAll('.input-row input');

boxes.forEach(box => {
  box.addEventListener('click', () => {
    boxes.forEach(otherBox => otherBox.classList.remove('active')); 
    box.classList.add('active'); 
  });
});