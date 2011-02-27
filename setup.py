from setuptools import setup, find_packages

setup(
    name='django-modeltranslation',
    version='0.2.0.2',
    description='Translates Django models using a registration approach.',
    author='Peter Eschler, Dirk Eschler',
    author_email='peschler@googlemail.com, eschler@gmail.com',
    url='http://code.google.com/p/django-modeltranslation/',
    packages=find_packages(),
    zip_safe=False,
    package_dir={'modeltranslation': 'modeltranslation'},
    package_data = {
        'modeltranslation': [
            'static/css/*.css',
            'static/js/*.js',
        ],
    },
    license='New BSD'
)
