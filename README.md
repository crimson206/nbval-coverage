# Nbval Coverage

## Quick Start

Use nbval to include your notebooks in pytest as well.
It won't include in the coverage.
Convert your notebooks into simplified pytest syntax,
so that pytest will test them, and they are included in the coverage.

**Install**
``` sh
pip install crimson-nbval-coverage
```

### Example

A test for this module is written in a notebook [example/test_processing.ipynb](example/test_processing.ipynb).

The [example/__pytest__/test_ipynb_test_processing.py](example/__pytest__/test_ipynb_test_processing.py) file is generated, where all the lines in the notebook moved in one function.

## Reference

- [nbval github](https://github.com/computationalmodelling/nbval)