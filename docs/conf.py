# Use the sphinx-book-theme (similar to d2l.ai)
html_theme = 'sphinx_book_theme'


extensions = [
    'myst_parser',
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx_copybutton',
]

# Optional: Configure MyST to support more markdown features
myst_enable_extensions = [
    "dollarmath",      # For $math$ syntax
    "amsmath",         # For advanced math
    "deflist",         # Definition lists
    "colon_fence",     # ::: fences
]

# Configure the theme
html_theme_options = {
    "repository_url": "https://github.com/ywang-phy/GPU-Programming-using-CUDA-and-CPP",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_download_button": True,
}