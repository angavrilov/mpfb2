"""This file contains the developer panel for the node editor."""

from mpfb._classmanager import ClassManager
from mpfb.services.logservice import LogService
from mpfb.services.uiservice import UiService
from mpfb.services.sceneconfigset import SceneConfigSet
from mpfb.ui.abstractpanel import Abstract_Panel
import bpy, os

from .developerpanel import DEVELOPER_PROPERTIES

_LOG = LogService.get_logger("ui.nodedeveloperpanel")


class MPFB_PT_Node_Developer_Panel(Abstract_Panel):
    """UI for various node developer functions."""
    bl_idname = "NODE_PT_mpfb_node_developer_panel"
    bl_space_type = 'NODE_EDITOR'
    bl_label = "Node developer"
    bl_region_type = "UI"
    bl_category = UiService.get_value("DEVELOPERCATEGORY")

    def _nodes(self, scene, layout):
        box = self._create_box(layout, "Dump nodes")
        DEVELOPER_PROPERTIES.draw_properties(scene, box, ["output_class_name"])
        box.operator("mpfb.print_node_group")
        box.operator("mpfb.create_molecules")
        box.operator("mpfb.create_cells")

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "ShaderNodeTree"

    def draw(self, context):
        _LOG.enter()
        layout = self.layout
        _LOG.debug("Context", context)
        scene = context.scene
        _LOG.debug("Scene", scene)
        node_tree = context.space_data.node_tree
        _LOG.debug("Node tree", node_tree)

        selected = context.selected_nodes
        _LOG.debug("Selected", selected)

        self._nodes(scene, layout)

ClassManager.add_class(MPFB_PT_Node_Developer_Panel)

