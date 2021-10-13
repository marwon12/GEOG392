import arcpy

#creates an event layer from csv and converts it into a feature class in a new GDB
arcpy.env.overwriteOutput = True

arcpy.CreateFileGDB_management(r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4","Lab4GDB")

return1 = arcpy.MakeXYEventLayer_management(r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4\garages.csv","x","y","garage")

arcpy.FeatureClassToGeodatabase_conversion(return1,r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4\Lab4GDB.gdb")

#copies a feature class from another GDB into our new GDB
arcpy.Copy_management(r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4\Campus.gdb\Structures",r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4\Lab4GDB.gdb\Structures")

#extracts the spatial information from the feature class
spatial_ref = arcpy.Describe(r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4\Lab4GDB.gdb\Structures").spatialReference

#projects spatial reference onto garage points
arcpy.Project_management(r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4\Lab4GDB.gdb\garage",r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4\Lab4GDB.gdb\garage_projection", spatial_ref)

#Makes a buffer of 150 meters of the garage projection
return2 = arcpy.Buffer_analysis(r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4\Lab4GDB.gdb\garage_projection",r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4\Lab4GDB.gdb\garage_projection_buffer", 150)

#Makes a intersect fo the garage buffer and structures
arcpy.Intersect_analysis([r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4\Lab4GDB.gdb\Structures",r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4\Lab4GDB.gdb\garage_projection_buffer"],r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4\Lab4GDB.gdb\garage_projection_intersect", 'ALL')

#converts the table to have the projected cordinates
arcpy.TableToTable_conversion(r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4\Lab4GDB.gdb\garage_projection_intersect",r"C:\Users\Admin\Desktop\Fall2021Sylibi\GIS\GEOG392\Lab4","ConvertedTable.csv")
