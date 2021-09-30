import arcpy

#creates an event layer from csv and converts it into a feature class in a new GDB
arcpy.env.overwriteOutput = True

arcpy.CreateFileGDB_management(r"C:\Users\marwon12\Desktop\Lab4","Lab4GDB")

return1 = arcpy.MakeXYEventLayer_management(r"C:\Users\marwon12\Desktop\Lab4\garages.csv","x","y","garage")

arcpy.FeatureClassToGeodatabase_conversion(r"C:\Users\marwon12\Desktop\Lab4,Lab4GDB")

#copies a feature class from another GDB into our new GDB
arcpy.CopyParameter(r"C:\Users\marwon12\Desktop\Lab4\Campus.gdb\structures",r"C:\Users\marwon12\Desktop\Lab4\Lab4GDB.gdb\structures")

#extracts the spatial information from the feature class
spatial_ref = arcpy.Describe(r"C:\Users\marwon12\Desktop\Lab4\Lab4GDB.gdb\structures").spatialReference