bl_info = {
    # required
    'name': '3D Max Modiftier List Addon',
    'blender': (2, 93, 0),
    'category': 'Mesh',
    # optional
    'version': (1, 0, 0),
    'author': 'Ivan Lee',
    'description': 'Modiftier List Addon for Blender',
}

import bpy
from bpy.types import Panel, PropertyGroup, Scene, WindowManager
from bpy.props import (
    IntProperty,
    EnumProperty,
    StringProperty,
    PointerProperty,
)

class Modiftier(bpy.types.Panel):
    
    bl_idname = 'Modiftier'
    bl_label = 'Modiftier List'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modifty"
    
    def draw(self, context):
        layout = self.layout
        
        obj = context.object

        layout.operator_menu_enum("object.modifier_add", "type")
        try:
            layout.template_list("ModifierList", "", obj, "modifiers", obj,"modifier_active_index")

            
    
        except:
            pass

class ModifierList(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data):
        if ( data.type != None ):
            mod_item = item
            """layout.prop(mod_item, "name", text="", emboss=True, icon_value=icon)"""
            layout.label(text=mod_item.name, icon_value=icon)
            layout.operator("object.modifier_move_up",text="" ,icon="TRIA_UP").modifier = item.name
            layout.operator("object.modifier_move_down",text="" ,icon="TRIA_DOWN").modifier = item.name
            layout.operator("object.modifier_remove",text="" ,icon="TRASH").modifier = item.name
            
         
class Modiftier_Parameters(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Parameters"
    bl_idname = "panel.Modiftier.Parameters"
    bl_parent_id = "Modiftier"
    
    def draw(self, context):
        layout = self.layout
        
        obj = context.object
         
        try:

            m_index = bpy.context.object.modifier_active_index
            mod = dir(context.object.modifiers[m_index])
            for p in mod:
                layout.prop(obj.modifiers[m_index],p)
            
    
        except:
            pass
            
CLASSES = [
    Modiftier,
    ModifierList,
    Modiftier_Parameters,
]

def register():
    print('registered') # just for debug
    for klass in CLASSES:
        bpy.utils.register_class(klass)
    bpy.types.Object.modifier_active_index = bpy.props.IntProperty()

def unregister():
    print('unregistered') # just for debug
    for klass in CLASSES:
        bpy.utils.unregister_class(klass)
    
if __name__ == '__main__':

    register()