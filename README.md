# Project Name

## Description

A test apllication to learn build applications with Django.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.6 or higher
*   pip (Python package installer)
*   Virtual environment (recommended)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/pirus99/fruit-app/
    cd fruit-app
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  **Create a `.env` file:**

    Copy the `example.env` file to `.env`:

    ```bash
    cp example.env .env
    ```

2.  **Edit the `.env` file:**

    Fill in the necessary values, such as your database credentials, secret key, and other configuration settings.  *Do not commit the `.env` file to version control!*

3.  **Update settings:**

    Update your `settings.py` to read environment variables using `os.environ.get()`.

    Example:

    ```python
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = os.environ.get('DEBUG', False)  # Default to False if not set
    ```

4.  **Database Setup:**

    *   **Make migrations:**

        ```bash
        python manage.py makemigrations
        ```

    *   **Apply migrations:**

        ```bash
        python manage.py migrate
        ```

### Running the Development Server

```bash
python manage.py runserver
