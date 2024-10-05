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
git branch -m main
git remote add origin https://github.com/ecstasyego/python-setuptools
git push -f origin main
```


</br></br></br>
## Visom
```bash
python -m visdom.server
```

```python
import numpy as np
import visdom

vis = visdom.Visdom()

# images
vis.images(np.random.normal(size=(300,500)), opts=dict(title='gray image'))
vis.images(np.random.normal(size=(300,500)), opts=dict(title='gray image', caption='description'))
vis.images(np.random.normal(size=(3, 300, 500)), opts=dict(title='color image'))
vis.images(np.random.normal(size=(3, 300, 500)), opts=dict(title='color image', caption='description'))
vis.images(np.random.normal(size=(5, 3, 300, 500)), opts=dict(title='images'))
vis.images(np.random.normal(size=(5, 3, 300, 500)), opts=dict(title='images', caption='description'))

# pie
vis.pie(np.array([10, 20, 30, 40, 50]), opts=dict(title='pie', legend=['legend1', 'legend2', 'legend3', 'legend4', 'legend5'], showlegend=True))

# bar
vis.bar(np.array([10, 20, 30, 40, 50]), opts=dict(title='bar', rownames=['label1', 'label2', 'label3', 'label4', 'label5'])) # 1d bar
vis.bar(np.array([10, 20, 30, 40, 50]), opts=dict(title='bar', legend=['legend1', 'legend2', 'legend3', 'legend4', 'legend5'], showlegend=True)) # 1d bar
vis.bar(np.random.randint(0, 100, size=(20,2)), opts=dict(title='bar')) # 2d bar
vis.bar(np.random.randint(0, 100, size=(20,2)), opts=dict(title='bar', legend=['legend1', 'legend2'])) # 2d bar
vis.bar(np.random.randint(0, 100, size=(20,2)), opts=dict(title='bar', legend=['legend1', 'legend2'], stacked=True)) # 2d bar


# line
vis.line(Y = np.random.normal(size=(10,2)), X = np.arange(10), opts=dict(title='line', legend=['legend1', 'legend2'], showlegend=True))

# scatter
vis.scatter(
    X = np.random.normal(size=(10,2)), 
    opts=dict(
        title='scatter', legend=['legend1', 'legend2'], showlegend=True,
        markersize=5
    )
)
vis.scatter(
    X = np.random.normal(size=(100, 2)), # 2d scatter 
    Y = np.random.randint(1, 6, size=(100,)),  # label: 1, 2, 3, 4, 5
    opts=dict(
        title='scatter', legend=['legend1', 'legend2', 'legend3', 'legend4', 'legend5'], showlegend=True,
        markersize = 5,
    )
)
vis.scatter(
    X = np.random.normal(size=(100, 3)), # 3d scatter
    Y = np.random.randint(1, 6, size=(100,)),  # label: 1, 2, 3, 4, 5
    opts=dict(
        title='scatter', legend=['legend1', 'legend2', 'legend3', 'legend4', 'legend5'], showlegend=True,
        markersize = 5,
    )
)

vis.close()
```



