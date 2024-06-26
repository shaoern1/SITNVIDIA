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
tar_dir = "../tar_train"
extract_path = "../tar_train/tar_output"
annotations_json_path = "../data/VideoInstruct_Dataset.json"
output_file_path = "../Jsonoutput/combined_data.json"


### Functions
tarextract(folderPath, outputPath)
Extracts all .mp4 files from .tar files in the specified folder and places them in the output directory.

combine_annotations_with_videos(jsonPath, videoFilesDict, outputFilePath)
Combines the annotations from the JSON file with the extracted .mp4 files and outputs a new JSON file with the annotated data.
```
### Updates
10 June 2024
- Updated "functions.py" to include video duration with "moviepy.editor" package
- Included ipynb file for initial and simple EDA on a subset of the dataset 

11 June 2024
- Refactor files to proper format

### Credits
Source: https://github.com/mbzuai-oryx/Video-ChatGPT