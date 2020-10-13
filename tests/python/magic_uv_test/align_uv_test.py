from . import common


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

    def test_ok(self):
        result = bpy.ops.uv.muv_align_uv_snap_set_point_target_to_cursor()
        self.assertSetEqual(result, {'FINISHED'})


class TestAlignUVSnapSetPointTargetToCursor(common.TestBase):
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
