# Ethiopian Recipe API

This Flask API provides a management system for Ethiopian food recipes. It allows users to view, search, and retrieve recipes using JSON data.

## Features

- View all recipes: `/recipes`
- Get a specific recipe by ID: `/recipe/<int:recipe_id>`
- Search recipes by title, ingredients, or instructions: `/recipes/<string:search_query>`

## Installation

1. Clone the repository:
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   ```

2. Navigate to the project directory:
   ```bash
   cd ethiopian-recipe-api
   ```

3. Create a virtual environment and install dependencies:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   pip install -r requirements.txt
   ```

## Usage

Run the application locally:
```bash
python app.py
```

The API will be accessible at `http://127.0.0.1:5000`.

## Deployment

This project is hosted on Render. You can deploy it easily by linking your GitHub repository to Render.

1. Sign up for a [Render](https://render.com) account.
2. Create a new Web Service using your GitHub repository.

## API Endpoints

- `/recipes` - Retrieve all recipes.
- `/recipe/<int:recipe_id>` - Get a specific recipe by ID.
- `/recipes/<string:search_query>` - Search recipes by title, ingredients, or instructions.

## License

[MIT](LICENSE)
