
""" To run: just call python -m pytest while in this directory
or add a configuration in pycharm
"""

import pytest
from eddymc_wrapper import eddy_wrapper
from tests import mcnp_examples, scale_examples
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources


@pytest.fixture
def f2_file(tmpdir):
    f2 = pkg_resources.read_text(mcnp_examples, 'F2.out')
    return f2.split('\n')


@pytest.fixture
def scale_file(tmpdir):
    file = pkg_resources.read_text(scale_examples, 'cylinder_ce.out')
    return file.split('\n')


@pytest.fixture
def text_file(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'not_an_mcnp_file.out')
    return file.split('\n')


@pytest.fixture
def crit_file(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'Criticality.out')
    return file.split('\n')


@pytest.fixture
def mcnp_input(tmpdir):
    file = pkg_resources.read_text(mcnp_examples, 'F4.mcnp')
    return file.split('\n')


def test_crit_checker_positive(crit_file):
    # arrange
    text = crit_file
    # act
    result = eddy_wrapper.check_if_crit(text)
    # assert
    assert result is True


def test_crit_checker_negative(f2_file):
    # arrange
    text = f2_file
    # act
    result = eddy_wrapper.check_if_crit(text)
    # assert
    assert result is False


def test_read_file():
    # arrange
    file = "mcnp_examples/F2.out"
    # act
    data = eddy_wrapper.read_file(file)
    # assert
    assert data[0].strip() == "Code Name & Version = MCNP_6.20, 6.2.0"
    assert len(data) == 884


def test_get_args_with_passed_arguments():
    # arrange
    name = 'mcnp_examples/F2.out'
    scaling_factor = 1.5
    # act
    filename, scaling_factor = eddy_wrapper.get_args(name, scaling_factor)
    # assert
    assert name == 'mcnp_examples/F2.out'
    assert scaling_factor == 1.5


def test_main_calls_eddy_core(mocker):
    # arrange
    name = 'mcnp_examples/F2.out'
    sf = 3.141592
    mocker.patch('eddymc_wrapper.eddy_wrapper.get_args', return_value=(name, sf))
    mocker_core = mocker.patch('eddymc_wrapper.eddy_wrapper.eddy.main')
    # act
    eddy_wrapper.main()
    # assert
    mocker_core.assert_called()


def test_main_with_non_mc_input():
    # arrange
    name = 'mcnp_examples/not_an_mcnp_file.out'
    sf = 1.2
    # act
    with pytest.raises(eddy_wrapper.eddy.NotAcceptedFileTypeError) as expected_failure:
        eddy_wrapper.main(name, sf)
    # assert
    assert expected_failure


def test_main_with_nonexistent_input_passed():
    # arrange
    name = 'mcnp_examples/nonexistent_file.out'
    # act
    # actually fails in get_filename()
    with pytest.raises(AssertionError) as expected_failure:
        eddy_wrapper.main(name)
    # assert
    assert expected_failure
