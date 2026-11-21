# def youtube_id(url):
url="https://youtu.be/0bxKHywx-P4?si=owpM3UYGM1-RIoTG"
url = url.strip()
check=["watch?v=", "youtu.be/", "/shorts/"]
for i in check:
    if not i in url:
        pass
    else:
        if i == "watch?v=":
            marker= url.split("watch?v=")
        elif i == "youtu.be/":
            marker= url.split("youtu.be/")[-1]
        elif i == "/shorts/":
            marker= url.split("/shorts/")[-1]
video_id=marker[:11]
print(video_id)