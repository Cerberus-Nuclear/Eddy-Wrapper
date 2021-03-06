![logo](https://cerberusnuclear.com/wp-content/uploads/2020/10/EddyLinkedin.jpg)


[![PyPI version](https://badge.fury.io/py/eddy-mc-wrapper.svg)](https://badge.fury.io/py/eddy-wrapper)

Eddy is a HTML output generator for MCNP and SCALE, it imports an MCNP or SCALE output file, extracts the important 
data, and writes it to a user-friendly HTML file.

This repository contains the source code version of Eddy-Wrapper. It is a wrapper program for Eddy-Core, which contains 
the core functionality of the Eddy Project. Eddy-Core is designed to work with a display-less remote server and as 
such cannot handle parts of Eddy's User Interface, which have been extracted to this package; when Eddy-Wrapper is run, 
it will call Eddy-Core to do the back-end work.

Eddy is also available as [a pre-compiled executable](https://github.com/Cerberus-Nuclear/Eddy).

### PyPI Package Usage
Eddy is available on the PyPI Python Package index as eddymc-wrapper, in order to allow easier integration into other 
programs. It can be installed using pip:

```bash
pip install eddy-mc-wrapper
```

and accessed using:

```python
from eddymc_wrapper import eddy_wrapper
eddy_wrapper.main()
```
where `eddy_wrapper.main()` can take the same two optional arguments; the filepath for the MCNP output and a scaling factor. 
If these are not supplied, the GUI will appear to request them when `eddy.main()` is called.

Alternatively, Eddy-Wrapper can be run from the command line with the output file and any applicable scaling factor as 
optional arguments; if no such arguments are supplied a GUI will appear to request them. It should be noted that if 
Eddy-Wrapper has been downloaded directly (such as from GitHub) rather than via PIP, eddy-core will also have to be installed.

General CLI usage:

```bash
python3 eddy_wrapper.py [-o outputfile] [-sf scaling_factor]
```

However, users wishing to incorporate Eddy into their own software projects may find it easier just to use Eddy-Core; 
information on how to include this module can be found in [the Eddy-Core repository](https://github.com/Cerberus-Nuclear/Eddy-Core).

## Features
Features include:
- Eddy can convert F2, F4, F5, F6 and F6+ tallies
- Eddy can accept average tallies, given in the form `F4:N (4 5)`
- Eddy can take an MCNP criticality output and show k-effective for the 
first half, second half and total calculation.
- Eddy will present a warning if an MCNP case was halted due to lost particles
- Eddy will clearly present any FATAL ERROR messages in the MCNP output
- Eddy currently **does not** accept multi-particle tallies of the form `F4:N,P`
- For F2, F4 and F5 tallies, the units are presented as microSieverts per hour.
  The actual result from MCNP is typically multiplied by some conversion factor, so the
  tally output could be in any unit. The uSv/h units have been left in for now as this
  seems to be by far the most common conversion factor used for shielding calculations. 
- Any valid HTML tags found in the MCNP output file will be escaped, preventing any unwanted
HTML or javascript injected into the MCNP output from making its way into the HTML output file.

Requirements

- Python 3.6 or later
- Jinja2 Python package is required (will be included automatically if Eddy is installed via pip)
- importlib_resources may be required for versions of python < 3.9
- pytest and pytest-mock Python packages are required to run the unit tests

<details>
  <summary>Example HTML outputs</summary>
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/eddy-screen-shot-2.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/Results_Summary-1.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/Results_Stats-1.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/WarningsComments.jpg" name="image-name">
  <img src="https://cerberusnuclear.com/wp-content/uploads/2020/10/particles-1.jpg" name="image-name">
</details>
