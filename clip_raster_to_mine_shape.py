# Import libraries.
import os
import subprocess

def rename_shapes(path):
    for shape in os.listdir(path):
        if shape.endswith("gpkg"):
            os.rename(path + shape, path + shape.split(".")[0] + ".shp")
    
#rename_shapes(r"C:/Users/Tim/Desktop/Myna/geology/data/mine_shapes_01/")

def clip_raster(shape, raster, raster_type):
    dest = shape.split("/")[-1].split(".")[0]
    dest = fr"C:/Users/Tim/Desktop/Myna/geology/data/cropped_outputs/{raster_type}/{dest}.tif"
    cmd = f"gdalwarp -overwrite -cutline {shape} -crop_to_cutline {raster} {dest}"
    p = subprocess.run(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, check=True)
    
    
shapes_list = [r"C:/Users/Tim/Desktop/Myna/geology/data/mine_shapes_01/" + i
               for i in os.listdir(r"C:/Users/Tim/Desktop/Myna/geology/data/mine_shapes_01/")]
raster = r"C:/Users/Tim/Desktop/Myna/geology/data/gravity/WA_400m_Grav_Merge_v1_2019.jp2"
if __name__ == "__main__":
    for i, shape in enumerate(shapes_list):
        if i % 50 == 0:
            print(f"Clipping is {(i / len(shapes_list)) * 100}% complete.")
        clip_raster(shape, raster, "gravity")