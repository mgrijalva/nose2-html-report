# Nose2 HTML Report
[![Build Status](https://travis-ci.org/mgrijalva/nose2-html-report.svg?branch=master)](https://travis-ci.org/mgrijalva/nose2-html-report)
[![Coverage Status](https://coveralls.io/repos/github/mgrijalva/nose2-html-report/badge.svg?branch=master)](https://coveralls.io/github/mgrijalva/nose2-html-report?branch=master)

### Installation
You can install the Nose2 HTML Report Plugin using `pip`:
```
pip install nose2-html-report
```

### Configuration
To get `nose2` to recognize the plugin add an entry into the `plugin` key of the `unittest` section of your `nose2.cfg` file. Configurations for the plugin should be placed into an `html-report` section of the configuration file. Below is a working example:
```
[unittest]
plugins = nose2_html_report.html_report

[html-report]
always-on = True
```

### Usage
Command line flag:
```
nose2 --html-report
```

If configured via `nose2.cfg`:
```
nose2
```
