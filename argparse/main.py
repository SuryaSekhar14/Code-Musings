import argparse

parser = argparse.ArgumentParser(description='Split an image or video file into multiple files, and also stitch them back together.')

parser.add_argument('file_path', metavar='file_path', type=str, help='Path to the file to be processed')

