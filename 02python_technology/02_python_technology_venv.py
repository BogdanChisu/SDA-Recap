
"""
------------------------------
VIRTUAL ENVIRONMENTS IN PYTHON
------------------------------

Due to the huge number of packages that perform various tasks, developers
have divided them in two categories:
- Internal or standard libraries
- external libraries:
    Windows - \Lib\site-packages
    Linux   - /site-packages
The location of the above mentioned directories is in the Python root folder

-------------------
Virtual Environment
-------------------

The main purpose od Python's virtual environment is to create an isolated
library space for ongoing projects. This means that each project can have
its own dependencies, regardless of which packages are used in parallel.

By default, pup will install packages globally for the entire system. And in
most cases this is not the desired action.

In order to separate one project from another, it is necessary to create
environments for each solution.

basic operations: installation
------------------------------

pip install virtualenv

basic operation: creation
-------------------------

Windows:     python -m venv <environment_name>
Linux / iOS: virtualenv <environment_name>

Structure of the venv in Windows:

-bin/Scripts     - contains the files that interact with the virtual
                   environment
                   (e.g. a script to activate the environment)
-include/Include - C language code files for compiling packages,
-lib/Lib         - copy of the site-packages folder

The most common way to name virtual environments is to simply give it the
name <<venv>> so that every programmer will recognize its folder.
It is recommended to execute the environment command (adding a new directory as
a result)d in the main folder of the project in which it is created.

basic operation: activation
---------------------------

Windows:   c:\path\to\environment\Scripts\activate.bat
Linux/iOS: source ./path/to/environment/bin/activate

basic operation: library installation
-------------------------------------

Once we're  in a virtual environment, we can install packages using the pip
tool. All features of this tool are allowed.

basic operation: deactivation:
------------------------------

deactivate

virtualenvwrapper
-----------------

virtualenvwrapper is a package that wraps the virtual environments tool. It
maintains virtualenv functionality but additionally organizes folders and
access to environments, and facilitates the most common operations peformed
in virtual environments.

virtualenvwrapper - installation
-----------------------------------
Windows - pip install virtualenvwrapper-win

Linux:
- pip install virtualenvwrapper
- source virtualenvwrapper.sh for access to the commands provided by the tool
- source ~/.bashrc -reloading the startup file

virtualenvwrapper - creation
-----------------------------

mkvirtualenv <environment_name>

virtualenvwrapper chooses the location for virtual environments by itself -
it is the hidden directory .virtualenvs, located in the home folder.

this location can be configured using the WORKON_HOME environment variable.

basic operations: activation
----------------------------

workon: <environment_name>

basic operations: deactivation
-------------------------------

leaving the environment is the same as for virtualenv:
deactivate

virtualenvwrapper - additional operations
-----------------------------------------
- lsvirtualenv - prints all environments created with the virtualenvwrapper
- rmvirtualenv <environment_name> - removes the virtual environment with the
   name specified
"""