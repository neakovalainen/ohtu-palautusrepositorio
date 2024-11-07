from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_version = toml.loads(content)
        return Project("Ohtutesting app", "sovellus, joka toimii testisyötteenä", "MIT",["pete", "pirkko", "pate"], ["python", "Flask"], ["coverage", "robotframework"])
