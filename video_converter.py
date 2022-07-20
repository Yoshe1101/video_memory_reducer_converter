import os
import sys

imputs = sys.argv[1]
imputs.append(sys.argv[2])

for i in imputs:
    if "-ext " in i:
        extension = i
    if "-path " in i:
        new_path = i


def convert_video(extension = ".mp4", new_path = ""):
    
    if not isinstance(extension, str):
        print('the extension given is not a string format')
        return False

    if not isinstance(new_path, str):
        print('The path value is not a string')
        return False
    if new_path == "":
        print('Using current path')
    else:
        os.chdir(new_path)

    files = os.listdir()
    video_files = [i for i in files if extension in i]

    videos_to_convert = []
    for v in video_files:
        var_out = f'"{"converted_" + v}"'.replace(' ', '_')
        if var_out not in video_files and 'converted_' not in v:
            videos_to_convert.append(v)

    for video in videos_to_convert:
        input_file = f'"{video}"'
        output_file = f'"{"converted_" + video}"'.replace(' ', '_')

        try:
            command = f' ffmpeg -n -i {input_file} -vcodec libx265 -crf 28 {output_file}'
            os.system(command)
            print(command)
        except:
            print(f'There was a problem with the video format {input_file} -no')
            

    print('Vieo files have been converted')
    return True
if __name__ == "__main__":
    convert_video()
