# Nose2 HTML Report
[![Build Status](https://travis-ci.org/mgrijalva/nose2-html-report.svg?branch=master)](https://travis-ci.org/mgrijalva/nose2-html-report)
[![Coverage Status](https://coveralls.io/repos/github/mgrijalva/nose2-html-report/badge.svg?branch=master)](https://coveralls.io/github/mgrijalva/nose2-html-report?branch=master)

### Introduction
A [nose2](https://github.com/nose-devs/nose2) plugin for generating searchable HTML reports of your test results.
- docstrings from tests are captured as test descriptions
- if a test fails, the traceback will be captured in the report
- report is searchable and filterable by passed/failed/error/etc.

![Report Screenshot](https://raw.githubusercontent.com/mgrijalva/nose2-html-report/master/docs/images/report.png)

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

#### Additional Settings
Specify the path for the HTML report. Defaults to `report.html`
```
[unittest]
plugins = nose2_html_report.html_report

[html-report]
always-on = True
path = test_results/my_custom_report_file.html
```

### Usage
Command line flag:
```
nose2 --html-report
```

If you have `always-on=True` inside your `nose2.cfg`:
```
nose2
```

### Contributing
This is a small side project of mine. Feel free to submit any pull requests.
