# GRBL Code

This project utilizes [GRBL](https://github.com/grbl/grbl), which is an open-source stepper motor driver controller designed to run natively on an Arduino Uno. However, the Arduino Nano has the same number of digital output pins as the Arduino Uno, so it is possible to modify the code to run on the Nano.

The Arduino Nano barely has enough memory to flash grbl on to it, but it does. From there, the cpu_map.h file needs to be modified, in order to redirect the output signals to the proper pins. For our case, the signals were redirected to the following pins:

![GrblNanoPinout](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Code/GRBL%20Code/GrblNanoPinout.PNG)

Every other part of grbl is unmodified, aside from a few grbl settings used for smoother operation. Since both the Arduino Uno and Arduino Nano utilize the ATmega 328 microcontroller, that was a large determining factor as to why we chose it to use it for this project.
