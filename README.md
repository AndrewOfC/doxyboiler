[[_TOC_]]
# Overview
Python script to add 'boilerplate' [Doxygen](http://www.doxygen.nl/) comments to header files [en masse](https://en.wiktionary.org/wiki/en_masse) using the [CppHeaderParser](https://pypi.org/project/CppHeaderParser/)

# Goal 
Produce a pypi package installable via pip/virtualenv

# Usage (proposal)


```bash
$ doxyboiler [options...] directories_or_files
```
| Option | Value/Effect |
| --------- | --------------- |
| -r        | Descend recursively |

# Project Setup
```bash
$ git clone https://github.com/AndrewOfC/doxyboiler.git
$ cd doxyboiler
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

# Notes
## Python2 vs Python3
On a related project I was having an issue using jinja2 templates with python3.   for loops in templates were not iterating as expected.   If it occurs here, I'm going to pin it down and write it up.

# References 

* [CppHeaderParser](https://pypi.org/project/CppHeaderParser/)
* [Doxygen](http://www.doxygen.nl/)