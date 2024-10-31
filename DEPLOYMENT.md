[&lt; Back to README file](/README.md)

# DEPLOYMENT

1. Clone the repository:
    -   Open a folder on your computer using the **Command Prompt** on Windows, **Terminal** on Mac or the respective on your device.
    -   Run the following command:
        -   `git clone https://github.com/cjphawes/restaurant-booking-system.git`
---
2. Create your own Github repository to host the code.
---
3. To set the remote repository location to your repository, run the command
    -   `git remote set-url origin <YOUR GITHUB REPO PATH>`
    ---
4. _Push_ the files to your repository to host the code, running the command:
    -   `git push`
    ---
5. Create a Heroku account, if you haven't already, click [Heroku sign-up](https://signup.heroku.com/?utm_source=google&utm_medium=paid_search&utm_campaign=emea_heraw&utm_content=general-branded-search-rsa&utm_term=heroku%20deploy&utm_source_platform=GoogleAds&gad_source=1&gclid=CjwKCAjw3624BhBAEiwAkxgTOnW3NMOV1WnmmRl3waphvbeJMziUKDW38F0Dy3uLfBJLsjNUm-vZdxoCp9MQAvD_BwE)
---
6. Create a new application, from selecting **Create new app** from the dropdown. Follow the steps on the page and click **Create app**.

![Create an app on Heroku_1](/static/test_images/dp_1.png)
![Create an app on Heroku_2](/static/test_images/dp_2.png)

---
7. Navigate to the **Deploy** tab, opening up the Deploy section.
![Deploy tab on Heroku](/static/test_images/dp_3.png)

---
8. Link your Github account and connect the application to the repository you just created.
![Connect Github account](/static/test_images/dp_4.png)

---
9. Navigate to the **Settings** tab, opening up the Settings section.
![Settings tab on Heroku](/static/test_images/dp_10.png)

---
10. Click **Add Buildpack**.
![Add buildpack](/static/test_images/dp_12.png)

---
11. Add the **Python** buildpack.
![Adding python buildpack](/static/test_images/dp_5.png)

---
12. Click **Reveal Configs**
![Reveal config vars](/static/test_images/dp_11.png)

---
13. Add these Config Vars:
    -   **KEY**: DISABLE_COLLECTSTATIC | **VALUE**: 1
    -   **KEY**: SECRET_KEY | **VALUE**: "YOUR OWN SECRET KEY"
    -   **KEY**: DATABASE_URL | **VALUE**: "YOUR OWN DATABASE URL"
![Adding config vars](/static/test_images/dp_6.png)

---
14. Return back to the **Deploy** tab, opening up the Deploy section.
![Deploy tab on Heroku](/static/test_images/dp_3.png)

---
15. At the bottom of the page, click **Deploy** branch.
![Deploy button](/static/test_images/dp_7.png)

---
16. Wait while Heroku is deploying your application.
![Awaiting deployment of project](/static/test_images/dp_8.png)

---
17. Once complete, click **View** to open the program in thw web browser.
![Deploy the project](/static/test_images/dp_9.png)

**Your project should now render in the browser! Have fun!**

[&lt; Back to README file](/README.md)