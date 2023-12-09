import setuptools
import skbuild


# TODO
# git checkout v23.2.0



skbuild.setup(
    name='energyplus',
    version='0.1.0a0',
    description='EnergyPlus with Python Bindings',
    python_requires='>=3.8',

    package_dir={'': 'packages'},
    packages=['energyplus'],
    package_data={'energyplus': ['**/*']},

    install_requires=[],
    extras_require={
        'dev': []
    },

    cmake_install_dir='./packages/energyplus/lib/',
    # TODO
    #cmake_install_target='energyplusapi',
    cmake_source_dir='./resources/EnergyPlus',
    cmake_args=[
        # NOTE required for pyenergyplus
        '-DBUILD_PACKAGE:BOOL=ON',
        #'--target', 'energyplusapi'


        '-DCMAKE_BUILD_TYPE:STRING=Release',
        '-DBUILD_FORTRAN:BOOL=OFF', 
        '-DDOCUMENTATION_BUILD:STRING=DoNotBuild',
        '-DOPENGL_REQUIRED:BOOL=OFF',
    ],
)