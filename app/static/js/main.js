// Função para validar o formulário
function validateForm() {
    const data = document.getElementById('data').value;
    const sala = document.getElementById('sala').value;
    const horario = document.getElementById('horario').value;
    const responsavel = document.getElementById('responsavel').value;
    const email = document.getElementById('email').value;

    if (!data || !sala || !horario || !responsavel || !email) {
        alert('Por favor, preencha todos os campos obrigatórios.');
        return false;
    }

    // Validação básica de email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Por favor, insira um email válido.');
        return false;
    }

    return true;
}

// Função para definir a data mínima no campo de data
document.addEventListener('DOMContentLoaded', function() {
    const dataInput = document.getElementById('data');
    if (dataInput) {
        const today = new Date();
        const tomorrow = new Date(today);
        tomorrow.setDate(tomorrow.getDate() + 1);
        
        // Formata a data para YYYY-MM-DD
        const formattedDate = tomorrow.toISOString().split('T')[0];
        dataInput.min = formattedDate;
    }
});

// Remove mensagens flash após 5 segundos
setTimeout(function() {
    const alerts = document.getElementsByClassName('alert');
    for (let alert of alerts) {
        alert.style.display = 'none';
    }
}, 5000);