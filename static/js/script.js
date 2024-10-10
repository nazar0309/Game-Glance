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
     // Handle Delete Button Click
     document.querySelectorAll('.delete_btn').forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();  // Prevent form submission
            let reviewId = this.getAttribute('review_id');
            let csrfToken = this.closest('form').querySelector('input[name="csrfmiddlewaretoken"]').value;
            
            // Send AJAX POST request to delete the review
            fetch(`/review/delete/${reviewId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                },
            }).then(response => response.json())
              .then(data => {
                  if (data.success) {
                      // Remove the review card from the page
                      this.closest('.review_card').remove();
                  }
              });
        });
    });

    // Handle Edit Button Click
    document.querySelectorAll('.edit_btn').forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();  // Prevent form submission
            let reviewId = this.getAttribute('review_id');
            let newBody = prompt("Enter the new review text:");
            let csrfToken = this.closest('form').querySelector('input[name="csrfmiddlewaretoken"]').value;

            if (newBody) {
                // Send AJAX POST request to edit the review
                fetch(`/review/edit/${reviewId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                    body: new URLSearchParams({
                        'body': newBody
                    })
                }).then(response => response.json())
                  .then(data => {
                      if (data.success) {
                          // Update the review text on the page
                          this.closest('.review_card').querySelector('p.review_body').textContent = newBody;
                      }
                  });
            }
        });
    });
});

   

