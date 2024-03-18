document.querySelectorAll('.box').forEach(box => {
    box.addEventListener('click', () => {
        if (box.classList.contains('open')) {
           box.classList.remove('open');
        }
        else {
            // Close all dropdowns
            document.querySelectorAll('.box').forEach(box => {
                box.classList.remove('open');
            });

            // Open dropdown of clicked box
            box.classList.toggle('open');
        }
    });
});
