<h1 align="center">Guess Moo</h1>

[View the live project here.](https://guess-moo.herokuapp.com/)

Guess Moo is a Python terminal farm animal guessing game, which runs in the Code Institute mock terminal on Heroku.
The main goal of the game is for the program to guess the farm animal the player is thinking of in 20 questions or less.
This project was inspired by guessing games like Twenty Questions and Akinator.

<h2 align="center"><img src="https://res.cloudinary.com/dksu5snru/image/upload/v1683753209/Guess%20Moo/guess_moo_fptsps.png"></h2>

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

-   ### User stories

    -   #### Website Creator Goals

        1. As a Website Creator, I want to build an easily accessible app for users to play the game.
        2. As a Website Creator, I want to build a fun game that can be enjoyable for users of all ages.
        3. As a Website Creator, I want the game to function as intended.

    -   #### First Time User Goals

        1. As a First Time User, I want to easily understand the main purpose of the site.
        2. As a First Time User, I want to be able to easily navigate throughout the site and play the game.
        3. As a First Time User, I want to be easily able to understand how to play the game.

    -   #### Returning User Goals
        1. As a Returning User, I want to be able to start a new game quickly and easily.

-   ### Design
    -   #### Colours
        The colours in the game are supplied by the Python Colorama Model.

-   ### Flowchart

## Features

-   #### Start Screen
    * The start screen is the first thing users will see upon loading the website.
    * The game logo is displayed and users are prompted to press enter to start:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1683753209/Guess%20Moo/guess_moo_fptsps.png">
-   #### Main Menu
    * The main menu feature displays a menu with 3 different options for users to choose from:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684723699/Guess%20Moo/main_menu_xwsdgt.png">
    * If the user enters invalid input, this error message is displayed:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684724358/Guess%20Moo/main_menu_error_to2x7m.png">
-   ####  Game Information
    * The game information feature displays text explaining how the game is played.
    * Users are then directed back to the main menu:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684723963/Guess%20Moo/game_info_vbgknl.png">
-   #### Game Introduction
    * This feature introduces the game, then asks users for their name:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684725132/Guess%20Moo/introduction_hvdne5.png">
    * If the user input doesn't contain any characters, the following error message is displayed:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684725532/Guess%20Moo/invalid_name_chars_i3ndz8.png">
    * If the user input contains non-alphabetic characters, the following error message is displayed:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684725811/Guess%20Moo/invalid_name_alpha_rjcal1.png">
    * Once a valid name is input, the user is prompted to think of a farm animal and press enter when they're ready for the first question.
    * "Cam" is used as an example of a valid name input below:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684726009/Guess%20Moo/valid_name_fcck2g.png">
-   #### Questions
    * Up to 20 questions are asked about the farm animal the user is thinking of.
    * The question number is displayed above each question.
    * The user is prompted to answer either "Yes", "No" or "I don't know".
    * Questions are separated by borders to improve readability.
    * The first question is randomly generated so that it isn't the same for every game:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684726413/Guess%20Moo/first_question_mxxir8.png">
    * If the user enters an invalid answer, the following error message is displayed:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684726711/Guess%20Moo/questions_invalid_answer_n2neqe.png">
    * When valid answers are received, the game continues asking up to 20 questions until it is ready to make a guess:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684727143/Guess%20Moo/questions_ykzcm7.png">
-   #### Guessing
    * Once enough information is gathered about the farm animal the user is thinking of,
    the program makes a guess based on the most likely farm animal:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684727448/Guess%20Moo/make_guess_mqzpse.png">
    * If the user enters "yes", the following game over message is displayed, including the number of questions asked before the guess was made:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684728154/Guess%20Moo/guessed_correctly_te45ps.png">
    * If the user enters "no", the following game over message is displayed:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684728412/Guess%20Moo/guessed_incorrectly_gqhikh.png">
    * If user input is invalid, the following error message is displayed:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684728737/Guess%20Moo/invalid_final_answer_funpav.png">
-   #### Game Over Menu
    * When a game ends, the game over menu is displayed so that users can choose how they want to proceed.
    * The game over menu is similar to the main menu but instead of having a "Play Game" option, the game over menu has a "Play Again" option:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684729164/Guess%20Moo/game_over_menu_dv6dmx.png">
-   #### Exit Message
    * This message is displayed when users choose the exit option from either the main menu or game over menu:
    <br>
    <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684729491/Guess%20Moo/exit_game_fpqyvp.png">

- ### Features for Future Implementation
    * More animals could be added to the game.
    * ASCII art animals could be added to display when an animal is guessed correctly.

## Technologies Used

-   ### Languages Used
    * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

-   ### Python Packages
    * [Random](https://docs.python.org/3/library/random.html?highlight=random#module-random): used to choose random animal traits for generating the game questions
    * [Colorama](https://pypi.org/project/colorama/): used to change the colour and style of text printed to the mock terminal.
    * [Time](https://pypi.org/project/time/): used for typewriter function in extras.py

-   ### Frameworks, Libraries & Programs Used
    1. [Lighthouse:](https://developers.google.com/web/tools/lighthouse)
    <br> Lighthouse was used for testing code health, accessibility, speed and search engine optimisation.
    1. [Codeanywhere:](https://app.codeanywhere.com/)
    <br> Codeanywhere was used to develop project and organise version control.
    1. [GitHub:](https://github.com/)
    <br> GitHub is used to store the code for this project.
    1. [Heroku:](https://heroku.com/)
    <br> Heroku was used to deploy the live project.
    1. [Figlet:](http://www.figlet.org/)
    <br> Figlet was used to create the game logo ASCII art.
    1. [PEP8 CI Python Linter:](https://pep8ci.herokuapp.com/)
    <br> The Code Institute PEP8 python linter was used to validate all the Python code.
    1. [Lucidchart:](https://lucid.app/)
    <br> Lucidchart was used to create the flowchart.

## Testing

-   ### <em>Automated Testing:</em>
    -   #### Code Institute Python Linter
        <details><summary>run.py:</summary>
        <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684739656/Guess%20Moo/ci_linter_run_drtp7s.png"></details>
        <details><summary>animals.py:</summary>
        <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684744771/Guess%20Moo/ci-linter-animals_ei4mmp.png"></details>
        <details><summary>extras.py:</summary>
        <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684745060/Guess%20Moo/ci_linter_extras_o4b0bb.png"></details>
        <details><summary>game_art.py:</summary>
        <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684747623/Guess%20Moo/ci_linter_game_art_znfsdy.png"></details>
    <strong>All python files passed the Code Institute Python linter with no errors or warnings.</strong>

    -   #### Google Lighthouse
        <details><summary>Lighthouse Results:</summary>
        <img src="https://res.cloudinary.com/dksu5snru/image/upload/v1684751792/Guess%20Moo/Lighthouse_pkngvr.jpg"></details>

-   ### <em>Manual Testing:</em>
This section will cover the manual testing of all the features of this application. The purpose of manual testing is to identify any potential bugs or issues in the application's functionalities. The following steps were repeated multiple times from early development. Print statements were used throughout the program to ensure everything functioned as intended.
The website was sent to as many friends, colleagues and family members as possible for testing and feedback.  
I played through the game countless times, seeking to uncover bugs and optimize user experience.

#### Testing User Stories from User Experience (UX) Section

-   ##### Website Creator Goals

    1. As a Website Creator, I want to build an easily accessible app for users to play the game.

        1. Upon entering the site, users are automatically greeted with a large, bold logo with the name of the game.
        2. The logo contains bright text intended to make it immediately clear that the purpose of this site is to play a guessing game.
        3. The game infomation section is the first item on the main menu, so that new users can quickly and easily get their heads around the aim of the game and how it works.

    2. As a Website Creator, I want to build a fun game that can be enjoyable for users of all ages.

        1. This game is simple enough for user's of all ages to understand and enjoy.
        2. I hope this game manages to capture at least a little bit of the sense of wonder and magic that Twenty Questions type games bring.

    3. As a Website Creator, I want the game to function as intended.
        1. The game has been tested extensively and functions as intended.

-   ##### First Time User Goals

    1. As a First Time User, I want to easily understand the main purpose of the site.

        1. The main purpose of the site is immediately clear as soon as the page loads,
           the logo displays the name of the game "Guess Moo" and the tagline, "The farm animal guessing game".

    2. As a First Time User, I want to be able to easily navigate throughout the site and play the game.

        1. A great amount of thought was given to the flow of the program and how the user would experience the game, navigation is clear and users are always provided a clear route to where they might need to go.

    3. As a First Time User, I want to be easily able to understand how to play the game.

        1. The game info section explains in easy to digest points exactly how the game works.

-   ##### Returning User Goals

    1. As a Returning User, I want to be able to start a new game quickly and easily.

        1. The play new game function was created with user experience in mind, making it quick and easy to start a new game after a game ends.

#### Feature Testing

| Feature              | Expected outcome                               | Does it work?  |
| -------------        |:-------------:                                                                                    | -----:|
| Start Screen | Displays upon first loading the page.   | Yes |
| Main Menu | Displays after the start screen, giving users 3 choices.  |   Yes |
| Game Info | Displays information on how the game is played.          |  Yes |
| Game Introduction |  Intoduces the game, asks users their name and validates the user input. |  Yes   |
| Questions |  Begins the game loop where up to 20 questions are asked about animal traits.   |  Yes    |
| Guessing | Makes a guess based on the most likely animal.                                                             |   Yes  |
| Game Over Menu |  Displays the game over menu after a game ends. |  Yes |
| Exit Message | Displays a message when users choose to exit the program.     |  Yes  |

#### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge, Firefox and Safari 
    browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop and multiple mobile 
    devices.
-   A large amount of testing was done to ensure that every animal in the list could be guessed correctly.
-   A great amount of testing was done to ensure that there were no bugs affecting the gameplay.
-   Friends and family members were asked to play the game and provide feedback to point out any 
    bugs and/or user experience issues.

### Bugs
#### <em>Fixed:</em>
- I encountered a wealth of bugs and trials throughout the creation of this project, below I will detail a few.
- When I first got to the stage where the program could guess an animal, it returned the entire animal dictionary which was a simple fix, the "animal" key specifically had to be printed and not the animal dictionary with the highest probability.
- I also encountered an issue where the if a correct guess was made before 20 questions had been asked, the game loop continued asking questions until 20 was reached. I had to add break statements to fix this issue.
- When colorama colour codes were used alongside the typewriter function in extras.py, the colours would not display and numbers were printed before the string instead, I had to keep all typewriter text white to prevent this from happening.
- Another bug I encountered was that traits were being added to the asked list immediately after a question was generated, which caused problems if invalid input was received, the question was still considered asked and wouldn't be asked again, so I moved the code to append traits to the asked list to after valid user input is received.
- When the game ended the screen was clearing without displaying the game over menu, this was fixed by simply moving the clear function.

#### <em>Still Existing:</em>
- No known bugs at this time.

## Deployment

* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. The next page is the project's Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
7. Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button
8. Click Reveal Config Vars again and enter CREDS into the Key box and the Google credentials into the Value box
9. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
10. Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order
11. Scroll to the top of the page and choose the Deploy tab
12. Select Github as the deployment method
13. Confirm you want to connect to GitHub
14. Search for the repository name and click the connect button
15. Scroll to the bottom of the deploy page and select the preferred deployment type
16. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

## Forking This Project

* Fork this project by following the steps:

1. Open [GitHub](https://github.com/)
2. Click on the project to be forked
3. Find the Fork button at the top right of the page
4. Once you click the button the fork will be in your repository

## Cloning This Project

* Clone this project by following the steps:
  
1. Open [GitHub](https://github.com/)
2. Click on the project to be cloned
3. You will be provided with three options to choose from, HTTPS, SSH, or GitHub CLI, click the clipboard icon in order to copy the URL
4. Once you click the button the fork will be in your repository
5. Open a new terminal
6. Change the current working directory to the location that you want the cloned directory
7. Type git clone and paste the URL copied in step 3
8. Press Enter and the project is cloned

## Credits

### Resources

-   This video tutorial provided some inspiration for my animals.py file but no code was directly used from this source: [YouTube](https://www.youtube.com/watch?v=lOfyN7zFI5s)
-   This article provided interesting information on Bayes Theorem in relation to games like these: [Medium](https://medium.com/analytics-vidhya/building-akinator-with-python-using-bayes-theorem-216253c98daa)

### Code

- Code from this site was used to create a typewriter effect in extras.py: [StackOverflow](https://stackoverflow.com/questions/42940747/python-simple-typewriter-effect)

-   Code from this site was used to create a function that clears the mock terminal screen: [geeksforgeeks](https://www.geeksforgeeks.org/clear-screen-python/)

### Content

-   The content of this website was written by the developer.

### Acknowledgements

<em>I would like to take the opportunity to thank:</em>
-   My mentor Richard Wells for continuous helpful feedback and guidance.
-   My partner Jamie for all of the support and encouragement and for helping out a lot with 
    testing the game.
-   My friends for helping with testing the game on different devices and providing useful 
    feedback and suggestions.
-   My Cohort Facilitator Irene for her support and helpful advice on Slack throughout the 
    development of this project.
