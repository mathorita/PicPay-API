# 💸 PicPay Backend Challenge

This project is a simulation of a money transfer system between users, inspired by the PicPay app. https://github.com/PicPay/picpay-desafio-backend

## 🚀 Features

- User registration (Common user or Shopkeeper)
- Money transfers between users
- Business rules validation:
  - Users cannot transfer to themselves
  - Shopkeepers are not allowed to send money
  - Senders must have sufficient balance
- Integration with external authorization service
- Notification to external service after a transaction
- Automated tests using `pytest` and `APIClient`
- JWT Protection
- IsSender and IsUser permissions (only owner can see the personal informations)
- DockerFile created

---

## 🧪 Tests

To run the test suite:

```bash
pytest
Required packages:
pip install pytest pytest-django

📦 How to Run the Project
Clone the repository:
git clone https://github.com/mathorita/PicPay-API.git
cd your-repo

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windowa

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

🔗 API Endpoints
POST /user/ — Register new user

GET /user/ — List all users

POST /transaction/ — Make a transaction between users

🛠 Tech Stack
Python 3

Django

Django REST Framework

Pytest

Requests

👨‍💻 Author
Developed by Matheus Toshiaki Horita
Contact: [matshiaki@gmail.com]

