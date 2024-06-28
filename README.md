# Miss Pink Bakes

This is a Python and Django application for a bakery, here you can view a list of products and place an order for them.

When a user visits the website users can register an account so that they can keep track of their orders.

Urser will get a list of item that they can browse true du eventuelly place an order.

[Here is the live version]()

![Website in diffrent browsers]()


# UX (User Experience)

## Target Audience

The targeted audience for this application are people who is having any type of celibrations where cakes and pastries are needed. This website is easy to navigate and easy to place an order. User have a shopping bag to keep track of item placed in the bag and the total amout, they can add and remove items in the bag.

## User Stories

There are two user who can access this application, the users and the site owner. The site owner can utilise all the futures for booking and cancelling a reservation. Site owen also have the tools to remove or add other users.

As a user you have access to making a reservation, accessing you reservation so that you can se the date and time if needed. You can also delete a reservation if needed.

### User Stories were 

* As a shopper I can view a list of products so that i can select some to purchase/order.
* As a shopper I can view individual product details so that i can identify the price, desprition, product rating, product image and available sizes.
* As a site user I can easily register for an account so that i have a personal account and be able to view my profile.
* As a site user I can easily login or logout so that i can access my personal account information.
* As a site user I can easily recover my password in case I forget it so that recover access to my account.
* As a shopper I can quickly identify deals, clearance items and special offers so that i can take advantage of special savings on products I'd like to purchase.
* As a site user I can receive an emial confirmation after registering so that ** i can verify that my account registration was successful.
* As a shopper I can sort the list of available products so that i easily can identify the best rated, best priced and categorically sorted products.
* As a shopper I can sort a specific category of product so that i can find the best-priced or best-rated product in a specific category or sort the products in that category by name.
* As a shopper I can sort multiple categories of products simultaneously so that i can find the best-priced or best-rated products across broad categories, such as "cake" or "cookies.
* As a shopper I can search for a product by name or description so that i can find a specific product I'd like to purchase.
* As a shopper I can view items in my bag/cart to be purchesed/ordered so that I can identify the total cost of my purchase and all items I will receive.
* As a shopper I can view a specific category of products so that I can quickly find products I'm interested in without having to search through all products.
* As a shopper I can easily view the total of my purchases at any time so that i avoid spending too much.
* As a site user I can have a personalized user profile so that i can view my personal order history and order confirmations, and save my payment information.
* As a shopper I can easily see what i've searched for and the number of results so that I can quickly decide whether the product I want is available.
* As a shopper I can easily select the size and quantity of a product so that I can ensure I dont accidentally select the wrong product, quantity or size.
* As a shopper I can adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout.
* As a shopper I can easily enter my payment information so that I can Check out quickly and with no hassles.
* As a shopper I can feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
* As a shopper I can view an order confirmation after checkout so that ** I can verify that I haven't made any mistakes.
* As a shopper I can receive an email confirmation after checking out so that I can keep the confirmation of what i I've purchased for my records.
* As a site owner I can add a product so that I have new items in my store.
* As a site owner I can edit/update products so that changes in product prices, descriptions, images and other product criteria are updates for shoppers.
* As a site owner I can delete a product so that a item is removed and are no longer for sale.



### User Stories that i didnt not implement

* 

## Wireframes

The following images shows wireframe of the primary design of the application. These wireframes were created using [Balsamiq Wireframe](https://balsamiq.com/)

### Wireframe of Home Page

This wireframe shows the main page, which is also the base wireframe for the other pages. This is the same if the user is logged in or not. Its give a good feel of the general layout of the page.

![Home page]()

### Agile Methodology

I used the Kanban board feature in github project repo ti layout the user stories required for this application. As I completed each user story I moved them across the banban board in stages, from "To do" to in progress and finally "done".

![Kanban board]()

### System Design

The system design i choose to go with in this application was, A collect the dates, time, party size and table numbers. B store that data and C retrieve that data. 

### Data Relationships

The relationship between data models in this application are as followed:

* Account
* Home
* Miss pink bakes
* Bag


### Application features

#### Account

Login - User will find a log in link in the navigationbar that will take the user to a login page. This is a standard login page displaying a from with username and password.
Signup - This page is for new users. It allows the user to enter the necessary details and displays a prompt if any of the form fields are left empty on submitting.

#### Base Template 

There are two common areas in all viewports throughout the application, the header and the foother. They are coded into a "base.html" template in the django framework and thus appear commonly across the site.

##### Header


![Header]()

##### Footer



![Footer]()

##### Home page

###### Hero Image



![Homepage]()


###### Menu 



![Menu]()

##### Cakes



![Cakes]()

##### Bread 



![Bread](static/images/book.JPG)



![]()



![](<static/images/double booking.JPG>)


##### Cookies and Brownies



![]()
  
##### Pastries



![](<>)

##### Special Offers



![](<>)

### Features left to Implement



## Technologies Used

The following is a list of the various technologies employed to build this project.

* HTML5 - Hypertext markup language used to give the website its overall structure and semantic value.
* CSS3 - Cascading Style Sheets used to apply consistent styles across all sections of the application.
* Bootstrap5 - CSS framework to assist in rapid site development. Augmented by some custom CSS also.
* Git/Gitpod - Gitpod used as development platform to build incremental versions of the application and Git commands to backup these changes to Github.
* Heroku - Heroku platform used for hosting the deployed application.
* PostgreSQL - This was used as the database storage for the application, it was added as a Resource in the Heroku hosting platform settings.
* Django - Python based web application framework used to build the application.
* Font Awesome - Fontawesome toolkit imported into HTML files and its icons used to show button icons and logo.
* Balsamiq Wireframes - Downloadable software to create the wireframe mockups.

## Testing 

Admin login: 
* Username: misspink
* Password: lovetobake

I have manually tested this project by doing the following:

* I tested playing this website in different browsers; Chrome, Firefox, Safari.
* I confirmed that new users can register and log in.
* I confirmed that the header, content in the home page and the about page are readble and all the links are clickable.
* I confirmed that the colors and font chosen are easy to read and accessible by running it through ligthouse in devtools.


## Bugs

Solved bugs

*
![]()
*
![Heroku app error](<>)

## Remaining Bugs

*  No bugs remaining 



 ## Deployment 

 This project was deployed in heroku and Github.

 * Steps for deployment:
   * Create a new Heroku app
   * Link the Heroku app to the repository.
   * Click on Deplo
 * Deployed on Github

  The live link to this page - [Joy Of Food](https://joy-of-food-f30aafe0b05b.herokuapp.com/)

## Credits

* Shopify for the pictures [Shopify](https://www.shopify.com/)
* Code institute for the template and the idea.


