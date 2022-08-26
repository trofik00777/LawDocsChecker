from docx import Document


class BaseManager:
    def __init__(self, *kwargs):
        raise NotImplementedError

    def __call__(self, doc: Document):
        raise NotImplementedError
