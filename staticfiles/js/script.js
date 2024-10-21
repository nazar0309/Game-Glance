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
    // Get all delete buttons
    const deleteButtons = document.querySelectorAll('.delete_btn');
    
    // Loop over each button and add an event listener
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Show a confirmation dialog
            let confirmation = confirm("Are you sure you want to delete this review?");
            
            // If the user confirms, submit the form related to the clicked button
            if (confirmation) {
                // Find the closest form and submit it
                button.closest('form').submit();
            }
        });
    });
});



   

