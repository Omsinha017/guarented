# Image Upload to Google Cloud Storage and MongoDB with Django

This Django project provides a solution for uploading images from a local folder to a Google Cloud Storage bucket and associating them with items stored in a MongoDB database. The uploaded images are asynchronously processed and their public URLs are stored in the database.

## Prerequisites

Before running the project, make sure you have the following prerequisites installed:

- Python (version 3.6 or above)
- Django (version 3.0 or above)
- Google Cloud SDK
- MongoDB

## Getting Started

Follow the steps below to set up and run the project:

1. Clone the repository:

```
git clone https://github.com/Omsinha017/guarented.git
```

2. Install the Python dependencies:

```
pip install -r requirements.txt
```

3. Set up Google Cloud Storage:

   - Create a Google Cloud Storage bucket.
   - Generate a service account key for your bucket and download the JSON file.
   - Rename the JSON file to `creds.json` and replace the existing `creds.json` file in the project directory.
   - Update the `GOOGLE_CLOUD_STORAGE_BUCKET`, `GOOGLE_CLOUD_STORAGE_ACCESS_KEY`, and `GOOGLE_CLOUD_STORAGE_SECRET_KEY` variables in the `settings.py` file with your bucket information.

4. Set up MongoDB:

   - Install MongoDB if you haven't already.
   - Start the MongoDB server.

5. Configure the database connection:

   - Update the `connect()` function in the `settings.py` file with your MongoDB database connection details.

6. Run the migrations:

```
python manage.py migrate
```

7. Run the Django development server:

```
python manage.py runserver
```

8. Access the image upload endpoint:

   - Open your postman and hit a post request to `http://localhost:8000/upload/images/`.
   - This endpoint handles the image upload process asynchronously.
   - After the images are uploaded, their public URLs will be stored in the MongoDB database.

## Folder Structure

The main files and folders in the project are as follows:

- `README.md`: Provides instructions and information about the project.
- `manage.py`: Django project management script.
- `requirements.txt`: Contains the Python dependencies required for the project.
- `Guarented/`: Django project directory.
  - `settings.py`: Django project settings file. Contains configuration settings, database connection details, and Google Cloud Storage settings.
  - `urls.py`: Django project URL configuration file. Contains the URL patterns for the project.
- `UploadImages/`: Django app directory.
  - `models.py`: Defines the database model for items. Uses mongoengine to interact with MongoDB.
  - `views.py`: Contains the view class for uploading images to Google Cloud Storage and associating them with items.
- `creds.json`: Service account key file for Google Cloud Storage authentication.

## Additional Notes

- The image upload process is handled asynchronously using Django's `async_to_sync()` function and the `async`/`await` syntax.
- The Google Cloud Storage bucket and MongoDB database connection details are stored in the `settings.py` file. Make sure to update them with your own credentials.
- The project uses the `google-cloud-storage` library to interact with Google Cloud Storage and the `mongoengine` library to interact with MongoDB.
- The uploaded images are stored in the `Images/` folder relative to the project directory. Update the `folder_path` variable in the `upload_image()` method of `views.py` if you want to change the folder location.
- The project handles errors during the image upload process and returns appropriate error messages as JSON responses.
## Screenshots

![Upload Images](https://drive.google.com/uc?export=view&id=1q5bJCbZ6UZumFMoNo8yEwTjF-ywiY5no)
