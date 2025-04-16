# Django Blog

A simple and elegant blogging platform built with Django. This application allows users to create and manage blog posts, pages, and author profiles.

## Features

- Responsive design using Bootstrap 5
- Blog posts with featured images
- Static pages
- Author profiles
- Admin interface for content management
- Pagination

## Requirements

- Python 3.13+
- Django 5.2
- Pillow (for image handling)

## Installation

1. Clone the repository
2. Install dependencies using uv:

```bash
cd django_blog
uv sync
source .venv/bin/activate
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Create a superuser:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Access the application at http://127.0.0.1:8000/

## Project Structure

- `blog/` - The main blog application
  - `models.py` - Data models (Author, Post, Page)
  - `views.py` - View functions and classes
  - `urls.py` - URL routing
  - `admin.py` - Admin interface configuration
- `templates/` - HTML templates
  - `base.html` - Base template with common elements
  - `blog/` - Blog-specific templates
- `static/` - Static files (CSS, JS, images)
- `media/` - User-uploaded files

## Usage

1. Log in to the admin interface at http://127.0.0.1:8000/admin/ using your superuser credentials
2. Create an Author profile linked to your user account
3. Create Pages for static content (About, Contact, etc.)
4. Create Posts with content, featured images, and excerpts
5. View your blog at http://127.0.0.1:8000/

## Models

### Author
- Extends the built-in User model
- Includes bio, profile picture, and website URL

### Post
- Title, slug, content, featured image
- Author (linked to Author model)
- Publication status (draft or published)
- Created, updated, and published dates

### Page
- Title, slug, content, featured image
- Publication status
- Order for menu positioning

## License

This project is open-source and available under the MIT License.
