#!/usr/bin/python3                                                                                                                                    
from PIL import Image                                                                                                                              
from resizeimage import resizeimage                                                                                                                   
count = 330

with open('oscar', 'r+b') as f:

     while count:
          line = f.readline()
          line2 = (str(line).split("'"))[1]
          line3 = ((line2.split("\\n"))[0].split("."))
          new_name = line3[0] + "." + line3[1] + ".cover." + line3[2]
          file_name = ".".join(line3)
          with open(file_name, 'r+b') as file_img:
               with Image.open(file_img) as image:
                    cover = resizeimage.resize_cover(image, [560, 315])
                    cover.save(new_name, image.format)
          count -= 1
