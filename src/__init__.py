# entire project development will be inside this folder and also basically when ever find_packages is called in setup.py
# it will look for __init__.py and try to build it ,( like we could just install it as seaborn but for that we need to install this to pypi)
# if any new folder is created within there also __init__.py will be created so that it can also be used/build