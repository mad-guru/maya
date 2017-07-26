#creates a per frame expression to load in a sequence of ptex images into an xgen expression
#madguru.com

import maya.cmds as cmds
import glob
import os.path
import shutil
import xgenm as xg #can be outside of maya accessing xgen
import xgenm.xgGlobal as xgg #inside maya accessing xgen with check if xgg.Maya:

#########################
# variables
#########################
startFrame = 
endFrame = 

curColl = 'collectionName'
curDescr = 'descriptionName'
curMap = 'paintmaps/growLength'
curEmitter = 'emitterObjName'
###########################

wkPath = cmds.workspace(q=True,rd=True)
curPath = wkPath+'xgen/collections/'+curColl+'/'+curDescr+'/'+curMap+'/'
curFile = curPath+curEmitter+'.ptx'

print 'if($frame < '+str(startFrame)+') { $a= map( \''+curFile+'_0'+str(startFrame)+'.ptx\'); }'
    
for curTime in range(startFrame, endFrame):

    print 'else if($frame == '+str(curTime)+') { $a= map( \''+curFile+'.0'+str(curTime)+'.ptx\'); }'

print 'else if($frame > '+str(endFrame)+') { $a= map( \''+curFile+'.0'+str(endFrame)+'.ptx\'); }'
print '$a'
