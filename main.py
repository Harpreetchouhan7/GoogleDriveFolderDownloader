from file_downloader import downloader
from folder_checker import inside_folder_checker
from file_checker import inside_file_checker
folder_url=input('Enter Public Url of Google Drive Folder: ')
a=0
try:
    filelist=inside_file_checker(url=folder_url)
    for i in filelist:
        a=a+1
        downloader(i)
    if len(inside_folder_checker(url=folder_url))>0:
        new_folder_list=inside_folder_checker(url=folder_url)
        for folder_url_inside in new_folder_list:
            file_list=inside_file_checker(url=folder_url_inside)
            for file in file_list:
                a=a+1
                downloader(url_token=file)
            if len(inside_folder_checker(url=folder_url_inside))>0:
                new_new_folder_list=inside_folder_checker(url=folder_url_inside)
                for folder_url_inside_inside in new_new_folder_list:
                    new_file_list_inside=inside_file_checker(url=folder_url_inside_inside)
                    for new_file_list in new_file_list_inside:
                        a=a+1
                        downloader(url_token=new_file_list)
                    if len(inside_folder_checker(url=folder_url_inside_inside))>0:
                        new_new_new_folder_list=inside_folder_checker(url=folder_url_inside_inside)
                        for folder_url_inside_inside_inside in new_new_new_folder_list:
                            new_new_file_list_inside=inside_file_checker(url=folder_url_inside_inside_inside)
                            for new_new_file_list in new_new_file_list_inside:
                                a=a+1
                                downloader(url_token=new_new_file_list)
    print('Total Number Of files Downloaded is '+str(a))
except:
    print('Please Enter vaild Url Folder')