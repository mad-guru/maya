#this is a simple python script for Maya
#outputs fbx files of each selected object
#to work around pivot issues in Unreal, it moves the object to the origin
#then moves it back after
#4/26/17
#status code snippet. I wrote it quick for my use, needs to be expanded for wider use.
#http://www.madguru.com

import maya.cmds as cmds
import maya.mel as mel

#enter output path here with / eg 
path = 'D:/output/fbx/'
objLs = cmds.ls(sl=1)
for obj in objLs:
    cmds.select(obj)
    
    #store xforms
    prevXform = cmds.xform(q=1, m= 1, ws=1)
    
    #move to origin
    cmds.move(0, 0, 0, obj, rpr=True)
    
    #export fbx
    mel.eval('FBXExportFileVersion -v FBX201600')
    mel.eval('FBXExportInAscii -v true')
    mel.eval('FBXExportInputConnections -v false')
    mel.eval('FBXExportInstances -v false')
    mel.eval('FBXExportConvertUnitString \"cm\"')
    mel.eval('FBXExportSmoothMesh -v true')
 
    mel.eval('FBXExportUpAxis \"z\"')
    mel.eval('FBXExport -f \"'+path+obj+'.fbx\" -s')
    print ('FBXExport -f \"'+path+obj+'.fbx\" -s')
    #restore xforms
    cmds.xform(obj, ws=1, m=prevXform)
    
    
