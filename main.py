import os
from src.feature.file_path.file_path_util import FilePathUtil
from src.const import *
from src.feature.video_clip.video_clip import VideoClip
from src.feature.video_clip.video_clip_util import VideoClipUtil
from tkinter import filedialog

filepath = filedialog.askopenfilename()
vcu = VideoClipUtil()
vc = VideoClip(vcu)
fpu = FilePathUtil()

os.makedirs(OUTPUT_FILE_DIR, exist_ok=True)
file_name = fpu.get_file_name(filepath)
vc.output_splited_video(
    filepath,
    180,
    OUTPUT_FILE_DIR + file_name
)
