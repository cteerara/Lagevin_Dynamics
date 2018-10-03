#!/bin/bash
coverage run --source=Lagevin setup.py test
coverage report -m
