# Eat Something
Eat Something is a website that allows an enduser to read family-friendly recipes, and engage with a community of users through post comments.
This project is built with Django, CSS, HTML, Python, and Javascript. It uses Django to manage users, registration, etc. Of these users, there are two types:
- A superuser that can post new recipes to the site and moderate comments.
- A standard user that can browse the site, 'like' recipes, and post comments.

**Click here to visit the [Eat Something](https://ci-eat-something.herokuapp.com/) website.**

**ADD IMAGE OF RESPONSIVE SITE**
Screenshot from ami.responsivedesign.is

## Table of Contents

- Features
    - Front Page
    - Navigation
    - Alerts
    - Registration
    - Recipe Page
    - Recipe Images
        - Custom Recipe Image
        - Default Recipe Image
    - Likes
    - Comments
    - Tags
    - Footer
    - Comment Moderation
    - Data Model
    - CRUD Functionality
        - Create
        - Read
        - Update
        - Delete
    - Responsive Design
- Design
- Agile Development/User Stories
- Accessibility
- Testing
    - Manual Testing
    - Automated Testing
    - Validator Testing
- Bugs
- Setup and Deployment
- Technologies Used
- Credits

## Features

### Front page
This shows the various recipes available on the website. Each recipe has a photo and some details, which the user can click into. Recipe posts are paginated, showing 6 per page.

![Front Page](/assets/readme_images/frontpage.png)

### Navigation
The nav bar always displays at the top of the page and lets the user return home. If they are not logged in, a log in/register option is available.

![Navigation with login button](/assets/readme_images/navlogin.png)
![Navigation with logout button](/assets/readme_images/navlogout.png)

### Alerts
An alert pops up when a user logs in or logs out. This alert times out after 3 seconds.

![Logout alert](/assets/readme_images/alert.png)

### Registration
Users can register new accounts on the website so that they may leave comments and like posts.

### Recipe Page
This shows the recipe in more detail. Note that if the user is logged in and is the author of a given recipe, they have additional options to edit and delete the recipe.

![Recipe page](/assets/readme_images/recipepage.png)

### Recipe Images
Each recipe can have an image attached, which is used in the recipe preview and on the recipe page as the hero image. If no image is attached to a recipe, a placeholder image is used instead.

#### Custom Recipe Image

![A recipe card with a custom image](/assets/readme_images/customimage.png)

#### Default Recipe Image

![A recipe card with the default image](/assets/readme_images/defaultimage.png)

### Likes
Posts can be liked and unliked by users that are logged in. Posts always show the total amount of likes they have received.

![A counter for a post's likes.](/assets/readme_images/likes.png)

### Comments
Users that are logged in can leave comments. All users can read comments.

![Example comments.](/assets/readme_images/comments.png)

### Footer
The page footer contains social media links and copyright information.

![Page footer](/assets/readme_images/footer.png)

### <a name="tags"></a>Recipe Tags
Recipe tags are implemented with a custom many-to-many model. There are many tags and each tag can be applied to many recipes. Tags are called in the RecipeDetail view and then in the recipe_detail.html template. As there is the possibility of many tags, they must be iterated through in the template itself:

    {% for tag in tags %}
    {{ tag }}
    {% endfor %}

Tags appear below each recipe.

![Example of tags in a recipe](/assets/readme_images/tags.png)

Tags are edited in the admin panel.

![Editing tags in the admin panel](/assets/readme_images/tagsadmin.png)

### Comment Moderation
Like posts, comments must be approved by an administrator before they go live on the webpage.

![Examples of authorised and unauthorised comments.](/assets/readme_images/commentmoderation.png)

### Data Model
Comments are created dependent on posts. Deleting a post will also delete all associated comments.

This project uses a custom model to handle Tags on recipes. More details on this model [here.](#tags)

### CRUD Functionality
#### Create
Recipes can be created through a webform. However, upon submission, they must be set to "Published" by the superuser in the admin panel. This is a simple method to prevent spam and low-quality posts.

#### Read
Users can read posts and comments.

#### Update
Recipes can be updated through a webform, provided the user that is logged in is the original author of that recipe. The link to update appears on any recipe page that belongs to the logged in user.

#### Delete
Recipes can be deleted through a webform, provided the user that is logged in is the original author of that recipe. The link to delete appears on any recipe page that belongs to the logged in user.

### Responsive Design
Thanks to the use of Bootstrap, the website is fully responsive to mobile devices.

![The page shown on a mobile screen.](/assets/readme_images/responsive.png)

## Design

- I have used [this colour palette from Coolors](https://coolors.co/palette/e63946-f1faee-a8dadc-457b9d-1d3557) to ensure consistency across the site and related components.
![Colour Palette](/assets/readme_images/colour_palette.png)

- I used Bootstrap for most of this project, using guidance from [Bootstrap's Getting Started Documentation.](https://getbootstrap.com/docs/5.1/getting-started/introduction/)

- In addition, I used my own custom CSS file, to create smaller and more specific styling effects. ON occasion, I have applied styling to exising Bootstrap classes.

## Agile Development / User Stories
I used User stories to guide development

![User Stories](/assets/readme_images/agile.png)

## Accessibility

## Testing

### Manual Testing

- The site functions as expected.
- All internal and external links work.
- The design is responsive to screen size.
- The site has been tested on multiple browers (Firefox and Chrome) and multiple mobile platforms (Android and iOS).

INSERT MARKDOWN TABLE TO MANUAL TESTING

### Automated Testing

I created some automated tests for the project. Guidance for automated testing was taken from the [Django documentation](https://docs.djangoproject.com/en/3.0/intro/tutorial05/) and further assistance was found in Tutor Support.

See recipes/tests.py for more deatails on automated testing. In order to run automated tests:

- Comment out current database in settings.py
- Then uncomment other database settings. 
- Revert these two changes after testing.

![Database code related to Automated Testing.](/assets/readme_images/automatedtesting1.png)

The command to run automated tests is: 

    python3 manage.py test recipes

![Output of Automated Testing.](/assets/readme_images/automatedtesting2.png)

### Validator Testing

- HTML validator
- CSS validator
- JS Hint
- Lighthouse

## Bugs

### Incorrect Model Variables
Unable to post comments with django reporting an error about a null field. Turns out I had mistyped a variable in my model, which I was then not correctly referring to in my view.

### Custom CSS Not Working
I couldn't get my base.html file to recognise my style.css file. Referring to my own styles did not update the contents of the page. I searched through Stack Overflow, Slack, Student Support and the answer was... I needed to clear my cache!

### Editing Bootstrap Classes in CSS
Bootstrap was applying colours to elements that did not match the colour scheme of my site and attempts to fix this were inelegant. After reading [this StackOverflow post](https://stackoverflow.com/questions/20721248/how-can-i-override-bootstrap-css-styles), I understood that I could reference the Boostrap class names directly in my style.css file. Thus, I added this piece of code:

    .btn-primary {
        background-color: red;
        border: none;
    }

### Unstyled AllAuth Pages
Login, Registration, Logout pages, etc, were using an ugly unstyled page, which didn't fit the wider site styling. 

![Unstyled sign-out page.](/assets/readme_images/signoutbroken.png)

Upon closer inspection, I noticed that the templates created by AllAuth used this line:

    {% extends "account/base.html" %}

which simply needed to be changed to:

    {% extends "base.html" %}

Upon which I could begin to style them as normal, with bootstrap, CSS, etc.

![Styled sign-out page.](/assets/readme_images/signoutfixed2.png)

![Styled sign-out page.](/assets/readme_images/signoutfixed1.png)

![Styled sign-out page.](/assets/readme_images/signoutfixed3.png)

### Deployment Errors

#### Incorrect Config Vars

When the project was finished, I found that the deployed site didn't work. After talking with Student Support and looking in the Heroku logs, we discovered a spelling mistake in my Heroku config vars!

#### Broken Static Files

On the deployed site, I noticed that my static files were no longer working - my CSS file and favicon.

### Updating and Deleting Posts

When creating code to update a recipe, I create a class view with GET and POST methods, in order to create a form, prepopulate it with existing content, and then allow the user to submit the corrections. However, the form continually didn't work. Upon submission, it would check is_valid, and the check would fail because the slug needed to be unique. However, the slug was never unique because the original recipe that is being edited has the same slug. This bug persisted for some time until I went to student support, who were about to show me the UpdateView class, as explained [here](https://www.geeksforgeeks.org/class-based-generic-views-django-create-retrieve-update-delete/).

This allowed me to reduce 60 lines of buggy code to:

    class EditRecipe(UpdateView):
        model = Recipe
        form_class = RecipeForm
        template_name = 'edit_post.html'
        success_url = '/'

It also allowed me to use DeleteView to achieve something similar with the code for deleting a recipe.

## Setup and Deployment

To setup the project, I followed the example in the I Think Therefore I Blog module.

Django was installed at beginning of project using the command: 

    pip3 install Django==3.2 gunicorn

Deployment at the start of the project following I Think Therefore I Blog example. Refer to the [cheatsheet](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit) for further details..

1. Create env.py to hold secret keys
2. Hook up Heroku and ensure that it is holding my secret key and database URL
3. Connect Cloudinary and ensure those setting are also in the Heroku variables
4. In Heroku, connect to the GitPod respository for this project and click deploy for the main branch.
5. THEN BUILD PROJECT
6. before final deployment, make sure the debug flag in settings.py is set to false.
7. Also X_FRAME_OPTIONS = 'SAMEORIGIN' so that summernote can run in the deployed version.
8. remove DISABLE_COLLECTSTATIC config var in Heroku.
9. Deploy branch again in Heroku.


From the I Think Therefore I Blog tutorial, I installed Summernote to provide a WYSIWYG editor in Django dashboard. Using the command:

    pip3 install django-summernote


I installed Bootstrap using guidance from https://getbootstrap.com/docs/5.1/getting-started/introduction/

## Technologies Used

- Javascript
- Python
- CSS
- HTML
- Django
- AllAuth
- Heroku
- Cloudinary
- GitHub
- GitPod
- GitHub Pages
- Firefox developer tools
- Chrome developer tools
- JSHint
- W3 HTML Validator
- W3 CSS Validator
- favicon.io

## Credits
- The basic structure of the website is inspired by the I Think Therefore I Blog tutorials. Parts of the page logic are also inspired by this and are marked as such in the comments.
- Guidance for working with forms and CRUD functionality from: https://docs.djangoproject.com/en/4.0/topics/forms/
- All images are Public Domain or Creative Commons.
- Salad placeholder image source: https://www.photosforclass.com/download/pb_2834549
- Kid Friendly Grilled Skewers
    - Image: https://www.photosforclass.com/download/pb_417994
    - Text: My own.
- Bluberry cookies 
    - Image: https://www.photosforclass.com/download/pb_1835414
    - Text: My own.
- Sugar cookies
    - Image: https://www.photosforclass.com/download/pb_1051884
    - Text: My own.
- Pasta
    - Image: https://www.photosforclass.com/download/pb_527286
    - Text: My own.
- Cupcakes
    - Image: https://www.photosforclass.com/download/pb_2285209
    - Text: My own.
- Egg breakfast
    - Image: https://www.photosforclass.com/download/pb_456351
    - Text: My own.
- Pancakes
    - Image: https://www.photosforclass.com/download/pb_2020863
    - Text: My own.
- Pizza
    - Image: https://www.photosforclass.com/download/pb_2068272
    - Text: My own.
- Berries
    - Image: https://www.photosforclass.com/download/pb_2277
    - Text: My own.
- Blueberry favicon from https://favicon.io/emoji-favicons/blueberries/