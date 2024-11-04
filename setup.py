from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    description="A simple math quiz game",
    author="Julian Greipel",
    author_email="jgreipel2@googlemail.com",
    license="Apache License 2.0",
    install_requires=[],  
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz",
        ]
    }
)
