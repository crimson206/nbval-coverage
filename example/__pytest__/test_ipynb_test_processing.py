import os
from crimson.nbval_coverage.generate_tests import process_notebooks_recursively, process_notebook, generate_pytest_path, delete_dir, Config

def test_example_test_processing():
    Config.is_notebook = False
    my_dir = './test.ipynb'
    lvl2_dir = './lvl2/simple_notebook.ipynb'
    notebook_root = '.'
    pytest_root = os.path.join(notebook_root, '__pytest__')
    if not Config.is_notebook:
        notebook_root = 'example'
        my_dir = os.path.join(notebook_root, my_dir)
        lvl2_dir = os.path.join(notebook_root, lvl2_dir)
        pytest_root = os.path.join(notebook_root, '__pytest_temp__')
        temp_dir = pytest_root
    generate_pytest_path(lvl2_dir, notebook_root, pytest_root)
    process_notebook(lvl2_dir, notebook_root, pytest_root)
    process_notebooks_recursively(notebook_root, pytest_root)
    if not Config.is_notebook:
        delete_dir(temp_dir)