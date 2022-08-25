from suds.client import Client
from suds import WebFault

from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.url = f"{app.url}api/soap/mantisconnect.php?wsdl"

    def can_login(self, username, password):
        client = Client(self.url)
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        client = Client(self.url)
        try:
            query = client.service.mc_projects_get_user_accessible(self.app.username, self.app.password)
            projects = []
            for object in query:
                project = Project(
                    id=object.id,
                    name = object.name,
                    description=object.description
                )
                projects.append(project)
            return projects
        except WebFault:
            return []
        