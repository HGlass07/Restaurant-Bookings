# The Baytree Restaurant - Booking System
## Contents:
1. Description
2. Design
3. Features
4. Testing
5. Deployment
6. Credits

--------------

[Site Link]

## Description:

This site designed to allow users to be able to set up bookings at a restaurant called The Baytree. It includes several features including the ability to create an account, make bookings with custom specifications, as well as alter these bookings after they have been made. 

When visiting the site, users are given a description of the restaurant and the booking system; as well as an opportunity to view a pdf version of the menu which can also be downloaded. The contact details for the restaurant are also visible at the top of the page. 

In order to make a booking, users are required to create an account - this is so they can keep track of their individual bookings and edit them whilst logged in. 




**Site-owner Goals:**


### User-stories:

**First-time user:**


**Returning user:**


--------------

## Design: 


**Wireframes - made using Balsamiq**
  
<details><summary>Wireframes</summary>

![wireframe1 screenshot](assets/images/wireframe1.png)

</details>

--------------
## Features:


--------------
## Testing:



**Bugs identified:**


**Validation:**
- W3C HTML validation 
<details><summary>HTML validation</summary>

![HTML val screenshot](assets/images/html_validation.png)

</details>


- W3C CSS validator
<details><summary>CSS validation</summary>

![CSS val screenshot](assets/images/css_validation.png)

</details>

- JSHint Javascript validator
<details><summary>JS validation</summary>

![JS val screenshot](assets/images/js_validation.png)

</details>

- Lighthouse - a lighthouse score was generated for the site, the results of which can be found below.

![homepage lighthouse score](assets/images/lighthouse.png)

- Am I Responsive and Responsinator 

![responsiveness quiz screenshot](assets/images/response1.png) ![responsiveness score screenshot](assets/images/response2.png)


--------------
## Deployment:

This app was deployed with Heroku and linked to a GitHub repository, using the steps below:

- Clone or fork the relevant repository
- Create a new app in Heroku
- Link the app to the relevant GitHub repository
- Create a config var named PORT set to a value of 8000
- Add the NodeJS and Python buildpacks
- Deploy the app, making sure the correct repository branch is selected, in this case 'main'


--------------
## Credits:

Images:

Pexels:
- Header image: 'Green Leaf', Min An

Favicon:
- Emoji Favicons > Herb, From the open source project Twemoji. Used under licence - https://creativecommons.org/licenses/by/4.0/


Django Models:

The models and views used in this project were created with the aid of the following:

- Form widgets, date/time objects - Django documentation
  https://docs.djangoproject.com/en/5.0/ref/forms/widgets/
  https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/

- Form strptime method - Programiz
  https://www.programiz.com/python-programming/datetime/strptime

- Reverse/reverse_lazy functions - Django documentation
  https://docs.djangoproject.com/en/5.0/ref/urlresolvers/

- Edit booking UpdateView - Geeks for Geeks
  https://www.geeksforgeeks.org/updateview-class-based-views-django/

- Booking custom model - inspired by Code Institute's 'Post' model used in the 'I Think Therefore I Blog' module



--------------
## Aknowledgements:

I would like to thank my tutor Antonio for his guidance in this project, as well as my friends and family for helping to test the app.
