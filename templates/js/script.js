        const selectorElement = document.querySelector('#select_model');
        const form = document.getElementById('models');
        const formCompany = document.querySelector('.company__form'),
              formEmployee = document.querySelector('.employee__form');


        document.addEventListener('DOMContentLoaded', () => {
            selectorElement.addEventListener('change', (event) => {
            if(selectorElement.value === 'company') {
                form.style.display = 'block';
                formCompany.style.display = 'block';
                formEmployee.style.display = 'none';
            }
            if(selectorElement.value === 'employee') {
                form.style.display = 'block';
                formEmployee.style.display = 'block';
                formCompany.style.display = 'none';

            }
            if(selectorElement.value === 'not'){
                form.style.display = 'none';
                formEmployee.style.display = 'none';
                formCompany.style.display = 'none';
            }
            });
            selectorElement.dispatchEvent(new Event('change'));
        });