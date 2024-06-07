# VideoProcessor

A simple program that extracts `.mp4` files from `.tar` files. Next, it will aggregate the `.mp4` files with `VideoInstruct_Dataset.json` to attach each question and answer label. This has been done with the goal of creating a clean and effective dataset to train a Large Multi-Modal Language Model.

## Usage

### main.py

- `tar_dir`: Filepath where `.tar` files containing `.mp4` will be placed (e.g., `tar_train` folder).
- `extract_path`: Filepath where you want the extracted `.mp4` files to be placed (e.g., `tar_output` folder).
- `annotations_json_path`: Path to the `VideoInstruct_Dataset.json` file.
- `output_file_path`: Filepath where the successfully annotated `.json` file will be placed (e.g., `Jsonoutput` folder).

### Example

```python
tar_dir = '/Users/shaoern/Desktop/SITNIVIDIA/tar_train'
extract_path = '/Users/shaoern/Desktop/SITNIVIDIA/tar_train/tar_output'
annotations_json_path = '/Users/shaoern/Desktop/SITNIVIDIA/VideoInstruct_Dataset.json'
output_file_path = '/Users/shaoern/Desktop/SITNIVIDIA/Jsonoutput/combined_data.json'


### Functions
tarextract(folderPath, outputPath)
Extracts all .mp4 files from .tar files in the specified folder and places them in the output directory.

combine_annotations_with_videos(jsonPath, videoFilesDict, outputFilePath)
Combines the annotations from the JSON file with the extracted .mp4 files and outputs a new JSON file with the annotated data.
```

### Credits
Source: https://github.com/mbzuai-oryx/Video-ChatGPT