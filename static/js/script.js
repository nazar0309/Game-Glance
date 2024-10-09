document.addEventListener('DOMContentLoaded', function () {
    // Set timeout to remove the 'show' class after 3 seconds to trigger fade-out
    setTimeout(function () {
        let alerts = document.querySelectorAll('.alert');
        alerts.forEach(function (alert) {
            alert.classList.remove('show'); // This will trigger the fade-out effect
            setTimeout(function () {
                alert.remove(); // Remove the alert from the DOM after fade-out completes
            }, 500); // Duration of the fade-out transition (matches the Bootstrap fade duration)
        });
    }, 3000); // 3 seconds delay before starting the fade-out
});

