from abc import ABC, abstractmethod
from typing import Optional
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

# Interfaz del repositorio (bajo acoplamiento)
class EntityRepository(ABC):
    
    @abstractmethod
    def get_all(self) -> list:
        pass
        
    @abstractmethod
    def get_by_keyword(self, keyword: str) -> Optional[dict]:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[dict]:
        pass
    
    @abstractmethod
    def get_users_for_group(self, group_id):
        pass
    
    @abstractmethod
    def get_groups_for_user(self, user_id):
        pass