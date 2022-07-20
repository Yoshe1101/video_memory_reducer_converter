import os
files = os.listdir()
video_files = [i for i in files if '.mp4' in i]

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