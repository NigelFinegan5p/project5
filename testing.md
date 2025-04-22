

## Code Validation

### HTML Validation

For my HTML files, I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

Since the project uses Jinja syntax (like {% extends "base.html" %} and {{ form|crispy }}) and requires user authentication, this method was used for validation:

1. Navigate to each individual page via the deployed Heroku app link.
2. Right-click the screen or use `CTRL+U` (`⌘+U` on Mac) to "View page source."
3. Copy the complete HTML code and paste it into the [validate by input](https://validator.w3.org/#validate_by_input) option.
4. Fix any errors or warnings, revalidate, and record results.

All pages passed validation. One error was shown, and I reached out to Tutor support regarding it. 


<details>

<summary> Home page </summary>

![Home page](https://github.com/NigelFinegan5p/project5/blob/main/xtra_documents/w3c/homepage.png)

</details>


<details>

<summary> All Products page </summary>

![Product page](https://github.com/NigelFinegan5p/project5/blob/main/xtra_documents/w3c/allproducts.png)

</details>


<details>

<summary> Coffee </summary>

![coffee page](https://github.com/NigelFinegan5p/project5/blob/main/xtra_documents/w3c/w3c.coffee.png)

</details>


<details>

<summary> boxes </summary>

![boxes page](https://github.com/NigelFinegan5p/project5/blob/main/xtra_documents/w3c/w3cboxes.png)

</details>


<details>

<summary> newsletter </summary>

![newsletter page](https://github.com/NigelFinegan5p/project5/blob/main/xtra_documents/w3c/w3cnewsletter.png)

</details>


<details>

<summary> contact </summary>

![contact page](https://github.com/NigelFinegan5p/project5/blob/main/xtra_documents/w3c/w3ccontact.png)

</details>


<details>

<summary> BAG </summary>

![bag page](https://github.com/NigelFinegan5p/project5/blob/main/xtra_documents/w3c/w3cbag.png)

</details>


<details>

<summary> checkout </summary>

![checkout page](https://github.com/NigelFinegan5p/project5/blob/main/xtra_documents/w3c/w3c.checkout.png)

</details>



<br>
<br>
<br>


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

All files passed with no errors.

<details>

<summary> CSS screenshot of file that passed </summary>

![Profile css](https://github.com/NigelFinegan5p/project5/blob/main/xtra_documents/w3c/css_validator.png)

</details>

---

<br>
<br>
<br>



### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate my JS files. The JS files in my project were not written by me but were taken from Boutique Ado, Stripe, and course material from Django by Antonio Miele.

All files passed with no errors.  The Stripe JS did not come from me so I am leaving it deployed.

<details>

<summary> Stripe screenshot </summary>

![Stripe JS](/xtra_documents/w3c/jshint.png)


</details>

---

<br>
<br>
<br>


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

All files passed with no errors, additionally the VS code and installed app has allowed each file to highlight errors (problems) and omissions in the CLI Command line interface.

Running the following commmand ( python -m flake8 --exclude .venv,.vscode,migrations )
This command shows any additional linting issues and unused code functions.

<details>

<summary> Screenshot of PEP8-compliant newsletter model.py file </summary>

![Profile pep8](/xtra_documents/pep8/pep8..png)


</details>



<details>

<summary> Screenshot of PEP8-compliant newsletter model views.py file </summary>

![Profile pep8](/xtra_documents/pep8/pep8...png)

</details>

---


<br>
<br>
<br>


## Dev Tools/Real World Device Testing
---

Responsiveness testing was carried out using Google Dev Tools on the devices detailed within the below table. Responsiveness was evident on all features throughout all tested devices. ( 320 x 640 tested extensively )
  
<br>
<br>

### Dev Tools Device Testing - all features tested, issues noted below

| Device             | Feature                              | Issue                | Fix                                                                 |
|--------------------|--------------------------------------|----------------------|----------------------------------------------------------------------|
| iPhone             | Product detail page                  | Page works well, adequate space | None needed                                                         |
| Responsive 320 x 640 | All features                        | No issues            | None needed                                                         |
| iPad Mini          | Product page and product detail page | Satisfactory layout  | Updated Bootstrap for responsiveness                                |
| Galaxy Z Fold 5    | Product page and product detail page | Satisfactory layout  | Updated CSS and Bootstrap for responsiveness and button color consistency |

   
<br>
<br>

### Real World Device Testing

| Device             | Feature       | Issue      | Fix         |
|--------------------|---------------|------------|-------------|
| Samsung S8         | All features  | No issues  | None needed |
| iPad Pro+ (2019)   | All features  | No issues  | None needed |
| HP ProBook         | All features  | No issues  | None needed |
| Google Android     | All features  | No issues  | None needed |
| Samsung S Series   | All features  | No issues  | None needed |

<br>
<br>

### Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Notes                                                                 |
|---------|-----------------------------------------------------------------------|
| Chrome  | Works as expected and intended (majority market share browser)       |
| Edge    | Works as intended                                                    |
| Safari  | Works as intended                                                    |
| Firefox | Works as intended                                                    |
| Opera   | Works as intended                                                    |
| Brave   | Works as intended                                                    |


<br>

All validation tools and device/browser testing confirm that the project functions as intended across platforms, with only minor tweaks needed for enhanced responsiveness and visual polish

<br>
<br>
<br>
<br>



## Lighthouse Audit

I tested my project using the Lighthouse tool in Chrome DevTools on each page to ensure it performs well across various aspects.

At first, I used the Lighthouse extension, which gave me higher performance scores. However, when I switched to using the Lighthouse tool in Chrome DevTools, the scores were lower than expected. To make sure I had accurate results, I retried the tests for all pages using DevTools, and the scores below are based on those updated tests.

While the performance scores are not as high as I would like them to be, I plan to work on improving them in future updates. My main concern was the accessibility scores, and I’m happy to report that they look great, which is a positive outcome.


### Lighthouse Results Table

<details>

<summary> Table </summary>

| Page                | Screenshot                                               | Comments |
|---------------------|----------------------------------------------------------|----------|
| **Home**            | ![Home Screenshot](#)                                    |          |
| **Products**        | ![Products Screenshot](#)                                |          |
| **Product Detail**  | ![Product Detail Screenshot](#)                           |          |
| **About**           | ![Our Story Screenshot](#)                               |          |
| **FAQ**             | ![FAQ Screenshot](#)                                     |          |
| **Contact**         | ![Contact Screenshot](#)                                  |          |
| **Contact Success** | ![Contact Success Screenshot](#)                          |          |
| **My Profile**      | ![My Profile Screenshot](#)                               |          |
| **Order Summary**   | ![Order Summary Screenshot](#)                            |          |
| **Newsletter**      | ![My Wishlist Screenshot](#)                             |          |
| **Register**        | ![Register Screenshot](#)                                |          |
| **Login**           | ![Login Screenshot](#)                                   |          |
| **Logout**          | ![Logout Screenshot](#)                                  |          |
| **Add Product**     | ![Add Product Screenshot](#)                              |          |
| **Edit Product**    | ![Edit Product Screenshot](#)                             |          |
| **Basket**          | ![Basket Screenshot](#)                                  |          |
| **Checkout**        | ![Checkout Screenshot](#)                                |          |
| **Order Confirmation**| ![Order Confirmation Screenshot](#)                      |          |

</details>



<br>
<br>
<br>
<br>
<br>
<br>


## 🔄 Stripe and Webhooks

### ✅ Stripe Payment Flow Test Plan

| **Step** | **Description** | **Expected Result** | **Status** |
|---------|------------------|----------------------|------------|
| **1. Load Checkout Page** | Navigate to the checkout page with a test product in the cart. | Checkout page loads with correct order details. | ✅ Pass |
| **2. Initiate Payment** | Enter delivery info and a valid test card (e.g., `4242 4242 4242 4242`), CVC, expiry, and ZIP. Click **Complete Order**. | Payment is processed and user is redirected to confirmation page. | ✅ Pass |
| **3. Validate Webhook Trigger** | Confirm that Stripe sends webhook events: `payment_intent.created`, `charge.succeeded`, `payment_intent.succeeded`, and `charge.updated`. | Webhooks are received with 200 responses and correctly logged. | ✅ Pass |
| **4. Verify Order in Database** | Check that a new order is recorded in the database. | Order matches the Stripe transaction ID and details. | ✅ Pass |
| **5. Test Payment Failure** | Use a failing card (e.g., `4000 0000 0000 9995` - insufficient funds). | Payment fails with appropriate error message. | ✅ Pass |
| **6. Check Email Notifications** | Confirm that a confirmation email is sent after successful payment. | Email is received with accurate order details. | ✅ Pass |
| **7. Test 3D Secure (Auth Required)** | Use a card that requires authentication (e.g., `4000 0025 0000 3155`). | 3D Secure authentication modal appears. | ✅ Pass |
| **8. Confirm Auth Success** | Complete the authentication in the test modal. | Payment succeeds, user is redirected, and webhook triggers. | ✅ Pass |
| **9. Test Auth Failure** | Intentionally fail the authentication in the test modal. | Payment fails with an authentication error. | ✅ Pass |



<br>
<br>
<br>
<br>
<br>
<br>
