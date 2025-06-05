import os


def get_badges_url():
    files = []
    folder_url = "C:/Users/admin/Desktop/my-web-app/static/img/Badges"
    for i in os.listdir(folder_url):
        files.append(i)
    return files