class Project:
    def __init__(self, name, description, licensee, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = licensee
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors_in_rows = "\n".join(f" - {author}" for author in self.authors)
        dependencies_in_rows = "\n".join(f" - {dependency}" for dependency in self.dependencies)
        dev_dependencies_in_rows = "\n".join(f" - {dependency}" for dependency in self.dev_dependencies)

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors: "
            f"\n{authors_in_rows}\n"
            f"\n Dependencies: "
            f"\n{dependencies_in_rows}\n"
            f"\nDevelopment dependencies:"
            f"\n{dev_dependencies_in_rows}"
        )
