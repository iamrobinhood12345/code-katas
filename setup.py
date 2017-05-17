from setuptools import setup

setup(
    name="code-katas",
    description="code katas",
    version=1.1,
    author="Ben Shields",
    author_email="",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["sum_nth_series"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={}
)