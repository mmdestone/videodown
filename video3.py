
# -*- coding: utf-8 -*-

# Created on 2018/3/22

 

 

import os

 

from Crypto.Cipher import AES

import requests

 
from multiprocessing import Pool
 

"""

下载M3U8文件里的所有片段

"""

 

 

 

 

def download(url):

    download_path = "G:\download\m3u8"

    if not os.path.exists(download_path):

        os.mkdir(download_path)

    all_content = requests.get(url).text  # 获取M3U8的文件内容
    file_line = all_content.split("\n")  # 读取文件里的每一行
    #print (file_line)
    # 通过判断文件头来确定是否是M3U8文件

    if file_line[0] != "#EXTM3U":

        raise BaseException("非M3U8的链接")

    else:

        unknow = True  # 用来判断是否找到了下载的地址

        for index, line in enumerate(file_line):

            if "EXTINF" in line:

                unknow = False

                # 拼出ts片段的URL
                #name=(file_line[index + 1]).rsplit("/", 1)[1]
                name=file_line[index + 1]
                pd_url = url.rsplit("/", 1)[0] + "/" + name
                print(pd_url)
                res = requests.get(pd_url)

                c_fule_name = str(file_line[index + 1])
                print(c_fule_name)
                key ="f2XTSovd78yA9uHJ"
                cryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC)
                with open(download_path + "\\" + name, 'wb') as f:
                    f.write(cryptor.decrypt(res.content))
                    #f.write(res.content)

                    f.flush()
      
        if unknow:

            raise BaseException("未找到对应的下载链接")

        else:

            print("下载完成")


if __name__ == '__main__':
    pool = Pool(10)
    pool.apply_async(download("https://www.qzamfz.com/20190903/UPR8cbhz/index.m3u8")) #执行任务
    pool.close()
    pool.join()

    
    #cmd copy /b d:\xxx\download_ts\*   d:\xxx\download_ts\new.mp4