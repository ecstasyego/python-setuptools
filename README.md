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
### Analysis
```python
import numpy as np
import pandas as pd
import sqlite3
import visdom

conn = sqlite3.connect(':memory:')
vis = visdom.Visdom()

pd.DataFrame(np.random.normal(size=(100, 5)), columns=list('ABCDE')).to_sql('TABLE01', conn, index=False)
pd.DataFrame(np.random.randint(0, 10, size=(100, 5)), columns=list('ABCDE')).map(lambda x: dict(enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))[x]).to_sql('TABLE02', conn, index=False)
dfs = pd.read_sql('select * from sqlite_master', conn)
df01 = pd.read_sql('select * from table01', conn)
df02 = pd.read_sql('select * from table02', conn)
display(dfs)

vis.line(df01.values, opts=dict(legend=df01.columns.tolist()))
vis.bar(df02['A'].value_counts().values, opts=dict(rownames=df02['A'].value_counts().index.tolist()))

conn.close()
vis.close()
```
  
### Application
```python
import os, shutil
import numpy as np
import pandas as pd
import sqlite3
import visdom

if os.path.exists('sqlites'):
    shutil.rmtree('sqlites')
os.mkdir('sqlites')

conn = sqlite3.connect('sqlites/main.sqlite3')
vis = visdom.Visdom()

pd.DataFrame(np.random.normal(size=(100, 5)), columns=list('ABCDE')).to_sql('TABLE01', conn, index=False)
pd.DataFrame(np.random.randint(0, 10, size=(100, 5)), columns=list('ABCDE')).map(lambda x: dict(enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']))[x]).to_sql('TABLE02', conn, index=False)
dfs = pd.read_sql('select * from sqlite_master', conn)
df01 = pd.read_sql('select * from table01', conn)
df02 = pd.read_sql('select * from table02', conn)
display(dfs)

vis.line(df01.values, opts=dict(legend=df01.columns.tolist()))
vis.bar(df02['A'].value_counts().values, opts=dict(rownames=df02['A'].value_counts().index.tolist()))

conn.close()
vis.close()
```
  
### Visom
```bash
python -m visdom.server
```

```python
import numpy as np
import visdom

vis = visdom.Visdom()
vis.check_connection()
vis.get_env_list()
vis.server, vis.port

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

  
### SQLite

```python
import sqlite3
import numpy as np
import pandas as pd

conn = sqlite3.connect('databases.db')
conn.close()

conn = sqlite3.connect('database01.db')
pd.DataFrame(np.random.randint(0, 5, size=(30, 5)), columns=list('ABCDE')).map(lambda x: dict(enumerate(['a', 'b', 'c', 'd', 'e']))[x]).to_sql('TABLE01', conn, index=False)
pd.DataFrame(np.random.randint(0, 5, size=(30, 5)), columns=list('ABCDE')).map(lambda x: dict(enumerate(['a', 'b', 'c', 'd', 'e']))[x]).to_sql('TABLE02', conn, index=False)
pd.DataFrame(np.random.randint(0, 5, size=(30, 5)), columns=list('ABCDE')).map(lambda x: dict(enumerate(['a', 'b', 'c', 'd', 'e']))[x]).to_sql('TABLE03', conn, index=False)
conn.close()

conn = sqlite3.connect('database02.db')
pd.DataFrame(np.random.randint(0, 5, size=(30, 5)), columns=list('ABCDE')).map(lambda x: dict(enumerate(['a', 'b', 'c', 'd', 'e']))[x]).to_sql('TABLE04', conn, index=False)
pd.DataFrame(np.random.randint(0, 5, size=(30, 5)), columns=list('ABCDE')).map(lambda x: dict(enumerate(['a', 'b', 'c', 'd', 'e']))[x]).to_sql('TABLE05', conn, index=False)
pd.DataFrame(np.random.randint(0, 5, size=(30, 5)), columns=list('ABCDE')).map(lambda x: dict(enumerate(['a', 'b', 'c', 'd', 'e']))[x]).to_sql('TABLE06', conn, index=False)
conn.close()

conn = sqlite3.connect('database03.db')
pd.DataFrame(np.random.randint(0, 5, size=(30, 5)), columns=list('ABCDE')).map(lambda x: dict(enumerate(['a', 'b', 'c', 'd', 'e']))[x]).to_sql('TABLE07', conn, index=False)
pd.DataFrame(np.random.randint(0, 5, size=(30, 5)), columns=list('ABCDE')).map(lambda x: dict(enumerate(['a', 'b', 'c', 'd', 'e']))[x]).to_sql('TABLE08', conn, index=False)
pd.DataFrame(np.random.randint(0, 5, size=(30, 5)), columns=list('ABCDE')).map(lambda x: dict(enumerate(['a', 'b', 'c', 'd', 'e']))[x]).to_sql('TABLE09', conn, index=False)
conn.close()

conn = sqlite3.connect('databases.db')
conn.execute('ATTACH DATABASE "database01.db" AS db1')
conn.execute('ATTACH DATABASE "database02.db" AS db2')
conn.execute('ATTACH DATABASE "database03.db" AS db3')
pd.read_sql('select * from db1.sqlite_master', conn)
pd.read_sql('select * from db2.sqlite_master', conn)
pd.read_sql('select * from db3.sqlite_master', conn)
conn.close()
```


  
### Dash
```python
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)
app.title = "TITLE"
app.layout = dcc.Markdown("Hello, World!")

if __name__ == '__main__':
    app.run_server(host="127.0.0.1", port='8050', debug=True)
```

  
### PyQt5
```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget(self))
        self.setMenuBar(QtWidgets.QMenuBar(self))
        self.setStatusBar(QtWidgets.QStatusBar(self))
        QtCore.QMetaObject.connectSlotsByName(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
