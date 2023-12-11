import skbuild


# TODO FIXME windows https://github.com/scikit-build/scikit-build/blob/9787cc2582311f731b3d0411b1175bd852db2ad6/skbuild/platform_specifics/abstract.py#L64

skbuild.setup(
    #name='energyplus',
    #version='0.1.0a0',
    #description='EnergyPlus with Python Bindings',
    #python_requires='>=3.8',

    package_dir={'': 'packages'},
    packages=['energyplus_core'],
    package_data={'energyplus_core': ['**/*']},

    #install_requires=[],
    #extras_require={
    #    'dev': []
    #},
    use_scm_version=True,
    setup_requires=[ 
        'setuptools_scm'
    ],

    cmake_install_dir='./packages/energyplus_core/lib/',
    cmake_source_dir='./resources/EnergyPlus',
    cmake_args=[
        # NOTE required for pyenergyplus
        '-DBUILD_PACKAGE:BOOL=ON',
    ],
)