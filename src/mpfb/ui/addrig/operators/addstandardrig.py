"""Operator for adding a standard rig."""

import bpy, os, gzip
from mpfb.services.logservice import LogService
from mpfb.services.objectservice import ObjectService
from mpfb.services.locationservice import LocationService
from mpfb import ClassManager

_LOG = LogService.get_logger("addrig.add_standard_rig")

class MPFB_OT_AddStandardRigOperator(bpy.types.Operator):
    """Add a standard (non-rigify) rig"""

    bl_idname = "mpfb.add_standard_rig"
    bl_label = "Add standard rig"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if context.active_object is not None:
            return ObjectService.object_is_basemesh(context.active_object)
        return False

    def execute(self, context):
        scene = context.scene

        if not ObjectService.object_is_basemesh(context.active_object):
            self.report({'ERROR'}, "Rigs can only be added to the base mesh")
            return {'FINISHED'}

        basemesh = context.active_object

        from mpfb.ui.addrig.addrigpanel import ADD_RIG_PROPERTIES # pylint: disable=C0415

        import_weights = ADD_RIG_PROPERTIES.get_value("import_weights", entity_reference=scene)

        self.report({'INFO'}, "A rig was added")
        return {'FINISHED'}


ClassManager.add_class(MPFB_OT_AddStandardRigOperator)

