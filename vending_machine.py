#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-

class VendingMachine:
    def __init__(self):
        self.total = 0

    def input(self,coin):
        if coin in [10,50,100,500,1000]:
            self.total += coin
            return
        raise RuntimeError('coin should be 10,50,100,500 or 1000')

    def refund(self):
        prev_total = self.total
        self.total = 0
        return prev_total
