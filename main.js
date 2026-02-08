// Convert trackable code to uppercase as user types
document.addEventListener('DOMContentLoaded', function() {
    const codeInput = document.getElementById('code');
    const viewHistoryLink = document.getElementById('viewHistory');

    if (codeInput) {
        codeInput.addEventListener('input', function(e) {
            this.value = this.value.toUpperCase();

            // Show/hide history link based on valid code
            if (this.value.match(/^[A-Z0-9]{8}$/)) {
                viewHistoryLink.href = `/history/${this.value}`;
                viewHistoryLink.classList.remove('d-none');
            } else {
                viewHistoryLink.classList.add('d-none');
            }
        });
    }
});
