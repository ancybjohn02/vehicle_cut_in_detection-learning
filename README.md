**Vehicle Cut-in Detection using Nuscenes and Argoverse Datasets**
============================================================


https://github.com/ancybjohn02/vehicle_cut_in_detection-learning/assets/116482955/a53ad57d-b92d-4b11-9c52-bafa0468d430



**Overview**
-----------

This project aims to detect vehicle cut-ins using computer vision and machine learning techniques. The project utilizes two popular autonomous driving datasets: Nuscenes and Argoverse. The goal is to develop a robust and accurate system that can detect cut-ins in real-time, enhancing road safety and autonomous vehicle performance.

**Folder Structure**
-------------------

The project folder structure is as follows:                  
.                                      
vci                              
├── main.py          
├── speed_acc_dist.py        
├── trajectory_pred        
│   ├── scs          
│   │   ├── datascripts          
│   │   │   ├── dataloader_nuscenes.py                                              
│   │   │   └── dataset_argoverse.py          
│   │   ├── modeling            
│   │   │   ├── decoder.py            
│   │   │   ├── global_graph.py            
│   │   │   ├── motion_refinement.py          
│   │   │   └── vectornet.py        
│   │   ├── utils            
│   │   │   ├── config.py            
│   │   │   ├── evaluation_metrics.py          
│   │   │   ├── loss.py            
│   │   │   ├── utils.py                          
│   │   │   └── visualise_nuscenes.py                      
│   │   ├── eval.py                      
│   │   ├── main_model.py                                
│   │   ├── test.py                                
│   │   └── train.py                              

**Dataset Description**
---------------------

Two datasets are used in this project:

1. **Nuscenes**: A public autonomous driving dataset containing 1000 scenes, each 20 seconds long, with 360-degree camera and lidar data.
2. **Argoverse**: A public autonomous driving dataset containing 324 scenes, each 30 seconds long, with 360-degree camera and lidar data.

**Project Components**
---------------------

1. **Trajectory Prediction**: A module that predicts the future trajectory of vehicles using a deep learning model.
2. **Speed, Acceleration, and Distance Calculation**: A module that calculates the relative speed, acceleration, and distance between vehicles using the Argoverse dataset.
3. **Cut-in Detection**: A module that detects cut-ins based on the calculated speed, acceleration, and distance values.

**How to Run**
--------------

1. Install the required packages by running `pip install -r requirements.txt`.
2. Run the `main.py` file
3. Provide a video file or camera feed as input to the `detect_cut_in` function.

**Note**
-----

This project is a work in progress, and the code is subject to change. Please report any issues or suggestions to the maintainers.

**Acknowledgments**
---------------

We acknowledge the creators of the Nuscenes and Argoverse datasets for providing high-quality data for autonomous driving research.
