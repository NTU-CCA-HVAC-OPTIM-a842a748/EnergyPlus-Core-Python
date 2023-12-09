#!/usr/bin/env sh
set -e

(
    cd "${PROJECT_ROOT:-./}/resources/EnergyPlus"
    git fetch --tags
    git checkout tags/${RELEASE_TAG:-$(git describe --tags `git rev-list --tags --max-count=1`)}
)
