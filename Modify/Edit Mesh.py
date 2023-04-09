bl_info = {
    # required
    'name': '3D Max Edit Poly Addon',
    'blender': (2, 93, 0),
    'category': 'Mesh',
    # optional
    'version': (1, 0, 0),
    'author': 'Ivan Lee',
    'description': 'Edit Poly Addon for Blender',
}

import bpy

class Edit_Mesh(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Modifty"

    bl_label = "Edit Poly"
    bl_idname = "panel.editmesh"
    
    def draw(self, context):
        layout = self.layout

class Edit_Mesh_Name(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Name"
    bl_idname = "panel.editmesh.Name"
    bl_parent_id = "panel.editmesh"
    
    def draw(self, context):
        row = self.layout
        if ( len(bpy.context.selected_objects) == 1):
            obj = bpy.context.selected_objects[0]
            row.prop(obj, "name")

class Edit_Mesh_Selection(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Selection"
    bl_idname = "panel.editmesh.selection"
    bl_parent_id = "panel.editmesh"
    
    def draw(self, context):
        layout = self.layout
        
        row1 = layout.row()
        row1.alignment = "CENTER"
        row1.operator("opr.selection" ,icon='VERTEXSEL',text="").type = "VERT"
        row1.operator("opr.selection" ,icon='EDGESEL',text="").type = "EDGE"
        row1.operator("opr.selection" ,icon='FACESEL',text="").type = "FACE"

        row2 = layout.row()
        row2.operator("mesh.select_less" ,text="Shrink")
        row2.operator("mesh.select_more" ,text="Grow")
        
        row3 = layout.row()
        row3.operator("mesh.loop_multi_select" ,text="Ring").ring = True
        row3.operator("mesh.loop_multi_select" ,text="Loop").ring = False


class Edit_Mesh_Geometry(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Edit Geometry"
    bl_idname = "panel.editmesh.editgeometry"
    bl_parent_id = "panel.editmesh"
    
    def draw(self, context):
        layout = self.layout
        
        row2 = layout.row()
        row2.operator("mesh.extrude_context" ,text="Extrude")
        row2.operator("mesh.bevel" ,text="Chamfer")
        
        row3 = layout.row()
        row3.operator("mesh.loopcut_slide" ,text="Connect")
        row3.operator("mesh.knife_tool" ,text="Cut")
        
        row4 = layout.row()
        row4.operator("mesh.bridge_edge_loops" ,text="Bridge")
        row4.operator("mesh.separate" ,text="Detach").type="SELECTED"



class opr_selection(bpy.types.Operator):
    
    bl_label = "Selection"
    bl_idname = "opr.selection"
    
    type: bpy.props.StringProperty()
    
    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        if ( len(bpy.context.selected_objects) == 1):

            if ( self.type == "VERT"):
                
                try:
                   bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
                except:
                   pass
            elif ( self.type == "EDGE" ):
                
                try:
                   bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
                except:
                   pass     
            elif ( self.type == "FACE" ):
                
                try:
                   bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
                except:
                   pass                
                
        return {"FINISHED"}


CLASSES = [
    Edit_Mesh,
    Edit_Mesh_Name,
    Edit_Mesh_Selection,
    opr_selection,
    Edit_Mesh_Geometry,
    
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