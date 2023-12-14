# EnergyPlus-Python


## Directory
- `resources/EnergyPlus`
  EnergyPlus base repository

## Usage
```
from energyplus.core import pyenergyplus
```

## Setup
```sh
git submodule update --init --recursive
```

## 
```sh
sh scripts/resources/EnergyPlus/update_release.sh
```

## Build
```sh
#SKBUILD_CMAKE_VERBOSE=true \
SKBUILD_LOGGING_LEVEL="DEBUG" \
SKBUILD_BUILD_DIR='build/{wheel_tag}' \
SKBUILD_CMAKE_ARGS='
  -D CMAKE_BUILD_TYPE:STRING=Release;
  -D BUILD_FORTRAN:BOOL=OFF;
  -D DOCUMENTATION_BUILD:STRING=DoNotBuild;
  -D OPENGL_REQUIRED:BOOL=OFF;
' \
python3 -m build . --wheel
#python3 -m pip install .
```

TODO ref https://scikit-build.readthedocs.io/en/latest/usage.html#environment-variable-configuration


```
    - name: Setup tmate session
      uses: mxschmitt/action-tmate@v3
      with:
        detached: true
```

## Versioning

https://www.moritzkoerber.com/posts/versioning-with-setuptools_scm/


## TODOs

https://github.com/pypa/gh-action-pypi-publish/discussions/15

```
git add . 
git commit -m sync
git tag -a v0.1.0.dev0
python -m setuptools_scm
git push --follow-tags
```