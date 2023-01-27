# Void detection using optical flow and vanishing points voting

![Status](https://img.shields.io/static/v1?style=flat&logo=github&label=status&message=finished&color=red) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)  [![GitHub forks](https://img.shields.io/github/forks/debOliveira/voidDetection.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/debOliveira/voidDetection/network/) [![GitHub stars](https://img.shields.io/github/stars/debOliveira/voidDetection.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/debOliveira/voidDetection/stargazers/) [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FdebOliveira%2FvoidDetection&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

This was a published paper in the **SBAI 2021** ([link to paper](https://www.sba.org.br/open_journal_systems/index.php/sbai/article/view/2586)). In this conference, this paper was **given honorable mention in the undergraduate category**.

In this work, we rely on algorithms that **extract vanishing points** from a pair of images captured via a _monocular camera_. These points are **voted using optical flow** to **estimate the furthest empty plane** from the camera to which the linear trajectory from the quadcopter is free of obstacles. This approach requires low-computational power and excludes the need for 3D models, external sensors or camera parameters. 

<p align="center"><img src="https://user-images.githubusercontent.com/48807586/133134034-49e1b6e9-eaba-4d26-9ca3-5bca7f438caa.png" width="500"/></p>

## Using this code

One can download the [notebook](notebook/public_opticalFlow_NavigationNet.ipynb) and compile in Jupyter or Collab. For easier use, all the funcstions can be found in the [py files folder](py%20files/). 

The visual verbose of the code was deactivated due to simplification. The code workflow is as below.

<p align="center"><img src="https://user-images.githubusercontent.com/48807586/133134284-4e62cc8a-50e2-4e44-a7aa-2c506fe52698.png" width="500"/></p>

**Please take a look at the [requirements](https://github.com/debOliveira/voidDetection/blob/main/requirements.txt).**

### Sample dataset

The images used are from the [NavigationNet dataset](https://www.mvig.org/research/nav/NavigationNet.html)

## Output examples

The green scatter plot represents the cluster centers. The yellow point indicates the LMCC. The white and red dots mark, respectively,  the elected  and rejected VP by the voting algorithm. The blue dot points the valid but non-elected VP.

<p align="center">
  <img src="https://user-images.githubusercontent.com/48807586/133134438-f7e5b073-2559-4693-9792-c22b36039e68.jpg" width="500"/>
  <img src="https://user-images.githubusercontent.com/48807586/133134454-c3390cfa-a521-4bcc-ad5d-feb3d81d7741.jpg" width="500"/>
  <img src="https://user-images.githubusercontent.com/48807586/133134475-128747a6-aaa4-4811-851d-7caf8a13bca2.jpg" width="500"/>
</p>

