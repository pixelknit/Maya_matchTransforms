import maya.cmds as cmd
import maya.mel


def matchtransforms(inObjects, inOperation):
   
    oTo = inObjects[len(inObjects) - 1]
    
    oFrom = inObjects
    oFrom.pop(len(inObjects) - 1)    
    
    if(inOperation == 0):
        pivotTranslate = cmds.xform( oTo, q = True, m = True, ws = True ) 
        cmds.xform(oFrom, a=True, m=pivotTranslate)
    
    if(inOperation == 1):
        pivotTranslate = cmds.xform(oTo, q = True, t = True, ws = True ) 
        cmds.xform(inObjToMatch, a=True, t=pivotTranslate)
    
    if(inOperation == 2):
        pivotTranslate = cmds.xform(oTo, q = True, ro = True, ws = True ) 
        cmds.xform(inObjToMatch, a=True, ro=pivotTranslate)
    
    if(inOperation == 3):
        pivotTranslate = cmds.xform(oTo, q = True, s = True, ws = True ) 
        cmds.xform(inObjToMatch, a=True, s=pivotTranslate)
    return


selection= cmds.ls(selection=True )
matchtransforms(selection,0)
