#!/usr/bin/env sh 
set -e

(
    cd "${PROJECT_ROOT:-.}"
    curl --parallel --location \
    https://github.com/github/gitignore/raw/HEAD/{Python,C,C++,CMake,Global/{Linux,Windows,macOS,Vim,SublimeText,VisualStudioCode}}.gitignore \
    https://github.com/scikit-build/scikit-build-sample-projects/raw/master/.gitignore \
    > .gitignore
)
