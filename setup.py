from setuptools import setup, find_packages

setup(
    name="timeseries-analytics-platform",
    version="1.0.0",
    description="Production-grade statistical time-series analytics platform",
    author="Analytics Team",
    python_requires=">=3.12",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.26.4",
        "pandas>=2.2.0",
        "scipy>=1.13.0",
        "pydantic>=2.6.1",
        "pydantic-settings>=2.1.0",
        "pytest>=7.4.4",
        "pytest-cov>=4.1.0",
        "matplotlib>=3.8.3",
        "kivy>=2.3.0",
        "kivymd>=1.2.0",
        "pillow>=10.1.0",
        "openpyxl>=3.1.2",
        "python-dateutil>=2.8.2",
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "timeseries-app=app.main:main",
        ],
    },
)
