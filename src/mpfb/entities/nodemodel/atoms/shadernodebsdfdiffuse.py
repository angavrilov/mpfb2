"""
{
    "attributes": [],
    "class": "ShaderNodeBsdfDiffuse",
    "inputs": [
        {
            "class": "NodeSocketColor",
            "identifier": "Color",
            "index": 0,
            "name": "Color"
        },
        {
            "class": "NodeSocketFloatFactor",
            "identifier": "Roughness",
            "index": 1,
            "name": "Roughness"
        },
        {
            "class": "NodeSocketVector",
            "identifier": "Normal",
            "index": 2,
            "name": "Normal"
        },
        {
            "class": "NodeSocketFloat",
            "identifier": "Weight",
            "index": 3,
            "name": "Weight"
        }
    ],
    "label": "Diffuse BSDF",
    "outputs": [
        {
            "class": "NodeSocketShader",
            "identifier": "BSDF",
            "index": 0,
            "list_as_argument": false,
            "name": "BSDF"
        }
    ]
}"""
def createShaderNodeBsdfDiffuse(self, name=None, color=None, label=None, x=None, y=None, Color=None, Roughness=None, Normal=None, Weight=None):
    node_def = dict()
    node_def["attributes"] = dict()
    node_def["inputs"] = dict()
    node_def["outputs"] = dict()
    node_def["class"] = "ShaderNodeBsdfDiffuse"
    node_def["name"] = name
    node_def["color"] = color
    node_def["label"] = label
    node_def["x"] = x
    node_def["y"] = y
    node_def["inputs"]["Color"] = Color
    node_def["inputs"]["Roughness"] = Roughness
    node_def["inputs"]["Normal"] = Normal
    node_def["inputs"]["Weight"] = Weight

    return self._create_node(node_def)