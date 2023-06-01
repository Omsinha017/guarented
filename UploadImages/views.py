import os
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from Guarented.settings import bucket
from .models import Item

class ImageUploadView(View):
    """
    A view class for uploading images to a storage bucket and associating them with items.

    Methods:
    - upload_image(): Uploads images from a local folder to the storage bucket and associates them with items.
    - post(request): Handles the HTTP POST request for image upload.

    """

    async def upload_image(self):
        """
        Uploads images from a local folder to the storage bucket and associates them with items.

        This method performs the following steps:
        1. Constructs the local folder path using the base directory of the Django project.
        2. Iterates over the files in the folder.
        3. Uploads each file to the storage bucket.
        4. Retrieves the public URL of the uploaded file.
        5. Extracts the file name without the extension.
        6. Retrieves the corresponding item from the database, if it exists.
        7. Appends the public URL to the item's images list if the item exists.
        8. Creates a new item with the file name as the item ID and the public URL as the first image if the item doesn't exist.
        9. Saves the item in the database.

        """
        folder_path = os.path.join(settings.BASE_DIR, 'Images')
        try:
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                blob = bucket.blob(file_name)
                blob.upload_from_filename(file_path)
                public_url = blob.public_url
                file_name_without_ext = os.path.splitext(file_name)[0]
                item = Item.objects(item_id=file_name_without_ext).first()
                if item:
                    item.images.append(public_url)
                else:
                    item = Item(item_id=file_name_without_ext, images=[public_url])
                item.save()
        except Exception as e:
            return JsonResponse({'error': 'Failed to upload images: ' + str(e)}, status=500)

    async def post(self, request):
        """
        Handles the HTTP POST request for image upload.

        This method calls the upload_image() method to upload images and associate them with items.
        It returns a JSON response with a success message or an error message in case of failure.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - JsonResponse: A JSON response with a success message or an error message.

        """
        try:
            await self.upload_image()
            return JsonResponse({'message': 'Images uploaded successfully'})
        except Exception as e:
            return JsonResponse({'error': 'Failed to upload images: ' + str(e)}, status=500)