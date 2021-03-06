MAP_LIST = [
    '---- Choose', 'baseColor', 'height', 'metalness', 'normal', 'specRoughness',
    '---- Base', 'baseWeight', 'baseColor', 'diffuseRoughness', 'metalness',
    '---- Specular', 'specWeight', 'specColor', 'specRughness', 'specIoR', 'specAnisotropy', 'rotation',
    '---- Transmission', 'transWeight', 'transColor', 'depth', 'scatter', 'transAnisotropy', 'dispertionAbbe',
    'extraRoughness',
    '---- Subsurface', 'sssWeight', 'sssColor', 'radius', 'scale', 'sssAnisotropy',
    '---- Coat', 'coatWeight', 'coatColor', 'coatRoughness', 'coatIoR', 'coatNormal',
    '---- Sheen', 'sheenWeight', 'color', 'roughness',
    '---- Emission', 'emissionWeight', 'emissionColor',
    '---- Thin film', 'thickness', 'thinIoR',
    '---- Geometry', 'opacity', 'height', 'normal', 'anisotropyTangent',
    '---- Matte', 'matteColor', 'matteOpacity',
    '---- Don\'t use'
]
MAP_LIST_REAL_ATTRIBUTES = [
    '---- Choose', 'baseColor', 'normalCamera', 'metalness', 'normalCamera', 'specularRoughness',
    '---- Base', 'base', 'baseColor', 'diffuseRoughness', 'metalness',
    '---- Specular', 'specular', 'specularColor', 'specularRoughness', 'specularIOR', 'specularAnisotropy',
    'specularRotation',
    '---- Transmission', 'transmission', 'transmissionColor', 'transmissionDepth', 'transmissionScatter',
    'transmissionScatterAnisotropy', 'transmissionDispersion', 'transmissionExtraRoughness',
    '---- Subsurface', 'subsurface', 'subsurfaceColor', 'subsurfaceRadius', 'subsurfaceScale', 'subsurfaceAnisotropy',
    '---- Coat', 'coat', 'coatColor', 'coatRoughness', 'coatIOR', 'coatNormal',
    '---- Sheen', 'sheen', 'sheenColor', 'sheenRoughness',
    '---- Emission', 'emission', 'emissionColor',
    '---- Thin film', 'thinFilmThickness', 'thinFilmIOR',
    '---- Geometry', 'opacity', 'normalCamera', 'normalCamera', 'tangent',
    '---- Matte', 'aiMatteColor', 'aiMatteColorA',
    '---- Don\'t use'
]

BASE_COLOR = [
    'baseColor', 'BaseColor', 'basecolor', 'color', 'Color', 'albedo', 'Albedo', 'diffuse', 'Diffuse', 'diff', 'Diff'
]
HEIGHT = [
    'displace', 'Displace', 'Displacement', 'displacement', 'height', 'Height',
    'bump', 'Bump', 'BumpMap', 'bumpMap', 'displacementMap', 'DisplacementMap'
]
METALNESS = [
    'metal', 'Metal', 'metalness', 'Metalness'
]
NORMAL = [
    'normal', 'Normal', 'normalMap', 'NormalMap'
]
ROUGHNESS = [
    'roughness', 'Roughness', 'specularRoughness', 'SpecularRoughness', 'specular', 'Specular', 'spec', 'Spec'
]
MATTE = [
    'Matte', 'matte'
]
OPACITY = [
    'Opacity', 'opacity', 'transparency', 'Transparency'
]
SUBSURFACE = [
    'subsurfaceColor', 'SubsurfaceColor', 'SSS', 'SSSColor', 'SSScolor', 'sss', 'sssColor', 'ssscolor'
]
EMISSION = [
    'emission', 'Emission', 'emissive', 'Emissive', 'light', 'Light'
]

MAP_LIST_COLOR_ATTRIBUTES_INDICES = [1, 4, 7, 13, 20, 21, 28, 29, 34, 37, 40, 44, 49, 51, 52, 54]
DONT_USE_IDS = [0, 6, 11, 18, 26, 32, 38, 42, 45, 48, 53, 56]
SHADER_TO_USE = 'aiStandardSurface'
NORMAL_NODE = 'aiNormalMap'
BUMP_NODE = 'aiBump2d'
