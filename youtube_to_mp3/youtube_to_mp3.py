import os
import subprocess
import datetime
from pytubefix import YouTube

parent_dir = 'D:\\mp3'


def youtube_to_mp3_convert(youtube_url: str):

    yt = YouTube(youtube_url)  # 크라잉넛  밤이깊었네
    yt.check_availability()

    print("영상 제목 : ", yt._title)

    print("영상 평점 : ", yt.rating)

    print("영상 썸네일 링크 : ", yt.thumbnail_url)

    print("영상 설명 : ", yt.description)

    vids = yt.streams.all()

    for i in range(len(vids)):
        print(i, '. ', vids[i])

    vnum = 0
    print(f"parent_dir : {parent_dir} - {vids[vnum]}")
    vids[vnum].download(parent_dir)

    default_filename = vids[vnum].default_filename
    # Windows 파일명에 사용할 수 없는 문자 제거
    invalid_chars = '<>:"|?*\\/'
    for char in invalid_chars:
        default_filename = default_filename.replace(char, "")
    print("default_filename : " + default_filename)

    lv_tmpFileNm, lv_tmpExtend = os.path.splitext(default_filename)

    print("lv_tmpFileNm : " + lv_tmpFileNm)
    print("lv_tmpExtend : " + lv_tmpExtend)

    new_filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    os.rename(parent_dir + '\\' + default_filename, parent_dir + '\\' + new_filename + lv_tmpExtend)

    subprocess.call(['E:\\utility\\ffmpeg\\bin\\ffmpeg', '-i', os.path.join(parent_dir, new_filename + lv_tmpExtend), os.path.join(parent_dir, new_filename + '.mp3')])

    os.rename(parent_dir + '\\' + new_filename + '.mp3', parent_dir + '\\' + lv_tmpFileNm + '.mp3')
    os.rename(parent_dir + '\\' + new_filename + lv_tmpExtend, parent_dir + '\\' + lv_tmpFileNm + lv_tmpExtend)

    print("동영상 다운로드및 mp3 변환 완료!!")



if __name__ == "__main__":

    youtube_list = [
        "https://www.youtube.com/watch?v=UJWd9JBGVC4&list=RDUJWd9JBGVC4&start_radio=1"
    ]

    for item_url in youtube_list:
        try:
            youtube_to_mp3_convert(item_url)
        except Exception as e:
            print(f"Error : {item_url} - {e}")
            continue
