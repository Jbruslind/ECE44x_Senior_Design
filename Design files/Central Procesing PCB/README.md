# Central Processing PCB

This PCB handles everything related to driving the motors from a software point of view. It interprets the motor coordinates sent from the Raspberry Pi, sends signals and power to the Auxiliary PCBs, and processes encoder data from the motors. 

![CentralPCB](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Central%20Procesing%20PCB/Images/CentralPCB.jpg)
![CentralPCBBottom](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Central%20Procesing%20PCB/Images/CentralPCB_Bottom.jpg)
![PCB_TopLayer](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Central%20Procesing%20PCB/Images/PCB_TopLayer.jpg)
![PCB_BottomLayer](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Central%20Procesing%20PCB/Images/PCB_BottomLayer.jpg)

## Ethernet Connectors

The Auxiliary Driver PCB accepts its input from the Central Processing PCBs in the form of an ethernet cable. The ethernet cable carries 24VDC, a direction signal, a step signal, and RX and TX lines for serial communication. The ethernet cable was chosen due to its ubiquity and low cost. Four pins in total are dedicated to power delivery, while the other four pins are dedicated to other signals. Since the Central Processing PCB has to control three separate Auxiliary Diver PCBs, the Central board has three ethernet ports (J3, J4, & J5), one for each Auxiliary PCB. 

![EthernetNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Central%20Procesing%20PCB/Images/EthernetNet.jpg)
![Ethernet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Central%20Procesing%20PCB/Images/Ethernet.jpg)

## Power Conversion and Distribution

The Central Processing PCB distributes power to the rest of the system from the external power supply. The board takes in power from J0, a male XT30 connector, which is rated up to 30A as the name implies. The power supply itself that we are using is rated for only 20A, so this is a non-issue. 

![ConNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Central%20Procesing%20PCB/Images/ConnectorNet.jpg)
![Connector](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Central%20Procesing%20PCB/Images/Connector.jpg)

The Central Processing PCB also requires a fairly robust 5VDC converter, since it is responsible for powering the Raspberry Pi as well as two ATMEGA328 microcontrollers. As such, the PCB utilizes the Bel Fuse SRBH-06H1A1R (U3 on the PCB \[missing a 3D model]), which is capable of stepping down a 24VDC input into a 5VDC output up to 6A. This is overkill for our system, as each of the listed components that draw from the SRBH-06H1A1R only take about 1A each. As such, we have a safety factor of 100%.

![RegulatorNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Central%20Procesing%20PCB/Images/RegulatorNet.jpg)
![Regulator](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Central%20Procesing%20PCB/Images/Regulator.jpg)

As mentioned above, the Central PCB provides 5VDC to the Raspberry Pi via its GPIO pins. This is not recommended by the makers of the Raspberry Pi, as the GPIO pins bypass the internal fusing and regulation done in order to ensure a safe and regulated 5V line for the system. Before going to the upside-down headers that allow the Central PCB to be worn as a Raspberry Pi hat, the 5V line on the Central PCB must go through a resettable thermal fuse (F1 on the PCB) in order to ensure that the Raspberry Pi cannot draw enough current to harm itself. The fuse we are using is the Bel Fuse 0ZCH0200FF2E, which is rated for 2A before tripping. Once tripped, the fuse will reset after being returned to room temperature.


![RPiNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Central%20Procesing%20PCB/Images/RPiNet.jpg)
![RPi](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Central%20Procesing%20PCB/Images/RPi.jpg)

Furthermore, the Central PCB is also responsible for providing 12VDC to drive the vacuum pump. The vacuum pump simply turns on when a voltage is applied to the terminals. Therefore, the system will utilize a relay to turn the pump on and off. The schematic is as shown:

