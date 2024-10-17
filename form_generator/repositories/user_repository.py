from form_generator.models.user import User
from form_generator.repositories.base_repository import NosqlRepository


class UserRepository(NosqlRepository):
    model = User