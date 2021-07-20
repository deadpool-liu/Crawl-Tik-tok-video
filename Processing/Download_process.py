# encoding = utf-8
# 将文件转移到OnParsing这个文件夹中
import os
import time
import shutil
import requests


class DownloadProcessing(object):
    def __init__(self):
        self.urls = "../Temp/data.txt"
        self.video_path = "../Video"
        self.new_file_name = str(time.time())[:10]
        self.on_parsing_dir = "../OnParsing"
        self.new_file = ""
        self.bug_log = "../Buglog"
        self.request_dir = ["Buglog", "OnParsing", "Processing", "Temp", "Video"]
        self.special_str = list(open("./special_str/special_str.txt", encoding="ISO-8859-1"))[0]

    def move_url_to_on_parsing(self):
        for d in self.request_dir:
            if not os.path.exists("../" + d):
                os.mkdir("../" + d)

        old_file = self.urls
        new_file = self.on_parsing_dir + "/" + self.new_file_name + ".txt"
        self.new_file = new_file

        shutil.move(old_file, new_file)
        print("当前解析文件", new_file)
        # with open(self.urls, "w", encoding="utf-8") as f:
        #     f.write("1")

    def parse_url(self):
        video_url = []
        f = open(self.new_file, encoding="ISO-8859-1")

        for line in f:
            line = "http://" + line.replace(self.special_str, "")

            if "=&vr=" in line:
                # print(line)
                video_url.append(line)

        return set(video_url)

    @staticmethod
    def get_url_content(url):
        state = False
        request_count = 1
        max_request_count = 5
        while not state:
            try:
                time.sleep(1)
                content = requests.get(url).content
                return content
            except Exception as e:
                # t = time.localtime()
                # log_file_name = str(t[0]) + "_" + str(t[1]) + "_" + str(t[2]) + ".txt"   # 2021_7_23.txt
                # log_time = str(t[0]) + "_" + str(t[1]) + "_" + str(t[2]) + str(t[3]) + "_" + str(t[4])
                print("{:=^50}".format("出错啦！10秒后重试，重试次数：{}/{}！".format(request_count, max_request_count)))
                print("Bug-info:", e)
                # with open(self.bug_log + log_file_name, "a") as f:
                #     f.write(log_time + "|" + str(Exception))
                if request_count <= max_request_count:
                    time.sleep(10)
                    request_count += 1
                else:
                    return None

    def download_video(self):
        save_dir = self.video_path + "/" + self.new_file_name
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        for url in self.parse_url():
            print("{:=^50}".format("running"))
            print(url)
            video = self.get_url_content(url)
            video_name = save_dir + str(time.time())[:10] + ".mp4"
            if video:
                with open(video_name, "wb") as f:
                    f.write(video)
                print("已保存视频：{}".format(video_name))


if __name__ == '__main__':
    download = DownloadProcessing()
    if not os.path.exists(download.urls):
        print("请先运行Fiddler并滑动浏览器后再启动本程序，10秒后自动退出运行！")
        time.sleep(10)
    else:
        print("{:=^50}".format("正在运行"))
        while True:
            download.move_url_to_on_parsing()
            download.download_video()

            time.sleep(600)
            print("{:=^50}".format("每10分钟自动爬取一次数据"))
            # 更新保存的文件名
            download.new_file_name = str(time.time())[:10]


