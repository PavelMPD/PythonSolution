import os
from math import ceil
from PIL import Image, ImageDraw
from documents.document import Document


class DocumentParser():
    def __init__(self):
        None

    def process(self, filename, template):
        items = {}
        with open(filename, "rb") as f:
            image = Image.open(f)
            width = image.size[0]
            height = image.size[1]
        for item_key in template.items:
            item = template.items[item_key]
            items[item_key] = (int(ceil(item[0]*width)), int(ceil(item[1]*height)),
                               int(ceil(item[2]*width)), int(ceil(item[3]*height)))
        return Document(filename, template, width, height, items)

    def draw_items(self, document, path=None):
        path = ('' if path is None else path) + document.pattern.document_type + ".jpg"
        with open(document.filename, "rb") as f:
            image = Image.open(f)
            draw = ImageDraw.Draw(image)
            for item_key in document.items:
                draw.rectangle(document.items[item_key])
            del draw
            image.save(path, "JPEG")

    def crop_items(self, document, path=None):
        if path is not None and not os.path.exists(path):
            os.makedirs(path)
        with open(document.filename, "rb") as f:
            image = Image.open(f)
            for item_key in document.items:
                self._crop(image, document.items[item_key], item_key, path)

    def _crop(self, image, rectangle, name, path=None):
        path = ('' if path is None else path) + name + ".jpg"
        region = image.crop(rectangle)
        region.save(path)