from pallets_sphinx_themes import get_version
from pallets_sphinx_themes import ProjectLink

# Project --------------------------------------------------------------

project = "secure-cookie"
copyright = "2007 Pallets"
author = "Pallets"
release, version = get_version("secure-cookie", version_length=1)

# General --------------------------------------------------------------

master_doc = "index"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.intersphinx", "pallets_sphinx_themes"]
intersphinx_mapping = {"python": ("https://docs.python.org/3/", None)}

# HTML -----------------------------------------------------------------

html_theme = "flask"
html_context = {
    "project_links": [
        ProjectLink("Donate to Pallets", "https://palletsprojects.com/donate"),
        ProjectLink("PyPI releases", "https://pypi.org/project/secure-cookie/"),
        ProjectLink("Source Code", "https://github.com/pallets/secure-cookie/"),
        ProjectLink(
            "Issue Tracker", "https://github.com/pallets/secure-cookie/issues/"
        ),
    ]
}
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html"],
}
singlehtml_sidebars = {"index": ["project.html", "localtoc.html"]}
html_title = "secure-cookie Documentation ({})".format(version)
html_show_sourcelink = False

# LaTeX ----------------------------------------------------------------

latex_documents = [
    (master_doc, "secure-cookie-{}.tex".format(version), html_title, author, "manual")
]
