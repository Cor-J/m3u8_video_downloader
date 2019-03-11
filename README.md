# m3u8_downloader



## 本程序会根据m3u8格式下载视频文件，并自动合并。


- 安装本包

    >pip install m3u8_video_downloader

- 想要使用这个，您需要在您想要保存视频的本地文件夹下，创建一个"readme.txt"文档。

    注意：本程序会从 "START"之后的内容开始下载，跳过之前的。
    
    内容如下：
    
    
    video_name_1
    
    http://example1.m3u8
    
    ---------------START------------------
    
    video_name_2
    
    http://example2.m3u8
    
-  之后,在你想保存视频的文件夹下执行cmd 操作：
    
    >m3u8_video_downloader

