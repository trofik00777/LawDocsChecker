from docx import Document

from ml.data_preprocessing import DocProcessor
from .base_manager import BaseManager


class DocManager(BaseManager):
    def __init__(self, *kwargs):
        pass

    def __call__(self, doc: Document):
        return DocProcessor.preprocess_doc(doc)

