# Problem Archive & Resolution Tool

Problem Archive & Resolution Tool (PART) is a website designed to make keeping track of maintenence tasks in a hospitality setting. Users can log defects, sort them into categories of their own choosing, provide new information (updates) when there are developements, and once the problem is resolved it is archived.

The website can be accessed [here](https://bb-gp-pp4-part-07cc42d9a56e.herokuapp.com/)

MOCKUP

It has been designed specifically with old buildings or facilities in mind, or where there may be a high turnover of staff, or where different shifts or roles within the business may not have existing ways of communicating the necesary easy fixes or workarounds that could save time and money. I have experienced all of these problems at the cinema where I work.

The design is minimalist, emphasizing presentation and readability of information. Colour is used to convey information. The images are uploaded by the users.

## Readme Contents

- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features to implement](#features-to-implement)
- [User Experience Design](#user-experience-design)
  - [User Journey](#user-journey)
  - [User Stories](#user-stories)
- [Technologies](#technologies)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
  - [Validator Testing](#validator-testing)
  - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Code](#code)
  - [Acknowledgements](#acknowledgements)


## Features

### Existing Features

- Defect database

  - ERD

- Account authorisation

  - To use any of the site's functionality, a user must sign up for an account. Attempting to navigate to any pages with defect data will result in a mostly empty page prompting the user to log in.

  - Once the user signs up for an account, they must still be approved. Once approved by an admin, the user will have some permissions, depending on their group. The groups and permissions are:
    - Level 1 - the user can view categories, defects and updates, and can log new defects, but cannot add updates or categories. This level is intended for low level employees who may be more likely to find something that needs reporting, but do not have the training or authorisation to fix them. The navigation bar is visible for level 1 and up.
    - Level 2 - the user can do everything a level 1 user can, but they can also add updates. This level is intended for supervisors/management, who would need to communicate the progress made resolving any defects.
    - Level 3 - the user can do everything level 1 & 2 users can, but they can also add categories, assign users to groups and edit defects, updates and categories. The users link is active in the navigation bar. This level is intended for the general manager or member of the management team responsible for maintenence.
    - Sperusers have all permissions.


- Account indicator

  - Situated at the top right corner of every page, the account indicator shows the username and access level, as well as options to sign in or out.

    - When logged out, the account indicator appears dark grey with the text 'not logged in'. Clicking on the text opens a menu with links to sign in and sign up pages.

    - When logged in, the account indicator shows the user's username. Clicking on the text opens a menu showing the user's access level and a link to the sign out page. Access levels are colour coded:
      - If a user has not been approved to use any of the site's functions, it appears red and shows 'no access'.
      - If a user has level 1 access, the indicator appears green and shows 'Level 1 access'.
      - If a user has level 2 access, the indicator appears pale blue and shows 'Level 2 access'.
      - If a user has level 3 access or is a superuser, the indicator appears gold and shows 'Level 3 access'.

- Navigation Bar

  - Includes links to all parts of the website, allowing users to easily navigate between them.

- Dashboard

- Log defect page

- Defects section

  - Search functionality

- Defect detail section

- Categories section

- Sign in page

- Sign out page

- Sign up page

- custom 404 and 500 pages

- Favicon

### Features to implement

- Light/dark mode

- non admin user CRUD

- keywords/tags

- More extensive filtering & sorting

- different cascade

## User Experience Design

### User Journey

- User Journey

  - A user first notices a problem and logs it as a defect, optionally adding an image to better illustrate location or severity.

  - If a manager was not the reporter, they can begin taking steps to resolve the issue, calling the relevant contractor and taking steps to mitigate in the meantime. This can all be communicated in updates.

  - A contractor arrives and fixes the problem, explaining to the manager what went wrong and what they did to fix it (and how much it cost.) The manager adds all of this information in an update, marking the defect as resolved.

  - The entry stays in the database so that if the same problem, or similar, arises the management can see everything that was tried last time including how long it took to fix and how much it cost, and can plan accordingly.


### User Stories

The [Github Projects Kanban board](https://github.com/users/bezabu/projects/5/views/1) was used to organise user stories.

The user stories are as follows:

- As a Site User I can register an account so that I can log in and use the site functionality
  - Acceptance Criteria
    - AC1 Given an email a user can register an account.
    - AC2 Then the user can log in.
    - AC3 The site content is hidden unless logged in

- As a Site User I can log defects so that problems with building facilities and structure can be tracked and mitigated/repaired easier
  - Acceptance Criteria:
    - AC1 A defect can be logged as a specific entry in a database
    - AC2 The entry contains relevant information such as location, category(plumbing/electrical etc), date reported
    - AC3 The defect can be viewed by other site users

- As a Site User I can fill out a form so that I can add new defect information to the database
  - Acceptance Criteria
    - AC1 If the user is logged in they can access the log defect form
    - AC2 The completed form adds data to the defect model
    - AC3 Successful form entries are confirmed


## Technologies

- HTML has been used to structure the website.
- CSS has been used to style the website.
- JavaScript was used for the edit and delete buttons.
- Python was used as the main language in which this project was coded.
- Django was the framework used to build this website.
- Bootstrap was used to create and style the front end of the website.
- Font Awesome icons have been used for category icons, column headers and user icons.
- Google Fonts have been used to import the Poppins font.
- Paint.NET was used to edit the hammer image before using it with Favicon.
- Favicon was used to create the favicon for the website.
- GitPod was used as IDE
- Google Chrome Developer Tools were used to inspect elements of the website and test different styles.
- GitHub has been used to store the code, images, and other contents of the website.
- Heroku was used to deploy the website to the web.
- Git was used for version control, pushing contents to GitHub.
- W3C Markup Validation Service was used to check HTML.
- W3C CSS Validation Service was used to check CSS.
- JSHint was used to test the javascript code.
- CI Python Linter was used to test Python code.
- Wave Web Accessibility Evaluation Tool was used to test the website's accessibility.
- Lighthouse was used to run an audit of the website.
- Am I Responsive was used to create the mockup.
- Grammarly was used to check for typos in Readme.md.


## Testing

### Manual Testing

### Automated Testing

Automated tests can be found in [test_forms.py]() and [test_views.py]()

image of tests passing

- All 20 automated tests passed


### Validator Testing

- All pages, including logged in content pass through the W3C Markup Validation Service with no errors

- CSS passes through the W3C CSS Validation Service with no errors

- Javascript passes through JSHint with no errors

- When using the WebAIM Web Accessibility Evaluation Tool, the following was returned:

  - 1 error was given for aria labels. I fixed this by moving the role="menu" attribute to the parent div of the two menu items.

  - 1 contrast error was given for the gin in button. I fixed this by changing the shade of blue from the bootstrap default to a slightly darker shade of blue.

  image wave

- All Python code passes through the CI Python Linter with no errors

- The website generates a score of 99 on all pages with the following exceptions:

  - The sign up page generates a score of 98

  - The defect detail page score varies depending on how many updates or images are present on the page.

  - The auth admin page generates a score of 85

image lighthouse

### Unfixed Bugs

There are no unfixed bugs.

## Deployment

The following steps were taken to deploy this project to Heroku:

1. Create new app in [Heroku](https://dashboard.heroku.com/apps), selecting Europe as the region

2. In Settings, config vars, add the config vars `CLOUDINARY_URL`, `DATABASE_URL` and `SECRET_KEY`

3. In the Deploy section, go to deployment method, select GitHub, search for the repository and click connect.

4. Scroll down to Manual Deploy, ensure the main branch is selected and click Deploy Branch

5. The deployed app may be found [here](https://bb-gp-pp4-part-07cc42d9a56e.herokuapp.com/)


## Credits

### Content

### Media

[This hammer image](https://commons.wikimedia.org/wiki/File:Hammer_Vector.svg) by Devin McElheran was used as for the favicon, used under CC BY-SA 4.0 DEED.


### Code

[This tutorial](https://www.makeuseof.com/create-custom-404-error-page-django/) was followed to set up the custom 404 & 500 pages.



### Acknowledgements