from model.project import Project
from random import choice


def test_del_random_project(app):
    if not len(app.project):
        app.project.create(Project(name="to_be_deleted", description="..."))
    old_projects = app.project.list()
    project = choice(old_projects)
    app.project.delete(project)
    assert len(old_projects) -1 == len(app.project)
    new_projects = app.project.list()
    old_projects.remove(project)
    assert sorted(old_projects) == sorted(new_projects)
