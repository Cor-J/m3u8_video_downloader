# m3u8_downloader


## You can use this for downloading video files by m3u8 links.

### How to install

    > pip install m3u8_video_downloader
    
      
### How to use

Two example of order is given as follow:

    > m3u8-video-downloader -n <your file name> - u <m3u8 url> -p <save path> -c<cpu number>
    
    > m3u8_video_downloader -n <name> -u <http://example1.m3u8> -p <G://example_path> -c<3>

If no saved path is given, the path where you are using the cmd is regarded as the default path.


- 1.If name and url parameters are not given, this program will find a "readme.txt" in the path, and download videos which addresses are written in this file.


    - The txt file should be written as follow format:


            video_name_1
            
            http://example1.m3u8
            
            ---------------START------------------
            
            video_name_2
            
            http://example2.m3u8
        
        
    - This program will ONLY download files bellow the string "START"

- 2.If the url and name are given, this program will download video from these parameters and save it.

    The "cpu number" shows how many cpu this program will use to download the video, the default number is half of your cpu numbers. You can set values to this parameter. if the number is less than 1, it means how much percent of the total cpu is used. If is an integer, it gives the number of cpu is used. If it is set as -1, it means using all the cpu resources(NOT RECOMMENDED).

  
