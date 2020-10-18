import bpy
import bmesh

from . import common
from . import compatibility as compat


class TestAlignUVCircle(common.TestBase):
    module_name = "align_uv"
    submodule_name = "circle"
    idname = [
        ('OPERATOR', 'uv.muv_align_uv_circle'),
    ]

    # Align UV has a complicated condition to test
    def test_nothing(self):
        pass


class TestAlignUVStraighten(common.TestBase):
    module_name = "align_uv"
    submodule_name = "straighten"
    idname = [
        ('OPERATOR', 'uv.muv_align_uv_straighten'),
    ]

    # Align UV has a complicated condition to test
    def test_nothing(self):
        pass


class TestAlignUVAxis(common.TestBase):
    module_name = "align_uv"
    submodule_name = "axis"
    idname = [
        ('OPERATOR', 'uv.muv_align_uv_axis'),
    ]

    # Align UV has a complicated condition to test
    def test_nothing(self):
        pass


class TestAlignUVSnapSetPointTargetToCursor(common.TestBase):
    module_name = "align_uv"
    submodule_name = "snap_set_point_target_to_cursor"
    idname = [
        ('OPERATOR', 'uv.muv_align_uv_snap_set_point_target_to_cursor'),
    ]

    # It is impossible to get cursor_location from the console.
    def test_nothing(self):
        pass


class TestAlignUVSnapSetPointTargetToVertexGroup(common.TestBase):
    module_name = "align_uv"
    submodule_name = "snap_set_point_target_to_vertex_group"
    idname = [
        ('OPERATOR', 'uv.muv_align_uv_snap_set_point_target_to_vertex_group'),
    ]

    def setUpEachMethod(self):
        obj_name = "Cube"

        common.select_object_only(obj_name)
        compat.set_active_object(bpy.data.objects[obj_name])
        bpy.ops.object.mode_set(mode='EDIT')

        bpy.context.scene.tool_settings.use_uv_select_sync = True

    def tearDownMethod(self):
        bpy.context.scene.tool_settings.use_uv_select_sync = False

    def test_ok(self):
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.uv_texture_add()
        result = bpy.ops.uv.muv_align_uv_snap_set_point_target_to_vertex_group()
        self.assertSetEqual(result, {'FINISHED'})


class TestAlignUVSnapToPoint(common.TestBase):
    module_name = "align_uv"
    submodule_name = "snap_to_point"
    idname = [
        ('OPERATOR', 'uv.muv_align_uv_snap_to_point'),
    ]

    def setUpEachMethod(self):
        obj_name = "Cube"

        common.select_object_only(obj_name)
        compat.set_active_object(bpy.data.objects[obj_name])
        bpy.ops.object.mode_set(mode='EDIT')

        bpy.context.scene.tool_settings.use_uv_select_sync = True

    def tearDownMethod(self):
        bpy.context.scene.tool_settings.use_uv_select_sync = False

    def test_ng_no_vertex(self):
        # Warning: Must select more than 1 Vertex.
        obj = bpy.context.active_object
        bm = bmesh.from_edit_mesh(obj.data)

        for f in bm.faces:
            f.select = False

        result = bpy.ops.uv.muv_align_uv_snap_to_point(group='VERTEX')
        self.assertSetEqual(result, {'CANCELLED'})

    def test_ng_no_face(self):
        # Warning: Must select more than 1 Face.
        obj = bpy.context.active_object
        bm = bmesh.from_edit_mesh(obj.data)

        for f in bm.faces:
            f.select = False

        result = bpy.ops.uv.muv_align_uv_snap_to_point(
            group='FACE', target=(0.5, 0.5))
        self.assertSetEqual(result, {'CANCELLED'})

    def test_ng_no_uv_island(self):
        # Warning: Must select more than 1 UV Island.
        obj = bpy.context.active_object
        bm = bmesh.from_edit_mesh(obj.data)

        for f in bm.faces:
            f.select = False

        result = bpy.ops.uv.muv_align_uv_snap_to_point(group='UV_ISLAND')
        self.assertSetEqual(result, {'CANCELLED'})

    def test_ok_vertex(self):
        obj = bpy.context.active_object
        bm = bmesh.from_edit_mesh(obj.data)

        for f in bm.faces:
            f.select = False
        bm.faces[0].select = True

        result = bpy.ops.uv.muv_align_uv_snap_to_point(group='VERTEX')
        self.assertSetEqual(result, {'FINISHED'})

    def test_ok_face(self):
        obj = bpy.context.active_object
        bm = bmesh.from_edit_mesh(obj.data)

        for f in bm.faces:
            f.select = False
        bm.faces[0].select = True

        result = bpy.ops.uv.muv_align_uv_snap_to_point(
            group='FACE', target=(0.5, 0.5))
        self.assertSetEqual(result, {'FINISHED'})

    def test_ok_uv_island(self):
        obj = bpy.context.active_object
        bm = bmesh.from_edit_mesh(obj.data)

        for f in bm.faces:
            f.select = False
        bm.faces[0].select = True

        result = bpy.ops.uv.muv_align_uv_snap_to_point(
            group='UV_ISLAND')
        self.assertSetEqual(result, {'FINISHED'})


class TestAlignUVSnapSetEdgeTargetToEdgeCenter(common.TestBase):
    module_name = "align_uv"
    submodule_name = "snap_set_edge_target_to_edge_center"
    idname = [
        ('OPERATOR', 'uv.muv_align_uv_snap_set_edge_target_to_edge_center'),
    ]

    def setUpEachMethod(self):
        obj_name = "Cube"

        common.select_object_only(obj_name)
        compat.set_active_object(bpy.data.objects[obj_name])
        bpy.ops.object.mode_set(mode='EDIT')

        bpy.context.scene.tool_settings.use_uv_select_sync = True

    def tearDownMethod(self):
        bpy.context.scene.tool_settings.use_uv_select_sync = False

    def test_ok(self):
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.uv_texture_add()
        result = bpy.ops.uv.muv_align_uv_snap_set_edge_target_to_edge_center()
        self.assertSetEqual(result, {'FINISHED'})
