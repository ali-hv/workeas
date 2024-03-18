document.querySelectorAll('.task-box').forEach(task => {
    task.addEventListener('click', () => {
        if (task.classList.contains('open')) {
           task.classList.remove('open');
        }
        else {
            // Close all dropdowns
            document.querySelectorAll('.task-box').forEach(task => {
                task.classList.remove('open');
            });

            // Open dropdown of clicked task-box
            task.classList.toggle('open');
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const tasks = document.querySelectorAll('.task-box');

    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase().trim();

        tasks.forEach(task => {
            const taskTitle = task.querySelector('h2').innerText.toLowerCase();
            const taskDescription = task.querySelector('p').innerText.toLowerCase();

            if (taskTitle.includes(searchTerm) || taskDescription.includes(searchTerm)) {
                task.style.display = 'block';
            } else {
                task.style.display = 'none';
            }
        });
    });
});

