# PyShor

This project provides a **Python** implementation of Shor's algorithm using Atos myQLM quantum library ([see here](https://atos.net/en/2019/press-release_2019_05_16/atos-launches-myqlm-to-democratize-quantum-programming-for-researchers-students-and-developers-worldwide)).

This project is in development. There are some problem with the function to perform the primality test.

## Installation

it is preferable to use a virtual environment You can do this by entering the following commands.

Install virtualenv:

`$ pip install virtualenv`

Create a new virtual environment:

`$ virtualenv venv`

Activate the environment:

`$ source ./venv/bin/activate`

Then you can install pyshor package:

`$ python setup.py install`

To run the tests you can enter the following command:

`$ python3 setup.py test`

## Usage

PyShor is a module that you can import in your own code. This module provides only one function that you can use to factor any non prime number strictly greatest than one.

*Example:*

    # Import the module
    from pyshor import factor_int
    
    # Obtain a non trivail factor of an integer
    factor = factor_int(61)
    print(factor) # Output  $ 

## Project Basis

The project is divided in two parts: the classical and the quantum ones. Of course, to solve integer
factorization we need classical and quantum algorithms.

* Classical algorithm are required first to reduce the factorization problem to period finding problem and finally to
extract the period from quantum measurement.

* The quantum algorithm (Shor's algorithm) solves the period finding problem in polynomial time.

Currently, PyShor is based on myQLM PyLinalg simulator to emulate a quantum computer needed to execute the quantum
algorithm. If you want to run the algorithm on a real quantum computer you can using myQLM tools. Of course, myQLM
provides tools to convert the code into executable code for existing quantum computer as Qiskit, Pyquil, etc (see myQLM interop).

If you want to learn more about how Shor's algorithm works you can [see here](https://homepages.cwi.nl/~rdewolf/qcnotes.pdf).