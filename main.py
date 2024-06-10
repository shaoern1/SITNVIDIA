from functions import VideoProcessor

# Define paths
tar_dir = "/Users/shaoern/Desktop/SITNVIDIA/tar_train"
extract_path = "/Users/shaoern/Desktop/SITNVIDIA/tar_train/tar_output"
annotations_json_path = "/Users/shaoern/Desktop/SITNVIDIA/VideoInstruct_Dataset.json"
output_file_path = "/Users/shaoern/Desktop/SITNVIDIA/Jsonoutput/combined_data.json"

# Initialize the VideoProcessor
processor = VideoProcessor(tar_dir, extract_path, annotations_json_path, output_file_path)

# Extract tar files and combine annotations
processor.extract_tar_files()
processor.combine_annotations_with_videos()
