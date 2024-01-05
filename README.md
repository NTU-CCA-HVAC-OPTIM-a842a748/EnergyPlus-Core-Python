# EnergyPlus-Python

## Installation
```sh
python3 -m pip install --extra-index-url https://test.pypi.org/simple energyplus-core
```

## Directory
- `resources/EnergyPlus`
  EnergyPlus base repository

## Usage
```
from energyplus.core import pyenergyplus
```

## Development
- Clone the current repo
- Clone the submodules
```sh
git submodule update --init --recursive
```
- (Optional) Update `resources/EnergyPlus` to latest tagged release
```sh
sh scripts/resources/EnergyPlus/update_release.sh
```
- Package (Minimal wheel)
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
#python3 -m build .
#python3 -m pip install .
```
- (Optional) Bump version
```sh
git tag -a v0.1.0.dev0
# check tagged version
python -m setuptools_scm
git push --follow-tags
```