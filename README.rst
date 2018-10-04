=======
Lagevin
=======


.. image:: https://img.shields.io/pypi/v/Lagevin.svg
        :target: https://pypi.python.org/pypi/Lagevin

.. image:: https://img.shields.io/travis/cteerara/Lagevin.svg
        :target: https://travis-ci.org/cteerara/Lagevin

.. image:: https://readthedocs.org/projects/Lagevin/badge/?version=latest
        :target: https://Lagevin.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/cteerara/Lagevin/shield.svg
     :target: https://pyup.io/repos/github/cteerara/Lagevin/
     :alt: Updates



Simulate Lagevin Dynamics


* Free software: MIT license
* Documentation: https://Lagevin.readthedocs.io.


Features
--------

Package simulate 1D Langevin dynamics for 1 particle with wall bound from 0 to 5. Package includes:

- Lagevin.py: This is the main file 
- LagIntegrator.py: This defines the time stepping integrator.
- LagIO.py: This defines function that takes care of reading input and writing outputs
- LagInput.py: This defines the input structure read from the input file.

How To Run
--------

To run the package go to the src directory Lagevin/src then run the file.
To run, do: 
  python Lagevin.py --temperature 300 --total_time 1000 --time_step 0.1 --initial_position 0.0 --initial_velocity 0.0 --damping_coefficient 0.1
where for example --temperature 300 means the input temperature is 300 for the simulation. This applies to all the parameters listed above.

* Coverage test
To run coverage, go to the Lagevin directory Lagevin/ then do:
  coverage run --source=src setup.py test;
  coverage report -m
  
Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
