# Able by M.I.L.K.D

This is the repo for the CSC 4110 Project, Able, by team M.I.L.K.D.

### Prerequisites

Required Software and Libraries

```
-Python 3.7.3
-Flask
-Flask-BootStrap
-Flask-SQLAlchemy
-Flask-WTF
-Flask-Migrate
-Flask-Login
```

You may also find all installed packages in the venv we used in requirements.txt

Installing
--------------------------------------------

### Using PyCharm

Create a new Python project from this repo. You will then need to use pip to install all the necessary libraries.

##### It is highly recommended to install the PyCharm Professional edition and use your .edu email for registration so you have access to Flask configurations. The Community edition may not work correctly if setting up the Flask configuration from scratch  ####

```
This is to be done from the python console in PyCharm or follow the alternative method below
---------------------------------------------------------------------------------------------
pip install Flask
pip install Flask-BootStrap
pip install Flask-SQLAlchemy
pip install Flask-WTF
pip install Flask-Migrate
pip install Flask-Login
```

An alternative to using the console is to go file > settings > Project:<projName> > Project interpreter
  From here you can click the '+' on the right side of the pane and search for the library
  Click 'Install Package' when you have the correct one selected
  
You may also use the command "pip install -r requirements.txt" from the console in PyCharm to automatically install all listed packages.

##### Make sure your configuration script path is pointing to 'able.py' when you run the program and set for flask. This can be done by selecting the 'edit configurations' option in the top right next to the 'run' button.

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [BootStrap](https://getbootstrap.com/) - An HTML and CSS library that makes designing web pages simple
* [PyCharm](https://www.jetbrains.com/pycharm/) - A sleek and powerful IDE by JetBrains for Python development
