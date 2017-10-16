# -*- coding: 850 -*-
'''
Created on 13 oct. 2017

@author: Rafael Cisneros 13-11156
@author: Miguel Canedo 13-10214
'''

import unittest
from billeteraElectronica import BilleteraElectronica
from credito import Consumo
from debito import Recarga

class TestBilleteraElectronica(unittest.TestCase):
    def setUp(self):
        self.billetera = BilleteraElectronica(1, "Rafael", "Cisneros", 24759502, 123)
    def tearDown(self):
        self.billetera = None

    def testBilletera(self):
        self.assertEqual(self.billetera.saldo(), 0,"La billetera deberia tener saldo 0")
        self.assertEqual(len(self.billetera.debitos), 0,"La billetera no deberia tener debitos")
        self.assertEqual(len(self.billetera.creditos), 0,"La billetera no deberia tener debitos")
        self.assertEqual(self.billetera.nombreOwner, "Rafael","Error con los nombres del due¤o de la billetera")
        self.assertEqual(self.billetera.apellidoOwner, "Cisneros","Error con los apellidos del due¤o de la billetera")
    
    def testSaldoBilletera0(self):
        self.assertEquals(0, self.billetera.saldo(), "La billetera deberia tener saldo 0")