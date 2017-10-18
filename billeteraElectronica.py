# -*- coding: 850 -*-
'''
Created on 14 oct. 2017

@author: Rafael Cisneros 13-11156
@author: Miguel Canedo 13-10214
'''

from credito import Credito
from debito import Debito


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
        s = 0
        for c in self.creditos:
            s+= c.monto
            
        for d in self.debitos:
            s -= d.monto
            
        return s

    def recargar(self, *args): # args es un objeto Credito o un conjunto de elementos [monto, fecha, idEstablecimiento]
        if len(args) == 3:
            recarga = Credito(args[0], args[1], args[2]) #(monto, fecha, idEstablecimiento)
        elif len(args) == 1:
            recarga = args[0]
        else:
            print("Error en la cantidad de argumentos")

        self.creditos.append(recarga)
        
    def consumir(self, *args): # args es un objeto Credito o un conjunto de elementos [monto, fecha, idEstablecimiento, pin]
        consumo = Debito(0, "19/07/96", 1)
        if len(args) == 4:
            if args[3] == self.pin: 
                consumo = Debito(args[0], args[1], args[2])
            else:
                return ("PIN incorrecto, no se logro realizar la transaccion.")
        elif len(args) == 2:
            if args[1] == self.pin: 
                consumo = args[0]
            else:
                print("PIN incorrecto, no se logro realizar la transaccion.")
        else:
            print("Error en la cantidad de argumentos")
        
        if self.saldo() >= consumo.monto:
            self.debitos.append(consumo)
        else:
            return ("No dispone del saldo suficiente para cubrir el consumo.")
