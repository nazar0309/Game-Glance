document.addEventListener("DOMContentLoaded", function() {
    // Get all the alerts with the custom-alert class
    const alert = document.querySelector('.custom-alert');
    if (alert) {
        // Set timeout to hide the alert after 3 seconds
        setTimeout(function() {
            alert.classList.remove('show');  // Bootstrap's fade-out class
            alert.classList.add('fade');     // Ensure fade-out transition
        }, 3000); // 3000ms = 3 seconds
    }
});