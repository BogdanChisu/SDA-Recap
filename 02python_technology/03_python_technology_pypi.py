"""
----------------
What is PyPi?
----------------

PyPI = Python Package Index

Simply, PyPi is the place from which the programmer - using the pip install
command, is able to  download any library (of course if such a library
exists).

----------------------------
Project Registration in PyPI
----------------------------

The setuptools library
The setup.py file,
The MANIFEST.in file,
The README file,
the twine tool

setuptools
-----------

setuptools is a library that makes it possible to properly package your
bundle of software and prepare it for sending to the server. According to
the information on website, the finished product is easy to download, build,
install, update and be removed.

In setuptools there are several important functions that make package
construction possible and easier:

- setup() - a function that collects information about a package and
   modules,
- find_packages() -the search function for python packages. It allows the
user to specify which packages should go to the software bundle and which
not. By default the entire directory is appended (including subdirectories).

Functions from the setuptools library can be used in a special file called
the setup.py.

The setup.py file
------------------

The setup.py file is the entry to the script that builds the package which
will be shared. Therefore, it is necessary to call the two functions
discused above.
The main block is the setup call with arguments determining the project data
and metadata. the most important information about the created package is
passed through arguments:

- name: parameter name(required!)
    It is the name under which our library will be visible in PyPI. Note:
    the name cannot be duplicate; due to the large number of libraries in
    PyPI, sometimes it is not easy to find the right, unique name.
- version: parameter version (required!)
    Current package version; any versioning method: v.0.0.1, ver.01, etc.
- shared packages within the project: parameter packages (required!)
    These are packages created for our program that we want to include in
    the library before sending it to the server. Please note that if
    important source elements are omitted, the package after being
    downloaded by pip will not be able to work properly. Most often,
    the argument is the value returned by the function find_packages. You
    can use it to include or exclude selected packages. If you call the
    function without parameters, the entire directory will be included in
    the package from the level where the setup.py file is located.
    What to remove from the project? For example, folders containing
    tests - no one needs to view them.
- license: parameter license,
- short description: parameter description
    A brief description summarizing the purpose and functionality of the
    created package.
- author: parameter author
    You can enter your name, team or company name where the project was
    created.
- information about external libraries used in the project: parameter
    install_requires. An important parameter. If our program is advanced,
    it probably uses the downloaded libraries and is unable to work without
    them. By providing a list with package names as the argument, we will
    contribute to the fact that if someone downloads our package and
    installs with the pip install command, other required libraries will
    also be automatically downloaded
- information on whether the project also contains other non-source files in
    Python: use parameter: include_package_data

https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords

-----------------
File MANIFEST.in
-----------------

Sometimes it is important to attach files to the library that do not contain
source code. Such files can be:
- text files with documentation
- data files in various formats(.xml, .csv, .json)
- configuration files

To inform the setup function from the setup.py file that there are files
other that the .py extension ones that should be included in the package,
you must create a file called MANIFEST.in. The file specifies the rules for
attaching individual files using the include keyword.

include README.rst
# include a readme file in the same directory as MANIFEST.in

include docs/* .txt
# include text files from the docs directory

include funniest/data.json
# include data.json from the funniest directory

The manifest file is essentially a table of contents. It is worth
remembering that if a file is not found, it will not be accepted into the
package. To order the setup function to read such a file, call it by adding
an include_package_data=True argument.

README file
-------------

The README is the documentation of our prgram made available to anyone who
wants to download our library. The content of the file may encourage
outsiders to try our product. When our package is registered in PyPI,
it will get its own website, and its content will be the content of the
README file. Due to the fact that the README file is not Python code,
it must be included in the MANIFEST.in file.

README can be written in two formats:
rst - reStructuredText - it will be called README.rst or
md - Markdown - it will be called README.md

Both formats allow you to create rich content and formatting - adding links,
paragraphs, graphics, but Markdown is much more popular and is the
recommended format.

Uploading files to PyPI
--------------------------

twine is a tools for publishing Python packages. If the package has a proper
structure with all required files, it can be registered in PyPI.

An example of the root directory structure may look like the one below:

top
|--package
|   |-- __initi__.py
|   |-- module.py
|   '-- things
|       |-- cross.png
|       |-- fplogo.png
|       |-- tick.png
|-- runner
|-- MANIFEST.in
|--README
|--setup.py

All required sources are in the <top> directory:
    - the README file
    - MANIFEST.in
    - README
    - setup.py

Now, all you have to do is register the project in PyPI using the twine
tool.

Registering the package in PyPI
-------------------------------

Registering a package (which already has the required structure) is a
three-step process:
    1. Create an account on https://pypi.org/account/register
    2. Use the setup tools library in connection with the suplemented
    setup.py file and execute the command:
        python setup.py sdist
        - A package will be created.
        - The package will be saved in the dist directory and will have the
        archive format with the extension .tar.gz
        - The package name will be the project name with the suffix version
    3. Having generated the package, you can share it globally with the
    twine tool, using the commanf:
    twine upload dist/project_name-0.1.0.tar.gz

    twine in the meantime asks for PyPI login details and if everyhting is
    okay sends and registers our package. From now on, the package can be
    installed on any computer using the pip tool.
"""