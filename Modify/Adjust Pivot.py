bl_info = {
    # required
    'name': '3D Max Adjust Pivot Addon',
    'blender': (2, 93, 0),
    'category': 'Mesh',
    # optional
    'version': (1, 0, 0),
    'author': 'Ivan Lee',
    'description': 'Adjust Pivot Addon for Blender',
}

import bpy

class AdjustPivot(bpy.types.Panel):
    
    bl_idname = 'Adjust Pivot'
    bl_label = 'Adjust Pivot'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modifty"
    
    def draw(self, context):
        layout = self.layout
        
        m1_box = layout.box()
        m1_box.label(text="Move/Rotate/Scale:")
        m1_box.operator("opr.affect_pivot",text="Affect Pivot Only" )
        
        m2_box = layout.box()
        m2_box.label(text="Alignment:")
        m2_box.operator("opr.center_pivot",text="Center to Object" )


class Pivot_Point(bpy.types.Operator):
    
    bl_idname = 'opr.affect_pivot'
    bl_label = 'affectpivot'
    
    def __init__(self):
        self.selection = ""
    
    def execute(self, context):

        return {"FINISHED"}

    def modal(self,context,event):
        if event.type == 'MOUSEMOVE':
           
            return {'PASS_THROUGH'}
        elif event.type == 'RIGHTMOUSE':
            
            
            bpy.context.scene.cursor.location= bpy.context.active_object.location
            bpy.ops.object.delete()

            
            self.selection.select_set(True)
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
            
            bpy.context.scene.cursor.location=(0,0,0)

            return {'FINISHED'}
        
        return {'PASS_THROUGH'}

    def invoke(self,context,event):

        """selected = bpy.context.active_object"""
        self.selection = context.object
        
        bpy.ops.object.empty_add()
        new_empty = bpy.context.active_object
        new_empty.location = self.selection.location
        bpy.context.scene.cursor.location = new_empty.location
        new_empty.scale = (0,0,0)
        new_empty.name = "Pivot Point"
        bpy.ops.wm.tool_set_by_id(name = "builtin.move")
        context.window_manager.modal_handler_add(self)
        
        return {'RUNNING_MODAL'}

        
    
    
class Pivot_Center(bpy.types.Operator):
    
    bl_idname = 'opr.center_pivot'
    bl_label = 'centerpivot'
    
    def execute(self, context):
        
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
        
        return {"FINISHED"}

CLASSES = [
    AdjustPivot,
    Pivot_Point,
    Pivot_Center,
]

def register():
    print('registered') # just for debug
    for klass in CLASSES:
        bpy.utils.register_class(klass)

def unregister():
    print('unregistered') # just for debug
    for klass in CLASSES:
        bpy.utils.unregister_class(klass)
    
if __name__ == '__main__':

    register()