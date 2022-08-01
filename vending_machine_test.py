#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-


from pytest import fail, mark
from vending_machine import VendingMachine

def test_instance():
    vm = VendingMachine()
    assert "VendingMachine" == type(vm).__name__
