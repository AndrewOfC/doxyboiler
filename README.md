[[_TOC_]]
# Overview
Python script to add 'boilerplate' [Doxygen](http://www.doxygen.nl/) comments to header files [en masse](https://en.wiktionary.org/wiki/en_masse) using the [CppHeaderParser](https://pypi.org/project/CppHeaderParser/).  

Comments are formatted using [jinja2](http://jinja.pocoo.org/) templates.

# Goal 
Produce a pypi package installable via pip/virtualenv

# Usage (proposal)


```bash
$ doxyboiler.py [options...] files
```
| Option         | Value/Effect |
| --------------- | --------------- |
| -v|increase verbosity.<br><br>Once, count of insertertions.<br>Twice, each insertion listed<br>Three, text of comments applied|
| --templates *dir*       | template file directory to use|
| --copy-templates *dir*|copy default templates to *dir*<br><br>Templates may then be customized and used with the --templates option|

# Project Setup
```bash
$ git clone https://github.com/AndrewOfC/doxyboiler.git
$ cd doxyboiler
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

# Notes
# Examples

[Before&After](docs/before_and_after.md)

# References 

* [CppHeaderParser](https://pypi.org/project/CppHeaderParser/)
* [Doxygen](http://www.doxygen.nl/)
* [Jinja2](http://jinja.pocoo.org/)