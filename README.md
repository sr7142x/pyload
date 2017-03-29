<p align="center"><a href="https://pyload.net"><img src="/media/banner.png" alt="pyLoad" /></a></p>

**pyLoad** is the Free and Open Source download manager written in Pure Python
and designed to be extremely lightweight, fully customizable and remotely
manageable.


[![Build Status](https://travis-ci.org/pyload/pyload.svg?branch=master)](https://travis-ci.org/pyload/pyload)
[![Requirements Status](https://requires.io/github/pyload/pyload/requirements.svg?branch=master)](https://requires.io/github/pyload/pyload/requirements/?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/pyload/pyload/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/pyload/pyload/?branch=master)[![CLA assistant](https://cla-assistant.io/readme/badge/pyload/pyload)](https://cla-assistant.io/pyload/pyload)
[![Coverage Status](https://coveralls.io/repos/github/pyload/pyload/badge.svg)](https://coveralls.io/github/pyload/pyload)
[![PyPI](https://img.shields.io/pypi/status/pyload.core.svg)](https://pypi.python.org/pypi/pyload.core)
[![PyPI](https://img.shields.io/pypi/v/pyload.core.svg)](https://pypi.python.org/pypi/pyload.core)
[![PyPI](https://img.shields.io/pypi/pyversions/pyload.core.svg)](https://pypi.python.org/pypi/pyload.core)

_**Contact Us** on:_

[![pyload.net](https://img.shields.io/badge/-pyload.net-orange.svg)](https://pyload.net)
[![Twitter](https://img.shields.io/badge/-twitter-429cd6.svg?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiA%2FPjwhRE9DVFlQRSBzdmcgIFBVQkxJQyAnLS8vVzNDLy9EVEQgU1ZHIDEuMC8vRU4nICAnaHR0cDovL3d3dy53My5vcmcvVFIvMjAwMS9SRUMtU1ZHLTIwMDEwOTA0L0RURC9zdmcxMC5kdGQnPjxzdmcgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMzIgMzIiIGhlaWdodD0iMzJweCIgaWQ9IkxheWVyXzEiIHZlcnNpb249IjEuMCIgdmlld0JveD0iMCAwIDMyIDMyIiB3aWR0aD0iMzJweCIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI%2BPHBhdGggZD0iTTMxLjk5Myw2LjA3N0MzMC44MTYsNi42LDI5LjU1Miw2Ljk1MywyOC4yMjMsNy4xMWMxLjM1NS0wLjgxMiwyLjM5Ni0yLjA5OCwyLjg4Ny0zLjYzICBjLTEuMjY5LDAuNzUxLTIuNjczLDEuMjk5LTQuMTY4LDEuNTkyQzI1Ljc0NCwzLjc5NywyNC4wMzgsMywyMi4xNDksM2MtMy42MjUsMC02LjU2MiwyLjkzOC02LjU2Miw2LjU2MyAgYzAsMC41MTQsMC4wNTcsMS4wMTYsMC4xNjksMS40OTZDMTAuMzAxLDEwLjc4NSw1LjQ2NSw4LjE3MiwyLjIyNyw0LjIwMWMtMC41NjQsMC45Ny0wLjg4OCwyLjA5Ny0wLjg4OCwzLjMgIGMwLDIuMjc4LDEuMTU5LDQuMjg2LDIuOTE5LDUuNDY0Yy0xLjA3NS0wLjAzNS0yLjA4Ny0wLjMyOS0yLjk3Mi0wLjgyMWMtMC4wMDEsMC4wMjctMC4wMDEsMC4wNTYtMC4wMDEsMC4wODIgIGMwLDMuMTgxLDIuMjYyLDUuODM0LDUuMjY1LDYuNDM3Yy0wLjU1LDAuMTQ5LTEuMTMsMC4yMy0xLjcyOSwwLjIzYy0wLjQyNCwwLTAuODM0LTAuMDQxLTEuMjM0LTAuMTE3ICBjMC44MzQsMi42MDYsMy4yNTksNC41MDQsNi4xMyw0LjU1OGMtMi4yNDUsMS43Ni01LjA3NSwyLjgxMS04LjE1LDIuODExYy0wLjUzLDAtMS4wNTMtMC4wMzEtMS41NjYtMC4wOTIgIEMyLjkwNSwyNy45MTMsNi4zNTUsMjksMTAuMDYyLDI5YzEyLjA3MiwwLDE4LjY3NS0xMC4wMDEsMTguNjc1LTE4LjY3NWMwLTAuMjg0LTAuMDA4LTAuNTY4LTAuMDItMC44NSAgQzMwLDguNTUsMzEuMTEyLDcuMzk1LDMxLjk5Myw2LjA3N3oiIGZpbGw9IiM1NUFDRUUiLz48Zy8%2BPGcvPjxnLz48Zy8%2BPGcvPjxnLz48L3N2Zz4%3D)](https://twitter.com/pyload)
[![Facebook](https://img.shields.io/badge/-facebook-3a589e.svg?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiA%2FPjwhRE9DVFlQRSBzdmcgIFBVQkxJQyAnLS8vVzNDLy9EVEQgU1ZHIDEuMC8vRU4nICAnaHR0cDovL3d3dy53My5vcmcvVFIvMjAwMS9SRUMtU1ZHLTIwMDEwOTA0L0RURC9zdmcxMC5kdGQnPjxzdmcgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMzIgMzIiIGhlaWdodD0iMzJweCIgaWQ9IkxheWVyXzEiIHZlcnNpb249IjEuMCIgdmlld0JveD0iMCAwIDMyIDMyIiB3aWR0aD0iMzJweCIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI%2BPGc%2BPHBhdGggZD0iTTMyLDMwYzAsMS4xMDQtMC44OTYsMi0yLDJIMmMtMS4xMDQsMC0yLTAuODk2LTItMlYyYzAtMS4xMDQsMC44OTYtMiwyLTJoMjhjMS4xMDQsMCwyLDAuODk2LDIsMlYzMHoiIGZpbGw9IiMzQjU5OTgiLz48cGF0aCBkPSJNMjIsMzJWMjBoNGwxLTVoLTV2LTJjMC0yLDEuMDAyLTMsMy0zaDJWNWMtMSwwLTIuMjQsMC00LDBjLTMuNjc1LDAtNiwyLjg4MS02LDd2M2gtNHY1aDR2MTJIMjJ6IiBmaWxsPSIjRkZGRkZGIiBpZD0iZiIvPjwvZz48Zy8%2BPGcvPjxnLz48Zy8%2BPGcvPjxnLz48L3N2Zz4%3D)](https://www.facebook.com/pyload)
[![Join the chat at https://gitter.im/pyload/pyload](https://badges.gitter.im/pyload/pyload.svg)](https://gitter.im/pyload/pyload?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![IRC Freenode](https://img.shields.io/badge/irc-freenode-lightgray.svg)](https://kiwiirc.com/client/irc.freenode.com/#pyload)


> **Notice:**
> [Master Branch](https://github.com/pyload/pyload/tree/master) is under
> heavy development, very unstable, often broken. **Do not use it for now!**
> Please, use the [Stable Branch](https://github.com/pyload/pyload/tree/stable)
> instead.


Table of contents
-----------------

- [Supported Platforms](#supported-platforms)
- [Dependencies](#dependencies)
  - [Supported Interpreters](#supported-interpreters)
  - [Required Packages](#required-packages)
  - [Optional Packages](#optional-packages)
  - [Test-suite Packages](#test-suite-packages)
- [Installation](#installation)
  - [PIP Install](#pip-install)
  - [Easy Install](#easy-install)
  - [Manually Install](#manually-install)
- [First Start](#first-start)
  - [Quick Start](#quick-start)
  - [Advanced Start](#advanced-start)
  - [Configuration](#configuration)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Script Usage](#script-usage)
- [Development](#development)
  - [Report an Issue](#report-an-issue)
  - [Submit a Code Contribution](#submit-a-code-contribution)
  - [Coding Guidelines](#coding-guidelines)
  - [~~Localization~~](#localization)
  - [~~Performances~~](#performances)
- [Licensing](#licensing)
  - [Main Program](#main-program)
  - [Plugins](#plugins)
- [Credits](#credits)
- [Release History](#release-history)


Supported Platforms
-------------------

**pyLoad** runs under **Windows**, **MacOS** and Unix based systems like **Linux** and **FreeBSD**.

> **Note:**
> Currently **MacOS** and **BSD** platforms are NOT fully supported, some features may be unstable
> or missing.

> **Note:**
> Embedded platforms, proprietary NAS and routers systems are NOT officially supported,
> **pyLoad** may be crash unexpectately or NOT work at all under them!


Dependencies
------------

You need at least *Python 2.6* or *Python 3.3* to run **pyLoad**
and all of its [required software dependencies](#required-packages).

All the dependencies should be automatically installed by the [PIP install](#pip-install) procedure.
If you prefer the [Easy install](#easy-install) procedure, all the needed packages should be already
included in the [Pre-built Package](https://github.com/pyload/pyload/releases) you'll choose.

> **Note:**
> [Test-suite packages](#test-suite-packages) are required only if you want to test
> your installation with the built-in test suite.

### Supported Interpreters

- Python 1
  - [ ] CPython 1.0
  - [ ] CPython 1.5
  - [ ] CPython 1.6
- **Python 2**
  - [ ] CPython 2.0
  - [ ] CPython 2.1
  - [ ] CPython 2.2
  - [ ] CPython 2.3
  - [ ] CPython 2.4
  - [ ] ~~CPython 2.5~~ *(not supported anymore)*
  - [x] **CPython 2.6** *(supported but deprecated)*
  - [x] **CPython 2.7**
  - [ ] PyPy
- **Python 3**
  - [ ] CPython 3.0
  - [ ] CPython 3.1
  - [ ] CPython 3.2
  - [x] **CPython 3.3**
  - [x] **CPython 3.4**
  - [x] **CPython 3.5**
  - [x] **CPython 3.6**
  - [ ] PyPy3

### Required Packages

Package name | Min version | Notes
------------ | ----------- | -----
argparse     | *           |
Beaker       | 1.6         |
bottle       | 0.10.0      |
daemonize    | *           |
future       | *           |
psutil       | *           |
pycurl       | *           |
requests     | 2.0         |
tld          | *           |
validators   | *           |

### Optional Packages

Package name    | Min version | Purpose               | Notes
--------------- | ----------- | --------------------- | ---------
beautifulsoup4  | *           | Additional features   |
bitmath         | *           | Additional features   |
bjoern          | *           | Lightweight webserver | Unix only
colorclass      | *           | Colored log           |
colorlog        | *           | Colored log           |
dbus-python     | *           | Additional features   | Unix only
goslate         | *           | Text translation      |
IPy             | *           | Additional features   |
Js2Py           | *           | JavaScript evaluation |
mod_pywebsocket | *           | Remote API support    |
Pillow          | 2.0         | Captcha recognition   |
pip             | *           | pyLoad auto-update    |
pycrypto        | *           | Click'n'Load support  |
pyOpenSSL       | *           | SSL connection        |
rarfile         | *           | Archive decompression |
Send2Trash      | *           | Trash support         |
setproctitle    | *           | Additional features   |
watchdog        | *           | Additional features   |

### Test-suite Packages

Package name     | Min version | Notes
---------------- | ----------- | -----
nose             | *           |
requests         | 1.2.2       |
websocket-client | 0.8.0       |


Installation
------------

> **Notice:**
> **Before start, make sure you have _Python_ installed on your system.**
> To learn how to install it see <https://wiki.python.org/moin/BeginnersGuide/Download>.

You can install **pyLoad** in several ways:
- [PIP install](#pip-install) *(recommended on Unix based systems)*
- [Easy install](#easy-install) *(recommended on Windows)*
- [Manually install](#manually-install)

### PIP Install

> **Notice:**
> **Before start, make sure you have _pip_ (and _setuptools_) installed on your system.**
> To learn how to install them see <https://pip.pypa.io/en/stable/installing/>.

Type in your command shell **with _administrator/root_ privileges**:

    pip install pyload.core[full]

If the above command fails, consider using the `--user`
[option](https://pip.pypa.io/en/latest/user_guide/#user-installs):

    pip install --user pyload.core

If that fails too, try the [Easy Install](#easy-install) procedure
or at least the [Manually Install](#manually-install) procedure.

### Easy Install

1. Download the [Pre-built Package](https://github.com/pyload/pyload/releases) for your platform.
2. Extract the downloaded archive.
3. Run *pyLoad* from the extracted archive path.

### Manually Install

1. Get the latest tarball of the source code from the ~~[Stable Branch](https://github.com/pyload/pyload/archive/stable.zip) **OR** the [Testing Branch](https://github.com/pyload/pyload/archive/testing.zip)~~
[Master Branch](https://github.com/pyload/pyload/archive/master.zip).
2. Extract the downloaded archive.
3. Change directory to the extracted archive path.
4. Run the built-in setup assistant as described in the [Configuration Section](#configuration).
5. If setup fails or **pyLoad** crashes on startup,
try manually installing the [software dependencies](#dependencies)
or [report your issue](#report-an-issue).


First Start
-----------

### Quick Start

To run **pyLoad** with default profile, just type in your command shell:

    pyload

To run as daemon, type:

    pyload --daemon

To show the help list, type:

    pyload --help

_**That's all Folks!**_

> **Note:**
> Depending on your environment, command `pyload` might be equivalent to `pyLoad.py` or `pyLoad.exe`.

> **Note:**
> On first start, the built-in setup assistant will be automatically launched to assist you to configure
> your profile.

> **Note:**
> The web user interface will be accessible pointing your web browser to the ip address
> and configured port (defaults to `http://localhost:8010`).

> **Note:**
> The remote API server instead will be listening to `http://localhost:7447`.

### Advanced Start

To run **pyLoad** with a custom profile, type:

    pyload -p <profilename>

To run as daemon, type:

    pyload -p <profilename> --daemon

> **Note:**
> The `profile` argument must be a string name, **NOT a directory path**!

> **Note:**
> The `profile` argument is **optional**, but if you do not enter any value,
> the profile `default` will be used.
> **New profiles will be created automatically inside the current config directory when declared**.

### Configuration

After finishing the setup assistant **pyLoad** is ready to use and more configuration can be done
via the web user interface.
Additionally you could simply edit the config files located in your config directory.

To run the built-in setup assistant, type:

    pyload setup

**OR** enter _(from the directory where **pyLoad** is installed)_:

    python setup.py install

> **Note:**
> The default path of the config directory is `%appdata%\pyload` on Windows platform
> and `~/.pyload` otherwise.

> **Note:**
> To learn how to change the config directory see the help list.


Usage
-----

### Basic Usage

To start **pyLoad** in verbose (debug) mode, type:

    pyload --debug

To enable the webserver debugging as well, append:

    pyload --debug --webdebug

To quit a pyLoad instance, type:

    pyload quit -p <profilename>

To restart a pyLoad instance, type:

    pyload restart -p <profilename>

To update the pyLoad core (plugins excluded), type:

    pyload update

~~To run the built-in test suite, type:~~

    pyload test

### Script Usage

You can import **pyLoad** directly in your script:

    import pyload

Available modules:

Package name | Description
------------ | -----------------------------
pyload.core  | pyLoad main program
pyload.rpc   | Official remote API interface
pyload.utils | Utils suite
pyload.webui | Official web user interface

Available functions in `core` module:

- `pyload.core.start(profile=None, configdir=None, refresh=0, remote=None, webui=None, debug=0,
  webdebug=0, daemon=False)`
  - **DESCRIPTION**: Start a process instance.
  - **RETURN**: Multiprocessing instance.
  - **ARGUMENTS**:
   - `profile` sets the profile name to use *(`default` if none entered)*.
   - `configdir` sets the config directory path to use *(`%appdata%\pyload` on Windows platforms
     or `~/.pyload` otherwise, if none entered)*.
   - `refresh` sets refresh/restore mode *(0=off; 1=removes compiled and temp files;
     2=plus restore default username `admin` and password `pyload`)*.
   - `remote` enables remote API interface at entered *`IP address:Port number`
     (use defaults if none entered)*.
   - `webui` enables web user interface at entered *`IP address:Port number`
     (use defaults if none entered)*.
   - `debug` sets debug mode *(0=off; 1=on; 2=verbose)*.
   - `webdebug` sets webserver debugging *(0=off; 1=on)*.
   - `daemon` daemonizes process.
- `pyload.core.quit(profile=None, wait=300)`
  - **DESCRIPTION**: Terminate a process instance.
  - **RETURN**: None type.
  - **ARGUMENTS**:
    - `profile` sets the profile name of the process to terminate
      *(terminate all the running processes if none entered)*.
    - `wait` sets the timeout (in seconds) before force to *kill* the process.
- `pyload.core.restart(profile=None, configdir=None, refresh=0, remote=None, webui=None, debug=0,
  webdebug=0, daemon=False)`
  - **DESCRIPTION**: Restart a process instance.
  - **RETURN**: Multiprocessing instance.
  - **ARGUMENTS**:
    - `profile` sets the profile name to use *(`default` if none entered)*.
    - `configdir` sets the config directory path to use *(`%appdata%\pyload` on Windows platforms
      or `~/.pyload` otherwise, if none entered)*.
    - `refresh` sets refresh/restore mode *(0=off; 1=removes compiled and temp files;
      2=plus restore default username `admin` and password `pyload`)*.
    - `remote` enables remote API interface at entered *`IP address:Port number`
      (use defaults if none entered)*.
    - `webui` enables web user interface at entered *`IP address:Port number`
      (use defaults if none entered)*.
    - `debug` sets debug mode *(0=off; 1=on; 2=verbose)*.
    - `webdebug` sets webserver debugging *(0=off; 1=on)*.
    - `daemon` daemonizes process.
- ~~`pyload.core.setup()`~~
  - **DESCRIPTION**: Setup the package.
  - **RETURN**: None type.
  - **ARGUMENTS**: None.
- `pyload.core.upgrade(dependencies=True, reinstall=False, prerelease=True)`
  - **DESCRIPTION**: Update the package.
  - **RETURN**: None type.
  - **ARGUMENTS**:
    - `dependencies` sets to update package dependencies.
    - `reinstall` sets to reinstall all packages even if they are already up-to-date.
    - `prerelease` sets to update to pre-release and development versions.
- `pyload.core.status(profile=None)`
  - **DESCRIPTION**: Show the process PID.
  - **RETURN**: PID list.
  - **ARGUMENTS**:
    - `profile` sets the profile name of the process to show *(show all the
      running processes if none entered)*.
- `pyload.core.info()`
  - **DESCRIPTION**: Show the package info.
  - **RETURN**: Info dict.
  - **ARGUMENTS**: None.
- `pyload.core.version()`
  - **DESCRIPTION**: Show the package version info.
  - **RETURN**: Version tuple.
  - **ARGUMENTS**: None.
- ~~`pyload.core.test()`~~
  - **DESCRIPTION**: Run the test suite.
  - **RETURN**: None type.
  - **ARGUMENTS**: None.

> **Note:**
> `pyload.core.start` and `pyload.core.restart` return immediately, even if the
> resulting instance is not already fully running!

> **Note:**
> To terminate a single pyLoad instance you MUST pass its profile name to the
> function `pyload.core.quit`, otherwise all the running instances of **pyLoad**
> will be terminated!

> **Note:**
> Calling function `pyload.core.restart` without a proper profile name will
> force to try to terminate the `default` profile one.

A quick example of how *start & stop* a couple instances of **pyLoad** launched
concurrently:

    import pyload
    pyload.core.start('myprofile1')
    pyload.core.start('MyProfile2')
    pyload.core.quit('myprofile1')
    pyload.core.quit('MyProfile2')


Development
-----------

- pyLoad repository: <https://github.com/pyload/pyload>.
- pyLoad documentation: <https://github.com/pyload/pyload/wiki>.
- pyLoad roadmap: <https://github.com/pyload/pyload/milestones>.

> **Note:**
> To report issues or submit your contributions, you need to be registered on *GitHub*.
> It's free and take less a minute to [signup](https://github.com/join).

### Report an Issue

To report an issue, suggest features, ask for a question or help us out,
[**open a ticket**](https://github.com/pyload/pyload/issues).

Please, always title your issues with a pertinent short description and expone accurately
the problem you encounter.

**Don't foget to attach a full debug log of your bugged session from the first start**
or we cannot help you.

> **Note:**
> To learn how to start **pyLoad** in *debug mode* see the [Usage Section](#usage).

### Submit a Code Contribution

To submit your code to the pyLoad repository
[**open a new _Pull Request_**](https://github.com/pyload/pyload/pulls).

You have to sign our [Contributor License Agreement](/CLA.md) to allow us to integrate your work
in the pyLoad repository.
You can sign it easily from within your pull request itself.

For further information see the [License Section](#license).

### Coding Guidelines

Please, follow the [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).

### Localization

> **Notice:**
> **Localization not yet available.**

> **Note:**
> The localization process is managed directly under the *Crowdin* page
> <http://crowdin.net/project/pyload>.

You can download the latest locale files from ~~<https://crowdin.com/download/project/pyload.zip>~~.

To compile them, run the built-in setup utility *(see the [Configuration Section](#configuration))*.

### Performances

> **Notice:**
> **Stats not yet available.**


Licensing
---------

### Main Program

Please refer to the included 
[![LICENSE](https://img.shields.io/pypi/l/pyload.core.svg)](/LICENSE.md)
for the extended license and CLA.

### Plugins

Please refer to the plugins
[LICENSE](https://github.com/pyload/plugins/blob/master/README.md)
for the extended license.


Credits
-------

Please refer to the included [CREDITS](/CREDITS.md) for the extended credits.


Release History
---------------

Please refer to the included [HISTORY](/HISTORY.md) for the detailed release
history.


------------------------------
###### © 2009-2017 pyLoad Team
