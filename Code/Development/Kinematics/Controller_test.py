import pygame

pygame.init()

pygame.joystick.init() #Initialize the overall class that controls joysticks

clock = pygame.time.Clock()

clock.tick(20)

print(pygame.joystick.get_count()) #Print the number of joysticks currently found on this machine

usb_controller = pygame.joystick.Joystick(0) #I'm gonna have a stroke reading the docs on this

#Basically you can initalize an actual "Joystick" class which has the ability to do button, axes, and trigger readings
#But for some reason the class is called "Joystick" compared to the parent class "joystick" <- wtf
#Anyway, just remember joystick -> big class, Joystick -> smaller class that has all the attributes we want

#Oh and the 0 is the id of the joystick we want (so depending on the number attached you could grab any of them)
while 1:
    pygame.event.get()
    usb_controller.init() #initialize for use
    
    a = 0
    
    #print(usb_controller.get_numaxes())
    
    #print(usb_controller.get_name())
    
    axes = usb_controller.get_numaxes()

    for i in range(axes):
        axis = usb_controller.get_axis(i)
        print(axis)

pygame.joystick.quit()