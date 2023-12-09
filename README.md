# energyplus-python

```sh
curl --parallel --location https://github.com/github/gitignore/raw/HEAD/{Python,Global/{Linux,Windows,macOS,Vim,SublimeText,VisualStudioCode}}.gitignore https://github.com/scikit-build/scikit-build-sample-projects/raw/master/.gitignore > .gitignore
```

## Usage
```
from energyplus import pyenergyplus
```


## Build

```
# SKBUILD_CONFIGURE_OPTIONS='-DCMAKE_BUILD_TYPE:STRING=Release'
# SKBUILD_BUILD_OPTIONS=''


git submodule update --init --recursive

(
cd resources/EnergyPlus
git fetch --tags
git checkout tags/v23.2.0
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