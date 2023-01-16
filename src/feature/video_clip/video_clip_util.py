from typing import List
from src.model.subclip_info import SubClipInfo



class VideoClipUtil:
    def __init__(self):
        return

    def generate_subclip_info(self,
                              total_during: int,
                              split_range: int,
                              output_file_name: str) -> List[SubClipInfo]:
        full_range_count = int(total_during // split_range)
        rest = total_during % split_range
        result = []
        start = 0
        end = 0

        for index in range(full_range_count):
            start = end
            end = start + split_range
            suffix = '({}-{})'.format(index+1, full_range_count+1)
            subclip_file_name = self.add_suffix(output_file_name, suffix)
            time_range = SubClipInfo(start, end, subclip_file_name)
            result.append(time_range)

        suffix = '(last)'
        subclip_file_name = self.add_suffix(output_file_name, suffix)
        result.append(SubClipInfo(end, end + rest, subclip_file_name))

        return result

    def add_suffix(self, original_path, suffix):
        before_dot, dot, ext = original_path.rpartition(".")
        return before_dot+suffix+dot+ext
