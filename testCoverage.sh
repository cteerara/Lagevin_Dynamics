#!/bin/bash
coverage run --source=src setup.py test
coverage report -m
