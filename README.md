# Game Glance

Hello Fellow Gamers!

Welcome to [**Game Glance**](https://game-glance0309-8d0894eb4eb4.herokuapp.com/), an interactive platform where gaming enthusiasts can explore a curated list of games, view detailed descriptions, and engage with the community by leaving reviews. Registered users can manage their reviews directly from the game description page, with the ability to edit or delete them if the review belongs to them. Users also have access to a Profile Page, where they can view all the reviews they have created and search for specific reviews using the search bar.


![GG Landing Page](/static/images/landing.png)
---

## Goals

### My Goals

For this project, I have aimed to:
- Provide an intuitive platform where users can browse a list of games and view detailed descriptions.
- Enable users to leave, edit, and delete reviews for individual games.
- Ensure users can manage their reviews directly from the game description page.
- Provide a search bar to help users quickly find games by title or keyword.
- Offer a **Related Games** section on each game's description page to suggest similar games.
- Give users a personalized **Profile Page** to view and manage their reviews, with a search bar to locate specific reviews.

## User Stories

| **As a** | **I can** | **So that** |
|----------|-----------|-------------|
| User | View a list of available games | I can explore games and choose which ones I want to know more about |
| User | Search for a specific game by title or keyword | I can quickly locate a game I’m interested in |
| User | Click on a game to see its detailed description | I can learn more about the game before deciding to leave a review |
| User | Register for an account | I can participate by leaving reviews and managing my profile |
| User | Leave reviews on a game's page | I can share my opinions or feedback about the game |
| User | Edit or delete my reviews directly from the game page | I can modify or remove feedback I no longer wish to display |
| User | See a list of related games on a game’s description page | I can discover more games that might interest me |
| User | View all the reviews I have written on my **Profile Page** | I can keep track of my contributions and manage my activity |
| User | Search for a specific review on my **Profile Page** | I can quickly find and manage my reviews |
| User | Log in and out of my account | I can access my personalized features and log out when I’m done |

### Project Board

GitHub Project Boards were used to manage the project. It helped me to prioritize the tasks and to keep track of my progress. 
This displays a mixture of completed, nearly completed and not started issues:

![KUIDAORE Project Board](/static/images/project_board.png)

This displays a mixture of completed, nearly completed and not started issues:

---

## Wireframes

[Take me to the Project Wireframes](/WIREFRAMES.md)

## ERD Model

[Take me to the Database Model](/ERDDIAGRAM.md)

## Features

### Existing Features
- **Games List**: ![Game List](/static/images/game_list.png) 
Displays all available games with basic information such as title, genre, and release date.
- **Search Bar**: ![Search Bar](/static/images/search_bar.png) 
Allows users to search for games by title or keyword to quickly locate games of interest.
- **Game Details Page**: ![Search Bar](/static/images/game_details.png) 
Clicking on a game shows its detailed description, including genre, platform, release date, and user reviews.
- **Reviewing System**: ![Search Bar](/static/images/reviews_section.png) 
Registered users can leave reviews on each game, sharing their thoughts and feedback with others.
- **Edit/Delete Reviews**: ![Search Bar](/static/images/edit_review.png)
 ![Search Bar](/static/images/delete_review.png) 
Users can manage their own reviews by editing or deleting them directly from the game description page.
- **Related Games Section**: ![Search Bar](/static/images/related_games.png) 
Each game’s description page shows related games, helping users discover more content.
- **Profile Page**: ![Search Bar](/static/images/profile.png) 
Displays all reviews a user has written, with the ability to search for specific reviews.
- **About Page**: ![Search Bar](/static/images/about.png) 
Contains information about the website and a contact form for users to send inquiries or feedback.
- **User Authentication**: ![Search Bar](/static/images/sign_in.png) 
![Search Bar](/static/images/sign_up.png) 
Secure registration, login, and logout functionality for managing accounts.

## Things to Mention

 **Core Features**:
   - **Game Listing**: Users can browse a curated list of games, with details such as release date, genre, platform, and description.
   - **Review System**: Registered users can write reviews for games, rate them, and engage with other users through comments.
   - **User Profiles**: Users have personal profiles to manage their reviews.
   - **Responsive Design**: The website is fully responsive and optimized for mobile and desktop viewing.
   
 **Database Structure**:
   - The database is structured to support a seamless many-to-many relationship, enabling games to have multiple reviews, and each user to contribute to various reviews.

## Future Features

1. **Game Recommendation System**:
   - Implement a personalized recommendation engine that suggests games based on user preferences and past interactions, including genres and other users' ratings.

2. **Social Media Integration**:
   - Enable social sharing options so users can share game reviews or their profiles on social media platforms like Twitter, Facebook, and Reddit.

3. **Advanced Search and Filter Options**:
   - Allow users to filter games based on multiple criteria (e.g., platform, release date, genre) and perform keyword searches for specific titles or developers.

4. **Rating System and Leaderboards**:
   - Add a rating system for each game, allowing users to give ratings that affect a game's popularity ranking. A leaderboard could showcase top-rated games each month.

5. **Wishlist and Watchlist**:
   - Allow users to create wishlists and watchlists for upcoming games, with notifications for release dates or significant game updates.
