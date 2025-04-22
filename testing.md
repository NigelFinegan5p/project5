# 🔥 **Testing Report – Coders Roast House** 🔥  
### 🖥️ Device, Responsiveness, and Browser Compatibility Testing ✅

![Coders Roast House Logo](/xtra_documents/features/FB-BANNER.jpg)  
*Ensuring top-notch performance across devices and browsers, because your coffee deserves the best brew!*

---


<br>
<br>
<br>
<br>
<br>
<br>



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



## 🛡️ Defensive Programming – Coders Roast House

Manual testing was conducted to validate core navigation, authentication, checkout, and admin functions.

<details>
<summary>Click to view test table</summary>

### ✅ Manual Testing Results

| **Page** | **User Action** | **Expected Result** | **Pass/Fail** | **Comments** |
|----------|------------------|----------------------|---------------|--------------|
| **Navigation Links** |||||
| Navbar - Link ( CRH )| Click on Coders Roast House | Redirect to Home page | Pass | |
| Navbar - Shop Now | Click on "Shop" Button | Big Button Landing Page | Pass | |
| Navbar - Shop > All products | Click | Products page filtered correctly | Pass | |
| Navbar - Shop > All coffee | Click | Products page filtered correctly | Pass | |
| Navbar - Shop > Coffee Boxes | Click | Products page filtered correctly | Pass | |
| Navbar - About | Click on "About" link | Dropdown appears with subpages | Pass | |
| About > Our Story & Contact form together | Click | Redirect to Contact & About | Pass | |
| About > FAQ | Click | Redirect to FAQ page | Pass | |
| About > Contact | Click | Redirect to Contact page | Pass | |
| Search | Enter search term and submit | Redirect to filtered results page | Pass | |
| Auth Links | Click Register / Login / Basket icons | Redirect to respective pages | Pass | |
| Account Dropdown | Click "Account" | Shows My Profile & Logout options | Pass | |
| Account > My Profile | Click | Redirect to Profile page | Pass | |
| Account > Logout | Click | Logs user out, redirect to Home | Pass | |
| Admin Dropdown | Click "Admin" | Shows admin options | Pass | |
| Admin > Admin Panel | Click | Redirect to Admin Dashboard | Pass | |
| Admin > Add New Product | Click | Redirect to Add Product page | Pass | |
| Admin > Edit/Delete Product | Click | Redirect to Product Management page | Pass | |
| **Footer** |||||
| Footer links (Copyright, sitemap, privacy policy, 6 x icons) | Click | Redirect to respective pages | Pass | |
| Newsletter ( Custom Model) | Click "Subscribe" | Show confirmation message | Pass | |
| Social Icons | Click | Open social platform in new tab | Pass | |
| **Registration & Login** |||||
| Register | Fill form and submit | Redirects to verification notice | Pass | |
| Login | Submit valid credentials | Redirect to Home page | Pass | |
| Logout | Use Account > Logout | Logs user out, redirect Home | Pass | |
| **User Profile** |||||
| Update Info | Submit form | Info is saved | Pass | |
| Order History | Click | Show order records, alert if empty | Pass | |
| **Site Navigation (Logged Out User)** |||||
| Try to access restricted page | Redirect to Login | Pass | |
| **Product Listings** |||||
| Product Image or Name | Click | Redirect to Product Details | Pass | |
| Sorting dropdown | Select option | Products reorder accordingly | Pass | |
| **Product Details** |||||
| View full image | Click on product image | Opens larger image | Pass | |
| Add to Basket | Click button | Adds item, show basket message | Pass | |
| Keep Shopping | Click | Returns to product list | Pass | |
| Logged out – Wishlist icon | Click | Redirect to Sign Up/Login | Pass | |
| **Admin Product Controls** |||||
| Edit button | Click | Redirect to edit form | Pass | |
| Delete button | Click | Show delete confirmation modal | Pass | |
| Delete modal - Confirm | Click | Delete product | Pass | |
| Delete modal - Cancel | Click | Close modal | Pass | |
| **FAQ** |||||
| Question dropdown | Click | Toggle answer visibility | Pass | |
| Back Home | Click | Return to Home page | Pass | |
| **Contact Page** |||||
| Form Inputs | Fill and submit | Redirect to success page, show message | Pass | |
| Back Home (Contact Success) | Click | Return to Home | Pass | |
| **Add/Edit Product – Admin Only** |||||
| Add/Edit product form | Fill and submit | Save and redirect appropriately | Pass | |
| Cancel (Edit) | Click | Return to Products page | Pass | |
| **Basket Functionality** |||||
| Quantity adjust | Use + / - buttons | Quantity changes | Pass | |
| Update link | Click after quantity change | Subtotal/total update | Pass | |
| Remove item | Click | Item removed, totals adjust | Pass | |
| Keep Shopping | Click | Return to Products page | Pass | |
| Secure Checkout | Click | Redirect to Checkout page | Pass | |
| **Checkout Page** |||||
| All input fields | Enter data | Required fields validated | Pass | |
| Stripe Payment | Enter test card | Process payment | Pass | |
| Save delivery info | Check box | Info saved to profile | Pass | |
| Order summary items | Click name/image | Redirect to Product page | Pass | |
| Adjust Basket | Click | Return to Basket page | Pass | |
| Complete Order | Click | Finalize order, redirect to confirmation | Pass | |

</details>



## 📧 Email Confirmation Testing – Coders Roast House


<details>
<summary>Click to view test table</summary>

### ✅ Email Functionality Test Table


| **Test Step** | **Scenario** | **Expected Email Behavior** | **Status** |
|---------------|--------------|------------------------------|------------|
| **1. Account Registration** | User registers with valid email | A confirmation email is sent with an activation or welcome link | ✅ Pass |
| **2. Order Placement** | User completes a successful order via Stripe | Email is sent with: <br>• Unique order number <br>• Itemized product list <br>• Prices and totals <br>• Delivery info <br>• Estimated delivery time | ✅ Pass |
| **3. Newsletter Signup** | User enters email in the newsletter form in footer and submits | Confirmation or "Thanks for subscribing" email is sent | ✅ Pass |
| **4. Duplicate Newsletter Signup** | Same user tries to sign up again | System prevents duplicate subscription or notifies user | ✅ Pass |
| **5. Email Content Accuracy** | Email reflects: <br>• Correct order details <br>• Pricing breakdown <br>• Accurate customer info | ✅ Pass |
| **6. Invalid Email Entry** | User tries to register or sign up with invalid email format | Form is rejected with error message | ✅ Pass |
| **7. Duplicate Account Registration** | User attempts to register with an already-used email | Error is displayed or prevented | ✅ Pass |
| **8. Spam Folder Check** | Confirmation or order email is sent | Email lands in inbox, not marked as spam | ✅ Pass |



</details>


<br>
<br>
<br>
<br>
<br>
<br>



# 🍖 Coders Roast House – Bug Fix Hold-Off 🐞

At Coders Roast House, we spotted that pesky bug where the minus (–) button in the shopping bag doesn’t disable when the quantity hits 1 — especially on desktop.

Code Institute offers a fix for this, and while it technically works, we found it added way too much lag to the “Add to Bag” process.

And let’s be real — no one wants a slow checkout when they’re hungry for clean code.

**So we skipped the fix** in the walkthrough version to keep the experience fast and smooth.

If you’re after full functionality and don’t mind the extra weight, you can still find the fix in the final code.



<br>
<br>
<br>
<br>
<br>
<br>



# 🔮 Future Features Coming Soon to Coders Roast House

Here’s a sneak peek at some delicious features we’re cooking up for future releases:

### 1. **Faster Checkout Experience**  
We’re working on a turbocharged checkout system that will make adding to your bag and completing purchases feel like a breeze — no lag, no delays.

### 2. **Dynamic Product Recommendations**  
Next, we’re adding personalized product recommendations right in your bag based on your browsing and past purchases. Get ready to discover more of what you love!

### 3. **Dark Mode for Night Owls**  
For all the late-night coders out there, we’re introducing a sleek Dark Mode to make your shopping experience easier on the eyes.

### 4. **User Account Features**  
Log in, save your favorite products, track your order history, and get special discounts. We’re giving you the tools to make your shopping experience even more personalized.

### 5. **Improved Mobile Experience**  
We’re fine-tuning our mobile layout and interactivity to ensure Coders Roast House works flawlessly across all devices.


### 6. **The Sophine Story**  
We’ll be sharing the beautiful origin story of our signature roast — Sophine Story From Click to Sip: A Coffee Story Worth Sharing — including its journey from a small hillside farm to your cup. Expect rich storytelling, heritage details, and heart.

### 7. **QR Code Cards**  
Scan and sip. Each bag will come with a QR code card that takes you straight to behind-the-scenes content: farm stories, brew tips, and even exclusive discount drops.

### 8. **Handwritten Notes from Farmers**  
Real notes. Real gratitude. We’re working on including personalized, handwritten-style messages from the farmers who grow our beans — because every roast has a face and a story.


