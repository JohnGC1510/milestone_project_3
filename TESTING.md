# Testing

## Table of Contents
---
* [Navigation](#navigation)
* [Home Page](#home)
    + [Login / Register](#login---register)
* [User pages](#user-pages)
    + [Profile Page](#profile-page)
    + [Questions Page](#questions-page)
    + [Class Page](#class-page)
    + [Modules Page](#modoules-page)
    + [Admin Pages](#admin-pages)
    + [Error Pages](#error-pages)
* [Performance](#performance)
* [Validators](#code-validation)
    + [HTML](#html)
    + [CSS](#css)
    + [JavaScript](#javascript)
* [PEP8](#pep8)
* [Compatibility](#compatibility)
    + [Hardware](#hardware)
    + [Browsers](#browsers)
* [User Stories](#user-stories)
    + [Student User](#student-user)
    + [Teacher User](#teacher-user)
    + [General User](#general-user)
  * [Known Bugs](#known-bugs)




## Navigation

### Home

#### Login / Register


### User Pages


#### Profile Page

#### Questions Page


Bug – My initial data structure made it difficult to present the question, question method or the solution based on if the student had not answered the question, had attempted it incorrectly or gotten the question correct as there was no unique way to determine if a student had answered a question. An initial change was adding an array to the students table storing the question_id of the questions the students had attempted. This appeared to work initially as when a question was answered the solution appeared and the rest of the questions remained unchanged, however this had its own bugs. Answers/unanswered questions/question methods displaying multiple times if answered incorrectly multiple times or multiple correct questions were answered as I was looping over the array of questions answered and over all questions without appropriate if conditions.  

Solution - I removed the question_answered array from the student table and replaced this with 3 arrays questions_unanswered, questions_correct and questions_incorrect. When a student was initially created the i_d of all current questions in the database would be added to the questions_unanswered array and the questions_correct, questions_incorrect arrays were both initialised empty. Question ids are moved between the arrays based on how the student answers the question. This allowed me to create a set of if conditions that covered all possible circumstances of answers (all correct, all incorrect, some correct etc.) which meant no duplication of methods/answers as there was always 1 unique outcome for each if condition. This now functions as intended with students able to attempt questions multiple times and no duplicates of a question/method/answer ever appear.  

#### Class Page

#### Modules Page

#### Admin Pages


### Error Pages

## Performance

## Code Validation

### HTML


### CSS



### JavaScript


## PEP8


## Compatibility

### Hardware


### Browsers


## User Stories

### Student User
1. As a student I want to easily be able to locate the questions I would like to practice 

Achieved, the student has a search bar based on the questions name and the question itself to allow filtering. In addition, there is a modules page that allows the students to filter the questions by the different GCSE modules.  

2. As a student I want to see how I am performing compared to other users: 

Achieved, on the class page each student can view how they are performing on a leader board of their class mates in terms of total questions answered and total questions correct. In addition, students are giving a working grade estimate which is a countrywide comparison tool.  

3. As a student I want to receive feedback for an incorrect question to understand what I have done: 

Partially Achieved, If you answer a question incorrectly then the site will provide you with a method to follow or a hint that will enable you to answer that question. However, this hint is generic for all users, this could be further improved on by having a bank of common incorrect answers and an appropriate response based on the incorrect answer.  

4. As a student I want to see how well I am doing: 

Achieved, the students profile page has a pie chart showing percentage of correctly answered questions for a clear and immediate update. The profile page also includes some basic statistics of how the student is performing as well as a working grade. Finally, a progress bar for each module is at the bottom of the profile page so students can see how much they have left to complete.   

5. As a student I want to be motivated to return to the website: 

Partially Achieved, the profile page provides a progress bar to show users how much they have completed and to push them to try reach 100% completion in all modules. The class leader board also offers competition which is an incentive to return to the site.  

### Teacher User

6. As a teacher I want to be easily able to view the progress of students in my class: 

Achieved, the teacher view of the class page shows an alphabetized (to represent class registers) table of data for the students showing working grades, questions attempted etc.  

7. Teachers want to be able to add and change questions easily to better suit their class 

Achieved, the profile page of the teacher allows them to view, add and edit there own questions.  

8. To be able communicate with my students using the website 

Not Achieved, adding a chat function/direct messaging function to allow teachers to message their students would have been ideal however it ended up being outside the scope of this project.  

9. As a teacher I want to know the experience previous schools/teachers have had using this website: 

Partially achieved, quotes on the homepage from past users highlight how some users have found success using the website.  

### General User

10. As a general user I want the purpose of the site to be immediately clear 

Achieved, clear hero image and captions demonstrate the side is about education and the name of the site/quotes make it clear it is a physics revision site.  

11. As a general user I want the site to be intuitive to use and navigate around: 

Achieved, icons change colour if they are hyperlinks, nav bar is clearly labelled and easy to use, it is always clear which part of the site you are on and how to navigate to a different page.   

12. As a general user I want the site be easily able to sign up/login to the site 

Achieved, clear navigation bar and sign up button make it easy to find and the form is structured clearly with clear instructions for the requirements of each part of the form that needs completing.

## Known Bugs



  
