import unittest
from document_parser import DocumentParser
from templates.template_factory import PatternFactory
from documents.document_types import DocumentTypes


class TestDocumentParser(unittest.TestCase):
    def test_process(self):
        pf = PatternFactory('..\\')
        pattern = pf.get_pattern(DocumentTypes.BELGIAN_EID_CARD_FRONT_SIDE)
        dp = DocumentParser()
        document = dp.process(r'..\examples\1.jpg', pattern)
        print(document.items)

    def test_crop_items(self):
        pf = PatternFactory('..\\')
        pattern = pf.get_pattern(DocumentTypes.BELGIAN_EID_CARD_FRONT_SIDE)
        dp = DocumentParser()
        document = dp.process(r'..\examples\1.jpg', pattern)
        print(document.items)
        dp.crop_items(document, document.pattern.document_type + '\\')

    def test_draw_items(self):
        pf = PatternFactory('..\\')
        pattern = pf.get_pattern(DocumentTypes.BELGIAN_EID_CARD_FRONT_SIDE)
        dp = DocumentParser()
        document = dp.process(r'..\examples\1.jpg', pattern)
        print(document.items)
        dp.draw_items(document, document.pattern.document_type + '\\')