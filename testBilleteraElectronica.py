# -*- coding: 850 -*-
'''
Created on 13 oct. 2017
@author: Rafael Cisneros 13-11156
@author: Miguel Canedo 13-10214
'''

import unittest

from billeteraElectronica import BilleteraElectronica
from credito import Credito
from debito import Debito

class TestBilleteraElectronica(unittest.TestCase):
    def setUp(self):
        self.billetera = BilleteraElectronica(1,"Rafael", "Cisneros", 24759502, 123)
        self.billeteraRara = BilleteraElectronica(2, "A'd-@lb3rto","Pe§ar†dÑ", 24901467, 000)
    def tearDown(self):
        self.billetera = None

    ###############################
    #           Fronteras         #
    ###############################
    def testSaldoBilletera0(self):
        self.assertEquals(self.billetera.saldo(), 0, "La billetera deberia tener saldo 0")
        
    def testMismoConsumoQueRecarga(self):
        recarga1 = Credito(122.00, "13/10/2017", 1)
        self.billetera.recargar(recarga1)
        consumo1 = Debito(122.00, "13/10/2017", 1)
        self.billetera.consumir(consumo1, 123)
        self.assertEqual(self.billetera.saldo(), 0, "Error en el nuevo saldo total")
    
    def testOwnerBilleteraConCaracteresEspeciales(self):
        self.assertEqual(self.billeteraRara.nombreOwner, "A'd-@lb3rto", "Error con los nombres del due√±o de la billetera")
        self.assertEqual(self.billeteraRara.apellidoOwner, "Pe§ar†dÑ","Error con los apellidos del due√±o de la billetera")

    def testPINInvalido(self):
        recarga1 = Credito(122.00, "13/10/2017", 1)
        self.billetera.recargar(recarga1)
        consumo1 = Debito(122.00, "13/10/2017", 1)
        self.billetera.consumir(consumo1, 321) 
 
    
    ###############################
    #           Esquina           #
    ###############################
    def testNombreRaroYPINIncorrecto(self):
        recarga1 = Credito(122.00, "13/10/2017", 1)
        self.billeteraRara.recargar(recarga1)
        consumo1 = Debito(122.00, "13/10/2017", 1)
        self.billeteraRara.consumir(consumo1, 321)
        self.assertEqual(self.billeteraRara.saldo(), 122, "Error en el nuevo saldo total")
    
    def testNombreRaroYSaldo0(self):
        self.assertEquals(self.billeteraRara.saldo(), 0, "La billetera deberia tener saldo 0")
    
    def testSaldo0YPINIncorrecto(self):
        consumo1 = Debito(122.00, "13/10/2017", 1)
        self.billetera.consumir(consumo1, 321)
        self.assertEqual(self.billetera.saldo(), 0, "Error en el nuevo saldo total")
    
    ###############################
    #           Interior          #
    ###############################
    def testBilletera(self):
        self.assertEqual(self.billetera.saldo(), 0, "La billetera deberia tener saldo 0")
        self.assertEqual(len(self.billetera.debitos), 0, "La billetera no deberia tener debitos")
        self.assertEqual(len(self.billetera.debitos), 0, "La billetera no deberia tener debitos")
        self.assertEqual(self.billetera.nombreOwner, "Rafael","Error con los nombres del due√±o de la billetera")
        self.assertEqual(self.billetera.apellidoOwner, "Cisneros","Error con los apellidos del due√±o de la billetera")
        self.assertEqual(self.billetera.ciOwner, 24759502, "Error en la cedula del due√±o de la billetera")
    
    def testConsumir(self):
        cantidadActualDebitos = len(self.billetera.debitos)
        recarga1 = Credito(122.00, "13/10/2017", 1)
        self.billetera.recargar(recarga1)
        consumo1 = Debito(22.00, "13/10/2017", 1)
        self.billetera.consumir(consumo1, 123)
        self.assertEqual(len(self.billetera.debitos), cantidadActualDebitos+1, "Error en la cantidad total de debitos")
        self.assertEqual(self.billetera.saldo(), 100, "Error en el nuevo saldo total")
    

    def testRecargar(self):
        saldoActual = self.billetera.saldo()
        cantidadActualCreditos = len(self.billetera.creditos)
        recarga = Credito(100.00, "13/10/2017", 1)
        self.billetera.recargar(recarga)
        self.assertEqual(len(self.billetera.creditos), cantidadActualCreditos+1, "Error en la cantidad total de creditos")
        self.assertEqual(self.billetera.saldo(), saldoActual + recarga.monto, "Error en el nuevo saldo total")

    def testSaldo(self):
        saldoActual = self.billetera.saldo()
        recarga1 = Credito(122.00, "13/10/2017", 1)
        self.billetera.recargar(recarga1)
        recarga2 = Credito(982.00, "13/10/2017", 1)
        self.billetera.recargar(recarga2)
        consumo1 = Debito(23.00, "13/10/2017", 1)
        self.billetera.consumir(consumo1, 123)
        consumo2 = Debito(642.00, "13/10/2017", 1)
        self.billetera.consumir(consumo2, 123)
        consumo3 = Debito(132.00, "13/10/2017", 1)
        self.billetera.consumir(consumo3, 123)
        consumo4 = Debito(111.00, "13/10/2017", 1)
        self.billetera.consumir(consumo4, 123)
        recarga3 = Credito(323.00, "13/10/2017", 1)
        self.billetera.recargar(recarga3)
        self.assertEqual(self.billetera.saldo(), (saldoActual + recarga1.monto + recarga2.monto + recarga3.monto - consumo1.monto -
                                                consumo2.monto - consumo3.monto - consumo4.monto), "Error en el nuevo saldo total")
    
    ###############################
    #           Malicia           #
    ###############################
    def testConsumirMasDeLoQueSeRecargo(self):
        recarga = Credito(50.00, "13/10/2017", 1)
        self.billetera.recargar(recarga)
        consumo = Debito(100.00, "13/10/2017", 1)
        self.billetera.consumir(consumo, 123)
        self.assertEqual(self.billetera.saldo(), 50, "Error en el nuevo saldo total")
    
    def testConsumirConSaldoInsuficiente(self):
        cantidadActualDebitos = len(self.billetera.debitos)
        consumo = Debito(100.00, "13/10/2017", 1)
        self.billetera.consumir(consumo, 123)
        self.assertEqual(len(self.billetera.debitos), cantidadActualDebitos, "Error en la cantidad total de debitos")
        self.assertEqual(self.billetera.saldo(), 0, "Error en el nuevo saldo total")
  
    def testConsumoAntesRecarga(self):
        consumo = Debito(100.00, "13/10/2017", 1)
        self.billetera.consumir(consumo, 123)
        recarga = Credito(50.00, "13/10/2017", 1)
        self.billetera.recargar(recarga)
        self.assertEqual(self.billetera.saldo(), 50, "Error en el nuevo saldo total")
        
    if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
        unittest.main()
