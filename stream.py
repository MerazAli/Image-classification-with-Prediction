# mkdir create a automatic directory image folder
!mkdir images

# This code tell about how much time take to execute a cell
!pip install ipython-autotime
%load_ext autotime


# Part 1: Data Gathering
# Donload all images in image folder
!pip install bing-image-downloader


from bing_image_downloader import downloader
downloader.download('Fast Cars',limit=10,output_dir='images')
downloader.download("sunflower" ,limit=20,output_dir='images')
downloader.download("ice cream cone",limit=10,output_dir='images')
downloader.download("rugby ball leather",limit=10,output_dir='images')
