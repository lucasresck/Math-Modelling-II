# coding: utf8

import random as ran

class Bolas:
    
    def __init__(self,largura,comprimento,tamc,p,g,dt):
        self.posb = PVector(
            ran.uniform((p+tamc)/2,(largura-p/2-tamc/2)),
            ran.uniform((p+tamc)/2,(comprimento-p/2-tamc/2))
        )
        self.vb = PVector(ran.uniform(100,200),ran.uniform(100,200))
        self.m = ran.uniform(5,15)
        self.peso = self.m*g #calcula força peso da bola 1
        self.ab = 0
        self.dt = dt
    
    def calculus_aceleration(self,k):
        Frb = (-k)*self.vb #calcula força de retardo
        Fb = self.peso + Frb #calcula força resultante
        ab = (1/self.m)*Fb
        return ab
    
    def metodo_euler(self,vb,ab):
        vb_0 = self.vb.copy()
        self.vb = ab.copy()
        self.vb.mult(self.dt)
        self.vb.add(vb_0)       
        drb = self.vb.copy()
        drb.mult(self.dt)
        self.posb.add(drb)
        return self.posb
        
    def calculus_posicion(self,k):
        self.ab = self.calculus_aceleration(k)
        self.posb = self.metodo_euler(self.vb,self.ab)
        return self.posb
            
    
        
