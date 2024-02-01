import os
from split_image import split_image, reverse_split
import subprocess
import re
# !!! Make sure FFMPEG is installed and added to PATH variables

directory_path = "toProcess"
processed_dir = os.path.join("processed")
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png")
VIDEO_EXTENSIONS = (".mp4", ".mov")
IMAGE_SLICES_ROWS = 2
IMAGE_SLICES_COLUMNS = 2


def split_large_video_files(file_path, processed_dir):
    """
    Split .mp4 and .mov files into multiple parts of 5 seconds each of HD resolution using FFMPEG 
    and save them as .mp4 in a directory called <filename> in the "processed" directory
    """

    # use ffmpeg to split the file into parts of 5 seconds each and re-encode the file in 1080p/HD Resolution
    cmd = ["ffmpeg", "-i", file_path, "-vf", "scale=1920:1080", "-reset_timestamps", "1", "-sc_threshold", "0", "-g", "5",
                   "-force_key_frames", "expr:gte(t, n_forced * 5)", "-segment_time", "5", "-f", "segment",
                   os.path.join(processed_dir, f"{os.path.splitext(file)[0]}_part%03d.mp4")]
            
    subprocess.run(cmd)


def stitch_video_back_together(file_path):
    """
    Stitch the video back together from the parts in the "processed" directory
    """
    pass


def split_large_image_files(file_path):
    """
    Split an image into 4 parts of equal size and save them in a directory called <filename> in the "processed" directory

    Usage: split_image(image_path, rows, cols, should_square, should_cleanup, [output_dir])
    """
    split_image(file_path, IMAGE_SLICES_ROWS, IMAGE_SLICES_COLUMNS, False, False, False, f"processed/{os.path.splitext(file)[0]}")


def stitch_image_back_together(image_path):
    """
    Stitch the image back together from the parts in the "processed" directory
    """
    print(os.listdir(f"processed/{image_path}/"))

    start_name, ext = os.path.splitext(image_path)
    print(start_name, ext)
    # Find all files that start with the same name as the image,
    # followed by "_" and a number, and with the same file extension.

    expr = re.compile(r"^" + start_name + "_\d+" + ext + "$")
    print(expr)

    paths_to_merge = sorted([f for f in os.listdir(
        f"processed/{image_path}/") if re.match(expr, f)], key=lambda x: int(x.split("_")[-1].split(".")[0]))
    print(paths_to_merge)

    reverse_split(paths_to_merge, IMAGE_SLICES_ROWS,
                    IMAGE_SLICES_COLUMNS, image_path, False, False)


if __name__ == "__main__":

    '''
    for file in os.listdir(directory_path):
        with open("processed.txt", "a+") as f:
            if file in f.read():
                continue
            else:
                f.write(file + "\n")
        file_path = os.path.join(directory_path, file)
    '''

    # loop through all the files in the directory and check if they have been processed before by checking if the folders with the same names exists in the "processed" directory
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        processed_video_file_path = os.path.join(processed_dir, f"{os.path.splitext(file)[0]}")
        processed_image_file_path = os.path.join(processed_dir, f"{os.path.splitext(file)[0]}")

        # check if the file has been processed before
        if os.path.exists(processed_video_file_path):
            continue
        elif os.path.exists(processed_image_file_path):
            continue
        else:
            with open("processed.txt", "a") as f:
                f.write(f"{file}\n")

    # check if the file is an MP4 or MOV file and if it is larger than 20MB
        if file.lower().endswith(VIDEO_EXTENSIONS) and os.path.getsize(file_path) > 20 * 1024 * 1024:
            os.mkdir(f"processed/{os.path.splitext(file)[0]}")
            split_large_video_files(file_path, f"processed/{os.path.splitext(file)[0]}")
        elif file.lower().endswith(IMAGE_EXTENSIONS):
            split_large_image_files(file_path)


# stitch_image_back_together("wallpaper.jpg")