from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ck2gfx_ColorCode:

    def __init__(self, key: str, ck2gfx_ColorCode36: "ck2gfx_Color" = None, ck2gfx_ColorCode: "ck2gfx_BitmapFont" = None):
        self.key = key
        self.ck2gfx_ColorCode36 = ck2gfx_ColorCode36
        self.ck2gfx_ColorCode = ck2gfx_ColorCode
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def ck2gfx_ColorCode36(self):
        return self.__ck2gfx_ColorCode36

    @ck2gfx_ColorCode36.setter
    def ck2gfx_ColorCode36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_ColorCode__ck2gfx_ColorCode36", None)
        self.__ck2gfx_ColorCode36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_Color37"):
                opp_val = getattr(old_value, "ck2gfx_Color37", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_Color37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_Color37"):
                opp_val = getattr(value, "ck2gfx_Color37", None)
                setattr(value, "ck2gfx_Color37", self)

    @property
    def ck2gfx_ColorCode(self):
        return self.__ck2gfx_ColorCode

    @ck2gfx_ColorCode.setter
    def ck2gfx_ColorCode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_ColorCode__ck2gfx_ColorCode", None)
        self.__ck2gfx_ColorCode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_BitmapFont34"):
                opp_val = getattr(old_value, "ck2gfx_BitmapFont34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_BitmapFont34"):
                opp_val = getattr(value, "ck2gfx_BitmapFont34", None)
                if opp_val is None:
                    setattr(value, "ck2gfx_BitmapFont34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ck2gfx_BitmapFont:

    def __init__(self, name: str, fontName: str, color: int, effect: bool, ck2gfx_BitmapFont: "ck2gfx_BitmapFonts" = None, ck2gfx_BitmapFont34: set["ck2gfx_ColorCode"] = None):
        self.name = name
        self.fontName = fontName
        self.color = color
        self.effect = effect
        self.ck2gfx_BitmapFont = ck2gfx_BitmapFont
        self.ck2gfx_BitmapFont34 = ck2gfx_BitmapFont34 if ck2gfx_BitmapFont34 is not None else set()
        
    @property
    def effect(self) -> bool:
        return self.__effect

    @effect.setter
    def effect(self, effect: bool):
        self.__effect = effect

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def color(self) -> int:
        return self.__color

    @color.setter
    def color(self, color: int):
        self.__color = color

    @property
    def fontName(self) -> str:
        return self.__fontName

    @fontName.setter
    def fontName(self, fontName: str):
        self.__fontName = fontName

    @property
    def ck2gfx_BitmapFont34(self):
        return self.__ck2gfx_BitmapFont34

    @ck2gfx_BitmapFont34.setter
    def ck2gfx_BitmapFont34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_BitmapFont__ck2gfx_BitmapFont34", None)
        self.__ck2gfx_BitmapFont34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ck2gfx_ColorCode"):
                    opp_val = getattr(item, "ck2gfx_ColorCode", None)
                    
                    if opp_val == self:
                        setattr(item, "ck2gfx_ColorCode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ck2gfx_ColorCode"):
                    opp_val = getattr(item, "ck2gfx_ColorCode", None)
                    
                    setattr(item, "ck2gfx_ColorCode", self)
                    

    @property
    def ck2gfx_BitmapFont(self):
        return self.__ck2gfx_BitmapFont

    @ck2gfx_BitmapFont.setter
    def ck2gfx_BitmapFont(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_BitmapFont__ck2gfx_BitmapFont", None)
        self.__ck2gfx_BitmapFont = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_BitmapFonts"):
                opp_val = getattr(old_value, "ck2gfx_BitmapFonts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_BitmapFonts"):
                opp_val = getattr(value, "ck2gfx_BitmapFonts", None)
                if opp_val is None:
                    setattr(value, "ck2gfx_BitmapFonts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ck2gfx_ArrowType:

    def __init__(self, endAt: float, height: float, type: int, heading: float, effect: str, name: str, size: float, textureFile: str, bodyTexture: str, ck2gfx_ArrowType: "ck2gfx_ColorRatio" = None, ck2gfx_ArrowType30: "ck2gfx_ColorRatio" = None):
        self.endAt = endAt
        self.height = height
        self.type = type
        self.heading = heading
        self.effect = effect
        self.name = name
        self.size = size
        self.textureFile = textureFile
        self.bodyTexture = bodyTexture
        self.ck2gfx_ArrowType = ck2gfx_ArrowType
        self.ck2gfx_ArrowType30 = ck2gfx_ArrowType30
        
    @property
    def type(self) -> int:
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def size(self) -> float:
        return self.__size

    @size.setter
    def size(self, size: float):
        self.__size = size

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect

    @property
    def textureFile(self) -> str:
        return self.__textureFile

    @textureFile.setter
    def textureFile(self, textureFile: str):
        self.__textureFile = textureFile

    @property
    def heading(self) -> float:
        return self.__heading

    @heading.setter
    def heading(self, heading: float):
        self.__heading = heading

    @property
    def endAt(self) -> float:
        return self.__endAt

    @endAt.setter
    def endAt(self, endAt: float):
        self.__endAt = endAt

    @property
    def bodyTexture(self) -> str:
        return self.__bodyTexture

    @bodyTexture.setter
    def bodyTexture(self, bodyTexture: str):
        self.__bodyTexture = bodyTexture

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ck2gfx_ArrowType30(self):
        return self.__ck2gfx_ArrowType30

    @ck2gfx_ArrowType30.setter
    def ck2gfx_ArrowType30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_ArrowType__ck2gfx_ArrowType30", None)
        self.__ck2gfx_ArrowType30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_ColorRatio31"):
                opp_val = getattr(old_value, "ck2gfx_ColorRatio31", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_ColorRatio31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_ColorRatio31"):
                opp_val = getattr(value, "ck2gfx_ColorRatio31", None)
                setattr(value, "ck2gfx_ColorRatio31", self)

    @property
    def ck2gfx_ArrowType(self):
        return self.__ck2gfx_ArrowType

    @ck2gfx_ArrowType.setter
    def ck2gfx_ArrowType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_ArrowType__ck2gfx_ArrowType", None)
        self.__ck2gfx_ArrowType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_ColorRatio28"):
                opp_val = getattr(old_value, "ck2gfx_ColorRatio28", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_ColorRatio28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_ColorRatio28"):
                opp_val = getattr(value, "ck2gfx_ColorRatio28", None)
                setattr(value, "ck2gfx_ColorRatio28", self)

class ck2gfx_Pdxmesh:

    def __init__(self, name: str, actorFile: str, scale: float, cullDistance: float, scaleOnCullDistance: bool):
        self.name = name
        self.actorFile = actorFile
        self.scale = scale
        self.cullDistance = cullDistance
        self.scaleOnCullDistance = scaleOnCullDistance
        
    @property
    def cullDistance(self) -> float:
        return self.__cullDistance

    @cullDistance.setter
    def cullDistance(self, cullDistance: float):
        self.__cullDistance = cullDistance

    @property
    def actorFile(self) -> str:
        return self.__actorFile

    @actorFile.setter
    def actorFile(self, actorFile: str):
        self.__actorFile = actorFile

    @property
    def scale(self) -> float:
        return self.__scale

    @scale.setter
    def scale(self, scale: float):
        self.__scale = scale

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def scaleOnCullDistance(self) -> bool:
        return self.__scaleOnCullDistance

    @scaleOnCullDistance.setter
    def scaleOnCullDistance(self, scaleOnCullDistance: bool):
        self.__scaleOnCullDistance = scaleOnCullDistance

class ck2gfx_BitmapFonts:

    pass
class ck2gfx_Animation:

    def __init__(self, name: str, file: str, defaultAnimationTime: float, ck2gfx_Animation: "ck2gfx_EMFXActorType" = None):
        self.name = name
        self.file = file
        self.defaultAnimationTime = defaultAnimationTime
        self.ck2gfx_Animation = ck2gfx_Animation
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def defaultAnimationTime(self) -> float:
        return self.__defaultAnimationTime

    @defaultAnimationTime.setter
    def defaultAnimationTime(self, defaultAnimationTime: float):
        self.__defaultAnimationTime = defaultAnimationTime

    @property
    def ck2gfx_Animation(self):
        return self.__ck2gfx_Animation

    @ck2gfx_Animation.setter
    def ck2gfx_Animation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_Animation__ck2gfx_Animation", None)
        self.__ck2gfx_Animation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_EMFXActorType"):
                opp_val = getattr(old_value, "ck2gfx_EMFXActorType", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_EMFXActorType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_EMFXActorType"):
                opp_val = getattr(value, "ck2gfx_EMFXActorType", None)
                setattr(value, "ck2gfx_EMFXActorType", self)

class ck2gfx_EMFXActorType:

    def __init__(self, idle: str, move: str, attack: str, scale: float, useAnimation: bool, cullDistance: float, scaleOnCullDistance: bool, name: str, actorFile: str, ck2gfx_EMFXActorType: "ck2gfx_Animation" = None):
        self.idle = idle
        self.move = move
        self.attack = attack
        self.scale = scale
        self.useAnimation = useAnimation
        self.cullDistance = cullDistance
        self.scaleOnCullDistance = scaleOnCullDistance
        self.name = name
        self.actorFile = actorFile
        self.ck2gfx_EMFXActorType = ck2gfx_EMFXActorType
        
    @property
    def cullDistance(self) -> float:
        return self.__cullDistance

    @cullDistance.setter
    def cullDistance(self, cullDistance: float):
        self.__cullDistance = cullDistance

    @property
    def scale(self) -> float:
        return self.__scale

    @scale.setter
    def scale(self, scale: float):
        self.__scale = scale

    @property
    def scaleOnCullDistance(self) -> bool:
        return self.__scaleOnCullDistance

    @scaleOnCullDistance.setter
    def scaleOnCullDistance(self, scaleOnCullDistance: bool):
        self.__scaleOnCullDistance = scaleOnCullDistance

    @property
    def attack(self) -> str:
        return self.__attack

    @attack.setter
    def attack(self, attack: str):
        self.__attack = attack

    @property
    def actorFile(self) -> str:
        return self.__actorFile

    @actorFile.setter
    def actorFile(self, actorFile: str):
        self.__actorFile = actorFile

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idle(self) -> str:
        return self.__idle

    @idle.setter
    def idle(self, idle: str):
        self.__idle = idle

    @property
    def useAnimation(self) -> bool:
        return self.__useAnimation

    @useAnimation.setter
    def useAnimation(self, useAnimation: bool):
        self.__useAnimation = useAnimation

    @property
    def move(self) -> str:
        return self.__move

    @move.setter
    def move(self, move: str):
        self.__move = move

    @property
    def ck2gfx_EMFXActorType(self):
        return self.__ck2gfx_EMFXActorType

    @ck2gfx_EMFXActorType.setter
    def ck2gfx_EMFXActorType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_EMFXActorType__ck2gfx_EMFXActorType", None)
        self.__ck2gfx_EMFXActorType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_Animation"):
                opp_val = getattr(old_value, "ck2gfx_Animation", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_Animation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_Animation"):
                opp_val = getattr(value, "ck2gfx_Animation", None)
                setattr(value, "ck2gfx_Animation", self)

class ck2gfx_ObjectTypes:

    pass
class ck2gfx_LineChartType:

    def __init__(self, lineWidth: int, name: str, ck2gfx_LineChartType: "ck2gfx_Coordinates" = None):
        self.lineWidth = lineWidth
        self.name = name
        self.ck2gfx_LineChartType = ck2gfx_LineChartType
        
    @property
    def lineWidth(self) -> int:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ck2gfx_LineChartType(self):
        return self.__ck2gfx_LineChartType

    @ck2gfx_LineChartType.setter
    def ck2gfx_LineChartType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_LineChartType__ck2gfx_LineChartType", None)
        self.__ck2gfx_LineChartType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_Coordinates19"):
                opp_val = getattr(old_value, "ck2gfx_Coordinates19", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_Coordinates19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_Coordinates19"):
                opp_val = getattr(value, "ck2gfx_Coordinates19", None)
                setattr(value, "ck2gfx_Coordinates19", self)

class ck2gfx_MaskedShieldType:

    def __init__(self, name: str, textureFile1: str, textureFile2: str, effectFile: str, allwaysTransparent: bool, clickSound: str):
        self.name = name
        self.textureFile1 = textureFile1
        self.textureFile2 = textureFile2
        self.effectFile = effectFile
        self.allwaysTransparent = allwaysTransparent
        self.clickSound = clickSound
        
    @property
    def effectFile(self) -> str:
        return self.__effectFile

    @effectFile.setter
    def effectFile(self, effectFile: str):
        self.__effectFile = effectFile

    @property
    def allwaysTransparent(self) -> bool:
        return self.__allwaysTransparent

    @allwaysTransparent.setter
    def allwaysTransparent(self, allwaysTransparent: bool):
        self.__allwaysTransparent = allwaysTransparent

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def clickSound(self) -> str:
        return self.__clickSound

    @clickSound.setter
    def clickSound(self, clickSound: str):
        self.__clickSound = clickSound

    @property
    def textureFile1(self) -> str:
        return self.__textureFile1

    @textureFile1.setter
    def textureFile1(self, textureFile1: str):
        self.__textureFile1 = textureFile1

    @property
    def textureFile2(self) -> str:
        return self.__textureFile2

    @textureFile2.setter
    def textureFile2(self, textureFile2: str):
        self.__textureFile2 = textureFile2

class ck2gfx_CoatOfArmsLayer:

    def __init__(self, mask: str, scale: float, ck2gfx_CoatOfArmsLayer: "ck2gfx_CoatOfArmsType" = None, ck2gfx_CoatOfArmsLayer22: "ck2gfx_Coordinates" = None):
        self.mask = mask
        self.scale = scale
        self.ck2gfx_CoatOfArmsLayer = ck2gfx_CoatOfArmsLayer
        self.ck2gfx_CoatOfArmsLayer22 = ck2gfx_CoatOfArmsLayer22
        
    @property
    def mask(self) -> str:
        return self.__mask

    @mask.setter
    def mask(self, mask: str):
        self.__mask = mask

    @property
    def scale(self) -> float:
        return self.__scale

    @scale.setter
    def scale(self, scale: float):
        self.__scale = scale

    @property
    def ck2gfx_CoatOfArmsLayer(self):
        return self.__ck2gfx_CoatOfArmsLayer

    @ck2gfx_CoatOfArmsLayer.setter
    def ck2gfx_CoatOfArmsLayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_CoatOfArmsLayer__ck2gfx_CoatOfArmsLayer", None)
        self.__ck2gfx_CoatOfArmsLayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_CoatOfArmsType"):
                opp_val = getattr(old_value, "ck2gfx_CoatOfArmsType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_CoatOfArmsType"):
                opp_val = getattr(value, "ck2gfx_CoatOfArmsType", None)
                if opp_val is None:
                    setattr(value, "ck2gfx_CoatOfArmsType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ck2gfx_CoatOfArmsLayer22(self):
        return self.__ck2gfx_CoatOfArmsLayer22

    @ck2gfx_CoatOfArmsLayer22.setter
    def ck2gfx_CoatOfArmsLayer22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_CoatOfArmsLayer__ck2gfx_CoatOfArmsLayer22", None)
        self.__ck2gfx_CoatOfArmsLayer22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_Coordinates23"):
                opp_val = getattr(old_value, "ck2gfx_Coordinates23", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_Coordinates23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_Coordinates23"):
                opp_val = getattr(value, "ck2gfx_Coordinates23", None)
                setattr(value, "ck2gfx_Coordinates23", self)

class ck2gfx_CoatOfArmsType:

    def __init__(self, name: str, frame: str, mask: str, sealOverlay: str, effect: str, ck2gfx_CoatOfArmsType: set["ck2gfx_CoatOfArmsLayer"] = None):
        self.name = name
        self.frame = frame
        self.mask = mask
        self.sealOverlay = sealOverlay
        self.effect = effect
        self.ck2gfx_CoatOfArmsType = ck2gfx_CoatOfArmsType if ck2gfx_CoatOfArmsType is not None else set()
        
    @property
    def frame(self) -> str:
        return self.__frame

    @frame.setter
    def frame(self, frame: str):
        self.__frame = frame

    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect

    @property
    def mask(self) -> str:
        return self.__mask

    @mask.setter
    def mask(self, mask: str):
        self.__mask = mask

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sealOverlay(self) -> str:
        return self.__sealOverlay

    @sealOverlay.setter
    def sealOverlay(self, sealOverlay: str):
        self.__sealOverlay = sealOverlay

    @property
    def ck2gfx_CoatOfArmsType(self):
        return self.__ck2gfx_CoatOfArmsType

    @ck2gfx_CoatOfArmsType.setter
    def ck2gfx_CoatOfArmsType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_CoatOfArmsType__ck2gfx_CoatOfArmsType", None)
        self.__ck2gfx_CoatOfArmsType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ck2gfx_CoatOfArmsLayer"):
                    opp_val = getattr(item, "ck2gfx_CoatOfArmsLayer", None)
                    
                    if opp_val == self:
                        setattr(item, "ck2gfx_CoatOfArmsLayer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ck2gfx_CoatOfArmsLayer"):
                    opp_val = getattr(item, "ck2gfx_CoatOfArmsLayer", None)
                    
                    setattr(item, "ck2gfx_CoatOfArmsLayer", self)
                    

class ck2gfx_PortraitType:

    def __init__(self, name: str, effectFile: str, layers: str, hairColorIndex: int, eyeColorIndex: int, headgearThatHidesHair: int, ck2gfx_PortraitType: set["ck2gfx_Color"] = None, ck2gfx_PortraitType16: set["ck2gfx_Color"] = None):
        self.name = name
        self.effectFile = effectFile
        self.layers = layers
        self.hairColorIndex = hairColorIndex
        self.eyeColorIndex = eyeColorIndex
        self.headgearThatHidesHair = headgearThatHidesHair
        self.ck2gfx_PortraitType = ck2gfx_PortraitType if ck2gfx_PortraitType is not None else set()
        self.ck2gfx_PortraitType16 = ck2gfx_PortraitType16 if ck2gfx_PortraitType16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def layers(self) -> str:
        return self.__layers

    @layers.setter
    def layers(self, layers: str):
        self.__layers = layers

    @property
    def eyeColorIndex(self) -> int:
        return self.__eyeColorIndex

    @eyeColorIndex.setter
    def eyeColorIndex(self, eyeColorIndex: int):
        self.__eyeColorIndex = eyeColorIndex

    @property
    def effectFile(self) -> str:
        return self.__effectFile

    @effectFile.setter
    def effectFile(self, effectFile: str):
        self.__effectFile = effectFile

    @property
    def headgearThatHidesHair(self) -> int:
        return self.__headgearThatHidesHair

    @headgearThatHidesHair.setter
    def headgearThatHidesHair(self, headgearThatHidesHair: int):
        self.__headgearThatHidesHair = headgearThatHidesHair

    @property
    def hairColorIndex(self) -> int:
        return self.__hairColorIndex

    @hairColorIndex.setter
    def hairColorIndex(self, hairColorIndex: int):
        self.__hairColorIndex = hairColorIndex

    @property
    def ck2gfx_PortraitType16(self):
        return self.__ck2gfx_PortraitType16

    @ck2gfx_PortraitType16.setter
    def ck2gfx_PortraitType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_PortraitType__ck2gfx_PortraitType16", None)
        self.__ck2gfx_PortraitType16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ck2gfx_Color17"):
                    opp_val = getattr(item, "ck2gfx_Color17", None)
                    
                    if opp_val == self:
                        setattr(item, "ck2gfx_Color17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ck2gfx_Color17"):
                    opp_val = getattr(item, "ck2gfx_Color17", None)
                    
                    setattr(item, "ck2gfx_Color17", self)
                    

    @property
    def ck2gfx_PortraitType(self):
        return self.__ck2gfx_PortraitType

    @ck2gfx_PortraitType.setter
    def ck2gfx_PortraitType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_PortraitType__ck2gfx_PortraitType", None)
        self.__ck2gfx_PortraitType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ck2gfx_Color"):
                    opp_val = getattr(item, "ck2gfx_Color", None)
                    
                    if opp_val == self:
                        setattr(item, "ck2gfx_Color", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ck2gfx_Color"):
                    opp_val = getattr(item, "ck2gfx_Color", None)
                    
                    setattr(item, "ck2gfx_Color", self)
                    

class ck2gfx_CorneredTileSpriteType:

    def __init__(self, allwaysTransparent: bool, noRefCount: bool, loadType: str, tilingCenter: bool, name: str, texturefile: str, ck2gfx_CorneredTileSpriteType5: "ck2gfx_Coordinates" = None, ck2gfx_CorneredTileSpriteType: "ck2gfx_Coordinates" = None):
        self.allwaysTransparent = allwaysTransparent
        self.noRefCount = noRefCount
        self.loadType = loadType
        self.tilingCenter = tilingCenter
        self.name = name
        self.texturefile = texturefile
        self.ck2gfx_CorneredTileSpriteType5 = ck2gfx_CorneredTileSpriteType5
        self.ck2gfx_CorneredTileSpriteType = ck2gfx_CorneredTileSpriteType
        
    @property
    def texturefile(self) -> str:
        return self.__texturefile

    @texturefile.setter
    def texturefile(self, texturefile: str):
        self.__texturefile = texturefile

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tilingCenter(self) -> bool:
        return self.__tilingCenter

    @tilingCenter.setter
    def tilingCenter(self, tilingCenter: bool):
        self.__tilingCenter = tilingCenter

    @property
    def loadType(self) -> str:
        return self.__loadType

    @loadType.setter
    def loadType(self, loadType: str):
        self.__loadType = loadType

    @property
    def allwaysTransparent(self) -> bool:
        return self.__allwaysTransparent

    @allwaysTransparent.setter
    def allwaysTransparent(self, allwaysTransparent: bool):
        self.__allwaysTransparent = allwaysTransparent

    @property
    def noRefCount(self) -> bool:
        return self.__noRefCount

    @noRefCount.setter
    def noRefCount(self, noRefCount: bool):
        self.__noRefCount = noRefCount

    @property
    def ck2gfx_CorneredTileSpriteType(self):
        return self.__ck2gfx_CorneredTileSpriteType

    @ck2gfx_CorneredTileSpriteType.setter
    def ck2gfx_CorneredTileSpriteType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_CorneredTileSpriteType__ck2gfx_CorneredTileSpriteType", None)
        self.__ck2gfx_CorneredTileSpriteType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_Coordinates"):
                opp_val = getattr(old_value, "ck2gfx_Coordinates", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_Coordinates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_Coordinates"):
                opp_val = getattr(value, "ck2gfx_Coordinates", None)
                setattr(value, "ck2gfx_Coordinates", self)

    @property
    def ck2gfx_CorneredTileSpriteType5(self):
        return self.__ck2gfx_CorneredTileSpriteType5

    @ck2gfx_CorneredTileSpriteType5.setter
    def ck2gfx_CorneredTileSpriteType5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_CorneredTileSpriteType__ck2gfx_CorneredTileSpriteType5", None)
        self.__ck2gfx_CorneredTileSpriteType5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_Coordinates6"):
                opp_val = getattr(old_value, "ck2gfx_Coordinates6", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_Coordinates6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_Coordinates6"):
                opp_val = getattr(value, "ck2gfx_Coordinates6", None)
                setattr(value, "ck2gfx_Coordinates6", self)

class ck2gfx_AnimatedSpriteType:

    def __init__(self, name: str, texturefile: str, noOfFrames: int, animationRateFps: float, looping: bool, playOnShow: bool):
        self.name = name
        self.texturefile = texturefile
        self.noOfFrames = noOfFrames
        self.animationRateFps = animationRateFps
        self.looping = looping
        self.playOnShow = playOnShow
        
    @property
    def looping(self) -> bool:
        return self.__looping

    @looping.setter
    def looping(self, looping: bool):
        self.__looping = looping

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def noOfFrames(self) -> int:
        return self.__noOfFrames

    @noOfFrames.setter
    def noOfFrames(self, noOfFrames: int):
        self.__noOfFrames = noOfFrames

    @property
    def playOnShow(self) -> bool:
        return self.__playOnShow

    @playOnShow.setter
    def playOnShow(self, playOnShow: bool):
        self.__playOnShow = playOnShow

    @property
    def animationRateFps(self) -> float:
        return self.__animationRateFps

    @animationRateFps.setter
    def animationRateFps(self, animationRateFps: float):
        self.__animationRateFps = animationRateFps

    @property
    def texturefile(self) -> str:
        return self.__texturefile

    @texturefile.setter
    def texturefile(self, texturefile: str):
        self.__texturefile = texturefile

class ck2gfx_ProgressbarType:

    def __init__(self, name: str, noRefCount: bool, textureFile1: str, textureFile2: str, horizontal: bool, effectFile: str, allwaysTransparent: bool, maxValue: float, loadType: str, ck2gfx_ProgressbarType: "ck2gfx_ColorRatio" = None, ck2gfx_ProgressbarType9: "ck2gfx_ColorRatio" = None, ck2gfx_ProgressbarType12: "ck2gfx_Coordinates" = None):
        self.name = name
        self.noRefCount = noRefCount
        self.textureFile1 = textureFile1
        self.textureFile2 = textureFile2
        self.horizontal = horizontal
        self.effectFile = effectFile
        self.allwaysTransparent = allwaysTransparent
        self.maxValue = maxValue
        self.loadType = loadType
        self.ck2gfx_ProgressbarType = ck2gfx_ProgressbarType
        self.ck2gfx_ProgressbarType9 = ck2gfx_ProgressbarType9
        self.ck2gfx_ProgressbarType12 = ck2gfx_ProgressbarType12
        
    @property
    def textureFile1(self) -> str:
        return self.__textureFile1

    @textureFile1.setter
    def textureFile1(self, textureFile1: str):
        self.__textureFile1 = textureFile1

    @property
    def horizontal(self) -> bool:
        return self.__horizontal

    @horizontal.setter
    def horizontal(self, horizontal: bool):
        self.__horizontal = horizontal

    @property
    def noRefCount(self) -> bool:
        return self.__noRefCount

    @noRefCount.setter
    def noRefCount(self, noRefCount: bool):
        self.__noRefCount = noRefCount

    @property
    def loadType(self) -> str:
        return self.__loadType

    @loadType.setter
    def loadType(self, loadType: str):
        self.__loadType = loadType

    @property
    def effectFile(self) -> str:
        return self.__effectFile

    @effectFile.setter
    def effectFile(self, effectFile: str):
        self.__effectFile = effectFile

    @property
    def allwaysTransparent(self) -> bool:
        return self.__allwaysTransparent

    @allwaysTransparent.setter
    def allwaysTransparent(self, allwaysTransparent: bool):
        self.__allwaysTransparent = allwaysTransparent

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def textureFile2(self) -> str:
        return self.__textureFile2

    @textureFile2.setter
    def textureFile2(self, textureFile2: str):
        self.__textureFile2 = textureFile2

    @property
    def maxValue(self) -> float:
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: float):
        self.__maxValue = maxValue

    @property
    def ck2gfx_ProgressbarType9(self):
        return self.__ck2gfx_ProgressbarType9

    @ck2gfx_ProgressbarType9.setter
    def ck2gfx_ProgressbarType9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_ProgressbarType__ck2gfx_ProgressbarType9", None)
        self.__ck2gfx_ProgressbarType9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_ColorRatio10"):
                opp_val = getattr(old_value, "ck2gfx_ColorRatio10", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_ColorRatio10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_ColorRatio10"):
                opp_val = getattr(value, "ck2gfx_ColorRatio10", None)
                setattr(value, "ck2gfx_ColorRatio10", self)

    @property
    def ck2gfx_ProgressbarType(self):
        return self.__ck2gfx_ProgressbarType

    @ck2gfx_ProgressbarType.setter
    def ck2gfx_ProgressbarType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_ProgressbarType__ck2gfx_ProgressbarType", None)
        self.__ck2gfx_ProgressbarType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_ColorRatio"):
                opp_val = getattr(old_value, "ck2gfx_ColorRatio", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_ColorRatio", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_ColorRatio"):
                opp_val = getattr(value, "ck2gfx_ColorRatio", None)
                setattr(value, "ck2gfx_ColorRatio", self)

    @property
    def ck2gfx_ProgressbarType12(self):
        return self.__ck2gfx_ProgressbarType12

    @ck2gfx_ProgressbarType12.setter
    def ck2gfx_ProgressbarType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_ProgressbarType__ck2gfx_ProgressbarType12", None)
        self.__ck2gfx_ProgressbarType12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_Coordinates13"):
                opp_val = getattr(old_value, "ck2gfx_Coordinates13", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_Coordinates13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_Coordinates13"):
                opp_val = getattr(value, "ck2gfx_Coordinates13", None)
                setattr(value, "ck2gfx_Coordinates13", self)

class ck2gfx_SpriteType:

    def __init__(self, name: str, textureFile: str, noOfFrames: int, loadType: str, allwaysTransparent: bool, noRefCount: bool, effectFile: str, transparenceCheck: bool, canBeLowres: bool, clickSound: str):
        self.name = name
        self.textureFile = textureFile
        self.noOfFrames = noOfFrames
        self.loadType = loadType
        self.allwaysTransparent = allwaysTransparent
        self.noRefCount = noRefCount
        self.effectFile = effectFile
        self.transparenceCheck = transparenceCheck
        self.canBeLowres = canBeLowres
        self.clickSound = clickSound
        
    @property
    def noRefCount(self) -> bool:
        return self.__noRefCount

    @noRefCount.setter
    def noRefCount(self, noRefCount: bool):
        self.__noRefCount = noRefCount

    @property
    def effectFile(self) -> str:
        return self.__effectFile

    @effectFile.setter
    def effectFile(self, effectFile: str):
        self.__effectFile = effectFile

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def allwaysTransparent(self) -> bool:
        return self.__allwaysTransparent

    @allwaysTransparent.setter
    def allwaysTransparent(self, allwaysTransparent: bool):
        self.__allwaysTransparent = allwaysTransparent

    @property
    def transparenceCheck(self) -> bool:
        return self.__transparenceCheck

    @transparenceCheck.setter
    def transparenceCheck(self, transparenceCheck: bool):
        self.__transparenceCheck = transparenceCheck

    @property
    def textureFile(self) -> str:
        return self.__textureFile

    @textureFile.setter
    def textureFile(self, textureFile: str):
        self.__textureFile = textureFile

    @property
    def canBeLowres(self) -> bool:
        return self.__canBeLowres

    @canBeLowres.setter
    def canBeLowres(self, canBeLowres: bool):
        self.__canBeLowres = canBeLowres

    @property
    def clickSound(self) -> str:
        return self.__clickSound

    @clickSound.setter
    def clickSound(self, clickSound: str):
        self.__clickSound = clickSound

    @property
    def loadType(self) -> str:
        return self.__loadType

    @loadType.setter
    def loadType(self, loadType: str):
        self.__loadType = loadType

    @property
    def noOfFrames(self) -> int:
        return self.__noOfFrames

    @noOfFrames.setter
    def noOfFrames(self, noOfFrames: int):
        self.__noOfFrames = noOfFrames

class ck2gfx_SpriteTypes:

    pass
class ck2gfx_Coordinates:

    def __init__(self, x: float, y: float, ck2gfx_Coordinates6: "ck2gfx_CorneredTileSpriteType" = None, ck2gfx_Coordinates: "ck2gfx_CorneredTileSpriteType" = None, ck2gfx_Coordinates13: "ck2gfx_ProgressbarType" = None, ck2gfx_Coordinates19: "ck2gfx_LineChartType" = None, ck2gfx_Coordinates23: "ck2gfx_CoatOfArmsLayer" = None):
        self.x = x
        self.y = y
        self.ck2gfx_Coordinates6 = ck2gfx_Coordinates6
        self.ck2gfx_Coordinates = ck2gfx_Coordinates
        self.ck2gfx_Coordinates13 = ck2gfx_Coordinates13
        self.ck2gfx_Coordinates19 = ck2gfx_Coordinates19
        self.ck2gfx_Coordinates23 = ck2gfx_Coordinates23
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def ck2gfx_Coordinates6(self):
        return self.__ck2gfx_Coordinates6

    @ck2gfx_Coordinates6.setter
    def ck2gfx_Coordinates6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_Coordinates__ck2gfx_Coordinates6", None)
        self.__ck2gfx_Coordinates6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_CorneredTileSpriteType5"):
                opp_val = getattr(old_value, "ck2gfx_CorneredTileSpriteType5", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_CorneredTileSpriteType5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_CorneredTileSpriteType5"):
                opp_val = getattr(value, "ck2gfx_CorneredTileSpriteType5", None)
                setattr(value, "ck2gfx_CorneredTileSpriteType5", self)

    @property
    def ck2gfx_Coordinates23(self):
        return self.__ck2gfx_Coordinates23

    @ck2gfx_Coordinates23.setter
    def ck2gfx_Coordinates23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_Coordinates__ck2gfx_Coordinates23", None)
        self.__ck2gfx_Coordinates23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_CoatOfArmsLayer22"):
                opp_val = getattr(old_value, "ck2gfx_CoatOfArmsLayer22", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_CoatOfArmsLayer22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_CoatOfArmsLayer22"):
                opp_val = getattr(value, "ck2gfx_CoatOfArmsLayer22", None)
                setattr(value, "ck2gfx_CoatOfArmsLayer22", self)

    @property
    def ck2gfx_Coordinates13(self):
        return self.__ck2gfx_Coordinates13

    @ck2gfx_Coordinates13.setter
    def ck2gfx_Coordinates13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_Coordinates__ck2gfx_Coordinates13", None)
        self.__ck2gfx_Coordinates13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_ProgressbarType12"):
                opp_val = getattr(old_value, "ck2gfx_ProgressbarType12", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_ProgressbarType12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_ProgressbarType12"):
                opp_val = getattr(value, "ck2gfx_ProgressbarType12", None)
                setattr(value, "ck2gfx_ProgressbarType12", self)

    @property
    def ck2gfx_Coordinates(self):
        return self.__ck2gfx_Coordinates

    @ck2gfx_Coordinates.setter
    def ck2gfx_Coordinates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_Coordinates__ck2gfx_Coordinates", None)
        self.__ck2gfx_Coordinates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_CorneredTileSpriteType"):
                opp_val = getattr(old_value, "ck2gfx_CorneredTileSpriteType", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_CorneredTileSpriteType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_CorneredTileSpriteType"):
                opp_val = getattr(value, "ck2gfx_CorneredTileSpriteType", None)
                setattr(value, "ck2gfx_CorneredTileSpriteType", self)

    @property
    def ck2gfx_Coordinates19(self):
        return self.__ck2gfx_Coordinates19

    @ck2gfx_Coordinates19.setter
    def ck2gfx_Coordinates19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_Coordinates__ck2gfx_Coordinates19", None)
        self.__ck2gfx_Coordinates19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_LineChartType"):
                opp_val = getattr(old_value, "ck2gfx_LineChartType", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_LineChartType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_LineChartType"):
                opp_val = getattr(value, "ck2gfx_LineChartType", None)
                setattr(value, "ck2gfx_LineChartType", self)

class ck2gfx_ColorRatio:

    def __init__(self, r: float, g: float, b: float, ck2gfx_ColorRatio: "ck2gfx_ProgressbarType" = None, ck2gfx_ColorRatio10: "ck2gfx_ProgressbarType" = None, ck2gfx_ColorRatio28: "ck2gfx_ArrowType" = None, ck2gfx_ColorRatio31: "ck2gfx_ArrowType" = None):
        self.r = r
        self.g = g
        self.b = b
        self.ck2gfx_ColorRatio = ck2gfx_ColorRatio
        self.ck2gfx_ColorRatio10 = ck2gfx_ColorRatio10
        self.ck2gfx_ColorRatio28 = ck2gfx_ColorRatio28
        self.ck2gfx_ColorRatio31 = ck2gfx_ColorRatio31
        
    @property
    def r(self) -> float:
        return self.__r

    @r.setter
    def r(self, r: float):
        self.__r = r

    @property
    def b(self) -> float:
        return self.__b

    @b.setter
    def b(self, b: float):
        self.__b = b

    @property
    def g(self) -> float:
        return self.__g

    @g.setter
    def g(self, g: float):
        self.__g = g

    @property
    def ck2gfx_ColorRatio(self):
        return self.__ck2gfx_ColorRatio

    @ck2gfx_ColorRatio.setter
    def ck2gfx_ColorRatio(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_ColorRatio__ck2gfx_ColorRatio", None)
        self.__ck2gfx_ColorRatio = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_ProgressbarType"):
                opp_val = getattr(old_value, "ck2gfx_ProgressbarType", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_ProgressbarType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_ProgressbarType"):
                opp_val = getattr(value, "ck2gfx_ProgressbarType", None)
                setattr(value, "ck2gfx_ProgressbarType", self)

    @property
    def ck2gfx_ColorRatio28(self):
        return self.__ck2gfx_ColorRatio28

    @ck2gfx_ColorRatio28.setter
    def ck2gfx_ColorRatio28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_ColorRatio__ck2gfx_ColorRatio28", None)
        self.__ck2gfx_ColorRatio28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_ArrowType"):
                opp_val = getattr(old_value, "ck2gfx_ArrowType", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_ArrowType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_ArrowType"):
                opp_val = getattr(value, "ck2gfx_ArrowType", None)
                setattr(value, "ck2gfx_ArrowType", self)

    @property
    def ck2gfx_ColorRatio31(self):
        return self.__ck2gfx_ColorRatio31

    @ck2gfx_ColorRatio31.setter
    def ck2gfx_ColorRatio31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_ColorRatio__ck2gfx_ColorRatio31", None)
        self.__ck2gfx_ColorRatio31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_ArrowType30"):
                opp_val = getattr(old_value, "ck2gfx_ArrowType30", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_ArrowType30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_ArrowType30"):
                opp_val = getattr(value, "ck2gfx_ArrowType30", None)
                setattr(value, "ck2gfx_ArrowType30", self)

    @property
    def ck2gfx_ColorRatio10(self):
        return self.__ck2gfx_ColorRatio10

    @ck2gfx_ColorRatio10.setter
    def ck2gfx_ColorRatio10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_ColorRatio__ck2gfx_ColorRatio10", None)
        self.__ck2gfx_ColorRatio10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_ProgressbarType9"):
                opp_val = getattr(old_value, "ck2gfx_ProgressbarType9", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_ProgressbarType9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_ProgressbarType9"):
                opp_val = getattr(value, "ck2gfx_ProgressbarType9", None)
                setattr(value, "ck2gfx_ProgressbarType9", self)

class ck2gfx_Color:

    def __init__(self, r: int, g: int, b: int, ck2gfx_Color: "ck2gfx_PortraitType" = None, ck2gfx_Color17: "ck2gfx_PortraitType" = None, ck2gfx_Color37: "ck2gfx_ColorCode" = None):
        self.r = r
        self.g = g
        self.b = b
        self.ck2gfx_Color = ck2gfx_Color
        self.ck2gfx_Color17 = ck2gfx_Color17
        self.ck2gfx_Color37 = ck2gfx_Color37
        
    @property
    def g(self) -> int:
        return self.__g

    @g.setter
    def g(self, g: int):
        self.__g = g

    @property
    def r(self) -> int:
        return self.__r

    @r.setter
    def r(self, r: int):
        self.__r = r

    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b

    @property
    def ck2gfx_Color37(self):
        return self.__ck2gfx_Color37

    @ck2gfx_Color37.setter
    def ck2gfx_Color37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_Color__ck2gfx_Color37", None)
        self.__ck2gfx_Color37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_ColorCode36"):
                opp_val = getattr(old_value, "ck2gfx_ColorCode36", None)
                if opp_val == self:
                    setattr(old_value, "ck2gfx_ColorCode36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_ColorCode36"):
                opp_val = getattr(value, "ck2gfx_ColorCode36", None)
                setattr(value, "ck2gfx_ColorCode36", self)

    @property
    def ck2gfx_Color(self):
        return self.__ck2gfx_Color

    @ck2gfx_Color.setter
    def ck2gfx_Color(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_Color__ck2gfx_Color", None)
        self.__ck2gfx_Color = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_PortraitType"):
                opp_val = getattr(old_value, "ck2gfx_PortraitType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_PortraitType"):
                opp_val = getattr(value, "ck2gfx_PortraitType", None)
                if opp_val is None:
                    setattr(value, "ck2gfx_PortraitType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ck2gfx_Color17(self):
        return self.__ck2gfx_Color17

    @ck2gfx_Color17.setter
    def ck2gfx_Color17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ck2gfx_Color__ck2gfx_Color17", None)
        self.__ck2gfx_Color17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ck2gfx_PortraitType16"):
                opp_val = getattr(old_value, "ck2gfx_PortraitType16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ck2gfx_PortraitType16"):
                opp_val = getattr(value, "ck2gfx_PortraitType16", None)
                if opp_val is None:
                    setattr(value, "ck2gfx_PortraitType16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ck2gfx_EObject:

    pass
class ck2gfx_Model:

    pass