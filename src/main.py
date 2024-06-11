from src.functions import VideoProcessor

# Define paths
tar_dir = "../tar_train"
extract_path = "../tar_train/tar_output"
annotations_json_path = "../data/VideoInstruct_Dataset.json"
output_file_path = "../Jsonoutput/combined_data.json"

# Initialize the VideoProcessor
processor = VideoProcessor(tar_dir, extract_path, annotations_json_path, output_file_path)

# Extract tar files and combine annotations
processor.extract_tar_files()
processor.combine_annotations_with_videos()
