
# SecureBuy Ecommerce Project 
#Go live 
[SecureBuy](https://secure-buy-bazaar-nkgv.vercel.app/)

SecureBuy is an ecommerce platform designed to provide customers with a secure and convenient online shopping experience. This README file offers an overview of the project, highlighting its key features and providing instructions for integrating payment with Paytm.

## Payment Integration with Paytm

To set up payment integration with Paytm, follow these steps:

1. Register your account with Paytm and obtain your Merchant ID and Key.

2. In the project directory, locate the `keys.py` file within the `arkapp` folder.

3. Open `keys.py` and specify your Merchant ID and Key as follows:

```python
# keys.py

PAYTM_MERCHANT_ID = "your_merchant_id_here"
PAYTM_MERCHANT_KEY = "your_merchant_key_here"
```

Replace "your_merchant_id_here" and "your_merchant_key_here" with your actual Paytm Merchant ID and Key.

If you require additional information or assistance, please don't hesitate to reach out for support.

Thank you for choosing SecureBuy for your ecommerce needs!

## Usage

### Main Features

1. **Add to Cart**: Shoppers can easily add products to their virtual cart for later purchase.

2. **Checkout Page**: SecureBuy offers a user-friendly checkout page where customers can review their selected items, apply discounts, and enter shipping details.

3. **Adding Products Category-Wise**: Products are neatly organized into categories, making it simple for users to find items based on their interests.

4. **Search Products Category-Wise**: Customers can search for products within specific categories, streamlining the shopping process.

5. **Update Cart**: Users have the flexibility to modify their shopping cart contents, adjust quantities, or remove items.

6. **Payment Integration with Paytm**: SecureBuy ensures secure payment processing through Paytm. To enable this feature, specify your Merchant ID and Key in the `keys.py` file of the `arkapp`.

7. **Shipping Address Form**: During the checkout process, customers can provide shipping address details to ensure a smooth delivery experience.

8. **User Profile**: Registered users can create and manage their profiles, including personal information and order history.

9. **100% Authentication with Email**: SecureBuy guarantees that user accounts are created and authenticated using email addresses for enhanced security.

## Screenshots
*Home page:
![image](https://github.com/mangesh123vispute/SecureBuy-Bazaar/assets/112755002/f439cccb-54c0-49ee-9af9-ab52d7401081)
*Registration with email verification:
![image](https://github.com/mangesh123vispute/SecureBuy-Bazaar/assets/112755002/d8eff3ec-ae01-42dd-9675-ff1a1c69c9ef)




## Database

We are using the SQLite database for this project.

## Dependencies

The project dependencies are listed in the `requirements.txt` file. Make sure to install them using `pip` before running the project.

