from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

print("Title: ", yt.title)

choice = input("Do you want audio or video? ")

if choice == "audio":
    a = yt.streams.filter(only_audio=True)
    a[0].download(r"D:\Users\tsili\Downloads\Youtube Downloader\Audio")

if choice == "video":
    v = yt.streams.get_highest_resolution()
    v.download(r"D:\Users\tsili\Downloads\Youtube Downloader\Video")

else:
    print('Enter "audio" or "video"')
