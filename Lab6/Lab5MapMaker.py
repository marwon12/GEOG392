#imports
import arcpy
#listing/creating the project
project = arcpy.mp.ArcGISProject(
    r"C:\Users\marwon12\Desktop\Lab6\map\map.aprx")
#creating map project
campus = project.listMaps('Map')[0]
#testing if it works
#print(campus.name)

#creating and testing layers
layers = campus.listLayers()
for layer in layers:
    #goes through layers and only outputs the feature layers
    if layer.isFeatureLayer == True:
        #lowercases the names checks if the feature class is correctly named
        if layer.name.lower() == "GarageParking".lower():
            symbology = layer.symbology
            #checks if the sybology is a renderer and creates the color and the breakcount
            if hasattr(symbology,"renderer") == True:
                symbology.updateRenderer("GraduatedColorsRenderer")
                symbology.renderer.breakCount = 5
                symbology.renderer.colorRamp = project.listColorRamps("Blues (continuous)")[0]
                layer.symbology = symbology
project.saveACopy(r"C:\Users\marwon12\Desktop\Lab6\map\mapTest.aprx")          
