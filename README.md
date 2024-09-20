# nbval-coverage

A tool to include Jupyter notebooks in pytest coverage reports.

## Quick Start

1. Install:
```sh
pip install crimson-nbval-coverage
```

2. Use `nbval-coverage` to convert your notebooks into simplified pytest syntax.

## Features

- Converts Jupyter notebooks to pytest-compatible format
- Includes converted tests in coverage reports
- Supports recursive processing of notebooks in directories

## Example

See [example/test_processing.ipynb](example/test_processing.ipynb) for a sample notebook.

The generated test file is [example/__pytest__/test_ipynb_test_processing.py](example/__pytest__/test_ipynb_test_processing.py).

## Reference

- [nbval GitHub repository](https://github.com/computationalmodelling/nbval)