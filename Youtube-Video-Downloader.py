    # Download Youtube video using python.

    # 1.Import pytube library and make sure it is up to date
    from pytube import YouTube
    # 2.Create a variable and store the video link
    link = input("enter URL of video")
    # 3. Extract the video in the link as an object
    video = YouTube(link)
    # 4.Get the highest resolution stream available
    stream = video.streams.get_highest_resolution()
    # 5. download the stream
    # You can also determine the directory by giving the file location in the brackets
    stream.download()
    # 6.Tada you're file has been downloaded
    print("file downloaded")
