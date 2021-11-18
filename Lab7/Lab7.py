import arcpy

#RS composite bands
#setting up file paths and variables for each band
blueBand = arcpy.sa.Raster(r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab7\LT05_L2SP_026039_20040425_20200903_02_T2_SR_B1.TIF")
GreenBand = arcpy.sa.Raster(r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab7\LT05_L2SP_026039_20040425_20200903_02_T2_SR_B2.TIF")
redBand = arcpy.sa.Raster(r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab7\LT05_L2SP_026039_20040425_20200903_02_T2_SR_B3.TIF")
nirBand = arcpy.sa.Raster(r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab7\LT05_L2SP_026039_20040425_20200903_02_T2_SR_B4.TIF")
#Setting up the composite image as a variable
comp = arcpy.CompositeBands_management([blueBand, GreenBand, redBand, nirBand], r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab7\comp.tif")


#hillshade
source = r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab7"
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(source + r"\n30_w097_1arc_v3.tif", source + r"\n30_w097_1arc_v3_hillshade.tif", azimuth, altitude, shadows, z_factor)

#slope
source = r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab7"
output_measurment = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(source + r"\n30_w097_1arc_v3.tif", source + r"\n30_w097_1arc_v3_slope.tif",  output_measurment, z_factor)
