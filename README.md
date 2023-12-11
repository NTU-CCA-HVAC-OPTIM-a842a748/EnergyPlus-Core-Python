# energyplus-python


## Usage
```
from energyplus_core import pyenergyplus
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
SKBUILD_CMAKE_VERBOSE=true \
SKBUILD_LOGGING_LEVEL="DEBUG" \
SKBUILD_CONFIGURE_OPTIONS='
  --log-level=TRACE
  -D CMAKE_BUILD_TYPE:STRING=Release
  -D BUILD_FORTRAN:BOOL=OFF
  -D DOCUMENTATION_BUILD:STRING=DoNotBuild
  -D OPENGL_REQUIRED:BOOL=OFF
' \
SKBUILD_BUILD_OPTIONS='' \
python3 -m build . --config-setting=--quiet
#python3 -m install .
```


```
# SKBUILD_CONFIGURE_OPTIONS='-DCMAKE_BUILD_TYPE:STRING=Release'
# SKBUILD_BUILD_OPTIONS=''


git submodule update --init --recursive

(
cd resources/EnergyPlus
git fetch --tags
git checkout tags/v23.2.0
git checkout tags/$(git describe --tags `git rev-list --tags --max-count=1`)
)

pip install . -v

python3 setup.py sdist bdist_wheel
```




TODO ref https://scikit-build.readthedocs.io/en/latest/usage.html#environment-variable-configuration

`SKBUILD_CONFIGURE_OPTIONS`/`CMAKE_ARGS`

This will add configuration options when configuring CMake. `SKBUILD_CONFIGURE_OPTIONS` will be used instead of `CMAKE_ARGS` if both are defined.

`SKBUILD_BUILD_OPTIONS`
Pass options to the build.

```
cmake -DCMAKE_BUILD_TYPE:STRING=$BUILD_TYPE \
    -DLINK_WITH_PYTHON:BOOL=ON -DPython_REQUIRED_VERSION:STRING=${{ steps.setup-python.outputs.python-version }} \
    -DPython_ROOT_DIR:PATH=$RUNNER_TOOL_CACHE/Python/${{ steps.setup-python.outputs.python-version }}/x64/ \
    -DBUILD_FORTRAN:BOOL=ON -DBUILD_PACKAGE:BOOL=ON \
    -DDOCUMENTATION_BUILD:STRING="BuildWithAll" -DTEX_INTERACTION:STRING="batchmode" -DENABLE_PCH:BOOL=OFF \



 BUILD_FORTRAN                    OFF
 BUILD_PACKAGE                    OFF
 BUILD_TESTING                    OFF
 CMAKE_BUILD_TYPE                 Release
 DOCUMENTATION_BUILD              DoNotBuild
 ENABLE_COVERAGE                  OFF
 ENABLE_PCH                       ON
 ENABLE_UNITY                     OFF
 LINK_WITH_PYTHON                 OFF
 OPENGL_REQUIRED                  OFF
 penumbra_COVERAGE                OFF


 target energyplusapi
```





TODO
```

    - name: Build Package
      working-directory: ./build
      shell: bash
      run: cmake --build . --target package -j 2

    - name: Upload Tarball to release
      uses: svenstaro/upload-release-action@v2
      with:
        repo_token: ${{ secrets.GITHUB_TOKEN }}
        file: build/EnergyPlus-*-x86_64.tar.gz
        tag: ${{ github.ref }}
        overwrite: true
        file_glob: true

    - name: Upload IFW to release
      uses: svenstaro/upload-release-action@v2
      with:
        repo_token: ${{ secrets.GITHUB_TOKEN }}
        file: build/EnergyPlus-*-x86_64.run
        tag: ${{ github.ref }}
        overwrite: true
        file_glob: true

    - name: Upload SH to release
      uses: svenstaro/upload-release-action@v2
      with:
        repo_token: ${{ secrets.GITHUB_TOKEN }}
        file: build/EnergyPlus-*-x86_64.sh
        tag: ${{ github.ref }}
        overwrite: true
        file_glob: true
        asset_name: ${{ matrix.os }}_LinuxShellInstaller

```



```

    - name: Archive packages (wheels)
      uses: actions/upload-artifact@v3
      with:
        name: wheels
        path: ${{ steps.packaging.outputs.files_wheels }}
        if-no-files-found: error

```


```
    - name: TODO Create GitHub Release
      id: create-release
      uses: softprops/action-gh-release@v1
      with:
        files: dist/*
        token: ${{ secrets.GITHUB_TOKEN }}
        release_name: Release ${{ github.event.after }}

    #- name: TODO Publish to PyPI
    #  uses: pypa/gh-action-pypi-publish@v2
    #  with:
    #    user: __token__
    #    password: ${{ secrets.PYPI_API_TOKEN }}

```


```
    - name: Setup tmate session
      uses: mxschmitt/action-tmate@v3
      with:
        detached: true
```