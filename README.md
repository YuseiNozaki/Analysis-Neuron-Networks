# Analysis Neuron Networks

## Overview
Simulate a network built by the Hodgkin-Huxley model.

## Description
The number of neurons, the connection　probability, the presence or absence of plasticity, and the intensity of the perturbation can all be varied in the simulation.

Basically, it plots the average synchronization rate between the connection probability and the firing time.

## Requirements
* Numpy
* Matplotlib
* tqdm

## Usage
If you want to simulate a single neuron, run "single_neuron.py".

If you want to simulate a network of neurons, run "main.py".

Feel free to change the contents of the code as needed.

## Structure
<pre>
.
├── README.md
├── __init__.py
├── const.py
├── function
│   ├── __init__.py
│   ├── activation.py
│   ├── calc_r.py
│   ├── convert_pulse_time.py
│   ├── coupling_table.py
│   ├── hodgkin_huxley.py
│   └── runge_kutta.py
├── main.py
├── neuron_network.py
├── requirements.txt
└── single_neuron.py
</pre>

## Works Cited
* R. R. Borges, F. S. Borges, E. L. Lameu, A. M. Batista, K. C. Iarosz, I. L. Caldas, R. L. Viana and M. A. F. Sanjuan, Commun. Nonlinear Sci. Numer. Simul. 34, 12-22 (2016).
