from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_xpath('//*[@id="menu-items"]/li[7]/a').click()
            wd.find_element_by_xpath('//*[@id="manage-menu"]/ul/li[2]/a').click()

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath('//*[@id="content"]/div[2]/form/fieldset/input[2]').click()
        self.fill_form(project)
        wd.find_element_by_xpath('//*[@id="manage-project-create-form"]/fieldset/span/input').click()
        self.app.open_home_page()
        self.project_cache = None
    
    def fill_form(self, project:Project):
        self.fill_form_field("name", project.name)
        self.fill_form_field("description", project.description)

    def fill_form_field(self, field_name, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)   

    def select(self, id=None):
        wd = self.app.wd
        wd.find_element_by_xpath(f'//a[@href="manage_proj_edit_page.php?project_id={id}"]').click()

    def delete(self, project):
        wd = self.app.wd
        self.select(id = project.id)
        wd.find_element_by_xpath('//*[@id="project-delete-form"]/fieldset/input[3]').click()
        wd.find_element_by_xpath('//*[@id="content"]/div/form/input[4]').click()
        self.project_cache = None

    def __len__(self):
        wd = self.app.wd
        self.open_projects_page()
        tbody = wd.find_element_by_xpath('//*[@id="content"]/div[2]/table/tbody')
        return len(tbody.find_elements_by_tag_name('tr'))

    project_cache = None

    def list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            tbody = wd.find_element_by_xpath('//*[@id="content"]/div[2]/table/tbody')
            rows = tbody.find_elements_by_tag_name('tr')
            self.project_cache = []
            for row in rows:
                cols = row.find_elements_by_tag_name('td')
                url = cols[0].find_element_by_tag_name('a').get_attribute("href")
                id = url.split("id=")[1]
                project = Project(
                    id=id,
                    name=cols[0].text,
                    description=cols[-1].text,
                )

                self.project_cache.append(project)
        return self.project_cache
