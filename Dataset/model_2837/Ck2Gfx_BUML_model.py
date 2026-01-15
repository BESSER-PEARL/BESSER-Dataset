####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
ck2gfx_Model = Class(name="ck2gfx::Model")
ck2gfx_EObject = Class(name="ck2gfx::EObject")
ck2gfx_Color = Class(name="ck2gfx::Color")
ck2gfx_ColorRatio = Class(name="ck2gfx::ColorRatio")
ck2gfx_Coordinates = Class(name="ck2gfx::Coordinates")
ck2gfx_SpriteTypes = Class(name="ck2gfx::SpriteTypes")
ck2gfx_SpriteType = Class(name="ck2gfx::SpriteType")
ck2gfx_ProgressbarType = Class(name="ck2gfx::ProgressbarType")
ck2gfx_AnimatedSpriteType = Class(name="ck2gfx::AnimatedSpriteType")
ck2gfx_CorneredTileSpriteType = Class(name="ck2gfx::CorneredTileSpriteType")
ck2gfx_PortraitType = Class(name="ck2gfx::PortraitType")
ck2gfx_CoatOfArmsType = Class(name="ck2gfx::CoatOfArmsType")
ck2gfx_CoatOfArmsLayer = Class(name="ck2gfx::CoatOfArmsLayer")
ck2gfx_MaskedShieldType = Class(name="ck2gfx::MaskedShieldType")
ck2gfx_LineChartType = Class(name="ck2gfx::LineChartType")
ck2gfx_ObjectTypes = Class(name="ck2gfx::ObjectTypes")
ck2gfx_EMFXActorType = Class(name="ck2gfx::EMFXActorType")
ck2gfx_Animation = Class(name="ck2gfx::Animation")
ck2gfx_BitmapFonts = Class(name="ck2gfx::BitmapFonts")
ck2gfx_Pdxmesh = Class(name="ck2gfx::Pdxmesh")
ck2gfx_ArrowType = Class(name="ck2gfx::ArrowType")
ck2gfx_BitmapFont = Class(name="ck2gfx::BitmapFont")
ck2gfx_ColorCode = Class(name="ck2gfx::ColorCode")

# ck2gfx_Model class attributes and methods

# ck2gfx_EObject class attributes and methods

# ck2gfx_Color class attributes and methods
ck2gfx_Color_r: Property = Property(name="r", type=IntegerType)
ck2gfx_Color_g: Property = Property(name="g", type=IntegerType)
ck2gfx_Color_b: Property = Property(name="b", type=IntegerType)
ck2gfx_Color.attributes={ck2gfx_Color_g, ck2gfx_Color_r, ck2gfx_Color_b}

# ck2gfx_ColorRatio class attributes and methods
ck2gfx_ColorRatio_r: Property = Property(name="r", type=FloatType)
ck2gfx_ColorRatio_g: Property = Property(name="g", type=FloatType)
ck2gfx_ColorRatio_b: Property = Property(name="b", type=FloatType)
ck2gfx_ColorRatio.attributes={ck2gfx_ColorRatio_r, ck2gfx_ColorRatio_b, ck2gfx_ColorRatio_g}

# ck2gfx_Coordinates class attributes and methods
ck2gfx_Coordinates_x: Property = Property(name="x", type=FloatType)
ck2gfx_Coordinates_y: Property = Property(name="y", type=FloatType)
ck2gfx_Coordinates.attributes={ck2gfx_Coordinates_x, ck2gfx_Coordinates_y}

# ck2gfx_SpriteTypes class attributes and methods

# ck2gfx_SpriteType class attributes and methods
ck2gfx_SpriteType_name: Property = Property(name="name", type=StringType)
ck2gfx_SpriteType_textureFile: Property = Property(name="textureFile", type=StringType)
ck2gfx_SpriteType_noOfFrames: Property = Property(name="noOfFrames", type=IntegerType)
ck2gfx_SpriteType_loadType: Property = Property(name="loadType", type=StringType)
ck2gfx_SpriteType_allwaysTransparent: Property = Property(name="allwaysTransparent", type=BooleanType)
ck2gfx_SpriteType_noRefCount: Property = Property(name="noRefCount", type=BooleanType)
ck2gfx_SpriteType_effectFile: Property = Property(name="effectFile", type=StringType)
ck2gfx_SpriteType_transparenceCheck: Property = Property(name="transparenceCheck", type=BooleanType)
ck2gfx_SpriteType_canBeLowres: Property = Property(name="canBeLowres", type=BooleanType)
ck2gfx_SpriteType_clickSound: Property = Property(name="clickSound", type=StringType)
ck2gfx_SpriteType.attributes={ck2gfx_SpriteType_noRefCount, ck2gfx_SpriteType_effectFile, ck2gfx_SpriteType_name, ck2gfx_SpriteType_allwaysTransparent, ck2gfx_SpriteType_transparenceCheck, ck2gfx_SpriteType_textureFile, ck2gfx_SpriteType_canBeLowres, ck2gfx_SpriteType_clickSound, ck2gfx_SpriteType_loadType, ck2gfx_SpriteType_noOfFrames}

# ck2gfx_ProgressbarType class attributes and methods
ck2gfx_ProgressbarType_name: Property = Property(name="name", type=StringType)
ck2gfx_ProgressbarType_noRefCount: Property = Property(name="noRefCount", type=BooleanType)
ck2gfx_ProgressbarType_textureFile1: Property = Property(name="textureFile1", type=StringType)
ck2gfx_ProgressbarType_textureFile2: Property = Property(name="textureFile2", type=StringType)
ck2gfx_ProgressbarType_horizontal: Property = Property(name="horizontal", type=BooleanType)
ck2gfx_ProgressbarType_effectFile: Property = Property(name="effectFile", type=StringType)
ck2gfx_ProgressbarType_allwaysTransparent: Property = Property(name="allwaysTransparent", type=BooleanType)
ck2gfx_ProgressbarType_maxValue: Property = Property(name="maxValue", type=FloatType)
ck2gfx_ProgressbarType_loadType: Property = Property(name="loadType", type=StringType)
ck2gfx_ProgressbarType.attributes={ck2gfx_ProgressbarType_textureFile1, ck2gfx_ProgressbarType_horizontal, ck2gfx_ProgressbarType_noRefCount, ck2gfx_ProgressbarType_loadType, ck2gfx_ProgressbarType_effectFile, ck2gfx_ProgressbarType_allwaysTransparent, ck2gfx_ProgressbarType_name, ck2gfx_ProgressbarType_textureFile2, ck2gfx_ProgressbarType_maxValue}

# ck2gfx_AnimatedSpriteType class attributes and methods
ck2gfx_AnimatedSpriteType_name: Property = Property(name="name", type=StringType)
ck2gfx_AnimatedSpriteType_texturefile: Property = Property(name="texturefile", type=StringType)
ck2gfx_AnimatedSpriteType_noOfFrames: Property = Property(name="noOfFrames", type=IntegerType)
ck2gfx_AnimatedSpriteType_animationRateFps: Property = Property(name="animationRateFps", type=FloatType)
ck2gfx_AnimatedSpriteType_looping: Property = Property(name="looping", type=BooleanType)
ck2gfx_AnimatedSpriteType_playOnShow: Property = Property(name="playOnShow", type=BooleanType)
ck2gfx_AnimatedSpriteType.attributes={ck2gfx_AnimatedSpriteType_looping, ck2gfx_AnimatedSpriteType_name, ck2gfx_AnimatedSpriteType_noOfFrames, ck2gfx_AnimatedSpriteType_playOnShow, ck2gfx_AnimatedSpriteType_animationRateFps, ck2gfx_AnimatedSpriteType_texturefile}

# ck2gfx_CorneredTileSpriteType class attributes and methods
ck2gfx_CorneredTileSpriteType_allwaysTransparent: Property = Property(name="allwaysTransparent", type=BooleanType)
ck2gfx_CorneredTileSpriteType_noRefCount: Property = Property(name="noRefCount", type=BooleanType)
ck2gfx_CorneredTileSpriteType_loadType: Property = Property(name="loadType", type=StringType)
ck2gfx_CorneredTileSpriteType_tilingCenter: Property = Property(name="tilingCenter", type=BooleanType)
ck2gfx_CorneredTileSpriteType_name: Property = Property(name="name", type=StringType)
ck2gfx_CorneredTileSpriteType_texturefile: Property = Property(name="texturefile", type=StringType)
ck2gfx_CorneredTileSpriteType.attributes={ck2gfx_CorneredTileSpriteType_texturefile, ck2gfx_CorneredTileSpriteType_name, ck2gfx_CorneredTileSpriteType_tilingCenter, ck2gfx_CorneredTileSpriteType_loadType, ck2gfx_CorneredTileSpriteType_allwaysTransparent, ck2gfx_CorneredTileSpriteType_noRefCount}

# ck2gfx_PortraitType class attributes and methods
ck2gfx_PortraitType_name: Property = Property(name="name", type=StringType)
ck2gfx_PortraitType_effectFile: Property = Property(name="effectFile", type=StringType)
ck2gfx_PortraitType_layers: Property = Property(name="layers", type=StringType)
ck2gfx_PortraitType_hairColorIndex: Property = Property(name="hairColorIndex", type=IntegerType)
ck2gfx_PortraitType_eyeColorIndex: Property = Property(name="eyeColorIndex", type=IntegerType)
ck2gfx_PortraitType_headgearThatHidesHair: Property = Property(name="headgearThatHidesHair", type=IntegerType)
ck2gfx_PortraitType.attributes={ck2gfx_PortraitType_name, ck2gfx_PortraitType_layers, ck2gfx_PortraitType_eyeColorIndex, ck2gfx_PortraitType_effectFile, ck2gfx_PortraitType_headgearThatHidesHair, ck2gfx_PortraitType_hairColorIndex}

# ck2gfx_CoatOfArmsType class attributes and methods
ck2gfx_CoatOfArmsType_name: Property = Property(name="name", type=StringType)
ck2gfx_CoatOfArmsType_frame: Property = Property(name="frame", type=StringType)
ck2gfx_CoatOfArmsType_mask: Property = Property(name="mask", type=StringType)
ck2gfx_CoatOfArmsType_sealOverlay: Property = Property(name="sealOverlay", type=StringType)
ck2gfx_CoatOfArmsType_effect: Property = Property(name="effect", type=StringType)
ck2gfx_CoatOfArmsType.attributes={ck2gfx_CoatOfArmsType_frame, ck2gfx_CoatOfArmsType_effect, ck2gfx_CoatOfArmsType_mask, ck2gfx_CoatOfArmsType_name, ck2gfx_CoatOfArmsType_sealOverlay}

# ck2gfx_CoatOfArmsLayer class attributes and methods
ck2gfx_CoatOfArmsLayer_mask: Property = Property(name="mask", type=StringType)
ck2gfx_CoatOfArmsLayer_scale: Property = Property(name="scale", type=FloatType)
ck2gfx_CoatOfArmsLayer.attributes={ck2gfx_CoatOfArmsLayer_mask, ck2gfx_CoatOfArmsLayer_scale}

# ck2gfx_MaskedShieldType class attributes and methods
ck2gfx_MaskedShieldType_name: Property = Property(name="name", type=StringType)
ck2gfx_MaskedShieldType_textureFile1: Property = Property(name="textureFile1", type=StringType)
ck2gfx_MaskedShieldType_textureFile2: Property = Property(name="textureFile2", type=StringType)
ck2gfx_MaskedShieldType_effectFile: Property = Property(name="effectFile", type=StringType)
ck2gfx_MaskedShieldType_allwaysTransparent: Property = Property(name="allwaysTransparent", type=BooleanType)
ck2gfx_MaskedShieldType_clickSound: Property = Property(name="clickSound", type=StringType)
ck2gfx_MaskedShieldType.attributes={ck2gfx_MaskedShieldType_effectFile, ck2gfx_MaskedShieldType_allwaysTransparent, ck2gfx_MaskedShieldType_name, ck2gfx_MaskedShieldType_clickSound, ck2gfx_MaskedShieldType_textureFile1, ck2gfx_MaskedShieldType_textureFile2}

# ck2gfx_LineChartType class attributes and methods
ck2gfx_LineChartType_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
ck2gfx_LineChartType_name: Property = Property(name="name", type=StringType)
ck2gfx_LineChartType.attributes={ck2gfx_LineChartType_lineWidth, ck2gfx_LineChartType_name}

# ck2gfx_ObjectTypes class attributes and methods

# ck2gfx_EMFXActorType class attributes and methods
ck2gfx_EMFXActorType_idle: Property = Property(name="idle", type=StringType)
ck2gfx_EMFXActorType_move: Property = Property(name="move", type=StringType)
ck2gfx_EMFXActorType_attack: Property = Property(name="attack", type=StringType)
ck2gfx_EMFXActorType_scale: Property = Property(name="scale", type=FloatType)
ck2gfx_EMFXActorType_useAnimation: Property = Property(name="useAnimation", type=BooleanType)
ck2gfx_EMFXActorType_cullDistance: Property = Property(name="cullDistance", type=FloatType)
ck2gfx_EMFXActorType_scaleOnCullDistance: Property = Property(name="scaleOnCullDistance", type=BooleanType)
ck2gfx_EMFXActorType_name: Property = Property(name="name", type=StringType)
ck2gfx_EMFXActorType_actorFile: Property = Property(name="actorFile", type=StringType)
ck2gfx_EMFXActorType.attributes={ck2gfx_EMFXActorType_cullDistance, ck2gfx_EMFXActorType_scale, ck2gfx_EMFXActorType_scaleOnCullDistance, ck2gfx_EMFXActorType_attack, ck2gfx_EMFXActorType_actorFile, ck2gfx_EMFXActorType_name, ck2gfx_EMFXActorType_idle, ck2gfx_EMFXActorType_useAnimation, ck2gfx_EMFXActorType_move}

# ck2gfx_Animation class attributes and methods
ck2gfx_Animation_name: Property = Property(name="name", type=StringType)
ck2gfx_Animation_file: Property = Property(name="file", type=StringType)
ck2gfx_Animation_defaultAnimationTime: Property = Property(name="defaultAnimationTime", type=FloatType)
ck2gfx_Animation.attributes={ck2gfx_Animation_name, ck2gfx_Animation_file, ck2gfx_Animation_defaultAnimationTime}

# ck2gfx_BitmapFonts class attributes and methods

# ck2gfx_Pdxmesh class attributes and methods
ck2gfx_Pdxmesh_name: Property = Property(name="name", type=StringType)
ck2gfx_Pdxmesh_actorFile: Property = Property(name="actorFile", type=StringType)
ck2gfx_Pdxmesh_scale: Property = Property(name="scale", type=FloatType)
ck2gfx_Pdxmesh_cullDistance: Property = Property(name="cullDistance", type=FloatType)
ck2gfx_Pdxmesh_scaleOnCullDistance: Property = Property(name="scaleOnCullDistance", type=BooleanType)
ck2gfx_Pdxmesh.attributes={ck2gfx_Pdxmesh_cullDistance, ck2gfx_Pdxmesh_actorFile, ck2gfx_Pdxmesh_scale, ck2gfx_Pdxmesh_name, ck2gfx_Pdxmesh_scaleOnCullDistance}

# ck2gfx_ArrowType class attributes and methods
ck2gfx_ArrowType_endAt: Property = Property(name="endAt", type=FloatType)
ck2gfx_ArrowType_height: Property = Property(name="height", type=FloatType)
ck2gfx_ArrowType_type: Property = Property(name="type", type=IntegerType)
ck2gfx_ArrowType_heading: Property = Property(name="heading", type=FloatType)
ck2gfx_ArrowType_effect: Property = Property(name="effect", type=StringType)
ck2gfx_ArrowType_name: Property = Property(name="name", type=StringType)
ck2gfx_ArrowType_size: Property = Property(name="size", type=FloatType)
ck2gfx_ArrowType_textureFile: Property = Property(name="textureFile", type=StringType)
ck2gfx_ArrowType_bodyTexture: Property = Property(name="bodyTexture", type=StringType)
ck2gfx_ArrowType.attributes={ck2gfx_ArrowType_type, ck2gfx_ArrowType_size, ck2gfx_ArrowType_height, ck2gfx_ArrowType_effect, ck2gfx_ArrowType_textureFile, ck2gfx_ArrowType_heading, ck2gfx_ArrowType_endAt, ck2gfx_ArrowType_bodyTexture, ck2gfx_ArrowType_name}

# ck2gfx_BitmapFont class attributes and methods
ck2gfx_BitmapFont_name: Property = Property(name="name", type=StringType)
ck2gfx_BitmapFont_fontName: Property = Property(name="fontName", type=StringType)
ck2gfx_BitmapFont_color: Property = Property(name="color", type=IntegerType)
ck2gfx_BitmapFont_effect: Property = Property(name="effect", type=BooleanType)
ck2gfx_BitmapFont.attributes={ck2gfx_BitmapFont_effect, ck2gfx_BitmapFont_name, ck2gfx_BitmapFont_color, ck2gfx_BitmapFont_fontName}

# ck2gfx_ColorCode class attributes and methods
ck2gfx_ColorCode_key: Property = Property(name="key", type=StringType)
ck2gfx_ColorCode.attributes={ck2gfx_ColorCode_key}

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="ck2gfx_EObject", type=ck2gfx_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_Model", type=ck2gfx_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="ck2gfx_EObject2", type=ck2gfx_SpriteTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_SpriteTypes", type=ck2gfx_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borderSize4: BinaryAssociation = BinaryAssociation(
    name="borderSize4",
    ends={
        Property(name="ck2gfx_Coordinates6", type=ck2gfx_CorneredTileSpriteType, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_CorneredTileSpriteType5", type=ck2gfx_Coordinates, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size3: BinaryAssociation = BinaryAssociation(
    name="size3",
    ends={
        Property(name="ck2gfx_Coordinates", type=ck2gfx_CorneredTileSpriteType, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_CorneredTileSpriteType", type=ck2gfx_Coordinates, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hairColor14: BinaryAssociation = BinaryAssociation(
    name="hairColor14",
    ends={
        Property(name="ck2gfx_Color", type=ck2gfx_PortraitType, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_PortraitType", type=ck2gfx_Color, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
color7: BinaryAssociation = BinaryAssociation(
    name="color7",
    ends={
        Property(name="ck2gfx_ColorRatio", type=ck2gfx_ProgressbarType, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_ProgressbarType", type=ck2gfx_ColorRatio, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color28: BinaryAssociation = BinaryAssociation(
    name="color28",
    ends={
        Property(name="ck2gfx_ColorRatio10", type=ck2gfx_ProgressbarType, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_ProgressbarType9", type=ck2gfx_ColorRatio, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size11: BinaryAssociation = BinaryAssociation(
    name="size11",
    ends={
        Property(name="ck2gfx_Coordinates13", type=ck2gfx_ProgressbarType, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_ProgressbarType12", type=ck2gfx_Coordinates, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
layers20: BinaryAssociation = BinaryAssociation(
    name="layers20",
    ends={
        Property(name="ck2gfx_CoatOfArmsLayer", type=ck2gfx_CoatOfArmsType, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_CoatOfArmsType", type=ck2gfx_CoatOfArmsLayer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eyeColor15: BinaryAssociation = BinaryAssociation(
    name="eyeColor15",
    ends={
        Property(name="ck2gfx_Color17", type=ck2gfx_PortraitType, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_PortraitType16", type=ck2gfx_Color, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
size18: BinaryAssociation = BinaryAssociation(
    name="size18",
    ends={
        Property(name="ck2gfx_Coordinates19", type=ck2gfx_LineChartType, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_LineChartType", type=ck2gfx_Coordinates, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
center21: BinaryAssociation = BinaryAssociation(
    name="center21",
    ends={
        Property(name="ck2gfx_Coordinates23", type=ck2gfx_CoatOfArmsLayer, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_CoatOfArmsLayer22", type=ck2gfx_Coordinates, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types24: BinaryAssociation = BinaryAssociation(
    name="types24",
    ends={
        Property(name="ck2gfx_EObject25", type=ck2gfx_ObjectTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_ObjectTypes", type=ck2gfx_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
animation26: BinaryAssociation = BinaryAssociation(
    name="animation26",
    ends={
        Property(name="ck2gfx_Animation", type=ck2gfx_EMFXActorType, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_EMFXActorType", type=ck2gfx_Animation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color27: BinaryAssociation = BinaryAssociation(
    name="color27",
    ends={
        Property(name="ck2gfx_ColorRatio28", type=ck2gfx_ArrowType, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_ArrowType", type=ck2gfx_ColorRatio, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color229: BinaryAssociation = BinaryAssociation(
    name="color229",
    ends={
        Property(name="ck2gfx_ColorRatio31", type=ck2gfx_ArrowType, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_ArrowType30", type=ck2gfx_ColorRatio, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value35: BinaryAssociation = BinaryAssociation(
    name="value35",
    ends={
        Property(name="ck2gfx_Color37", type=ck2gfx_ColorCode, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_ColorCode36", type=ck2gfx_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types32: BinaryAssociation = BinaryAssociation(
    name="types32",
    ends={
        Property(name="ck2gfx_BitmapFont", type=ck2gfx_BitmapFonts, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_BitmapFonts", type=ck2gfx_BitmapFont, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colorcodes33: BinaryAssociation = BinaryAssociation(
    name="colorcodes33",
    ends={
        Property(name="ck2gfx_ColorCode", type=ck2gfx_BitmapFont, multiplicity=Multiplicity(1, 1)),
        Property(name="ck2gfx_BitmapFont34", type=ck2gfx_ColorCode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ck2gfx",
    types={ck2gfx_Model, ck2gfx_EObject, ck2gfx_Color, ck2gfx_ColorRatio, ck2gfx_Coordinates, ck2gfx_SpriteTypes, ck2gfx_SpriteType, ck2gfx_ProgressbarType, ck2gfx_AnimatedSpriteType, ck2gfx_CorneredTileSpriteType, ck2gfx_PortraitType, ck2gfx_CoatOfArmsType, ck2gfx_CoatOfArmsLayer, ck2gfx_MaskedShieldType, ck2gfx_LineChartType, ck2gfx_ObjectTypes, ck2gfx_EMFXActorType, ck2gfx_Animation, ck2gfx_BitmapFonts, ck2gfx_Pdxmesh, ck2gfx_ArrowType, ck2gfx_BitmapFont, ck2gfx_ColorCode},
    associations={types0, types1, borderSize4, size3, hairColor14, color7, color28, size11, layers20, eyeColor15, size18, center21, types24, animation26, color27, color229, value35, types32, colorcodes33},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)