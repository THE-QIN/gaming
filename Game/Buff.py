import pygame
from numpy import random as rnd

class Buff():
    
    def __init__(self,arena,warna=(255,0,0),nama="buff"):
        self.nama = nama
        buff_pos_x = rnd.random_integers(0,arena.get_jumlah_kolom()-1)
        buff_pos_y = rnd.random_integers(0,arena.get_jumlah_baris()-1)
        self.pos = (buff_pos_x,buff_pos_y)
        self.warna = warna
        self.surface = arena.get_surface()
        self.lebar = arena.get_jarak_kolom()
        self.tinggi = arena.get_jarak_baris()
        self.arena = arena
        arena.assign_member(self)
        
    def get_pos(self):
        return self.pos
    
    def ubah_pos(self):
        buff_pos_x = rnd.random_integers(0,self.arena.get_jumlah_kolom()-1)
        buff_pos_y = rnd.random_integers(0,self.arena.get_jumlah_baris()-1)
        self.pos = (buff_pos_x,buff_pos_y)
        
    def draw(self):
        start_x = self.lebar*self.pos[0]
        start_y = self.tinggi*self.pos[1]
        pygame.draw.rect(self.surface, self.warna,(start_x,start_y,self.lebar,self.tinggi))
        
    def __repr__(self):
        return self.nama