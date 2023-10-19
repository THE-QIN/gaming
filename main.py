import pygame
from Game import Arena,Snack,Buff

# initialisasi game
# arena
arena = Arena(500,500,20,20)
# object game
snack = Snack(arena,(10,10),arah_x=1)
buff = Buff(arena,nama="buff")

# aplikasi sama rendering time
isRun = True
tick = 10

while isRun:
    # user window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
            
    # update
    snack.move()
    
    if snack.is_collide():
        arena.reset_member()
        snack.reset()
        buff = Buff(arena,nama="buff")
        
    if snack.get_pos() == buff.get_pos():
        snack.tambah_kotak()
        buff.ubah_pos()
        
    # render 
    arena.render(tick)
    
pygame.quit()