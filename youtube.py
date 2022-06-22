import pytube

print("URL: ")
url = input()

pytube.YouTube(url).streams.breakget_highest_resolution().download(
    'D:\Alexon\Descargas')
