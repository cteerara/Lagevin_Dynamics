#!/bin/bash

python Lagevin.py --temperature 300 --total_time 1000 --time_step 0.1 --initial_position 0.0 --initial_velocity 0.0 --damping_coefficient 0.1

rm *.pyc
