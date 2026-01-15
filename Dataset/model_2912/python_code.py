from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class lSGL_GeneratorConfig:

    def __init__(self, cfgName: str, values: str, lSGL_GeneratorConfig: "lSGL_GeneratorAnnotation" = None):
        self.cfgName = cfgName
        self.values = values
        self.lSGL_GeneratorConfig = lSGL_GeneratorConfig
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

    @property
    def cfgName(self) -> str:
        return self.__cfgName

    @cfgName.setter
    def cfgName(self, cfgName: str):
        self.__cfgName = cfgName

    @property
    def lSGL_GeneratorConfig(self):
        return self.__lSGL_GeneratorConfig

    @lSGL_GeneratorConfig.setter
    def lSGL_GeneratorConfig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_GeneratorConfig__lSGL_GeneratorConfig", None)
        self.__lSGL_GeneratorConfig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_GeneratorAnnotation36"):
                opp_val = getattr(old_value, "lSGL_GeneratorAnnotation36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_GeneratorAnnotation36"):
                opp_val = getattr(value, "lSGL_GeneratorAnnotation36", None)
                if opp_val is None:
                    setattr(value, "lSGL_GeneratorAnnotation36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lSGL_Attribute:

    def __init__(self, isMap: bool, isList: bool, isArray: bool, name: str, lSGL_Attribute22: set["lSGL_Annotation"] = None, lSGL_Attribute24: "lSGL_AttributeType" = None, lSGL_Attribute27: "lSGL_AttributeType" = None, lSGL_Attribute: "lSGL_Entity" = None, lSGL_Attribute45: "lSGL_Projection" = None):
        self.isMap = isMap
        self.isList = isList
        self.isArray = isArray
        self.name = name
        self.lSGL_Attribute22 = lSGL_Attribute22 if lSGL_Attribute22 is not None else set()
        self.lSGL_Attribute24 = lSGL_Attribute24
        self.lSGL_Attribute27 = lSGL_Attribute27
        self.lSGL_Attribute = lSGL_Attribute
        self.lSGL_Attribute45 = lSGL_Attribute45
        
    @property
    def isArray(self) -> bool:
        return self.__isArray

    @isArray.setter
    def isArray(self, isArray: bool):
        self.__isArray = isArray

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isList(self) -> bool:
        return self.__isList

    @isList.setter
    def isList(self, isList: bool):
        self.__isList = isList

    @property
    def isMap(self) -> bool:
        return self.__isMap

    @isMap.setter
    def isMap(self, isMap: bool):
        self.__isMap = isMap

    @property
    def lSGL_Attribute22(self):
        return self.__lSGL_Attribute22

    @lSGL_Attribute22.setter
    def lSGL_Attribute22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Attribute__lSGL_Attribute22", None)
        self.__lSGL_Attribute22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lSGL_Annotation"):
                    opp_val = getattr(item, "lSGL_Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "lSGL_Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lSGL_Annotation"):
                    opp_val = getattr(item, "lSGL_Annotation", None)
                    
                    setattr(item, "lSGL_Annotation", self)
                    

    @property
    def lSGL_Attribute27(self):
        return self.__lSGL_Attribute27

    @lSGL_Attribute27.setter
    def lSGL_Attribute27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Attribute__lSGL_Attribute27", None)
        self.__lSGL_Attribute27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_AttributeType28"):
                opp_val = getattr(old_value, "lSGL_AttributeType28", None)
                if opp_val == self:
                    setattr(old_value, "lSGL_AttributeType28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_AttributeType28"):
                opp_val = getattr(value, "lSGL_AttributeType28", None)
                setattr(value, "lSGL_AttributeType28", self)

    @property
    def lSGL_Attribute(self):
        return self.__lSGL_Attribute

    @lSGL_Attribute.setter
    def lSGL_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Attribute__lSGL_Attribute", None)
        self.__lSGL_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_Entity18"):
                opp_val = getattr(old_value, "lSGL_Entity18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_Entity18"):
                opp_val = getattr(value, "lSGL_Entity18", None)
                if opp_val is None:
                    setattr(value, "lSGL_Entity18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lSGL_Attribute45(self):
        return self.__lSGL_Attribute45

    @lSGL_Attribute45.setter
    def lSGL_Attribute45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Attribute__lSGL_Attribute45", None)
        self.__lSGL_Attribute45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_Projection44"):
                opp_val = getattr(old_value, "lSGL_Projection44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_Projection44"):
                opp_val = getattr(value, "lSGL_Projection44", None)
                if opp_val is None:
                    setattr(value, "lSGL_Projection44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lSGL_Attribute24(self):
        return self.__lSGL_Attribute24

    @lSGL_Attribute24.setter
    def lSGL_Attribute24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Attribute__lSGL_Attribute24", None)
        self.__lSGL_Attribute24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_AttributeType25"):
                opp_val = getattr(old_value, "lSGL_AttributeType25", None)
                if opp_val == self:
                    setattr(old_value, "lSGL_AttributeType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_AttributeType25"):
                opp_val = getattr(value, "lSGL_AttributeType25", None)
                setattr(value, "lSGL_AttributeType25", self)

class lSGL_GeneratorAnnotation:

    pass
class lSGL_Annotation:

    def __init__(self, name: str, value: str, lSGL_Annotation: "lSGL_Attribute" = None):
        self.name = name
        self.value = value
        self.lSGL_Annotation = lSGL_Annotation
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def lSGL_Annotation(self):
        return self.__lSGL_Annotation

    @lSGL_Annotation.setter
    def lSGL_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Annotation__lSGL_Annotation", None)
        self.__lSGL_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_Attribute22"):
                opp_val = getattr(old_value, "lSGL_Attribute22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_Attribute22"):
                opp_val = getattr(value, "lSGL_Attribute22", None)
                if opp_val is None:
                    setattr(value, "lSGL_Attribute22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lSGL_AttributeType:

    def __init__(self, nullable: bool, typeName: str, lSGL_AttributeType: "lSGL_Type" = None, lSGL_AttributeType25: "lSGL_Attribute" = None, lSGL_AttributeType28: "lSGL_Attribute" = None):
        self.nullable = nullable
        self.typeName = typeName
        self.lSGL_AttributeType = lSGL_AttributeType
        self.lSGL_AttributeType25 = lSGL_AttributeType25
        self.lSGL_AttributeType28 = lSGL_AttributeType28
        
    @property
    def nullable(self) -> bool:
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable

    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def lSGL_AttributeType25(self):
        return self.__lSGL_AttributeType25

    @lSGL_AttributeType25.setter
    def lSGL_AttributeType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_AttributeType__lSGL_AttributeType25", None)
        self.__lSGL_AttributeType25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_Attribute24"):
                opp_val = getattr(old_value, "lSGL_Attribute24", None)
                if opp_val == self:
                    setattr(old_value, "lSGL_Attribute24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_Attribute24"):
                opp_val = getattr(value, "lSGL_Attribute24", None)
                setattr(value, "lSGL_Attribute24", self)

    @property
    def lSGL_AttributeType28(self):
        return self.__lSGL_AttributeType28

    @lSGL_AttributeType28.setter
    def lSGL_AttributeType28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_AttributeType__lSGL_AttributeType28", None)
        self.__lSGL_AttributeType28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_Attribute27"):
                opp_val = getattr(old_value, "lSGL_Attribute27", None)
                if opp_val == self:
                    setattr(old_value, "lSGL_Attribute27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_Attribute27"):
                opp_val = getattr(value, "lSGL_Attribute27", None)
                setattr(value, "lSGL_Attribute27", self)

    @property
    def lSGL_AttributeType(self):
        return self.__lSGL_AttributeType

    @lSGL_AttributeType.setter
    def lSGL_AttributeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_AttributeType__lSGL_AttributeType", None)
        self.__lSGL_AttributeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_Type20"):
                opp_val = getattr(old_value, "lSGL_Type20", None)
                if opp_val == self:
                    setattr(old_value, "lSGL_Type20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_Type20"):
                opp_val = getattr(value, "lSGL_Type20", None)
                setattr(value, "lSGL_Type20", self)

class lSGL_EnumItem:

    def __init__(self, name: str, value: str, lSGL_EnumItem: "lSGL_Enum" = None):
        self.name = name
        self.value = value
        self.lSGL_EnumItem = lSGL_EnumItem
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lSGL_EnumItem(self):
        return self.__lSGL_EnumItem

    @lSGL_EnumItem.setter
    def lSGL_EnumItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_EnumItem__lSGL_EnumItem", None)
        self.__lSGL_EnumItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_Enum"):
                opp_val = getattr(old_value, "lSGL_Enum", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_Enum"):
                opp_val = getattr(value, "lSGL_Enum", None)
                if opp_val is None:
                    setattr(value, "lSGL_Enum", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class lSGL_Entity(Type):

    pass
class lSGL_Enum(Type):

    pass
class lSGL_ConfigProperty:

    def __init__(self, name: str, value: str, lSGL_ConfigProperty11: "lSGL_Config" = None, lSGL_ConfigProperty: "lSGL_Generator" = None):
        self.name = name
        self.value = value
        self.lSGL_ConfigProperty11 = lSGL_ConfigProperty11
        self.lSGL_ConfigProperty = lSGL_ConfigProperty
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lSGL_ConfigProperty11(self):
        return self.__lSGL_ConfigProperty11

    @lSGL_ConfigProperty11.setter
    def lSGL_ConfigProperty11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_ConfigProperty__lSGL_ConfigProperty11", None)
        self.__lSGL_ConfigProperty11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_Config10"):
                opp_val = getattr(old_value, "lSGL_Config10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_Config10"):
                opp_val = getattr(value, "lSGL_Config10", None)
                if opp_val is None:
                    setattr(value, "lSGL_Config10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lSGL_ConfigProperty(self):
        return self.__lSGL_ConfigProperty

    @lSGL_ConfigProperty.setter
    def lSGL_ConfigProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_ConfigProperty__lSGL_ConfigProperty", None)
        self.__lSGL_ConfigProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_Generator6"):
                opp_val = getattr(old_value, "lSGL_Generator6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_Generator6"):
                opp_val = getattr(value, "lSGL_Generator6", None)
                if opp_val is None:
                    setattr(value, "lSGL_Generator6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lSGL_Config:

    def __init__(self, name: str, lSGL_Config: "lSGL_Generator" = None, lSGL_Config10: set["lSGL_ConfigProperty"] = None, lSGL_Config34: "lSGL_GeneratorAnnotation" = None):
        self.name = name
        self.lSGL_Config = lSGL_Config
        self.lSGL_Config10 = lSGL_Config10 if lSGL_Config10 is not None else set()
        self.lSGL_Config34 = lSGL_Config34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lSGL_Config10(self):
        return self.__lSGL_Config10

    @lSGL_Config10.setter
    def lSGL_Config10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Config__lSGL_Config10", None)
        self.__lSGL_Config10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lSGL_ConfigProperty11"):
                    opp_val = getattr(item, "lSGL_ConfigProperty11", None)
                    
                    if opp_val == self:
                        setattr(item, "lSGL_ConfigProperty11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lSGL_ConfigProperty11"):
                    opp_val = getattr(item, "lSGL_ConfigProperty11", None)
                    
                    setattr(item, "lSGL_ConfigProperty11", self)
                    

    @property
    def lSGL_Config(self):
        return self.__lSGL_Config

    @lSGL_Config.setter
    def lSGL_Config(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Config__lSGL_Config", None)
        self.__lSGL_Config = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_Generator8"):
                opp_val = getattr(old_value, "lSGL_Generator8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_Generator8"):
                opp_val = getattr(value, "lSGL_Generator8", None)
                if opp_val is None:
                    setattr(value, "lSGL_Generator8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lSGL_Config34(self):
        return self.__lSGL_Config34

    @lSGL_Config34.setter
    def lSGL_Config34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Config__lSGL_Config34", None)
        self.__lSGL_Config34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_GeneratorAnnotation33"):
                opp_val = getattr(old_value, "lSGL_GeneratorAnnotation33", None)
                if opp_val == self:
                    setattr(old_value, "lSGL_GeneratorAnnotation33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_GeneratorAnnotation33"):
                opp_val = getattr(value, "lSGL_GeneratorAnnotation33", None)
                setattr(value, "lSGL_GeneratorAnnotation33", self)

class lSGL_Model:

    pass
class lSGL_Projection:

    def __init__(self, excluding: bool, name: str, lSGL_Projection: "lSGL_Model" = None, lSGL_Projection38: set["lSGL_GeneratorAnnotation"] = None, lSGL_Projection41: "lSGL_Entity" = None, lSGL_Projection44: set["lSGL_Attribute"] = None):
        self.excluding = excluding
        self.name = name
        self.lSGL_Projection = lSGL_Projection
        self.lSGL_Projection38 = lSGL_Projection38 if lSGL_Projection38 is not None else set()
        self.lSGL_Projection41 = lSGL_Projection41
        self.lSGL_Projection44 = lSGL_Projection44 if lSGL_Projection44 is not None else set()
        
    @property
    def excluding(self) -> bool:
        return self.__excluding

    @excluding.setter
    def excluding(self, excluding: bool):
        self.__excluding = excluding

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lSGL_Projection41(self):
        return self.__lSGL_Projection41

    @lSGL_Projection41.setter
    def lSGL_Projection41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Projection__lSGL_Projection41", None)
        self.__lSGL_Projection41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_Entity42"):
                opp_val = getattr(old_value, "lSGL_Entity42", None)
                if opp_val == self:
                    setattr(old_value, "lSGL_Entity42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_Entity42"):
                opp_val = getattr(value, "lSGL_Entity42", None)
                setattr(value, "lSGL_Entity42", self)

    @property
    def lSGL_Projection38(self):
        return self.__lSGL_Projection38

    @lSGL_Projection38.setter
    def lSGL_Projection38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Projection__lSGL_Projection38", None)
        self.__lSGL_Projection38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lSGL_GeneratorAnnotation39"):
                    opp_val = getattr(item, "lSGL_GeneratorAnnotation39", None)
                    
                    if opp_val == self:
                        setattr(item, "lSGL_GeneratorAnnotation39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lSGL_GeneratorAnnotation39"):
                    opp_val = getattr(item, "lSGL_GeneratorAnnotation39", None)
                    
                    setattr(item, "lSGL_GeneratorAnnotation39", self)
                    

    @property
    def lSGL_Projection44(self):
        return self.__lSGL_Projection44

    @lSGL_Projection44.setter
    def lSGL_Projection44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Projection__lSGL_Projection44", None)
        self.__lSGL_Projection44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lSGL_Attribute45"):
                    opp_val = getattr(item, "lSGL_Attribute45", None)
                    
                    if opp_val == self:
                        setattr(item, "lSGL_Attribute45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lSGL_Attribute45"):
                    opp_val = getattr(item, "lSGL_Attribute45", None)
                    
                    setattr(item, "lSGL_Attribute45", self)
                    

    @property
    def lSGL_Projection(self):
        return self.__lSGL_Projection

    @lSGL_Projection.setter
    def lSGL_Projection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Projection__lSGL_Projection", None)
        self.__lSGL_Projection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_Model4"):
                opp_val = getattr(old_value, "lSGL_Model4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_Model4"):
                opp_val = getattr(value, "lSGL_Model4", None)
                if opp_val is None:
                    setattr(value, "lSGL_Model4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lSGL_Type:

    def __init__(self, name: str, lSGL_Type: "lSGL_Model" = None, lSGL_Type20: "lSGL_AttributeType" = None):
        self.name = name
        self.lSGL_Type = lSGL_Type
        self.lSGL_Type20 = lSGL_Type20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lSGL_Type(self):
        return self.__lSGL_Type

    @lSGL_Type.setter
    def lSGL_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Type__lSGL_Type", None)
        self.__lSGL_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_Model2"):
                opp_val = getattr(old_value, "lSGL_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_Model2"):
                opp_val = getattr(value, "lSGL_Model2", None)
                if opp_val is None:
                    setattr(value, "lSGL_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lSGL_Type20(self):
        return self.__lSGL_Type20

    @lSGL_Type20.setter
    def lSGL_Type20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Type__lSGL_Type20", None)
        self.__lSGL_Type20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_AttributeType"):
                opp_val = getattr(old_value, "lSGL_AttributeType", None)
                if opp_val == self:
                    setattr(old_value, "lSGL_AttributeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_AttributeType"):
                opp_val = getattr(value, "lSGL_AttributeType", None)
                setattr(value, "lSGL_AttributeType", self)

class lSGL_Generator:

    def __init__(self, name: str, lSGL_Generator: "lSGL_Model" = None, lSGL_Generator8: set["lSGL_Config"] = None, lSGL_Generator6: set["lSGL_ConfigProperty"] = None, lSGL_Generator31: "lSGL_GeneratorAnnotation" = None):
        self.name = name
        self.lSGL_Generator = lSGL_Generator
        self.lSGL_Generator8 = lSGL_Generator8 if lSGL_Generator8 is not None else set()
        self.lSGL_Generator6 = lSGL_Generator6 if lSGL_Generator6 is not None else set()
        self.lSGL_Generator31 = lSGL_Generator31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lSGL_Generator31(self):
        return self.__lSGL_Generator31

    @lSGL_Generator31.setter
    def lSGL_Generator31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Generator__lSGL_Generator31", None)
        self.__lSGL_Generator31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_GeneratorAnnotation30"):
                opp_val = getattr(old_value, "lSGL_GeneratorAnnotation30", None)
                if opp_val == self:
                    setattr(old_value, "lSGL_GeneratorAnnotation30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_GeneratorAnnotation30"):
                opp_val = getattr(value, "lSGL_GeneratorAnnotation30", None)
                setattr(value, "lSGL_GeneratorAnnotation30", self)

    @property
    def lSGL_Generator8(self):
        return self.__lSGL_Generator8

    @lSGL_Generator8.setter
    def lSGL_Generator8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Generator__lSGL_Generator8", None)
        self.__lSGL_Generator8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lSGL_Config"):
                    opp_val = getattr(item, "lSGL_Config", None)
                    
                    if opp_val == self:
                        setattr(item, "lSGL_Config", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lSGL_Config"):
                    opp_val = getattr(item, "lSGL_Config", None)
                    
                    setattr(item, "lSGL_Config", self)
                    

    @property
    def lSGL_Generator(self):
        return self.__lSGL_Generator

    @lSGL_Generator.setter
    def lSGL_Generator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Generator__lSGL_Generator", None)
        self.__lSGL_Generator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lSGL_Model"):
                opp_val = getattr(old_value, "lSGL_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lSGL_Model"):
                opp_val = getattr(value, "lSGL_Model", None)
                if opp_val is None:
                    setattr(value, "lSGL_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lSGL_Generator6(self):
        return self.__lSGL_Generator6

    @lSGL_Generator6.setter
    def lSGL_Generator6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lSGL_Generator__lSGL_Generator6", None)
        self.__lSGL_Generator6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lSGL_ConfigProperty"):
                    opp_val = getattr(item, "lSGL_ConfigProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "lSGL_ConfigProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lSGL_ConfigProperty"):
                    opp_val = getattr(item, "lSGL_ConfigProperty", None)
                    
                    setattr(item, "lSGL_ConfigProperty", self)
                    
