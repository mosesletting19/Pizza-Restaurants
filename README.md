# Pizza Challenge API

## Overview

This Flask application provides an API for managing pizza restaurants, pizzas, and restaurant-pizza associations.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   ```

2. **Navigate to the project directory:**
   ```bash
   cd pizza-challenge
   ```

3. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment:**

   On macOS and Linux:
   ```bash
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

5. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask application:**
   ```bash
   python app.py
   ```

2. **Access the API endpoints using a tool like Postman or cURL:**

   - Endpoint 1
   - Endpoint 2
   - ...

## Models

The application has the following models:

- Restaurant: Represents a pizza restaurant.
- Pizza: Represents a type of pizza.
- RestaurantPizza: Represents the association between a restaurant and a pizza.

## Constraints and Validations

- Restaurant model:
  - Name must be less than 50 characters in length.
  - Name must be unique.

- Pizza model:
  - No specific constraints or validations provided in the challenge.

- RestaurantPizza model:
  - Price must be between 1 and 30.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.




