#Python Project Generator
Pynew is a simple script that allows user to generate python project folder structure using one line.

```
$ pynew Project
```

```
Project/
|-- bin/
|   |-- project
|
|-- project/
|   |-- test/
|   |   |-- __init__.py
|   |
|   |-- __init__.py
|   |-- main.py
|
|-- docs/
|
|-- setup.py
```

#Installation
Symlink the script in `/bin` to your `~/bin/`

```
$ ln -s where_you_keep_your_pynew_dir/bin/pynew ~/bin/pynew
```
This allows you to use the script in most personal directories

#License
This project is released under the [MIT License](http://opensource.org/licenses/MIT)
