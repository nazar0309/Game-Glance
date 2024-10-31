[&lt; Back to README file](/README.md)

# TESTING

The project was tested constantly throughout the development process. I had multiple users try out my website on multiple web browsers to spot bugs or grammatical mistakes which they found and I corrected.

## Validation Testing

### Python Validation
I used the Code Institute Python Linter to ensure sure the source code throughout was PEP8 compliant. No errors/warnings were detected.

about/admin.py
![about/admin.py](/static/test_images/py_test_1.png)

about/apps.py
![about/apps.py](/static/test_images/py_test_2.png)

about/forms.py
![about/forms.py](/static/test_images/py_test_3.png)

about/models.py
![about/models.py](/static/test_images/py_test_4.png)

about/views.py
![about/views.py](/static/test_images/py_test_5.png)

gameblog/admin.py
![gameblog/admin.py](/static/test_images/py_test_6.png)

gameblog/forms.py
![gameblog/forms.py](/static/test_images/py_test_7.png)

gameblog/models.py
![gameblog/models.py](/static/test_images/py_test_8.png)

gameblog/views.py
![gameblog/views.py](/static/test_images/py_test_9.png)

gameglance/settings.py
![gameglance/settings.py](/static/test_images/py_test_10.png)

gameglance/urls.py
![gameglance/urls.py](/static/test_images/py_test_11.png)

user_profile/views.py
![user_profile/views.py](/static/test_images/py_test_12.png)



### HTML Validation Warnings and Errors

When validating the HTML templates for this project, I had encountered several warnings and errors. These messages primarily concern Django template language usage and do not affect the code execution or functionality of the application. Here’s a summary of these commonly encountered issues:

1. **Missing DOCTYPE**:
   - Since our HTML templates extend Django’s `base.html` or other parent templates, `<!DOCTYPE html>` may not be recognized by validators in each individual template. However, the final rendered HTML output includes it, ensuring proper document structure.

2. **Invalid Characters in Attribute Values**:
   - Django template tags, such as `{% url 'view_name' param %}` and `{{ variable }}`, are used dynamically within the HTML. These tags often trigger validation errors (`Illegal character in path segment`) but are interpreted correctly by Django’s templating engine, allowing the URLs and variable values to render as expected.

3. **`iframe` `frameborder` Attribute**:
   - The `frameborder` attribute for `<iframe>` elements is considered obsolete in HTML5. It is kept here for specific styling or backward compatibility but has no functional impact on the app.

4. **`button` Inside `a` Elements**:
   - Validation warns against using `<button>` elements inside `<a>` tags. In cases where this structure is used, the app functionality remains intact.

5. **Missing `<title>` Element**:
   - The title is typically included in `base.html`, but individual templates may lack it, resulting in a validation warning. The final rendered HTML will include a single `<title>` tag as expected.

These issues arise from the dynamic nature of Django’s templating syntax, which validators cannot interpret. They do not affect the functioning of the application, and the app runs smoothly despite these warnings. The Django template language is properly parsed at runtime, ensuring all variables, URLs, and elements render as intended.

### CSS Validation

All of the custom CSS lines in the project have been validated and found to be error-free. The stylesheets adhere to best practices, ensuring consistent rendering across browsers and devices. This contributes to the stability and visual appeal of the application, with no issues affecting layout, responsiveness, or design functionality.

![style.css](/static/test_images/css_test.png)

### JS Validation

No errors were found when passing it through the validator

![script.js](/static/test_images/js_test.png)

## Manual Testing (BDD)

- Be aware! Some of the evidence below may not show modal elements even though they appear during testing.

| ID No. | Action | Testing | Result | Evidence |
|--------|--------|---------|--------|----------|
| **1** | View games list | Navigate to the games section | The webpage displays a list of available games | ![View Games List](/static/test_images/ev_1.png) |
| **2** | Click on a game for details | Select a game from the list | The webpage displays the appropriate game template with a detailed description | ![Game Details](/static/test_images/ev_2.png) |
| **3** | View related games | Check for related games in the game description | The webpage displays games with the same genre | ![View Related Games](/static/test_images/ev_3.png) |
| **4** | Leave a review for a game | Input review details and click "Submit Review" | The review is submitted and displayed under the game | ![Submit Game Review](/static/test_images/ev_4.png) |
| **5** | Access the user profile | Click on the user profile icon | The webpage changes to the user profile page | ![View User Profile](/static/test_images/ev_5.png) |
| **6** | View reviews left by the user | Navigate to the reviews section in the profile | The webpage displays a list of reviews submitted by the user | ![View User Reviews](/static/test_images/ev_6.png) |
| **7** | Edit a review | Click on the edit button next to a review | The review editing form appears with existing details | ![Edit Game Review](/static/test_images/ev_7.png) |
| **8** | Submit edited review | Modify the review details and click "Submit" | The edited review is updated on the game page | ![Submit Edited Review](/static/test_images/ev_8.png) |
| **9** | Delete a review | Click on the delete button next to a review | A confirmation modal appears to confirm deletion | ![Delete Review](/static/test_images/ev_9.png) |
| **10** | Confirm deletion of review | Click "Confirm" in the deletion modal | The webpage returns to the page where the delete action was initiated | ![Confirm Delete Review](/static/test_images/ev_10.png) |
| **11** | Logout from the profile | Click on the logout button in the profile | The webpage redirects to the home page and shows "Log in" | ![Logout User](/static/test_images/ev_19.png) |
| **12** | Redirect to the home page | Click on the home logo | The webpage redirects to the home page | |
| **13** | Enter an incorrect URL | Manually input a URL that doesn't exist | The webpage redirects to the custom 404 page | ![Custom 404 Page](/static/test_images/ev_11.png) |
| **14** | Search for a game title | Enter an exact game title in the search bar | The webpage redirects to the corresponding game details page | |
| **15** | Search with partial game title | Enter letters from a game title in the search bar | The webpage displays a filtered list of games that match the query | ![Filtered Game List from Search](/static/test_images/ev_12.png) |
| **16** | Access the About page | Navigate to the About section from the navigation menu | The webpage displays information about the website ||
| **17** | Submit collaboration form | Fill in the name, email, and message fields and click "Submit" | The form is submitted successfully with a confirmation message | ![Submit Collaboration Form](/static/test_images/ev_13.png) |
| **18** | Validate email format | Enter an invalid email format and click "Submit" | The webpage displays an error message for invalid email | ![Invalid Email Format Error](/static/test_images/ev_14.png) |
| **19** | Verify edit/delete buttons | Check for edit/delete buttons on the reviews page for user's reviews | Edit and delete buttons appear next to the reviews that belong to the user | ![Edit/Delete Buttons on Reviews Page](/static/test_images/ev_15.png) |
| **20** | Delete review from profile page | Click delete button on a review from the profile page | The confirmation modal appears, click "Confirm" | The user is returned to the profile page with the review removed ||
| **21** | Delete review from game details page | Click delete button on a review from the game details page | The confirmation modal appears, click "Confirm" | The user is returned to the game details page with the review removed ||
| **22** | Access profile page from another browser | Attempt to access the profile page from a different browser where the user is not authenticated | The webpage shows an "Access Denied" message or redirects to the login page | ![Access Denied to Profile Page](/static/test_images/ev_16.png) |
| **23** | Access edit review page from another browser | Attempt to access the edit review page from a different browser where the user is not authenticated | The webpage shows an "Access Denied" message or redirects to the login page | ![Access Denied to Edit Review Page](/static/test_images/ev_17.png) |
| **24** | Check pagination on game list | Navigate to the games list page | The page displays a limited number of games with pagination controls ||
| **25** | Navigate to next page of games | Click on the next page button | The webpage updates to show the next set of games ||
| **26** | Navigate to previous page of games | Click on the previous page button | The webpage updates to show the previous set of games |

## User Story Testing

| ID No. | User Story                   | Requirements Met |
|--------|-------------------------------|------------------|
| **1**  | Game list                    | Yes             |
| **2**  | Click a value to filter the view | Yes             |
| **3**  | Manage reviews               | Yes             |
| **4**  | Click a value to filter the view | Yes             |
| **5**  | View Searching               | Yes             |
| **6**  | Click a value to filter the view | Yes             |
| **7**  | Game Searching               | Yes             |
| **8**  | Click a value to filter the view | Yes             |

## Lighthouse Dev Tools
I used the Lighthouse Dev Tools to assess the performance and accessibility of my website.

#### Home Page
![Lighthouse Dev Tool](/static/test_images/l_test_1.png)

#### About Page
![Lighthouse Dev Tool](/static/test_images/l_test_2.png)

#### Game Details Page
![Lighthouse Dev Tool](/static/test_images/l_test_3.png)

- *Note:* Lighthouse couldn't display the embedded YouTube video on this page due to rendering limitations. However, this video functions correctly across various devices based on thorough testing.

#### Log Out Page
![Lighthouse Dev Tool](/static/test_images/l_test_4.png)

- *Note:* Lighthouse could not open the **Profile Page** or **Review Edit Page** due to security restrictions. Both pages are accessible only to authenticated users.

- The performance level may vary depending on image sizes and embedded media.

[&lt; Back to README file](/README.md)










