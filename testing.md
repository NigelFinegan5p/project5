

## Code Validation

### HTML Validation

For my HTML files, I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

Due to the usage of Jinja syntax (e.g., `{% extends "base.html" %}` and `{{ form|crispy }}`) and authentication requirements, the following approach was used for validation:

1. Navigate to each individual page via the deployed Heroku app link.
2. Right-click the screen or use `CTRL+U` (`⌘+U` on Mac) to "View page source."
3. Copy the complete HTML code and paste it into the [validate by input](https://validator.w3.org/#validate_by_input) option.
4. Fix any errors or warnings, revalidate, and record results.

All pages passed validation, except for the Add Product and Edit Product pages.


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



### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate my JS files.  The JS files in my project were not written by me but taken from Boutique Ado, Stripe and CountryField.

All files passed with no errors.  The Stripe one has an extra semi-colon and two undefined variables, but as it did not come from me I am leaving it alone.

<details>

<summary> Stripe screenshot </summary>

![Stripe JS](/xtra_documents/w3c/jshint.png)


</details>

---

