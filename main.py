from functions import VideoProcessor

# Define paths
tar_dir = "/Users/shaoern/Desktop/SITNIVIDIA/tar_train/"
extract_path = "/Users/shaoern/Desktop/SITNIVIDIA/tar_train/tar_output"
annotations_json_path = "/Users/shaoern/Desktop/SITNIVIDIA/VideoInstruct_Dataset.json"
output_file_path = "/Users/shaoern/Desktop/SITNIVIDIA/Jsonoutput/combined_data.json"

# Initialize the VideoProcessor
processor = VideoProcessor(tar_dir, extract_path, annotations_json_path, ou]tput_file_path)

# Extract tar files and combine annotations
processor.extract_tar_files()
processor.combine_annotations_with_videos()
