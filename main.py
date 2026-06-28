import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(840, 500))
print('Setup Finish')

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close Window
            quit() # End pygame

