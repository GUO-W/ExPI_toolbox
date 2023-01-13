### ExPI_toolbox
A toolbox for ExPI dataset.

This repo contains functions for data reading/ 2D3Dprojection / 2D3D visualisation / matching the images with 3D annotations.

For detailed information about the dataset, please see:
[Project page](https://team.inria.fr/robotlearn/multi-person-extreme-motion-prediction/)
[paper](https://arxiv.org/abs/2105.08825) 


**News**

11/2021 The 3D Mocap data is released!

01/2023 The full video data for all views and the mesh data are released!


---
### Preparing data
Please apply and download different parts of the ExPI dataset [here](https://zenodo.org/record/5578329#.Y8ChFOzP23K), and extract images from .mp4 to .jpg (by ffmpeg for example), put the images in IMG/.
The full datatse should be:

```
ExPI_release_all
|-- IMG
    |-- acro1
        |-- a-frame1
            |-- IMG
                |-- cam-012
                    |-- img-000050.jpg 
                    `-- ...
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
|-- Mesh
    |-- acro1
        |-- a-frame1
            |-- OBJ
                |-- model-00050.mtl
                |-- model-00050.obj
                |--model-00050.png
                `-- ...
        |-- a-frame2 
        `-- ...
    `-- acro2 
        `-- ...
|-- 3DMocap
`-- Toolbox


```

**Note** Note that first frame of the extracted images is not img-000000.jpg , but should correspond to the value of mesh.start in talign.csv. This is to align with the meshes and mocap data.

For acro1, we provide 68 views, for acro2 we provide 67 views. 


---
### Quick Start 
This repo contains functions for data reading/ 2D3Dprojection / 2D3D visualisation / matching the images with 3D annotations.

You could use the repo for 2d/3d visualization (image/video) by simply running vis.sh

Example: sh vis.sh acro2 a-frame1 30 '2d3d'

Result will be saved in ./out.

Different visualisation options:
* 2d: visualize RGB along with 2D pose projection.
* 3d: visualize 3D skeletons.
* 2d3d: visualize RGB along with 2D pose projection/ corresponding 3D skeletons at the same time.


---
### Use the data for different tasks
The dataset could be used for multiple tasks such as human motion prediction/generation, pose estimation etc.

For writing the dataloader, please refer to [code](https://github.com/GUO-W/MultiMotion), which is a repo for 3D motion prediction (where only mocap 3D data is used) if needed.
For train/test split protocols, please refer to [paper](https://arxiv.org/abs/2105.08825) if needed.

If you would like to just choose a few views for tasks such as human nerf / pose estimation from single-/multi- views, we suggest to use the following views which are four approximate ortogonal views having the actors near the center of the figure.:
* acro1: cam-012 / cam-020 / cam-030 / cam-038
* acro2: cam-011 / cam-019 / cam-030 / cam-037

When processing monocular RGB pose estimation, we suggest that you take all these 4 views (or more) into consideration (so you will enlarge the dataset by x4 times).

---
### Citing
If you find our code or data helpful, please cite our work
 
@article{guo2021multi,
    title={Multi-Person Extreme Motion Prediction}, 
    author={Wen,Guo and Xiaoyu, Bie and Xavier, Alameda-Pineda, Francesc,Moreno-Noguer}, 
    journal={arXiv preprint arXiv:2105.08825}, 
    year={2021} }
