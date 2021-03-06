# Pass Physics
![Am I responsive image](static/images/am_I_responsive.PNG)
The Pass physics website is a tool aimed at helping GCSE physics students better prepare for their exams in and outside of a school environment.
The website is intended to be used by both teaching staff and school pupils. The pupils will be able to answer exam questions on the many 
modules in physics GCSE and receive immediate feedback on their attempts. The website will provide an ideal method and solution to the problem
giving pupils the most efficient way to answer their problems. The site provides a class for the pupils to join (currently one of three) in
which they are able to compete against other pupils on a leader board to assist in motivating the pupils to study. 

The teaching staff have the ability to add their own questions to the database for their pupils if they feel there is a particular topic that
there pupils should have more of a focus on. The teachers will also have access to the class area where they are able to view the current progress
of their class. The questions mark themselves and will reduce the marking load for teachers as well as providing statistical feedback on how pupils are preforming.

## **Live project**
---
[View the live version of the project here](https://pass-physics.herokuapp.com/)

---
### **Business and Developer Goals**
- To assist GCSE physics students in obtaining the best possible exam results. 
- To promote Pass Physics wesbite so that more schools sign up increasing our business revenue
- To have project using a detailed database as part of his portfolio 

### **Student Goals**
- To give themselves the best chance of passing their physics GCSE by practicing questions
- To compete against other students to encourage repeat visits
- Promote the website by word of mouth with other students
### **Teacher Goals**
- To have a resource that gives students constructive feedback when attempting exam questions
- To have a resource that allows them to easily compare how their students are performing on exam questions
- To minimize marking load
## Table of Contents
1. [User Design](#ux)
2. [WireFrames](#wireframes)
3. [Features](#features)
4. [Data Structure](#data-structure)
5. [Technologies](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)
## UX
---
### **Ideal User**
- Anyone studying towards GCSE physics
- Anyone with an interest in learning physics
- Any teachers of physics
- Any schools looking to expand their library of resources
### **User Stories**
As a student I want:
1. To easily be able to locate the questions I would like to practice
2. To see how I am performing compared to other users
3. To receive feedback after a incorrect question so I understand what I have done wrong
4. To see how well I am performing 
5. To be motivated to return to the website

As a teacher I want:
1. To be easily view the progress of students in my class
2. To be able to add and change questions easily to better suit my class
3.  To be able to communicate with my students using the website
4. To know the experience previous teachers have had using this website

As a general user I want:
1. The purpose of the site to be immediately clear
2. The site to be intuitive to use and navigate around
3. I want to easily be able to sign up to/login to the site. 
### **Design Choices**
#### **Font**
 I used Raleway for the headings and lato for the body. Raleway looked elegant and lato was clearly spaced and easy to read and the two fonts complemented each other well. 

#### **Icons**
I used Font Awesome icons for my social media links as it gives a intuitive way for users to access the sites social media. I also used Font Awesome icons to make my search bar more intuitive to use. 

#### **Colors**
The color scheme was light grey - blue. Blue and grey are two colours that complement each other well and are not overpowering. The light grey was based ont the logo and the blue from the hero image. The hero image was darkened considerably to allow for the call-to-action text to be clearly displayed. Hence the blues you find throughout the rest of the site are considerably lighter than the blue seen on the hero image. 

When choosing colours on the students profile page I went with the traditional red, amber, green colours to indicate progress to make it intuitively clear.

#### **User Pages**
When designing the user pages I tried to keep the pages simplistic to allow maximum ease of use to encourage users to return more regularly. The design also allows for users to easily access their unique user data. 

#### **Hero Image**
I wanted the hero image to fit the theme of the site and believe it does lead you to think about STEM education and primarily physics and mathematics. The call to action button clearly encourages you to sign up and experience the site yourself. 

### **Wireframes**
### Home Page
![Home-Page-Wireframe](static/wireframes/home_page_wf.PNG)
### Profile Page - Student View Only
![Studnet-Profile-Page-Wireframe](static/wireframes/profile_page_student_wf.PNG)
### Profile Page - Teacher View Only
![Teacher-Profile-Page-Wireframe](static/wireframes/profile_page_teacher_wf.PNG)
### Profile Page - Administrator View Only
![Admin-Profile-Page-Wireframe](static/wireframes/profile_page_admin_wf.PNG)
### All Questions Page
![All-Questions-Wireframe](static/wireframes/all_questions_wf.PNG)
### Modules Page
![Modules-Wireframe](static/wireframes/modules_wf.PNG)
### Manage Modules Page - Admin only
![Manage-Modules-Wireframe](static/wireframes/manage_modules_wf.PNG)
### Class Page - Student View Only
![Students-Class-Wireframe](static/wireframes/class_wf_student.PNG)
### Class Page - Teacher View Only
![Students-Class-Wireframe](static/wireframes/class_wf_teacher.PNG)
## Features
---
### **Existing Features**
---
#### Home Page
- Advertises the site and provides easy access to sign in/login to the user areas. 
#### Registration/Login
- A user is able to create a student or teacher account and can choose to join one of 3 classes when they sign up. 
- If the user has an account they are able to login
- Passwords are hashed to ensure they are kept private.
- If a guest users attempts to access an area of the site that requires you to be logged in they will be redirected to a page that encourages them to sign uor log in.
- If a student user attempts to access teacher/admin areas of the site then they will be redirected to a page that informs them they do not have the correct premissions to access this page and given a link to their profile page.
#### Profile Page
- Users will all have a unique profile page

- A teachers users profile will enable them to add/edit questions for their class. Teachers are only able to edit and delete their own questions.

![teacher profile picture](static/images/profile_teacher.png)

- An admin users profile page is identical to the teacher profile page however they are the only user able to edit and delete other teacher users questions. 

- A students profile displays some statics on how the student is perfoming.

![student profile picture](static/images/profile_student.png)
Jeff has completed all the electricity questions, 50%  of the radioactivity questions, a third of the energy questions and none of the particles questions. He can tell his current working grade and a pie chart represents his current performance. 

#### CRUD Functionality
- Teacher users can add, edit and delete questions there own questions
- When deleting questions from database defensive programming practices are implemented. 

![demonstration of defensive programming](static/images/defensive_programming.png)

- Additionally admin users can add, edit and delete modules.

#### Questions page
- Teacher and admin users are simply able to view the questions left by all users and search through the questions using a search bar. 

- The questions page for students allows them to answer the questions, they can attempt an individual question as many times as they wish until they get the correct answer. Students can search for specific questions to answer.

![student questions view](static/images/student_questions.png)

- The student view either provides the question and answer form to complete, a question and method and a answer form to complete or a question, method and solution to the question. The display changes based on whether a student has attempted a question, answered it incorrectly or answered it correctly. An example of all 3 views can be seen in the top 3 questions in the above screenshot.

#### Class Page

- The class page allows student users to compare there progress to other students and provides a competitive element to the site to try encourage student users to return and attempt more questions. A student user is placed and highlighted in a top-ten leader board in the class. 

![student class view](static/images/student_class.png)

- The teacher class page allows the teacher to track how the full class is performing by providing data on each student. The students are arranged into alphabetical order by surname to match register order in a class.

![teacher class view](static/images/class_teacher.png)

#### Modules Page

- The modules page is similar to the questions page, students are able to answer the questions and teachers are able to view the questions. The modules page requires an additional filtering option which would be useful a student user wanted to revise a specific module or a teacher wanted to know the questions available for a specific module. 

- Admin users are able to add modules to the website from their manage modules tab. 
### **Features left to implement** 

- As more questions are added to the database it would be useful to add pagination to the questions and modules page. 

- The classes page has very few feautres for both the student and the teacher. In the student class page I would like to improve the database to track the number of questions answered per week and add a feature for 'star of the week' as well as changing the leader board so that the user is displayed even if they are not in the top 10.

- It would be useful if students were able to answer multiple questions at once, I would like to make changes to my database to enable this to be possible.

- I would like to change how feedback is given when a user answers a question incorrectly, quite often there are common wrong answers to a question, if a user enters a common wrong answer I would like to provide a specific hint to help with that misconception which would involve adding an array of incorrect answers and methods to the database. 

- The class system is basic as you need to choose a class when you sign up, it would be useful to implement some class control for teachers so that they are able to add classes and add and remove student users from their class as appropriate. 

- Implement the CRUD functionality for modules correctly as deleting and editing modules currently have a detrimental impact on the project.


## **Data Structure**
---
A NoSQL database was used for this project. Please see the tables below for more information on each data type and my reason for using it and my database diagram which clearly shows the relationships between my different collections. 
### Database
<img src="static/images/questions_data.PNG" height="750px" width="500px"> <img src="static/images/user_data.PNG" height="750px" width="500px">
### Database Relationships - Inital 
![Database-relationships](static/images/db_relationships.png)
### Final Database and Relationships
The main changes in the final version fo the database is to the students collection.

Student users should be able to answer a question and if they get it incorret then a method should be displayed, if they get it correct then both the method and correct answer should be displayed. 

This was very difficult to achieve with my initial database hence I changed to using 3 arrays, questions_unaswered is filled upon account creation with all question_ids from questions currently in the database and the other two arrays are initialised empty. question_ids are moved from questions_unanswered to either question_correct and questions_incorrect depending on the users response. This then allowed me a way to change what the user saw depending on the answer given.

The first_name and surname were added to the class section to allow for easier sorting of the students in the class section, however upon reflection this addition to the database was not required and can be removed as the duplication of this data is completely unneeded. 
![Database-relationships](static/images/final_db_relationships.PNG)
### Current Issues with database
The current database has 3 main issues:
1. Duplicated data - I have duplicated username, first_name and surname in the users and students collections to allow for easier coding at points. I have duplicated class in users, teachers and students, class only needs to be in one of these collections.  
2. Unneeded collections and data - As the class collection in teacher is duplicated the teacher collection is actually not required. The percentage_correct and current_grade information does not need to be stored in the collection as it can always be dynamically generated from questions_answered and questions_correct.
3. Student questions solution unideal - This solution lead to a complicated series of for loops and if statements in the all-questions section to allow me to display content as desired, re-writing the database could greatly simplify the all_quiestions.html file.
### Future Improvements to Database
1.	Duplicated data - To fix this issue I would remove first_name, surname and username from the students collection. I would also remove class from both the teachers and students collection. This would mean needing to change pages where student names are accessed from the student collection and adjusting my sorting function.
2.	Unneeded collections and data - I would entirely remove the teachers collection. Additionally I would remove the current_grade and percentage_correct values from the student. The values are already generated inside the program and can just be calculated when they are required as this uses much less memory than a database request.
3.	Student questions solutions unideal - I could completely change the students and questions collection. One solution would be to replace the students and questions collection with 2 collections - a table of questions and a table to record student answers. The student answers collection would store a record every time a student answers a question. The collection would store the students unqiue id, the unique question id, a boolean variable that indicated if the question was correctly answered and a score based on the weight of the question. You could use the boolean value to easily change the view and the number of items in the collection would be the number of questions attempted. Both collections being a table would you to access all questions at once; allowing for the submission of multiple questions.


## Technologies Used
---
This project used the languages Python, HTML5, javascript and CSS3.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The main framework used to build the project
- [Jinja Templating language](https://jinja.palletsprojects.com/en/2.11.x/) was used to allow for python logic within the html files
- [MongoDB](https://www.mongodb.com/) - the noSQL database used for the project
- [jQuery](https://jquery.com/) - The jQuery library was used on all pages.
- [GitPod](https://gitpod.io/workspaces/) - The entire website was developed in GitPod
- [GitHub](https://github.com/) - GitHub was used to store the project and to deploy it using the master branch on the github site
- [Heroku](https://www.heroku.com/) - Heroku was used to host the project
- [Bootstrap](https://getbootstrap.com/) - The grid structure was used to structure the website and make it responsive and some default items in bootstrap were used as a starting point.
- [FontAwesome](https://fontawesome.com/) - Font Awesome was used for various icons throughout the side.
- [Google Fonts](https://fonts.google.com/) - The fonts I used were provided by Google Font

## Testing
---
**For the testing please see [testing.md](TESTING.md)**


## Deployment
---
The project was hosted on Github and deployed through heroku. 

### Requirements to deploy the project are a:
- Python 3 developing environment
- Github account
- MongoDB account
- Heroku account 

### Step 1 - Clone my repository
- To clone my repository you first need to logged into github and go to [my repository](https://github.com/JohnGC1510/milestone_project_3)
- Click on the "code" button just above the files

- Click "Open with GitHub Desktop" and follow the instructions in the GitHub desktop application. Other ways to clone a repository can be found [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) 

### Step 2 - Working with local clone
-  To work with the local clone you need to ensure all environmental variables have been set in an env.py file. These variables are private so ensure that you have a .gitignore file that prevents your env.py file being pushed to github. An example of a env.py file can be seen below:
```
import os
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "***************")
os.environ.setdefault("MONGO_URI", "***********")
os.environ.setdefault("MONGO_DBNAME", "jargon_dict") 
```

- When cloning the project you should cloned the requiremnts.txt file, if this is not the case then use the following command in the CLI:
```
$ pip3 freeze -- local > requirements.txt
```
This file will contain a list of dependencies for the project. These can be installed with the following command in the CLI:
```
$ pip install -r requirements.txt
```

- Ensure you have a procfile as this will tell heroku how to run the application. A procfile can be created in the CLI using:
```
$ echo web: python app.py > Procfile
```

- Ensure you have added and pushed both the procfile and the requriments.txt file using git add . git commit and git push.

- Finally ensure you have created your database in MongoDB with the following collections:
    1. users
    2. students
    3. questions
    4. modules
    5. class
    6. teachers

- You should now be able to run the project locally using:
```
$ python3 app.py
```
### Step 3 - Deploying to Heroku
The project will automatically deploy to heroku after the following has been completed:
- Open you are logged in to Heroku create a new app selecting the appropriate region.

- Deployment method "GitHub" (if this section is accidentally missed, you can use the tab selection within your dashboard "DEPLOY")

- Select the "connect to GitHub" button and search for your repository using the form provided.

Once you have connected your GitHub repository:
- Navigate to the "Settings" tab:
- Scroll to the section "Config Vars" and click "reveal config vars" button:
    - Input all data found in your env.py file into this section. 
    - An example using my earlier example of an env.py file would be a config var with a key of IP and with a value of 0.0.0.0
- Navigate back to the "Deploy" tab:
    - Scroll to automatic deploys and enable automatic deployment.
    - Scroll to the "Manual Deploy" tab:
        1. Select the branch you wish to deploy (master is default)
        2. Click the "Deploy Branch" button. (This may take some time as Heroku uploads the app to their servers.) 

- Once the build is complete, a "View App" button will appear and you should be informed that the app has successfully deployed.

- Common issues include outdated requirements.txt and/or missing Procfile, if errors occur, check these are both correct before investigating further 


## Credits
---

- [Dbdiagram](https://dbdiagram.io/home) was used to create my entity-relationship diagrams.


### **Code**
- A solution to push the footer to the bottom of the page to make the site was found [here](https://dev.to/domysee/keeping-the-footer-at-the-bottom-with-css-flexbox-5h5f)


### **Acknowledgements**
- My mentor Ignatius for his fantastic support and assistance.
- The slack community for their continued support.
