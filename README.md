# Void detection using optical flow and vanishing points voting

In this work, we rely on algorithms that **extract vanishing points** from a pair of images captured via a _monocular camera_. These points are **voted using optical flow** to **estimate the furthest empty plane** from the camera to which the linear trajectory from the quadcopter is free of obstacles. This approach requires low-computational power and excludes the need for 3D models, external sensors or camera parameters. 

![image](https://drive.google.com/uc?export=view&id=1rJ8vTF5vADZwNEFQt16ox9MjS2wA2Mql)

## Using this code

One can download the [notebook](notebook/public_opticalFlow_NavigationNet.ipynb) and compile in Jupyter or Collab. For easier use, all the funcstions can be found in the [py files folder](py%20files/). 

The visual verbose of the code was deactivated due to simplification. The code workflow is as below.

![image](https://drive.google.com/uc?export=view&id=1-NY6VPRw3nsQc79HcUCBdXsx1qXVPEbu)

### Sample dataset

The images used are from the [NavigationNet dataset](https://www.mvig.org/research/nav/NavigationNet.html)

## Output examples

The green scatter plot represents the cluster centers. The yellow point indicates the LMCC. The white and red dots mark, respectively,  the elected  and rejected VP by the voting algorithm. The blue dot points the valid but non-elected VP.


![image](https://drive.google.com/uc?export=view&id=10nrftDbwnmYQY-q2ntBfhLlo7sSH3ZIS)

![image](https://drive.google.com/uc?export=view&id=11G2-y6lKZ97PvP6POItSAwuD_wb3ud84)

![image](https://drive.google.com/uc?export=view&id=12CyB4trHjvBehtxVvE6yka7IptRLTaDo)

### Still to update

- [x] Commit separate functions and requirements text file
- [ ] Push the visual verbose notebook
