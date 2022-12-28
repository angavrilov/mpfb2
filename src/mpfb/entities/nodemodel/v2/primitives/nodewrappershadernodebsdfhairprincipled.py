import bpy, json

_ORIGINAL_NODE_DEF = json.loads("""
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
        "parametrization": {
            "class": "enum",
            "name": "parametrization",
            "value": "COLOR"
        },
        "width": {
            "class": "float",
            "name": "width",
            "value": 240.0
        }
    },
    "class": "ShaderNodeBsdfHairPrincipled",
    "inputs": {
        "Absorption Coefficient": {
            "class": "NodeSocketVector",
            "default_value": [
                0.24553099274635315,
                0.5199999809265137,
                1.3650000095367432
            ],
            "identifier": "Absorption Coefficient",
            "name": "Absorption Coefficient",
            "value_type": "VECTOR"
        },
        "Coat": {
            "class": "NodeSocketFloatFactor",
            "default_value": 0.0,
            "identifier": "Coat",
            "name": "Coat",
            "value_type": "VALUE"
        },
        "Color": {
            "class": "NodeSocketColor",
            "default_value": [
                0.01751299947500229,
                0.005762999877333641,
                0.002059000078588724,
                1.0
            ],
            "identifier": "Color",
            "name": "Color",
            "value_type": "RGBA"
        },
        "IOR": {
            "class": "NodeSocketFloat",
            "default_value": 1.5499999523162842,
            "identifier": "IOR",
            "name": "IOR",
            "value_type": "VALUE"
        },
        "Melanin": {
            "class": "NodeSocketFloatFactor",
            "default_value": 0.800000011920929,
            "identifier": "Melanin",
            "name": "Melanin",
            "value_type": "VALUE"
        },
        "Melanin Redness": {
            "class": "NodeSocketFloatFactor",
            "default_value": 1.0,
            "identifier": "Melanin Redness",
            "name": "Melanin Redness",
            "value_type": "VALUE"
        },
        "Offset": {
            "class": "NodeSocketFloatAngle",
            "default_value": 0.03490658476948738,
            "identifier": "Offset",
            "name": "Offset",
            "value_type": "VALUE"
        },
        "Radial Roughness": {
            "class": "NodeSocketFloatFactor",
            "default_value": 0.30000001192092896,
            "identifier": "Radial Roughness",
            "name": "Radial Roughness",
            "value_type": "VALUE"
        },
        "Random": {
            "class": "NodeSocketFloat",
            "default_value": 0.0,
            "identifier": "Random",
            "name": "Random",
            "value_type": "VALUE"
        },
        "Random Color": {
            "class": "NodeSocketFloatFactor",
            "default_value": 0.0,
            "identifier": "Random Color",
            "name": "Random Color",
            "value_type": "VALUE"
        },
        "Random Roughness": {
            "class": "NodeSocketFloatFactor",
            "default_value": 0.0,
            "identifier": "Random Roughness",
            "name": "Random Roughness",
            "value_type": "VALUE"
        },
        "Roughness": {
            "class": "NodeSocketFloatFactor",
            "default_value": 0.30000001192092896,
            "identifier": "Roughness",
            "name": "Roughness",
            "value_type": "VALUE"
        },
        "Tint": {
            "class": "NodeSocketColor",
            "default_value": [
                1.0,
                1.0,
                1.0,
                1.0
            ],
            "identifier": "Tint",
            "name": "Tint",
            "value_type": "RGBA"
        },
        "Weight": {
            "class": "NodeSocketFloat",
            "default_value": 0.0,
            "identifier": "Weight",
            "name": "Weight",
            "value_type": "VALUE"
        }
    },
    "outputs": {
        "BSDF": {
            "class": "NodeSocketShader",
            "default_value": null,
            "identifier": "BSDF",
            "name": "BSDF",
            "value_type": "SHADER"
        }
    }
}""")

from .abstractnodewrapper import AbstractNodeWrapper

class _NodeWrapperShaderNodeBsdfHairPrincipled(AbstractNodeWrapper):
    def __init__(self):
        AbstractNodeWrapper.__init__(self, _ORIGINAL_NODE_DEF)

snBsdfHairPrincipled = _NodeWrapperShaderNodeBsdfHairPrincipled()