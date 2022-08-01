#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-


from pytest import fail, mark
from vending_machine import VendingMachine

def test_instance():
    vm = VendingMachine()
    assert "VendingMachine" == type(vm).__name__
    assert 0 == vm.total

def test_input():
    vm = VendingMachine()
    vm.input(10)
    assert 10 == vm.total

def test_refund():
    vm = VendingMachine()
    vm.input(10)
    vm.input(50)
    vm.input(100)
    vm.input(500)
    assert 660 == vm.refund()
    assert 0 == vm.total

def test_input_exception():
    vm = VendingMachine()
    for c in [-1,"a",0,49,2000]:
        try:
            vm.input(c)
        except RuntimeError:
            continue
        else:
            fail("not throwing for " + str(c))
