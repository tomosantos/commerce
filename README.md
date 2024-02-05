# WeBay - CS50 Web Project 2

## Introduction:

Welcome to WeBay, a web application developed as Project 2 for CS50 Web. WeBay is an online auction platform built using Django, Python, HTML, CSS, JavaScript, and Bootstrap 5. In this documentation, we'll explore the main features implemented and the underlying structure of the project.

## Technologies Used:

- Django;
- Python;
- SQLite;
- HTML, CSS, JavaScript;
- Bootstrap 5.

## Models:

WeBay utilizes five main models to manage different aspects of the platform:

- **Bids**: Manages the bidding process for products.
- **Categories**: Categorizes products for better organization.
- **Comments**: Allows users to add comments to product listings.
- **Listings**: Represents individual products available for auction.
- **Users**: Manages user information and ownership of products.

## Overview:

### Creating a New Product:

- Navigate to the index page.
- Click on the "Create New Product" option.
- Provide the necessary information, such as title, description, photo, and price.

### Product Overview:

- The index page displays all active products with details like photo, title, description, price, and a button leading to the specific product page.

### Product Page:

- Displays detailed information about a product.
- Features include title, photo, detailed description, owner information, and price.
- Users can increase their bid or set the auction closing price if they are the owner.
- Options to end the auction or add the product to the watchlist.

### Watchlist:

- Users can add products to their watchlist for easy tracking.
- The watchlist page displays the user's saved products.
- Products can be removed from the watchlist.

### Comments:

- Users can add comments to product listings.
- Comments section allows for interaction and discussion.

### Category Filtering:

- WeBay supports filtering products based on categories.
- Users can view products within specific categories like electronics, books, etc.

### Auction Simulation:

- Simulate closing an auction by making a bid.
- Switch to the owner account and close the auction.
- The winning bid is displayed on the respective product page.

### Django Admin:

- Administrators can use the Django Admin platform to manage products, comments, and bids.
- Provides functionalities like viewing, adding, editing, and deleting.

