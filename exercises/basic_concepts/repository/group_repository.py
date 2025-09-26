import json
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

class GroupRepository:
    
    def get_all(self):
        plog("Fetching groups from repository", DEBUG)
        with open('exercises/basic_concepts/repository/groups.json', 'r') as file:
            users = json.load(file)
        return users
    
    def get_by_keyword(self, keyword: str):
        plog(f"Fetching group from repository with keyword {keyword}", DEBUG)
        
        groups = self.get_all()
        found = False
        
        keyword = keyword.lower()
        for group in groups:
            group_name = group["name"].lower()
            if group_name == keyword:
                found = True
                return group
        if not found:
            return None 
            
    def get_by_id(self, id: int):
        plog(f"Fetching group from repository with id {id}", DEBUG)
        
        groups = self.get_all()
        found = False
        
        id = int(id)
        for group in groups:
            group_id = int(group["id"])
            if group_id == id:
                found = True
                return group
        if not found:
            return None  
    
    def get_users_for_group(self, group_id):
        pass

    def get_groups_for_user(self, user_id):
        pass