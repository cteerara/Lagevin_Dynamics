#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `Lagevin` package."""

import pytest
import sys
import os
import numpy as np

sys.path.append("../")
from click.testing import CliRunner

from Lagevin import Lagevin
from Lagevin import cli
from Lagevin import LagIO
from Lagevin import LagIntegrator as LInt
from Lagevin import LagInput

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'Lagevin.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

#-------------------------------------------
# test LagIO
def test_LagIO_readInput_ValidInput():
    # Check case for Valid input
    os.chdir("input")
    result=LagIO.readInput('test_Lag.in')
    assert result.IniPos == 0.0
    assert result.IniVel == 0.0
    assert result.IniTemp == 300
    assert result.DampCoef == 0.1
    assert result.dt == 0.1
    assert result.ttot == 10000

def test_LagIO_readInput_InvalidInput():
    # Check case for Invalid input
    #os.chdir("input")
    result=LagIO.readInput('test_Lag_None.in')
    assert result.IniPos == 0.0
    assert result.IniVel == 0.0
    assert result.IniTemp == 0.0
    assert result.DampCoef == 0.0
    assert result.dt == 1
    assert result.ttot == 10

#def test_LagIO_writeInput():
    
#---------------------------------------
# test integrator
def test_LagIntegrator_RK4():
      lagin = LagIO.readInput("test_Lag.in")
      def RHS(y,t):
        return y
      F0 = 1.0
      F = F0
      t = 1
      lagin.dt = 1e-4
      lagin.ttot = int(1/lagin.dt)
      x = np.linspace(0.0,0.0,num=lagin.ttot)
      for i in range(1,lagin.ttot):
        t = lagin.dt*i
        F = LInt.RK4(RHS, lagin, (F,t))
      assert np.abs(F-np.exp(1)) < 1e-2  

#------------------------------------
# Test Lagevin.py
def test_Lagevin_getInput():
  result = Lagevin.getInput() 
  assert result.IniPos == 0.0
  assert result.IniVel == 0.0
  assert result.IniTemp == 0.0
  assert result.DampCoef == 0.0
  assert result.dt == 1
  assert result.ttot == 10


def test_Lagevin_vel_RHS():
  # with random seed == 1, using the test_Lag.in input file, vel_RHS should give the result equal to 12.482... We only take up to the 3rd decimal place 
  lagin = LagIO.readInput("test_Lag.in")
  np.random.seed(1)
  result = Lagevin.vel_RHS(1,lagin,2)
  assert 12482 == int(result*1e3)

def test_Lagevin_pos_RHS():
  result = Lagevin.pos_RHS(1,2,1)
  assert result == 2

def test_Lagevin_Main():
  result = Lagevin.Main()
  assert result == 0
