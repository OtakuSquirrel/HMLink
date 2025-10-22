import hou

# import importlib

# importlib.reload(hml)

filedir = "C:/ModelIO/"

# hml.hmhout()
def hmhout(output_dir=filedir, tempfilename = True):
    if len(hou.selectedNodes())>0:
        outnode = hou.selectedNodes()[0]
    else:
        print('select a node')
        return 0
    
    
    
    parent = outnode.parent()
    ropfbx = parent.createNode('rop_fbx')
    ropfbx.setInput(0, outnode)

    if tempfilename:
        tempname = 'HMLinkTemp'
        outputfile = output_dir + tempname + '.fbx'
    else:
        outnodename = outnode.name()
        outputfile = output_dir + outnodename + '.fbx'
    
    ropfbx.parm('sopoutput').set(outputfile)
    ropfbx.parm('execute').pressButton()
    
    ropfbx.destroy()

# hml.hmhin()
def hmhin(input_dir=filedir, tempfilename = True, altname = ''):
    if len(hou.selectedNodes())>0:
        selnode = hou.selectedNodes()[0]
    else:
        print('select a node')
        return 0

    parent = selnode.parent()
    
    filenode = parent.createNode('file')

    if tempfilename:
        tempname = 'HMLinkTemp'
        inputfile = input_dir + tempname + '.fbx'
    else:
        outnodename = altname
        inputfile = input_dir + outnodename + '.fbx'

    filenode.parm('file').set(inputfile)
    filenode.parm('reload').pressButton()

    hou.clearAllSelected()
    stashnode = parent.createNode('stash')
    stashnode.setInput(0,filenode)
    stashnode.parm('stashinput').pressButton()
    stashnode.setSelected(True) 
    stashnode.setDisplayFlag(True)
    stashnode.setRenderFlag(True)

    filenode.destroy()


# Select all stash node

def select_stash_type_siblings():
    # 获取当前选中的节点
    selected_nodes = hou.selectedNodes()
    
    if not selected_nodes:
        hou.ui.displayMessage("请先选择一个节点", severity=hou.severityType.Warning)
        return
    
    # 获取第一个选中节点的父节点
    first_selected = selected_nodes[0]
    parent_node = first_selected.parent()
    
    if parent_node is None:
        hou.ui.displayMessage("所选节点没有父级，无法查找同级节点", severity=hou.severityType.Warning)
        return
    
    # 获取同级节点中所有 Stash 类型的节点
    stash_nodes = [node for node in parent_node.children() 
                 if node.type().name() == "stash"]
    
    # 清除选择并选中符合条件的节点
    hou.clearAllSelected()
    for node in stash_nodes:
        node.setSelected(True)
    
    # 显示结果
    if stash_nodes:
        msg = f"已选中 {len(stash_nodes)} 个 Stash 类型的同级节点"
    else:
        msg = f"在 {parent_node.path()} 下未找到 Stash 类型的节点"
    
    print(msg)
