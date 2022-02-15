from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

print("Title: ", yt.title)

choice = input("Do you want audio or video? ")

if choice == "audio":
    a = yt.streams.filter(only_audio=True)
    a[0].download(r"your Path to download your audio")

if choice == "video":
    v = yt.streams.get_highest_resolution()
    v.download(r"your Path to download your video")

else:
    print('Enter "audio" or "video"')
