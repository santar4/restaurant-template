from cloudinary_storage.storage import MediaCloudinaryStorage
import cloudinary.uploader


class DishImageStorage(MediaCloudinaryStorage):
    """Спеціальний storage для завантаження фото страв"""

    def _save(self, name, content):
        """Завантажує файл на Cloudinary без суфіксів"""
        name_without_ext = name.rsplit('.', 1)[0]
        file_ext = name.rsplit('.', 1)[1]

        result = cloudinary.uploader.upload(
            content,
            public_id=name_without_ext,
            overwrite=True,
            resource_type='auto',
        )

        return result['public_id'] + '.' + file_ext