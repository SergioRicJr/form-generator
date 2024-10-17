from form_generator.models.form import Form
from form_generator.repositories.base_repository import NosqlRepository


class FormRepository(NosqlRepository):
    model = Form