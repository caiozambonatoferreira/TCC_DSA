Ensure you have the following installed on your machine:

- Python 3.8+
- Node.js 14+ and npm/yarn
- Git

---

## The project is implemented in Python 3.7+ and uses the following key libraries:

- `DjangoREST`
- `BeautifulSoup`
- `requests`

## Setup Instructions

### 1. Clone the Repository

`git clone git@github.com:caiozambonatoferreira/TCC_DSA.git`

### 2. Create a venv in the root folder

`python -m venv venv`

#### And activate the venv

`call venv/Scripts/activate`

(If you are not on Windows, use `source venv/bin/activate `)

### 3. Enter the /backend folder and install all dependencies present in the file requirements.txt

`pip install -r requirements.txt`

### 4. Apply all the migrations

`python manage.py makemigrations`

And then 

`python manage.py migrate`

### 5. Try running the API with the following command:

`python manage.py runserver`

*The project should be running in http://127.0.0.1:8000/*

## Frontend

### 1. Enter the /frontend folder and install the dependencies

`npm install`

### 2. Run the server

`npm run serve`

*The project should be running in http://localhost:8080/*

