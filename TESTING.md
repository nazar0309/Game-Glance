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


