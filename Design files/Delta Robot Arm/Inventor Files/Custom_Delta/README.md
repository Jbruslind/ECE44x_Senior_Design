# Custom Delta Files
ECE 441 - 443 Project folder with files for senior capstone project for Jorian Bruslind, Mack Hall, and Zach Bendt

## Custom Delta Assembly

This model is the top level assembly for all the other models. This includes 
smaller assemblies (such as the end effector, skelton, motor node and main PCB) as well 
as standalone components (such as the Delta Arm or Motor Mount). The model has been constrained 
so that it is possible to simulate simple movement for the delta end effector (in the vertical direction). 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Custom_Delta_Assembly.png" width="300" height="300" />

### Frame Skeleton 

This model is a sub assembly that creates the general skelton shape for the Delta robot. It uses 20/20 
aluminum T-slot extrusion to create a hexagon shape and is large enough to support the entire workspace 
area for the delta mechanism (as calculated by the Marginally Clever robotics Delta robot tool).  

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Frame_Skeleton.png" width="300" height="300" />

#### Acrylic Panel

The Acryic panel model was designed to be laser cut or CNC'd using typical 3 - 5 mm acrylic plates. This model was made to conform to 
the shape of the 60 deg 20/20 joint on the bottom portion of the panel and has 4 mounting holes on either side in order to provide stiffness 
to the overall frame. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Acrylic_Panel.png" width="300" height="300" />

#### Acrylic Panel Mounts

This model is the exact same as the Acrylic Panel but this was determined to be used for mounting various PCBs/main electrical elements (such as the power supply 
and Raspberry Pi). 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Acrylic_Panel_Mount.png" width="300" height="300" />


#### T-slot Extrusion (350mm, 450mm)

There isn't really anything special about these models other than it is different lengths of 20mm T slot aluminum extrusion. This was the standard 
building material we used to create the frame. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/2020_Tslot_350.png" width="300" height="300" />

The general drawing for 2020 Tslot extrusion is shown below (given in mm)

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/2020_drawing.jpg" width="300" height="300" />


#### 60deg 20/20 Joint 

This part was a custom designed component that linked 3 T Slot extrusion profiles so that it created a 60 degree angle on the horizontal plane and a 90 degree 
angle with the vertical plane. 6 copies of this model allowed for the overall hexagon frame to take shape. This component was 3D printed using PLA material 
and was designed to withstand 4N of pushing force from either side (as shown in the simluation model) 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/60_deg_2020_joint.png" width="300" height="300" />


Simulation Model

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/60_deg_2020_joint_sim.png" width="300" height="300" />

### End Effector 

This assembly was created to help organize the end effector components. These components include the actual mechanical end effector mount, the suction cup
and nylon barb that will link the pnumatic hose. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/End_Effector_V2.png" width="300" height="300" />

#### End Effector V2

#### Vaccum Cup and Fitting 

#### Nylon Barb

### Motor Node 

### Main PCB RPI Assembly

The Automated Microbial Analysis project aims to develop a system which is able to analyze a series of microbial samples on a special media 
called PetriFilm automatically. This is a 3M product that is used in a variety of scientific capacities, mainly in food science and the medical field. 

<!---![PetriFilm](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Admin_Stuff/Mechanical%20Research%20and%20Implementation/Pictures/3MPetrifilm.jpg){ width=50% }-->


