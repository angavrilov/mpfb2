"""
{
    "attributes": {
        "color": {
            "class": "Color",
            "name": "color",
            "value": [
                0.6079999804496765,
                0.6079999804496765,
                0.6079999804496765
            ]
        },
        "height": {
            "class": "float",
            "name": "height",
            "value": 100.0
        },
        "location": {
            "class": "Vector",
            "name": "location",
            "value": [
                0.0,
                0.0
            ]
        },
        "width": {
            "class": "float",
            "name": "width",
            "value": 140.0
        }
    },
    "class": "ShaderNodeCombineXYZ",
    "inputs": {
        "X": {
            "class": "NodeSocketFloat",
            "default_value": 0.0,
            "identifier": "X",
            "name": "X",
            "value_type": "VALUE"
        },
        "Y": {
            "class": "NodeSocketFloat",
            "default_value": 0.0,
            "identifier": "Y",
            "name": "Y",
            "value_type": "VALUE"
        },
        "Z": {
            "class": "NodeSocketFloat",
            "default_value": 0.0,
            "identifier": "Z",
            "name": "Z",
            "value_type": "VALUE"
        }
    },
    "outputs": {
        "Vector": {
            "class": "NodeSocketVector",
            "default_value": [
                0.0,
                0.0,
                0.0
            ],
            "identifier": "Vector",
            "name": "Vector",
            "value_type": "VECTOR"
        }
    }
}"""

from .abstractnodewrapper import AbstractNodeWrapper

class NodeWrapperShaderNodeCombineXYZ:
    def __init__(self):
        pass