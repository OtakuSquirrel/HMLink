# How to create Shelf in Houdini
# run in houdini python shell:
#
# import hml_shelf
# import importlib
# importlib.reload(hml_shelf)
# hml_shelf.shelf()
#

# def shelf():
#     import hou
#     shelf_set = hou.shelves.shelves()
#     shelfname = 'HMLink'

#     if shelfname in shelf_set:
#         old_shelf = shelf_set[shelfname]
#         old_shelf.destroy()

#     hmlinkshelf = hou.shelves.newShelf(name='HMLink', label='HMLink')

#     hout = '''
# # output
# import hou
# import importlib
# import hml
# importlib.reload(hml)
# hml.hmhout()
#     '''

#     hin = '''
# import hou
# import importlib
# import hml
# importlib.reload(hml)
# hml.hmhin()
#     '''

#     hselectstash = '''
# import hou
# import importlib
# import hml
# importlib.reload(hml)
# hml.select_stash_type_siblings()
# '''

#     tools = hou.shelves.tools()

#     if 'hmlout' in tools:
#         old_out = tools['hmlout']
#         old_out.destroy()

#     if 'hmlin' in tools:
#         old_in = tools['hmlin']
#         old_in.destroy()


#     outtool = hou.shelves.newTool(name='hmlout', label='out', script=hout)

#     intool = hou.shelves.newTool(name='hmlin', label='in', script=hin)

#     hmlinkshelf.setTools([outtool, intool])

def shelf():
    import hou
    shelf_set = hou.shelves.shelves()
    shelfname = 'HMLink'

    if shelfname in shelf_set:
        old_shelf = shelf_set[shelfname]
        old_shelf.destroy()

    hmlinkshelf = hou.shelves.newShelf(name='HMLink', label='HMLink')

    # 使用字典管理所有工具命令
    tool_commands = {
        'hmlout': {
            'label': 'out',
            'script': '''
import hou
import importlib
import hml
importlib.reload(hml)
hml.hmhout()
'''
        },
        'hmlin': {
            'label': 'in', 
            'script': '''
import hou
import importlib
import hml
importlib.reload(hml)
hml.hmhin()
'''
        },
        'hselectstash': {
            'label': 'select stash',
            'script': '''
import hou
import importlib
import hml
importlib.reload(hml)
hml.select_stash_type_siblings()
'''
        }
    }

    tools = hou.shelves.tools()
    tool_objects = []

    # 遍历字典创建工具
    for tool_name, tool_info in tool_commands.items():
        # 删除已存在的同名工具
        if tool_name in tools:
            old_tool = tools[tool_name]
            old_tool.destroy()
        
        # 创建新工具
        new_tool = hou.shelves.newTool(
            name=tool_name,
            label=tool_info['label'],
            script=tool_info['script']
        )
        tool_objects.append(new_tool)

    # 设置工具到shelf
    hmlinkshelf.setTools(tool_objects)