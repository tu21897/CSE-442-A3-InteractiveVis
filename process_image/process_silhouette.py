from multiprocessing.connection import wait
from PIL import Image
import time

def main():
    # img = Image.open("process_image/full_silhouette_fix.png")
    # img_transparent = Image.open("process_image/full_silhouette_fix_transparent.png")
    img_mirror = Image.open("process_image/full_silhouette_fix_transparent_mirror.png")
    # img_down_arrow = Image.open("process_image/down_arrow.png")
    # img_tube = Image.open("process_image/tube.png")
    # data = img_transparent.convert("RGBA").getdata()
    data2 = img_mirror.convert("RGBA").getdata()
    # data3 = img_down_arrow.convert("RGBA").getdata()
    # data4 = img_tube.convert("RGBA").getdata()
    # data = img.convert("RGBA").getdata()
    # cycle_rgba_rounding(150, 170, True, data, img)
    # change_img_color(img_transparent, data, (42,126,191,255), "docs/silhouette_final.png")
    # change_img_color(img_mirror, data2, (29,28,35,255), "docs/silhouette_final_mirror.png")
    change_img_color(img_mirror, data2, (42,126,191,255), "docs/silhouette_final_mirror2.png")
    # change_img_color2(img_down_arrow, data3, (42,126,191,255), "docs/down_arrow_final.png")
    # change_img_color2(img_tube, data4, (42,126,191,255), "docs/tube_final.png")

    

def cycle_rgba_rounding(a, b, transparent, data, img):
    replace_data =[]
    for i in range(a, b):
        for pix_rgba in data:
            if pix_rgba[0] < i or pix_rgba[1] < i or pix_rgba[2] < i:
                replace_data.append((0,0,0,255))
            else:
                if (transparent):
                    replace_data.append((255,255,255,0))
                else:
                    replace_data.append((255,255,255,255))
        img.putdata(replace_data)
        img.save("process_image/full_silhouette_fix_transparent.png", format="png")
        replace_data = []
        print("iteration value: ", i)
        time.sleep(0.1)

def change_img_color(img, data, color, dest):
    replace_data = []
    for pix_rgba in data:
            # print(pix_rgba)
            if pix_rgba[3] == 0:
                replace_data.append(pix_rgba)
            else:
                replace_data.append(color)
    img.putdata(replace_data)
    img.save(dest, format="png")

def change_img_color2(img, data, color, dest):
    replace_data = []
    for pix_rgba in data:
            # print(pix_rgba)
            if (pix_rgba[0] > 200 and pix_rgba[1] > 200 and pix_rgba[2] > 200):
                replace_data.append((255,255,255,0))
            else:
                replace_data.append(color)
    img.putdata(replace_data)
    img.save(dest, format="png")

if __name__ == "__main__":
    main()