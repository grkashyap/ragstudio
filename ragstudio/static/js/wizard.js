function highlightStep(step) {
    for (let i = 1; i <= 4; i++) {
        const circle = document.getElementById(`circle-${i}`);
        if (circle) {
            circle.classList.toggle('active', i <= step);
        }
    }
}