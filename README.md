### ExPI_toolbox
A toolbox for ExPI dataset.


(**!!! The data is not publicly released yet. Please do NOT distribute the data and code !!! **)

---
### Preparing data
Please download ExPI dataset, and extract images from .mp4 to .jpg (by ffmpeg for example), put the images in IMG/, to have:

'''
ExPI_ROOT_PATH
|-- acro1
    |-- a-frame1
        |-- IMG
            |-- cam-012
            |-- cam-020
            |-- cam-030
            `-- cam-038
        |-- mocap_cleaned.tsv
        |-- calib-new.xml
        `-- talign.csv
    |-- a-frame2
    `-- ...
`-- acro2
    `-- ...


In the full dataset of ExPI, we have 68 different camera views. Here we just include 4 views (the 4 best views for 3D pose estimation by RGB images):

acro1: cam-012 / cam-020 / cam-030 / cam-038

acro2: cam-011 / cam-019 / cam-030 / cam-037

For detailed information about the dataset, please see:
[Project page](https://team.inria.fr/robotlearn/multi-person-extreme-motion-prediction/)
[paper](https://arxiv.org/abs/2105.08825) 


---
### Use the data for different tasks
When processing monocular RGB pose estimation, we suggest that you take all these 4 views into consideration (so you will enlarge the dataset by x4 times).

For writing the dataloader, please refer to [code](https://github.com/GUO-W/MultiMotion), which is a repo for 3D motion prediction (where only mocap 3D data is used) if needed.
For train/test split protocols, please refer to [paper](https://arxiv.org/abs/2105.08825) if needed.


---
### Quick Start 
This repo contains functions for data reading/ 2D3Dprojection / 2D3D visualisation / matching the images with 3D annotations.

You could use the repo for 2d/3d visualization (image/video) by simply running vis.sh:
* 2d: visualize RGB along with 2D pose projection.
* 3d: visualize 3D skeletons.
* 2d3d: visualize RGB along with 2D pose projection/ corresponding 3D skeletons at the same time.
Example: sh vis.sh acro2 a-frame1 30 '2d3d'

The 2d/3d visualization result you get would be something like in this [video](https://team.inria.fr/robotlearn/multi-person-extreme-motion-prediction/).

---
### Citing
If you find our code or data helpful, please cite our work
 
@article{guo2021multi,
    title={Multi-Person Extreme Motion Prediction}, 
    author={Wen,Guo and Xiaoyu, Bie and Xavier, Alameda-Pineda, Francesc,Moreno-Noguer}, 
    journal={arXiv preprint arXiv:2105.08825}, 
    year={2021} }
