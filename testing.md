# 🔥 **Testing Report – Coders Roast House** 🔥  
### 🖥️ Device, Responsiveness, and Browser Compatibility Testing ✅

![Coders Roast House Logo](/xtra_documents/features/logo2.jpg)  
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

<details>

<summary> Bag App </summary>

![Bag App pep8](/xtra_documents/pep/pep2/bag/bag1.png)
![Bag App pep8](/xtra_documents/pep/pep2/bag/bag2.png)

</details>

<details>

<summary> Book App </summary>

![Book App pep8](/xtra_documents/pep/pep2/book/book1.png)
![Book App pep8](/xtra_documents/pep/pep2/book/book2.png)
![Book App pep8](/xtra_documents/pep/pep2/book/book3.png)
![Book App pep8](/xtra_documents/pep/pep2/book/book4.png)

</details>

<details>

<summary> Checkout App </summary>

![Checkout App pep8](/xtra_documents/pep/pep2/checkout/check1.png)
![Checkout App pep8](/xtra_documents/pep/pep2/checkout/check2.png)
![Checkout App pep8](/xtra_documents/pep/pep2/checkout/check3.png)
![Checkout App pep8](/xtra_documents/pep/pep2/checkout/check4.png)
![Checkout App pep8](/xtra_documents/pep/pep2/checkout/check5.png)
![Checkout App pep8](/xtra_documents/pep/pep2/checkout/check6.png)
![Checkout App pep8](/xtra_documents/pep/pep2/checkout/check7.png)

</details>

<details>

<summary> Coders App </summary>

![Coders App pep8](/xtra_documents/pep/pep2/coders/coders1.png)

</details>

<details>

<summary> Contact App </summary>

![Contact App pep8](/xtra_documents/pep/pep2/contact/contact1.png)
![Contact App pep8](/xtra_documents/pep/pep2/contact/contact2.png)
![Contact App pep8](/xtra_documents/pep/pep2/contact/contact3.png)

</details>

<details>

<summary> Faq App </summary>

![Faq App pep8](/xtra_documents/pep/pep2/faq/faq1.png)
![Faq App pep8](/xtra_documents/pep/pep2/faq/faq2.png)

</details>

<details>

<summary> Newsletter App </summary>

![Newsletter App pep8](/xtra_documents/pep/pep2/newsletter/news1.png)
![Newsletter App pep8](/xtra_documents/pep/pep2/newsletter/news2.png)
![Newsletter App pep8](/xtra_documents/pep/pep2/newsletter/news3.png)

</details>

<details>

<summary> Products App </summary>

![Products App pep8](/xtra_documents/pep/pep2/products/product1.png)
![Products App pep8](/xtra_documents/pep/pep2/products/product2.png)
![Products App pep8](/xtra_documents/pep/pep2/products/product3.png)

</details>

<details>

<summary> Profiles App </summary>

![Profiles App pep8](/xtra_documents/pep/pep2/profiles/profiles1.png)
![Profiles App pep8](/xtra_documents/pep/pep2/profiles/profiles2.png)
![Profiles App pep8](/xtra_documents/pep/pep2/profiles/profiles3.png)

</details>


---


<br>
<br>
<br>
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
| **Home**            | ![Home Screenshot](/xtra_documents/devtools/chrome/home.png)                                    |          |
| **Products**        | ![Products Screenshot](/xtra_documents/devtools/chrome/products.png)                                |          |
| **Product Detail**  | ![Product Detail Screenshot](/xtra_documents/devtools/chrome/productdetail.png)                           |          |
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

We’re brewing up some exciting updates to enhance your coffee experience. Here’s a sneak peek at what’s coming soon — and we promise, it’s hotter than your morning cup of coffee:

### 1. **Faster Checkout Experience**  
We know your time is valuable (especially when there’s coffee to be had). Our new turbocharged checkout system will get your order through faster than your Wi-Fi speed test can process. No lag, no delays — just smooth, seamless purchasing. 

### 2. **Dynamic Product Recommendations**  
Ever wish your shopping experience could read your mind? Well, we’re getting pretty close. With personalized product recommendations based on what you’ve browsed and purchased, we’re making sure you never run out of coffee — or cool new finds. It's like having your own coffee concierge.  

### 3. **Dark Mode for Night Owls**  
For those late-night coding sprints or 2 a.m. coffee cravings, we’re introducing Dark Mode. Because who needs a blinding screen when you’re trying to caffeinate in peace? It's sleek, stylish, and easy on the eyes — so you can keep sipping without squinting.

### 4. **User Account Features**  
Your coffee experience just got even more personal. With new user accounts, you’ll be able to save your favorite products, track your order history, and access special discounts. It’s like your own digital coffee vault — only with less danger of running out of beans.

### 5. **Improved Mobile Experience**  
We know you’re always on the go, so we’re optimizing our mobile layout to make shopping from your phone even smoother. Whether you’re in line at the coffee shop or in your pajamas at 2 a.m., Coders Roast House will always be at your fingertips. No glitches, just great coffee.

### 6. **The Sophine Story**  
Meet Sophine — our best customer, and also the inspiration behind our signature roast. As a designer who’s always on the lookout for perfect details, Sophine's journey with Coders Roast House started on a quest for exceptional, ethically-sourced coffee. From the moment she took her first sip, she fell in love with the rich, bold flavor of our beans.  

We’re sharing her journey with you — from the small hillside farm where it all begins, to the careful roasting process, and ultimately to the cup in Sophine's hands. It’s a story of craftsmanship, passion, and a designer's eye for perfection. And much like her design work, Sophine's relationship with our coffee is all about the perfect balance of heritage, heart, and just the right amount of drama. 

This isn’t just coffee — it’s a story that’s been brewed with care, creativity, and a deep connection to those who truly appreciate the art of coffee.


### 7. **QR Code Cards**  
Each bag will come with a QR code card that opens the door to behind-the-scenes goodness: farm stories, brew tips, and even exclusive discounts. Just scan, sip, and let the coffee adventure begin. It’s like having a VIP pass to the world of Coders Roast House.

### 8. **Handwritten Notes from Farmers**  
Every cup has a story, and now you’ll hear it straight from the source. We’re adding handwritten-style notes from the farmers who grow our beans, sharing their gratitude and a personal connection to your coffee. It’s like getting a thank-you note with your morning brew. (Because who doesn’t love a good handwritten note?)




<br>
<br>
<br>
<br>
<br>
<br>


# Am I Responsive?

## Deployed Site
Tested and delpoyed the live version here: [Am I Responsive](https://ui.dev/amiresponsive)

## Bypass X-Frame Headers for Site Mockups (Django Projects)

### Chrome Extension
Tired of X-Frame headers blocking your preview? Install the **"Ignore X-Frame Headers"** Chrome extension. It'll let you bypass those annoying security restrictions temporarily. Once you’ve done that, just reload the responsive preview page and voilà—view your site across all devices without hassle.

### Gitpod Solution
Running the project on Gitpod? Sweet. Once your project’s active, head over to the **Ports tab** and make port 8000 public by clicking the padlock icon. Then, use the live preview URL in your responsive tool for a flawless device preview. No more guesswork!


<details>

<summary> Responsive Image </summary>

![Am i responsive](/xtra_documents/responsive/ami1.png)

</details>


<details>

<summary> Responsive Image </summary>

![Am i responsive2](/xtra_documents/responsive/ami2.png)

</details>





<br>
<br>
<br>
<br>
<br>
<br>

### The Evolution of Project Swan: A Journey Through QA, Project Management, and Scope

You've officially reached the conclusion of **Project Swan** — an ambitious journey that started as a small idea and grew into something much larger than we initially imagined. **Congratulations!** Take a moment to appreciate how far you've come. And yes, go ahead, enjoy that well-deserved coffee — you've earned it.

**Project Swan** began as part of the **Code Institute’s HTML/CSS coffee house walkthrough**, a simple static site designed to introduce key web development concepts. But what started as a mockup of a coffee shop website quickly evolved into a full-stack eCommerce platform. As the vision expanded, so did the **scope**. The basic café site transformed into an online store with a fully functional shopping cart, checkout flow, and Stripe integration — a far cry from the humble beginnings.

We kicked things off on **December 28th, 2024**, still recovering from the holiday rush, fueled by leftover snacks, and no doubt, a little too much caffeine. The early stages were filled with excitement and optimism. However, as we progressed, we learned that managing the **scope**, keeping an eye on **timelines**, and staying disciplined with **project management** would be key to delivering a successful product.

---

### The Project Management Realities: Scope, Scale, and Timelines

- **Managing Scope:** Early on, we had to balance **ambition** with **realism**. What started as a small, static café site quickly grew into a full-stack application. As features piled up, so did the complexity. It became clear that we had to be strategic about how much we could actually deliver, especially when time was limited. We continuously checked back with the initial goals, ensuring the scope didn’t expand beyond what was feasible within the given timeline.

- **Scale and Complexity:** As features like the shopping cart, Stripe integration, and dynamic user accounts were introduced, the scale of the project increased. Suddenly, we were working with **backend** and **frontend** complexities that were much more involved than anticipated. At this point, effective **project management** was crucial. We had to prioritize tasks, break down each feature into manageable chunks, and track progress carefully to avoid scope creep.

- **Timelines:** We learned the hard way that no project is immune to **timeline challenges**. Initially, we underestimated how long some of the features — particularly the payment gateway integration — would take. This put significant pressure on me and tested my **time management** skills to the maximum. Deadlines loomed, and it was clear that i needed a more disciplined approach to keep things on track. I was constantly re-evaluating timelines, but through careful adjustments and iterative planning, finally we were able to meet most of our goals.

---

### What We Learned: Key QA Insights

- **Debugging is a craft, not a checklist:** As our first eCommerce project evolved from a simple static site to a fully integrated platform, debugging became a nuanced process. It wasn’t just about fixing issues but about proactively identifying and addressing potential problems early on. **Manual click-by-click testing** played a key role, allowing us to uncover hidden issues, especially when testing complex flows like the shopping cart and payment processing via **Stripe**. We also used **webhooks for Stripe** to validate payment transactions and ensure proper order updates.

- **Running tests 3x in the CLI:** Introducing features like the shopping cart and **Stripe integration** led to flaky tests and occasional inconsistencies. To ensure accuracy, we ran tests multiple times through the **CLI** using **Python**, **Stripe CLI**, and **PowerShell**. Running tests **3x in the terminal** helped us replicate real-world user conditions and provided a better understanding of how the platform performed in various scenarios. This approach allowed us to detect and resolve issues more efficiently.

- **Flaky tests: The unpredictable elements:** With new features came challenges like flaky tests, particularly in integration points such as **Stripe** payments. These inconsistencies made us question the reliability of our testing strategy. However, instead of getting frustrated, we tackled each flaky test with persistence. Running tests through the CLI and manually reproducing the issues helped us refine our approach and improve the stability of the platform.

Despite the challenges, we emerged with valuable insights and a project that is now functional, feature-rich, and much more reliable. Yes, a few bugs remain, but they are part of the learning journey and will continue to shape our development process.


---

### Key Takeaways from **Project Swan**:

- **Testing is non-negotiable:** As the project grew, we learned that testing must always align with the evolving scope of the project. Early testing helped us avoid last-minute panic fixes. **Project Swan** showed us that testing is more than just a box to check — it’s essential to prevent scope creep from affecting the end product.

- **Planning and discipline are paramount:** One of the hardest lessons we learned was that discipline in project management ensures success. As the scope grew, so did the temptation to cut corners. However, sticking to a plan, managing timelines effectively, and consistently testing allowed us to meet deadlines without compromising the quality of the final product.

- **Assertive testing ensures quality:** With new features like the shopping cart and Stripe integration, testing became even more critical. **Assertive testing** — testing what matters most to the user — allowed us to avoid unexpected failures. The lesson: If a feature is essential, it needs to be tested **rigorously** and **early**.

---

**Project Swan** has been a tremendous learning experience. We’ve gained a deeper understanding of **scope management**, **timelines**, and the need for careful **project planning** to maintain quality as a project grows in scale. In the end, success wasn’t about luck — it was about staying focused, being adaptable, and always improving.

---

**Happy roasting,**  
☕🔥 — *The Project Swan Conclusion*
