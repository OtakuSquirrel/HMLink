# Out
import maya.cmds as cmds
path = "C:/ModelIO/HMLinkTemp.fbx"
def hmlout(outpath):
    cmds.file(outpath,  force=True, options="v=0",type="FBX export",preserveReferences=True, exportSelected=True,prompt=False)
hmlout(path)

# In
import maya.cmds as cmds
path = "C:/ModelIO/HMLinkTemp.fbx"
def hmlin(inpath):
    cmds.file(inpath,i=True,type="FBX",ignoreVersion=True,mergeNamespacesOnClash=False,options="v=0;",pr=True,importFrameRate=True,importTimeRange="override")
hmlin(path)