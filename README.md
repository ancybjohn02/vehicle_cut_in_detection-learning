# **Vehicle Cut-in Detection using Nuscenes and Argoverse Datasets**
===========================================================================================================


https://github.com/ancybjohn02/vehicle_cut_in_detection-learning/assets/116482955/a53ad57d-b92d-4b11-9c52-bafa0468d430



**Overview**
-----------

This project focuses on detecting vehicle cut-ins by leveraging advanced computer vision and machine learning techniques to enhance road safety and improve the decision-making capabilities of autonomous vehicles. By utilizing two renowned autonomous driving datasets, NuScenes and Argoverse, the system is trained and evaluated under realistic traffic scenarios to ensure robustness and reliability. The proposed framework integrates multiple components, including a Trajectory Prediction Module that forecasts future vehicle movements using deep learning models, a Speed, Acceleration, and Distance Calculation Module that derives dynamic motion parameters from trajectory data, and a Cut-in Detection Module that identifies potential cut-in events based on these motion cues. Together, these modules work cohesively to build a real-time, intelligent system capable of detecting risky lane-change behaviors, thereby contributing to safer and more efficient autonomous driving systems.


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

Two datasets are used in this project, they are:

1. **Nuscenes**: A public autonomous driving dataset containing 1000 scenes, each 20 seconds long, with 360-degree camera and lidar data.
2. **Argoverse**: A public autonomous driving dataset containing 324 scenes, each 30 seconds long, with 360-degree camera and lidar data.

**Project Components**
---------------------

1. **Trajectory Prediction**:
   - Predicts future vehicle trajectories using deep learning architectures such as LSTM and Transformer-based models.
   - Incorporates past trajectory data, heading angle, and velocity profiles to forecast motion up to several seconds ahead.
   - Trained and evaluated using the NuScenes dataset, which provides high-resolution annotated trajectories for multiple agents in urban traffic scenes.
     
2.  **Speed, Acceleration, and Distance Calculation**:
   - Computes the relative speed, acceleration, and inter-vehicle distance between the ego vehicle and surrounding vehicles.
   - Uses trajectory data from the Argoverse Motion Forecasting Dataset, leveraging its accurate localization and temporal synchronization features.
   - Provides a continuous dynamic state profile that serves as an input for real-time risk assessment.
     
3. **Cut-in Detection**:
   - Detects cut-in maneuvers based on the relative motion metrics derived from the previous module.
   - Utilizes threshold-based and learning-based models (e.g., Random Forest, CNN-LSTM hybrids) to determine potential cut-in events.
   - Integrates visual cues (bounding box positions, lane markings, and heading vectors) to improve detection accuracy in complex traffic scenes.
     
**How to Run**
--------------

1. Install the required packages by running `pip install -r requirements.txt`.
2. Run the `main.py` file
3. Provide a video file or camera feed as input to the `detect_cut_in` function.

**Project Presentation**
------------------------

Here is the presentation for our project, detailing our approach to detecting vehicle cut-ins using Nuscenes and Argoverse datasets to enhance road safety and autonomous vehicle performance.

[Vehicle cut-in detection .pptx](https://github.com/user-attachments/files/16132086/Vehicle.cut-in.detection.pptx)

**Project Report**
--------------------

[Vehicle cut-in detection_Tech Geeks-1.pdf](https://github.com/user-attachments/files/16140442/Vehicle.cut-in.detection_Tech.Geeks-1.pdf)



**Note**
-----

This project is a work in progress, and the code may change. Please report any issues or suggestions to the maintainers to help us improve the project. Open-source contributions help us enhance the system, benefiting the community.

**Acknowledgments**
---------------

We acknowledge the creators of the Nuscenes and Argoverse datasets for providing high-quality data for autonomous driving research.
