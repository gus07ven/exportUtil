ExportUtil
==========

CLI for exporting users to stdout or a specific file path in JSON or CSV format.

Usage
-----

Pass in the path and format in which you want your users to be exported.

Example:


``$ hr --path=/src/test.txt --format=JSON      # To print to a specific file``


``$ hr --format=CSV                            # To print to a standard output``


Installation From Source
------------------------

To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:

``$ pip install --user -e .``


Preparing for Development
-------------------------

Follow these steps to start developing with this project:

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository: ``git clone git@github.com:gus07ven/exportUtil``
3. ``cd`` into the repository
4. Activate virtualenv: ``pipenv shell``
5. Install dependencies: ``pipenv install``