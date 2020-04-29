This file contains the source code for the Microbial Analysis Tool software.
All code has been thoroughly commented.
It consists of: 
GUI.py - User interface source code
The bulk of the design and layout portion of this module was auto generated using QtDesigner then modified to fit our purposes.
The GUI has two threads running simultaneously. One updates the image that is displayed as well as the sample data. The other handles the automation controls and image analysis.

deltaImageProcessor.py - Handles image capture, and data output to .csv file.

colonyCounter.py - Computer Vision analysis
This module takes in a file from the "/images" folder located in the current working directory, performs computer vision analysis and applies keypoints over any detected colonies.

robo_controls.py – Sends automation control messages.
This module sends automation control messages via serial interface to the ATmega328 where they are decoded and used to set the motor anagles.
