#/!usr/bin/env python
# -*- coding: 850 -*-
'''
Created on 13 oct. 2017

@author: Rafael Cisneros
'''

import unittest
from ClassBilleteraElectronica import BilleteraElectronica
from ClassCredito import Credito
from ClassDebito import Debito

class TestBilleteraElectronica(unittest.TestCase):

    def setUp(self):
        self.billetera = BilleteraElectronica(1,"Rafael","Cisneros",24759502,123)


    def tearDown(self):
        self.billetera = None

    def testBilletera(self):
        self.assertEqual(self.billetera.saldo, 0,"La billetera deberia tener saldo 0")
        self.assertEqual(len(self.billetera.debitos), 0,"La billetera no deberia tener debitos")
        self.assertEqual(len(self.billetera.debitos), 0,"La billetera no deberia tener debitos")
        self.assertEqual(self.billetera.nombresDue¤o, "Rafael","Error con los nombres del due¤o de la billetera")
        self.assertEqual(self.billetera.nombresDue¤o, "Rafael","Error con los apellidos del due¤o de la billetera")

     if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
        unittest.main()
