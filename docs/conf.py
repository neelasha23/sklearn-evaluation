import os
import requests


def get_pr(owner, repo, number):
    """Get pull request information"""
    return requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{number}",
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    ).json()


def get_repo_and_branch_for_pr(owner, repo, number):
    """Return the fork repo and branch branch for a given pull request number"""
    response = get_pr(owner, repo, number)
    full_name = response["head"]["repo"]["full_name"]
    ref = response["head"]["ref"]
    url = f"https://github.com/{full_name}"
    return url, ref


# TODO: handle the "stable" case
DEFAULT = "master"
version_name = os.environ.get("READTHEDOCS_VERSION_NAME", DEFAULT)

if version_name == "latest":
    version_name = DEFAULT

print(f"Version: {version_name}")


try:
    int(version_name)
except ValueError:
    repository_url = "https://github.com/ploomber/sklearn-evaluation"
    repository_branch = version_name
else:
    repository_url, repository_branch = get_repo_and_branch_for_pr(
        "ploomber", "sklearn-evaluation", version_name
    )


print(f"URL: {repository_url}. Branch: {repository_branch}")


###############################################################################
# Auto-generated by `jupyter-book config`
# If you wish to continue using _config.yml, make edits to that file and
# re-generate this one.
###############################################################################
author = "Ploomber"
comments_config = {"hypothesis": False, "utterances": False}
copyright = "2023"
exclude_patterns = ["README.md"]
execution_allow_errors = False
execution_excludepatterns = []
execution_in_temp = True
execution_show_tb = True
execution_timeout = 30
extensions = [
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "myst_nb",
    "jupyter_book",
    "sphinx_thebe",
    "sphinx_comments",
    "sphinx_external_toc",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx_book_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "matplotlib.sphinxext.plot_directive",
    "sphinx_jupyterbook_latex",
]
external_toc_exclude_missing = True
external_toc_path = "_toc.yml"
html_baseurl = ""
html_favicon = ""
html_logo = "logo.jpeg"
html_show_copyright = True
html_sourcelink_suffix = ""
html_theme = "sphinx_book_theme"
html_theme_options = {
    "search_bar_text": "Search this book...",
    "launch_buttons": {
        "notebook_interface": "jupyterlab",
        "binderhub_url": "https://binder.ploomber.io",
        "jupyterhub_url": "",
        "thebe": False,
        "colab_url": "",
    },
    "path_to_docs": "docs",
    "repository_url": repository_url,
    "repository_branch": repository_branch,
    "google_analytics_id": "G-3KL9PSJBZZ",
    "extra_navbar": 'Join us on <a href="https://ploomber.io/community/">Slack!</a>',
    "extra_footer": "",
    "home_page_in_toc": True,
    "announcement": "To launch any tutorial in JupyterLab, click on the 🚀 button below!",
    "use_repository_button": True,
    "use_edit_page_button": False,
    "use_issues_button": True,
}
html_title = "sklearn-evaluation"
intersphinx_mapping = {
    "sklearn": ["http://scikit-learn.org/stable", None],
    "matplotlib": ["http://matplotlib.org/", None],
}
jupyter_cache = ""
jupyter_execute_notebooks = "auto"
latex_engine = "pdflatex"
myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "linkify",
    "substitution",
    "tasklist",
]
myst_url_schemes = ["mailto", "http", "https"]
nb_output_stderr = "show"
numfig = True
plot_html_show_formats = False
plot_html_show_source_link = False
plot_include_source = True
pygments_style = "sphinx"
suppress_warnings = ["myst.domains", "myst.header"]
use_jupyterbook_latex = True
use_multitoc_numbering = True