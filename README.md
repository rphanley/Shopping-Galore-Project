[![Build Status](https://travis-ci.org/rphanley/galore.svg?branch=master)](https://travis-ci.org/rphanley/galore)

# Milestone project 4: Shopping-Galore Project

Shopping-Galore is a full-stack ecommerce website. It allows authenticated users to browse and search for listed products, add them to a cart, checkout and pay. On the frontend, it uses HTML, CSS, Bootstrap and Javascript to render the pages and handle user input. It uses the Python-based Django framework as backend. The model data is stored in a Postgres relational database hosted with the site on Heroku. Static data, such as product pictures and styling, are hosted on an Amazon S3 bucket.  Payment is made via Stripe using a dummy credit card transaction. 
New visitors to the site can browse and/or search for products. But to create a shopping cart and checkout, they must register and log in to the site. The advantage of having a login is that the user can then save the cart before checkout. They can log out and return to the site on the same or other device. Their shopping cart is persisted until they checkout. Once they have made some purchases, they can view their profile, including their user information and order history. They can give feedback on products via a form and rate them. 
 

 
## UX

I created this project as a good example of a full stack project backed by a relational database, which performs a useful function in today's world. It shows
how Django can be used to create multiple apps for the requirement in question, while handling a lot of the standard database functionality.

 
The target user of the site is anyone interested in browsing and/or shopping for products. The site is aimed at the following user stories:

1)   I want to browse products on the website, potentially to buy.

2)   I want to both view and buy products, after creating a login.
 

3)   I want to be able to preserve my shopping cart until the next time I log in. This would be useful for:
		- Larger orders, I can return to the website later and complete them.
		- If I need some information/approval for some order items, I can enter the other items and complete the order later.
		- Another more urgent task comes up, and I need to come back to complete the order later.
		- In case of a sudden loss of power (battery running out on a device etc) or loss of network connection.

4)    I want to checkout my shopping cart with my address and credit card details. If there is a loss of power or network connectivity, or the browser
	  is closed accidentally, I want to preserve any address fields I have already filled in. The information will be restored when I return to checkout.

5)    I want to view my previous orders for accounting purposes etc, or submit product feedback on them.

 

- My wireframe sketches were uploaded to the 'diagrams' folder under the 'galore' project: ( https://github.com/rphanley/galore/tree/master/diagrams ). It shows the 11 wireframe diagrams for the website pages, as well as an Entity Relationship diagram for the Django database models used in the project.

 


## Features

The site consists of 11 distinct pages/views:

1)	Home/landing page displaying all products
2)  User registration page
3)	User login page
4)	Home page after login
5)	Home page after adding product(s) to the cart
6)	Cart view page
7)	Checkout page showing cart items and payment form
8)	Home page after confirming payment
9)	'MyGalore' page showing user profile, order history and product feedback button
10)	Feedback page with form and submit button
11)	Confirmation page after submitting feedback


There is a navbar across the top of all pages showing the title "Galore" which is a link to the home page. To the right on the navbar is a menu containing 3 items, these change according to the context of the page. On the landing page these are 'Register', 'Log In', and 'Cart'. After login, the first 2 options change to 'MyGalore' and 'Log Out'. On smaller devices, the navbar menu collapses to a 'hamburger' style icon to give access to the options.
There is a message area at the top left of each page, under the navbar. This is used to prompt the user on what they can do, and display some confirmation messages. Once the user is logged in, each page then has a search input box and button to allow the user to search for products at any time.
 
 
### Existing Features
- The 'Register' page allows the user to register for an account by entering a username, email address, and password. They must confirm the password before 
  clicking the 'Create Account' button.
  
- The user is then logged in, and can browse or search for products. If they are logging in on a new session, they use the 'Login' page, entering their 	  username or email address and password.

- The user is then shown a scrollable view of all products. Each product is displayed on a separate card, which contains the image of the product, its name,   description, price, and rating. Under this, the user can enter the quantity and click the Add button to add the product(s) to the cart. On large devices, 2  product cards are displayed side by side, while on smaller mobile devices, the cards are stacked one by one.

- Once the user has added items to the cart, the 'Cart' menu option on top displays a badge with a running total of the quantity of items in the cart. The  cart items are saved in the database as they are entered. If the quantity of any product is changed using the Amend button, it should be updated in the cart. Setting a quantity of 0 for any item will remove it from the cart.

- When the user has completed adding items to the cart, they can log out, or shut down the browser if needed. The cart will be present when they log in again. 
- To pay for the items, the user clicks on the green 'Checkout' button at the bottom of the cart page. The cart items are displayed on the checkout page, followed by the Payment Details form.

- The user enters the order details: Full name, Phone number, Country, Postcode, Town or city, Street address1, Street address2, and County. Then they enter the credit card details: Credit card number, Security code (CVV), expiry Month, expiry Year. For the purpose of testing with Stripe payments, a dummy Visa credit card number 4242424242424242 with any 3 digit CVV, and any expiry date in the future was used. 

- There is a frontend Javascript feature added for the order details. As in user story (4), if the user partially fills out the address details in the form,   and are then interrupted, the fields they have entered will be persisted in the browser's local storage until they return to the checkout page. The       interruption could be loss of battery power or the browser being accidentally closed for example. If the user returns to the checkout form on the same device to complete the transaction, a message query pops up with the text 'There is saved name/address data available. Click OK to use it in the form, or Cancel to continue with a blank form.' If the user clicks OK, the saved form data is used to populate the relevant fields again. The content of each field is saved when the user clicks on the next item. However, no credit card details are saved for security reasons. The order form fields are linked to the Javascript via the 'onblur' attribute in the individual field widgets of the checkout app (forms.py) .

- After successfully processing the Stripe payment, a message 'You have successfully paid!' is shown in the message area at the top of the page. The home page is displayed again with all available products. At this point the user can continue shopping with a new cart if needed.

- Clicking on 'MyGalore' on the navbar brings the user to the profile page. This shows their profile (username and email address), and their order history if they have already ordered and paid for items. The orders are listed, showing the Order ID and date of each order. A table shows the quantity, product, and price of each line item in the order. The total price is displayed on the last line.

- If there is an order history, a 'Give product feedback' button is shown at the top. Clicking this brings the user to a feedback page where they can select the product from a drop down menu. They enter their username and email address, feedback content and a rating for the product. The rating value must be between 0 and 5. The product rating is initially 0.0 for a new product. The first rating feedback becomes the new rating, and subsequent ratings are averaged with the existing value. The average rating is displayed on the product card.

- Once the user clicks the 'Submit' button at the bottom of the feedback page, a confirmation page is displayed with a message 'Thanks for your feedback!', and a link 'Enter more feedback?' to take the user back to the feedback page if needed.

- If the user has completed all transactions with the site, they can click 'Log Out' on the navbar. A page is displayed with the message 'You have logged out. Visit us again soon!'. At that point the site is ready for them to log in again, or register a new user. The navbar menu changes to reflect this.
 


### Features Left to Implement

- Future versions of the site could add categories to the products, to enable easier searching of a large number of products and a breakdown of the 
  categories of products for accounting purposes etc.

- If a search fails, the site could show a list of items with similar names to the search text.

- The rating system could be improved by displaying a 'star' graphic similar to popular ecommerce websites, to show a better visual representation.

- The site could incorporate viewing of product feedback and/or frequently asked questions (FAQ's).

- The site could include a feature like 'people who bought this item also looked at item x' etc along the lines of Amazon etc.

- The site could apply a discounting system for frequent users, or across sale items.

## Technologies Used

- This project uses **HTML** for basic layout and text, and **CSS** for styling the content.

- [Django](https://www.djangoproject.com/)
    - This project uses Django as a web framework to ease the creation of this database driven website. Django is based on the Python programming language, and is free to use and open source. It focuses on reusability of code (the 'don't repeat yourself or DRY principle) and allows rapid development with clean design and less code. It can be seen as having a 'Model View Controller (MVC)' architecture in that it has database handling (model), a method of handling HTTP requests with a templating system ('Views') and a dispatcher for URL's (controller). It is 'batteries included' in that it includes among others,  commonly used authentication features, and an admin system for editing the database models and content for a website. 
	
- **Javascript** is used to connect to Stripe for payments procesing, and the frontend logic around the order form.

- [Bootstrap](https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css)
    - This project uses **Bootstrap** to ease frontend development by use of the Bootstrap grid system and design templates. It is based on Javascript, and provides responsive CSS to adjust to different screen sizes in phones, tablet and desktop devices. The Bootstrap Navbar feature is used to provide access to the site pages, and logo at the top of the page.


- [Stripe](https://stripe.com) 
   - Stripe is an online payments processing company who provide application programmer interfaces (API's) which web developers can use to 
   integrate payment processing in to their websites. This website uses a Javascript API to connect to Stripe and process credit card payments. A dummy Visa credit card number 4242424242424242 is used with any 3 digit CVV number and a card expiry date in the future. Stripe processes the payment as normal, but no actual credit card is deducted during transactions. Developers must sign up with Stripe, and can monitor transactions via a dashboard on the Stripe website.

- [Amazon S3](https://aws.amazon.com/s3/)
	- S3 or Simple Storage Service is a cloud-based storage service offered by Amazon Web Services (AWS). Data is stored in 	'buckets' and can be accessed via a unique user-assigned key. It is used in this project to store image files for the products on the website, and for 		static files such as CSS, fonts and Javascript. The deployed project setttings point the website to the S3 storage for these files.

- [Heroku](https://heroku.com)
    - This project is deployed on the Heroku platform, which is used to host web applications in many programming languages including Python. The applications run in virtual containers known as "Dynos". This project uses a Postgres relational database add-on hosted on Heroku to store the model data, for example product or cart data. The settings for the project are stored as config variables in Heroku, including keys for access to the website, Amazon S3 and Stripe, and the URL for the Postgres database. Heroku can be set up to deploy the project automatically once the code is checked in to GitHub.

## Testing

The project used the built in Django testing framework to test the models used: Checkout, Cart, Feedback and Product. They are contained in the tests.py file of each app. The tests validate the models by setting up a temporary database for each model, creating an object (for example a test product), and checking that the object fields behave as expected. The tests check that the object was correctly named, and validates any limitations. For example, if an integer field has a minimum and maximum allowed value, the tests verify that there is a validation error if a value outside that range is used. The Rating field of the Product model allows values between 0.0 and 5. The tests use values of -0.1 and 5.1 to check for validation errors. Similarly, if a string type field has a maximum allowed number of characters, the tests verify that there is a validation error if a longer string is used.
The tests were run successfully for all models by typing **'python3 manage.py test'** from the command prompt in Gitpod. An individual app model could be tested using **'python3 manage.py test product'** for example.

The deployed website was tested with the following devices and scenarios:

- Asus F553M laptop with Google Chrome,Microsoft Edge and Opera browsers
- Asus F553M laptop with Google Chrome developer tools used to view various mobile (phone and tablet) device screen sizes
- Apple iPhone with Safari browser
- Motorola Moto G4 Android smartphone with Google Chrome
- Samsung Galaxy Tab 2 Android tablet with Firefox and FlashFox browsers


The test cases were as follows, run manually in sequence:

### Test Cases
1) **Home page load:** Home page should load with the full list of products visible, message area, search input, and correct menu items Register,
	Log In, and Cart. Clicking the 'Galore' logo on the navbar should return to the home page at any time. On mobile devices the menu items should be visible after clicking the 'hamburger' icon on the top right to expand the menu. Clicking it again should collapse the menu.

2) **Register:** Clicking on Register should allow the user to create a new account by providing a username, email address and password. User should be logged in 	after clicking the Create account button.

3) **Log In:** Clicking on Log In should allow the user to log in with a previously registered username and password. Only the correct username and password 	   should allow access.

4) **After log in:** The menu items should change to 'MyGalore', 'Log Out' and 'Cart'. The search input should be visible, and a welcome message to inform the user that they can now buy products or save their cart until next login. The full list of products should be visible by scrolling, with name, description, price and rating displayed for each product. There should be a Quantity input box with an Add button.

5) **Search input:** Enter a search query in the Search input box, for example 'bed'. Click 'Search' and a list of products containing the search term should be displayed. Test with different search strings.

6) **Add products to cart:** Add different quantities of products to the cart by entering the quantity in the input box and clicking Add. After each product is added, verify that the Cart menu item on the navbar has a badge showing the total quantity of products added to the cart. The message area should confirm that x of product has been added to the cart each time an Add button is clicked. 

7) **Cart view:**  Click on the Cart menu item. Only products which were added to the cart should be displayed, with the selected quantity of each. There should be an Amend button for each product. Enter a new quantity for each product and click Amend. Verify that the quantity updates correctly for each. On one product, change the quantity to 0 and verify that the product is removed from the cart view. 


8) **Checkout view:** Click on the Checkout button at the bottom of the page. the selected products and quantities of each should be displayed, and the Cart menu item should still display the badge with the total quantity of items. The total price for all items should be shown under the products. Following that there should now be a Payment Details form with name and address fields, and credit card fields for number, security code/CVV, expiry month and year. There should be a Submit button displayed at the bottom of the page.

9) **Partial form recovery:** Fill out the name, number and address fields of the Payment Details form. Leave the credit card details empty. On the same device, close the browser tab, reopen it and go to the site home page. Log back in. The cart should be preserved as it was before the browser was closed. Click 'Cart' and verify that the cart products and quantities are the same as before. Click 'Checkout' and click into any of the name/address fields of the 
Payment Details form. A pop-up query should be displayed with the message 'There is saved name/address data available. Click OK to use it in the form, or Cancel to continue with a blank form'. Click OK. The name/address fields should be populated with the same details as filled in previously. 

10) **Partial form recovery (declined):** Repeat testcase 9, but this time click 'Cancel' on the pop-up query. The Payment Details form should remain blank.

11) **Payment:** Fill out the Payment Details form. Enter the credit card number 4242424242424242, any 3 digit number for CVV, and any future month and year for expiry date. Click on the Submit Payment button at the bottom of the page. The home page should be displayed, with no badge beside the Cart menu item (cart is now empty). There should be a message displayed 'You have successfully paid!'. The full list of products should be displayed again, with quantity input and Add buttons for each.

12) **MyGalore page:** Click on the 'MyGalore' menu item on the navbar. The user profile should be displayed under the search input box, titled 'Your profile'. The username and email address should be shown. If there are any completed orders for the user, there should be 'Your Order History' displayed, as well as a 'Give Product Feedback' button. The order ID and date for each order should be shown. There should be a table showing the quantity, product name and price for each item, and a total price for the order at the bottom. Test before and after the first order for a new user. Only the profile section should be displayed for a user with no completed orders.

13) **Feedback page:** From the 'MyGalore' page of a user with completed orders, click the 'Give product feedback' button. There should be a 'Feedback Form' displayed under the search input. Select a product from the dropdown menu, enter the user name, email and feedback text on the product. Enter a rating for the product between 0.0 and 5, and click Submit. There should be an acknowledgement page displayed, with the text 'Thanks for your feedback!' and a link 'Enter more feedback?' underneath. Clicking the link should return to the feedback page. The new rating for a product should be an average of its previous rating and the submitted rating.

14) **Log out:** Click the 'Log Out' menu item on the navbar. The page should clear, with 'You have logged out. Visit us again soon!' and the search input displayed.

Testing showed the following results:


**Test Table**

|  **Test Case**    |  **Chrome**         |  **Edge**           |  **Opera**        |  **Dev tools**         |  **iPhone**          |  **Moto G4**     |  **Galaxy Tab2** |       
| ------------- | ----------- | ------- | -------- | ------------- | ---------- | ----------- | ------------- |  
| **1** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **2** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **3** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **4** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **5** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **6** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **7** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **8** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  | 
| **9** | Pass  | Pass | Pass  | Pass | Pass  | Pass | **Fail**  |
| **10** | Pass  | Pass | Pass  | Pass | Pass  | Pass | **Fail**  |
| **11** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  |
| **12** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  |
| **13** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  |
| **14** | Pass  | Pass | Pass  | Pass | Pass  | Pass | Pass  |


All products were visible, displayed either side by side on large devices or stacked one above another on mobile devices. There was a small amount of wraparound of product card text and overspill of images on some views on mobile devices and Chrome dev tools. All menu items, buttons and links worked as expected.
 **Testcases 9 and 10 were marked as fails for the Galaxy Tab 2**. They worked as expected on the Firefox browser, but on the FlashFox browser there was no popup query or recovery of payment form data. I investigated the browser settings, but could find no setting affecting the setting of data in localStorage. It may be that other settings, or a newer version of the browser is needed to support localStorage.




## Deployment

The project was deployed on Heroku. To do this, I created a new Galore app area on Heroku, then in the 'Deploy' tab I linked to the [GitHub repository](https://github.com/rphanley/galore) for the project. Settings for the project were set up in the Config Vars area of the Settings tab on Heroku. After building the app successfully, the project was deployed at [Shopping-Galore](https://shopping-galore.herokuapp.com/)

**Local Install**: The website can be installed locally by clicking the "Clone or download" button on the Github repository then clicking on "Download ZIP" to download the folder structure and all files to your device. The website could be installed in a Python virtual environment, for example as outlined [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) . The requirements.txt file in the root folder can be used to install all required Python packages, using e.g 'pip3 install -r requirements.txt' at the command prompt for Python3. The local install would need a local settings file such as an env.py, with entries for the keys required for the project e.g

		**os.environ.setdefault("SECRET_KEY",<secret app key>)**
		
and a 'import env' command in the settings.py file. Other keys required by the project are: "STRIPE_PUBLISHABLE", "STRIPE_SECRET","AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY" and DATABASE_URL (link to the database). 



## Credits

### Content
- Stock images of products courtesy of [Canva](https://www.canva.com/)
- Feedback feature adapted from (https://fazle.me/creating-simple-feedback-system-using-django/)


### Acknowledgements
I want to acknowledge again the help and guidance from my tutor Xavier, and mentor Ignatius, in developing this project.
