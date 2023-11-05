SecureBuy Ecommerce Project
SecureBuy is an ecommerce project that provides a secure and convenient online shopping experience for customers. This README file provides an overview of the project, its main features, and instructions for integrating payment with Paytm.

Main Features
1. Add to Cart
Users can add products to their shopping cart for easy access and checkout.
2. Checkout Page
SecureBuy provides a user-friendly checkout page where customers can review their selected items, apply discounts, and enter shipping details.
3. Adding Products Category-Wise
Products are categorized for easy navigation and search. Users can browse and shop by category.
4. Search Products Category-Wise
Customers can search for products within specific categories, making it easier to find what they need.
5. Update Cart
Users can modify the contents of their shopping cart, such as changing quantities or removing items.
6. Payment Integration with Paytm
SecureBuy offers secure payment processing through Paytm. To enable this feature, you need to specify your Merchant ID and Key in the keys.py file of the arkapp.
7. Shipping Address Form
Customers can provide their shipping address details during the checkout process to ensure timely delivery.
8. User Profile
Registered users can create and manage their profiles, including personal information and order history.
9. 100% Authentication with Email
SecureBuy ensures that user accounts are created and authenticated using email addresses for added security.
Payment Integration with Paytm
To enable payment integration with Paytm, you need to follow these steps:

Register your account with Paytm and obtain your Merchant ID and Key.

In the project directory, locate the keys.py file within the arkapp folder.

Open keys.py and specify your Merchant ID and Key as follows:

python
Copy code
# keys.py

PAYTM_MERCHANT_ID = "your_merchant_id_here"
PAYTM_MERCHANT_KEY = "your_merchant_key_here"
Make sure to replace "your_merchant_id_here" and "your_merchant_key_here" with your actual Paytm Merchant ID and Key.

Once you have configured the Paytm integration, SecureBuy will be able to process payments securely through Paytm.

If you need any further information or assistance, please feel free to reach out for support.

Thank you for choosing SecureBuy for your ecommerce needs!
