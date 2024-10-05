# python-setuptools

**Directory Structure**
```
.python-setuptools
├── README.md
├── requirements.txt
├── setup.py
├── package
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   └── module.cpython-312.pyc
│   └── module.py
├── PackageName.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
├── build
│   ├── bdist.linux-x86_64
│   └── lib
│       └── package
│           ├── __init__.py
│           └── module.py
└── dist
    ├── PackageName-0.0.1-py3-none-any.whl
    └── packagename-0.0.1.tar.gz
```
  
**BUILD**: build, dist
```bash
$ python setup.py sdist bdist_wheel
```
  
**INSTALL**: PackageName.egg-info
```bash
$ pip install -e . 
$ pip install -e .[interactive]
$ pip show PackageName
```
```python
import package
from package import module

package.module.function()
module.function()
```
  
**DISTRIBUTION**
```bash
$ twine upload dist/*
```

**UNINSTALLATION**
```bash
$ pip uninstall PackageName
```


<br/><br/><br/>
## Build 
`setup.py`   
```python
from setuptools import setup, find_packages

setup(
    name='PackageName',
    version='0.0.1',
    packages=find_packages(include=['python-setuptools', 'python-setuptools.*'])
)
```
```bash
python setup.py install
python setup.py develop
```

### setup.py
```python
from setuptools import setup, find_packages

setup(
    name='package',
    version='0.1.0',
    packages=find_packages(include=['python-setuptools', 'python-setuptools.*']),
    install_requires=[
        'pandas==0.23.3',
        'numpy>=1.14.5',
        'matplotlib>=2.2.0',
        'jupyter'],
    extras_require={
        'interactive': [
            'matplotlib>=2.2.0',
            'jupyter'],
    }
)
```


### requirements.py
```bash
pandas==0.23.3
numpy==1.14.5
matplotlib==2.2.0
...
```
```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```


</br></br></br>
## Git
```bash
git init
git add .
git commit -m "initialize"
git remote add origin https://github.com/ecstasyego/python-setuptools
git push -f origin main
```
