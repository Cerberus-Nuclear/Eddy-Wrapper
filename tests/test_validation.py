#!/usr/bin/env python3
# Peter Evans
# Cerberus Nuclear Ltd

"""This module is very much a work in progress,
it is intended to eventually be used to automate a number
of validation tests.
"""

import glob
from eddymc_wrapper import eddy_wrapper
from eddymc_core import eddy  # needed for NotAcceptedFileTypeError


def test_examples_run():
    # try to run all the mcnp example cases
    for file in glob.glob('mcnp_examples/*.out'):
        try:
            eddy_wrapper.main(file, scaling_factor=1.5)
        except eddy.NotAcceptedFileTypeError:
            pass
        except:
            print(f"Exception thrown when running {file}")
            raise

    # try to run all the scale example cases
    for file in glob.glob('scale_examples/*.out'):
        try:
            eddy_wrapper.main(file, scaling_factor=1.5)
        except:
            print(f"Exception thrown when running {file}")
            raise
