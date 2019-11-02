import os
import glob

left = os.listdir("left/image_02/data")
right = os.listdir("right/image_03/data")
s = ""
file = open("split.txt", "w") 
for l, r in zip(left, right):
    try:
        l_frame = l.replace(".jpg", "")
        r_frame = r.replace(".jpg", "")
        file.write("left {} l\n".format(int(l_frame)))
        file.write("right {} r\n".format(int(r_frame)))
    except:
        print("skipped")

# for filename in os.listdir("image_03"):
#     frame = filename.replace("frame", "").replace(".jpg", "")
#     src = "image_03/" + filename
#     try:
#         dst = "image_03/" + "0"*(10-len(str(int(frame)))) + str(int(frame)) + ".jpg"
#         os.rename(src, dst) 
#     except:
#         print("skipped")
    


file.close()
