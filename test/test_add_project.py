from model.project import Project
from uuid import uuid4

def test_add_project(app):
    project = Project(name=str(uuid4())[:7], description="test_project")
    old_projects = app.project.list()
    app.project.create(project)
    assert len(old_projects) +1 == len(app.project)
    new_projects = app.project.list()
    old_projects.append(project)
    assert sorted(old_projects) == sorted(new_projects)
