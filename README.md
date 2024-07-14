# qaoa
Implementation of the Quantum Approximate Optimization Algorithm (QAOA) for the [Maximum Cut (MaxCut) problem](https://en.wikipedia.org/wiki/Maximum_cut) with [Qiskit](https://www.ibm.com/quantum/qiskit)

## What's in here?
Here you can find the code we use in some of our quantum optimization projects.
* `classes` contains two classes, one to generate graph instances for the MaxCut problem and the other to implement and QAOA-type quantum circuits.
* `data` contains some pre-generated data (graphs created with the `Problems` class) and an example data generation notebook.
* `documentation` contains two minimal documentation notebooks about the classes and utilities in this repository.
* `functions` contains utilities to work with the classes in `classes`, solve the MaxCut problem and othe related tasks.
* `tutorials` contains a minimal example notebook showing a possible pipeline where the MaxCut problem is solved in a specific instance.
* `config.py` is a configuration file used to specify some settings (e.g. the number of QAOA layers).
* `requirements.txt` contains the requirements (install the file before using the code in this repository)

## Use this repository
If you want to use the code in this repository in your projects, please cite explicitely our work, and
* Clone the repository with `git clone https://github.com/NesyaLab/qaoa`
* Install the requirements with `pip install -r requirements.txt`

For further guidance check the examples in the `documentation` and `tutorials` directories.
