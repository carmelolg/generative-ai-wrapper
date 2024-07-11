import base64
from io import BytesIO


class ImageUtils(object):

    __instance = None

    @staticmethod
    def get_instance():

        if ImageUtils.__instance is None:
            ImageUtils()

        return ImageUtils.__instance

    def __init__(self):
        if ImageUtils.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ImageUtils.__instance = self

    def convert_to_base64(self, path_image):
        with open(path_image, "rb") as image_file:
            return base64.b64encode(image_file.read())
