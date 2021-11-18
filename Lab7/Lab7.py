import arcpy



#slope
source = r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab7"
output_measurment = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(source + r"\n30_w097_1arc_v3.tif", source + r"\n30_w097_1arc_v3_slope.tif",  output_measurment, z_factor)
