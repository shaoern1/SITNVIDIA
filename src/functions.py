import json
import tarfile
import os
from moviepy.editor import VideoFileClip

class VideoProcessor:
    def __init__(self, tar_dir, extract_path, annotations_json_path, output_file_path):
        self.tar_dir = tar_dir
        self.extract_path = extract_path
        self.annotations_json_path = annotations_json_path
        self.output_file_path = output_file_path
        self.video_files = {}

    def extract_tar_files(self):
        if not os.path.exists(self.extract_path):
            os.makedirs(self.extract_path)

        for filename in os.listdir(self.tar_dir):
            file_path = os.path.join(self.tar_dir, filename)
            if os.path.isfile(file_path) and tarfile.is_tarfile(file_path):
                with tarfile.open(file_path, 'r') as tar:
                    tar.extractall(path=self.extract_path)
                    for member in tar.getmembers():
                        if member.isfile():
                            video_id = os.path.splitext(os.path.basename(member.name))[0]
                            video_path = os.path.join(self.extract_path, member.name)
                            duration, framerate = self.get_video_properties(video_path)
                            self.video_files[video_id] = {
                                "path": video_path,
                                "duration": duration,
                                "framerate": framerate
                            }
        print("Extraction complete:", self.video_files)
        return self.video_files

    def get_video_properties(self, video_path):
        """Returns the duration and framerate of the video."""
        try:
            with VideoFileClip(video_path) as video:
                return video.duration, round(video.fps,2)
        except Exception as e:
            print(f"Error reading video properties from {video_path}: {e}")
            return None, None

    def combine_annotations_with_videos(self):
        """
        Combine annotations with video file paths and save to a new JSON file.
        """
        with open(self.annotations_json_path, 'r') as f:
            annotations_data = json.load(f)

        if annotations_data:
            print("First annotation entry:", json.dumps(annotations_data[0], indent=4))
        else:
            print("No data found in annotations JSON")

        combined_data = {}
        for annotation in annotations_data:
            video_id = annotation.get("video_id")
            video_info = self.video_files.get(video_id)
            if video_info:
                if video_id not in combined_data:
                    combined_data[video_id] = {
                        "video_id": video_id,
                        "video_path": video_info["path"],
                        "duration": video_info["duration"],
                        "framerate":video_info["framerate"],
                        "questions_and_answers": []
                    }

                if "q" in annotation and "a" in annotation:
                    combined_data[video_id]["questions_and_answers"].append({
                        "question": annotation["q"],
                        "answer": annotation["a"]
                    })

                if "qa_pairs" in annotation:
                    for qa_pair in annotation["qa_pairs"]:
                        combined_data[video_id]["questions_and_answers"].append({
                            "question": qa_pair.get("q", "No question found"),
                            "answer": qa_pair.get("a", "No answer found")
                        })
            else:
                print(f"Warning: No video file found for video_id: {video_id}")

        combined_data_list = list(combined_data.values())

        print(f"Writing combined data to {self.output_file_path}")
        with open(self.output_file_path, 'w') as f:
            json.dump(combined_data_list, f, indent=4)

        print(f"Combined data has been written to {self.output_file_path}")
        return combined_data_list