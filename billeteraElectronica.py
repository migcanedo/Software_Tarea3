# -*- coding: 850 -*-
'''
Created on 14 oct. 2017

@author: Rafael Cisneros 13-11156
@author: Miguel Canedo 13-10214
'''

class BilleteraElectronica:
    def __init__(self, id, n, a, ci, p):
        self.id = id
        self.nombreOwner = n
        self.apellidoOwner = a
        self.ciOwner = ci
        self.pin = p
        self.debitos = []
        self.creditos = []
        
    def saldo(self):
        return 0
    
    def recargar(self, pin, monto, fecha, id):
        return
    
    def consumir(self, pin, monto , fecha, id):
        return