from distutils.core import setup, Extension, DEBUG

sfc_module = Extension('CPSintolSDK', sources = ['Module.cpp'])

setup(name = 'CPSintolSDK', version = '1.0',
    description = 'Python Package with CPSintolSDK C++ extension',
    ext_modules = [sfc_module]
    )