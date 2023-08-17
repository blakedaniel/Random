from moviepy.editor import VideoFileClip
from os import path
import argparse

def convert_mov_to_gif(input_path:str, output_path:str, fps=10):
    input_path = path.expanduser(input_path)
    output_path = path.expanduser(output_path)
    clip = VideoFileClip(input_path)
    clip.write_gif(output_path, fps=fps)
    clip.close()

def main():
    parser = argparse.ArgumentParser(description='Convert mov to gif')
    parser.add_argument('input_path', type=str, help='input path')
    parser.add_argument('output_path', type=str, help='output path')
    args = parser.parse_args()
    
    input_path = args.input_path
    output_path = args.output_path
    convert_mov_to_gif(input_path, output_path)
    
if __name__ == '__main__':
    main()
