#converts a sequence of images to ptex for use with xgen
#create map and save first frame before running via paint tool to convert to ptex
#madguru.com

import maya.cmds as cmds
import maya.mel as mel
import shutil

#########################
# variables
#########################
startFrame = 
endFrame = 

curColl = 'collectionName'
curDescr = 'descriptionName'
curMap = 'paintmaps/growLength'
curEmitter = 'emitterObjName'

fileNode = 'HyperShadeFileNodeName'
txlVal = 100
###########################
wkPath = cmds.workspace(q=True,rd=True)
curPath = wkPath+'xgen/collections/'+curColl+'/'+curDescr+'/'+curMap+'/'
curFile = curPath+curEmitter+'.ptx'



for curTime in range(startFrame, endFrame):
    cmds.currentTime(curTime)
    cmds.ptexBake(inMesh=curEmitter, o=curPath, bt=fileNode, tpu=txlVal)
    
    if os.path.isfile(curFile):
        shutil.copy2(curFile, curPath+curEmitter+'.0'+str(int(cmds.currentTime(q=True)))+'.ptx')
