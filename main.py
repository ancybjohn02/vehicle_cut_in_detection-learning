import cv2
import numpy as np
from trajectory_pred.scs.utils.config import Config
from trajectory_pred.scs.main_model import MainModel
from trajectory_pred.scs.datascripts.dataset_argoverse import ArgoverseDataset
from vci import speed_acc_dist

# Load the trajectory prediction model
config = Config()
model = MainModel(config)
model.load_weights('trajectory_pred/saved_model')

# Load the Argoverse dataset
dataset_dir = 'argoverse/tracking/dataset'
log_id = 'sequence_name'
speed_acc_dist_module = speed_acc_dist.SpeedAccDist(dataset_dir, log_id)

def detect_cut_in(video_feed):
    # Initialize the video capture
    cap = cv2.VideoCapture(video_feed)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Preprocess the frame
        frame = cv2.resize(frame, (640, 480))
        frame = frame / 255.0
        
        # Extract the trajectory prediction output
        trajectory_output = model.predict(frame)
        
        # Calculate the relative speed, acceleration, and distance
        speeds, accelerations, distances, ttcs = speed_acc_dist_module.calculate()
        
        # Check if it's a cut-in
        for track_id, ttc in ttcs.items():
            if 0.5 < ttc[-1] < 0.7:
                print("Warning: Cut-in detected for track ID", track_id)
                # Send a warning signal 
        
        # Visualize the output 
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # Use a video file or camera feed
    video_feed = 'video/file'  # or 0 for camera feed
    detect_cut_in(video_feed)