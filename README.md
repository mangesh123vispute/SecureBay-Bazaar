# SecureBuy Ecommerce Project

SecureBuy is an ecommerce platform designed to provide customers with a secure and convenient online shopping experience. This README file offers an overview of the project, highlighting its key features and providing instructions for integrating payment with Paytm.

## Main Features

### 1. Add to Cart
- Shoppers can easily add products to their virtual cart for later purchase.

### 2. Checkout Page
- SecureBuy offers a user-friendly checkout page where customers can review their selected items, apply discounts, and enter shipping details.

### 3. Adding Products Category-Wise
- Products are neatly organized into categories, making it simple for users to find items based on their interests.

### 4. Search Products Category-Wise
- Customers can search for products within specific categories, streamlining the shopping process.

### 5. Update Cart
- Users have the flexibility to modify their shopping cart contents, adjust quantities, or remove items.

### 6. Payment Integration with Paytm
- SecureBuy ensures secure payment processing through Paytm. To enable this feature, specify your Merchant ID and Key in the `keys.py` file of the `arkapp`.

### 7. Shipping Address Form
- During the checkout process, customers can provide shipping address details to ensure a smooth delivery experience.

### 8. User Profile
- Registered users can create and manage their profiles, including personal information and order history.

### 9. 100% Authentication with Email
- SecureBuy guarantees that user accounts are created and authenticated using email addresses for enhanced security.

## Payment Integration with Paytm

To set up payment integration with Paytm, follow these steps:

1. Register your account with Paytm and obtain your Merchant ID and Key.

2. In the project directory, locate the `keys.py` file within the `arkapp` folder.

3. Open `keys.py` and specify your Merchant ID and Key as follows:

```python
# keys.py

PAYTM_MERCHANT_ID = "your_merchant_id_here"
PAYTM_MERCHANT_KEY = "your_merchant_key_here"

Replace "your_merchant_id_here" and "your_merchant_key_here" with your actual Paytm Merchant ID and Key.

Once you've configured the Paytm integration, SecureBuy will securely process payments through Paytm.

If you require additional information or assistance, please don't hesitate to reach out for support.

Thank you for choosing SecureBuy for your ecommerce needs!


You can create a `README.md` file in your project's root directory and paste the content above into it.
