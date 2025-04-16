

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

| Browser | Notes |
| --- | --- |
| Chrome | Works as expected & intended ( majority Market share browser ) |
| Edge | Works as intended |
| Safari | Works as intended |
| Firefox | Works as intended |

<br>

All validation tools and device/browser testing confirm that the project functions as intended across platforms, with only minor tweaks needed for enhanced responsiveness and visual polish

<br>
<br>
<br>
<br>




