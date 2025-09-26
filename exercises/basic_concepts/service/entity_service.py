# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

from exercises.basic_concepts.repository.interface import EntityRepository

class EntityService:
    """
    Service component that contains business logic.

    Uses dependency injection to receive a repository instance.
    """

    def __init__(self, repository: EntityRepository):
        """Initializes the service with a given repository."""
        plog("Initializing UserService with repository", DEBUG)
        self.repository = repository

    def list_users(self):
        """Retrieves the list of users from the repository."""
        plog("Listing users from service", INFO)
        return self.repository.get_all()
    
    def list_groups(self):
        """Retrieves the list of groups from the repository."""
        plog("Listing groups from service", INFO)
        return self.repository.get_all()
    
    def get_by_keyword(self, keyword: str):
        plog("Retrieving user with keyword", INFO)
        return self.repository.get_by_keyword(keyword=keyword)
    
    def get_by_id(self, id: int):
        plog("Retrieving user with id", INFO)
        return self.repository.get_by_id(id=id)
    
    def get_users_for_group(self, group_id: int):
        plog("Retrieving users with group id", INFO)
        return self.repository.get_users_for_group(group_id=group_id)
    
    def get_groups_for_user(self, user_id: int):
        plog("Retrieving groups with user id", INFO)
        return self.repository.get_groups_for_user(user_id=user_id)