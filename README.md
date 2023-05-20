# Django REST Project

This project is a Django-based RESTful API that provides endpoints for managing a collection of items.

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/django-rest-project.git

2. Create a virtual environment:
    ```bash
    cd django-rest-project
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the dependencies
    ```bash
   pip install -r requirements.txt

4. Run database migrations
    ```bash
   python manage.py migrate

5. Start the development server:
    ```bash
   python manage.py runserver

6. Access the API in your browser at http://localhost:8000/chatbot_api/.

## API Endpoints
No Authorizations are required for accessing below mentioned api endpoints
1. /chatbot_api/food_search/:

    POST: Make a query if a food item matches your diet plan.<br>Request Body
    
    ```json
    
    {
    "food":"<food-item-name>",
    "diet":"<diet-plan-name>"
    }
    ```
    Response
    ```json
    {
        "response":"<text-response>",
    }   
    ```

2. /chatbot_api/diet_selector/:

    POST: Suggest a diet plan according to user requirements.<br>Request Body
    
    ```json
    {
        "age": "",
        "sex": "",
        "height": "",
        "weight": "",
        "to_gain_or_loose": "",
        "vegan_or_non": ""
    }
    ```
    Response
    ```json
    {
        "response":"<text-response>",
    }   
    ```


     