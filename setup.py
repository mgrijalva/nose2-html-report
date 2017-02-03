from setuptools import setup

setup(
    name='nose2_html_report',
    packages=['nose2_html_report'],
    version='0.3.0',
    description='Generate an HTML report for your unit tests',
    long_description=open('README.md', 'r').read(),
    author='Michael Grijalva',
    author_email='michaelgrij@gmail.com',
    license='MIT',
    install_requires=['jinja2'],
    package_data={
        'nose2_html_report': ['templates/report.html']
    },
    url='https://github.com/mgrijalva/nose2-html-report',
    download_url='',
    keywords=['nose2', 'testing', 'reporting'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ]
)
