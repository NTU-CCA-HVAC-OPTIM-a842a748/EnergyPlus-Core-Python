# scripts
Maintenance Scripts

## Directory
- `resources/EnergyPlus/update_release.sh` \
    Use this script to bump submodule `resources/EnergyPlus`
    to a specific (or latest) `git`-tagged version.

    Environment Variables:
    - `RELEASE_TAG`: to make sure only the specified version
    (instead of the latest) gets checked out.
    - `PROJECT_ROOT`: to specify the project root 
    (`..` is relative to this file).

    Example (run this from where I am at):
    ```sh 
    PROJECT_ROOT=.. RELEASE_TAG=v23.2.0 \
    sh scripts/resources/EnergyPlus/update_release.sh
    ```

- `scripts/generate_gitignore.sh` \
    Use this script to update the `.gitignore` file.

    Environment Variables:
    - `PROJECT_ROOT`: see above.

    Example (run this from where I am at):
    ```sh 
    PROJECT_ROOT=.. \
    sh scripts/generate_gitignore.sh
    ```