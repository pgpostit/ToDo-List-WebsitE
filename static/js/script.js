
const checkboxes = document.querySelectorAll('input[type="checkbox"]');

// Percorre cada checkbox
checkboxes.forEach((checkbox) => {
  
  checkbox.addEventListener('change', () => {
    
    const label = checkbox.nextElementSibling;

    if (checkbox.checked) {
      
      label.style.textDecoration = 'line-through';
    } else {
      
      label.style.textDecoration = 'none';
    }
  });
});


const form = document.getElementById('taskForm');


form.addEventListener('submit', (event) => {
  event.preventDefault(); 

  console.log('Formulário enviado!');
});


form.addEventListener('keypress', (event) => {
  if (event.key === 'Enter') {
    event.preventDefault(); 
    form.submit(); 
  }
});
