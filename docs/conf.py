# Use the sphinx-book-theme (similar to d2l.ai)
html_theme = 'sphinx_book_theme'

# Enable markdown support
extensions = [
    'myst_parser',
    'sphinx.ext.mathjax',  # For math equations
    'sphinx.ext.autodoc',
    'sphinx_copybutton',   # Copy button for code blocks
]

# Configure the theme
html_theme_options = {
    "repository_url": "https://github.com/ywang-phy/GPU-Programming-using-CUDA-and-CPP",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_download_button": True,
}