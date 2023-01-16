from moviepy.video.io.VideoFileClip import VideoFileClip
from .video_clip_util import VideoClipUtil


class VideoClip:
    def __init__(self, util: VideoClipUtil):
        self.util = util

    def output_splited_video(self, input_file_path, split_range, output_file_path):
        clip = VideoFileClip(input_file_path)
        print("output_file_path: {}".format(output_file_path))
        time_range_list = self.util.generate_subclip_info(
            clip.duration,
            split_range,
            output_file_path,
        )
        for subclip_info in time_range_list:
            part = clip.subclip(subclip_info.start, subclip_info.end)
            print(subclip_info.file_name)
            part.write_videofile(subclip_info.file_name)
