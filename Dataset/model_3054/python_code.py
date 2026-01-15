from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class entityDsl_ComboBoxItem:

    def __init__(self, text: str, entityDsl_ComboBoxItem: "entityDsl_ComboBox" = None):
        self.text = text
        self.entityDsl_ComboBoxItem = entityDsl_ComboBoxItem
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def entityDsl_ComboBoxItem(self):
        return self.__entityDsl_ComboBoxItem

    @entityDsl_ComboBoxItem.setter
    def entityDsl_ComboBoxItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_ComboBoxItem__entityDsl_ComboBoxItem", None)
        self.__entityDsl_ComboBoxItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_ComboBox"):
                opp_val = getattr(old_value, "entityDsl_ComboBox", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_ComboBox"):
                opp_val = getattr(value, "entityDsl_ComboBox", None)
                if opp_val is None:
                    setattr(value, "entityDsl_ComboBox", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class entityDsl_RadioButton:

    def __init__(self, text: str, entityDsl_RadioButton: "entityDsl_RadioButtonGroup" = None):
        self.text = text
        self.entityDsl_RadioButton = entityDsl_RadioButton
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def entityDsl_RadioButton(self):
        return self.__entityDsl_RadioButton

    @entityDsl_RadioButton.setter
    def entityDsl_RadioButton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_RadioButton__entityDsl_RadioButton", None)
        self.__entityDsl_RadioButton = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_RadioButtonGroup"):
                opp_val = getattr(old_value, "entityDsl_RadioButtonGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_RadioButtonGroup"):
                opp_val = getattr(value, "entityDsl_RadioButtonGroup", None)
                if opp_val is None:
                    setattr(value, "entityDsl_RadioButtonGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class WinFormControlType:

    pass
class entityDsl_ComboBox(WinFormControlType):

    pass
class entityDsl_Spinner(WinFormControlType):

    def __init__(self, defaultValue: int, minimumValue: int, maximumValue: int):
        self.defaultValue = defaultValue
        self.minimumValue = minimumValue
        self.maximumValue = maximumValue
        
    @property
    def defaultValue(self) -> int:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: int):
        self.__defaultValue = defaultValue

    @property
    def minimumValue(self) -> int:
        return self.__minimumValue

    @minimumValue.setter
    def minimumValue(self, minimumValue: int):
        self.__minimumValue = minimumValue

    @property
    def maximumValue(self) -> int:
        return self.__maximumValue

    @maximumValue.setter
    def maximumValue(self, maximumValue: int):
        self.__maximumValue = maximumValue

class entityDsl_CheckBox(WinFormControlType):

    pass
class entityDsl_RadioButtonGroup(WinFormControlType):

    pass
class entityDsl_TrackBar(WinFormControlType):

    def __init__(self, increment: int, denominator: int, minimumValue: int, maximumValue: int, stringValues: str, defaultTick: int, entityDsl_TrackBar: "entityDsl_DataType" = None):
        self.increment = increment
        self.denominator = denominator
        self.minimumValue = minimumValue
        self.maximumValue = maximumValue
        self.stringValues = stringValues
        self.defaultTick = defaultTick
        self.entityDsl_TrackBar = entityDsl_TrackBar
        
    @property
    def increment(self) -> int:
        return self.__increment

    @increment.setter
    def increment(self, increment: int):
        self.__increment = increment

    @property
    def denominator(self) -> int:
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator: int):
        self.__denominator = denominator

    @property
    def maximumValue(self) -> int:
        return self.__maximumValue

    @maximumValue.setter
    def maximumValue(self, maximumValue: int):
        self.__maximumValue = maximumValue

    @property
    def defaultTick(self) -> int:
        return self.__defaultTick

    @defaultTick.setter
    def defaultTick(self, defaultTick: int):
        self.__defaultTick = defaultTick

    @property
    def stringValues(self) -> str:
        return self.__stringValues

    @stringValues.setter
    def stringValues(self, stringValues: str):
        self.__stringValues = stringValues

    @property
    def minimumValue(self) -> int:
        return self.__minimumValue

    @minimumValue.setter
    def minimumValue(self, minimumValue: int):
        self.__minimumValue = minimumValue

    @property
    def entityDsl_TrackBar(self):
        return self.__entityDsl_TrackBar

    @entityDsl_TrackBar.setter
    def entityDsl_TrackBar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_TrackBar__entityDsl_TrackBar", None)
        self.__entityDsl_TrackBar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_DataType"):
                opp_val = getattr(old_value, "entityDsl_DataType", None)
                if opp_val == self:
                    setattr(old_value, "entityDsl_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_DataType"):
                opp_val = getattr(value, "entityDsl_DataType", None)
                setattr(value, "entityDsl_DataType", self)

class entityDsl_TextBox:

    def __init__(self, minTextLength: int, maxTextLength: int, name: str, entityDsl_TextBox: "entityDsl_WinFormControlType" = None, entityDsl_TextBox15: "entityDsl_DataType" = None):
        self.minTextLength = minTextLength
        self.maxTextLength = maxTextLength
        self.name = name
        self.entityDsl_TextBox = entityDsl_TextBox
        self.entityDsl_TextBox15 = entityDsl_TextBox15
        
    @property
    def maxTextLength(self) -> int:
        return self.__maxTextLength

    @maxTextLength.setter
    def maxTextLength(self, maxTextLength: int):
        self.__maxTextLength = maxTextLength

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def minTextLength(self) -> int:
        return self.__minTextLength

    @minTextLength.setter
    def minTextLength(self, minTextLength: int):
        self.__minTextLength = minTextLength

    @property
    def entityDsl_TextBox(self):
        return self.__entityDsl_TextBox

    @entityDsl_TextBox.setter
    def entityDsl_TextBox(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_TextBox__entityDsl_TextBox", None)
        self.__entityDsl_TextBox = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_WinFormControlType8"):
                opp_val = getattr(old_value, "entityDsl_WinFormControlType8", None)
                if opp_val == self:
                    setattr(old_value, "entityDsl_WinFormControlType8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_WinFormControlType8"):
                opp_val = getattr(value, "entityDsl_WinFormControlType8", None)
                setattr(value, "entityDsl_WinFormControlType8", self)

    @property
    def entityDsl_TextBox15(self):
        return self.__entityDsl_TextBox15

    @entityDsl_TextBox15.setter
    def entityDsl_TextBox15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_TextBox__entityDsl_TextBox15", None)
        self.__entityDsl_TextBox15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_DataType16"):
                opp_val = getattr(old_value, "entityDsl_DataType16", None)
                if opp_val == self:
                    setattr(old_value, "entityDsl_DataType16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_DataType16"):
                opp_val = getattr(value, "entityDsl_DataType16", None)
                setattr(value, "entityDsl_DataType16", self)

class entityDsl_DataType:

    def __init__(self, type: str, entityDsl_DataType: "entityDsl_TrackBar" = None, entityDsl_DataType13: "entityDsl_RadioButtonGroup" = None, entityDsl_DataType16: "entityDsl_TextBox" = None, entityDsl_DataType20: "entityDsl_ComboBox" = None):
        self.type = type
        self.entityDsl_DataType = entityDsl_DataType
        self.entityDsl_DataType13 = entityDsl_DataType13
        self.entityDsl_DataType16 = entityDsl_DataType16
        self.entityDsl_DataType20 = entityDsl_DataType20
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def entityDsl_DataType20(self):
        return self.__entityDsl_DataType20

    @entityDsl_DataType20.setter
    def entityDsl_DataType20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_DataType__entityDsl_DataType20", None)
        self.__entityDsl_DataType20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_ComboBox19"):
                opp_val = getattr(old_value, "entityDsl_ComboBox19", None)
                if opp_val == self:
                    setattr(old_value, "entityDsl_ComboBox19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_ComboBox19"):
                opp_val = getattr(value, "entityDsl_ComboBox19", None)
                setattr(value, "entityDsl_ComboBox19", self)

    @property
    def entityDsl_DataType13(self):
        return self.__entityDsl_DataType13

    @entityDsl_DataType13.setter
    def entityDsl_DataType13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_DataType__entityDsl_DataType13", None)
        self.__entityDsl_DataType13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_RadioButtonGroup12"):
                opp_val = getattr(old_value, "entityDsl_RadioButtonGroup12", None)
                if opp_val == self:
                    setattr(old_value, "entityDsl_RadioButtonGroup12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_RadioButtonGroup12"):
                opp_val = getattr(value, "entityDsl_RadioButtonGroup12", None)
                setattr(value, "entityDsl_RadioButtonGroup12", self)

    @property
    def entityDsl_DataType16(self):
        return self.__entityDsl_DataType16

    @entityDsl_DataType16.setter
    def entityDsl_DataType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_DataType__entityDsl_DataType16", None)
        self.__entityDsl_DataType16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_TextBox15"):
                opp_val = getattr(old_value, "entityDsl_TextBox15", None)
                if opp_val == self:
                    setattr(old_value, "entityDsl_TextBox15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_TextBox15"):
                opp_val = getattr(value, "entityDsl_TextBox15", None)
                setattr(value, "entityDsl_TextBox15", self)

    @property
    def entityDsl_DataType(self):
        return self.__entityDsl_DataType

    @entityDsl_DataType.setter
    def entityDsl_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_DataType__entityDsl_DataType", None)
        self.__entityDsl_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_TrackBar"):
                opp_val = getattr(old_value, "entityDsl_TrackBar", None)
                if opp_val == self:
                    setattr(old_value, "entityDsl_TrackBar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_TrackBar"):
                opp_val = getattr(value, "entityDsl_TrackBar", None)
                setattr(value, "entityDsl_TrackBar", self)

class entityDsl_Label:

    def __init__(self, text: str, entityDsl_Label: "entityDsl_Attribute" = None):
        self.text = text
        self.entityDsl_Label = entityDsl_Label
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def entityDsl_Label(self):
        return self.__entityDsl_Label

    @entityDsl_Label.setter
    def entityDsl_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_Label__entityDsl_Label", None)
        self.__entityDsl_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_Attribute6"):
                opp_val = getattr(old_value, "entityDsl_Attribute6", None)
                if opp_val == self:
                    setattr(old_value, "entityDsl_Attribute6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_Attribute6"):
                opp_val = getattr(value, "entityDsl_Attribute6", None)
                setattr(value, "entityDsl_Attribute6", self)

class entityDsl_WinFormControlType:

    def __init__(self, name: str, entityDsl_WinFormControlType: "entityDsl_Attribute" = None, entityDsl_WinFormControlType8: "entityDsl_TextBox" = None):
        self.name = name
        self.entityDsl_WinFormControlType = entityDsl_WinFormControlType
        self.entityDsl_WinFormControlType8 = entityDsl_WinFormControlType8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entityDsl_WinFormControlType(self):
        return self.__entityDsl_WinFormControlType

    @entityDsl_WinFormControlType.setter
    def entityDsl_WinFormControlType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_WinFormControlType__entityDsl_WinFormControlType", None)
        self.__entityDsl_WinFormControlType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_Attribute4"):
                opp_val = getattr(old_value, "entityDsl_Attribute4", None)
                if opp_val == self:
                    setattr(old_value, "entityDsl_Attribute4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_Attribute4"):
                opp_val = getattr(value, "entityDsl_Attribute4", None)
                setattr(value, "entityDsl_Attribute4", self)

    @property
    def entityDsl_WinFormControlType8(self):
        return self.__entityDsl_WinFormControlType8

    @entityDsl_WinFormControlType8.setter
    def entityDsl_WinFormControlType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_WinFormControlType__entityDsl_WinFormControlType8", None)
        self.__entityDsl_WinFormControlType8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_TextBox"):
                opp_val = getattr(old_value, "entityDsl_TextBox", None)
                if opp_val == self:
                    setattr(old_value, "entityDsl_TextBox", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_TextBox"):
                opp_val = getattr(value, "entityDsl_TextBox", None)
                setattr(value, "entityDsl_TextBox", self)

class entityDsl_Attribute:

    def __init__(self, required: str, name: str, entityDsl_Attribute: "entityDsl_Entity" = None, entityDsl_Attribute4: "entityDsl_WinFormControlType" = None, entityDsl_Attribute6: "entityDsl_Label" = None):
        self.required = required
        self.name = name
        self.entityDsl_Attribute = entityDsl_Attribute
        self.entityDsl_Attribute4 = entityDsl_Attribute4
        self.entityDsl_Attribute6 = entityDsl_Attribute6
        
    @property
    def required(self) -> str:
        return self.__required

    @required.setter
    def required(self, required: str):
        self.__required = required

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entityDsl_Attribute(self):
        return self.__entityDsl_Attribute

    @entityDsl_Attribute.setter
    def entityDsl_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_Attribute__entityDsl_Attribute", None)
        self.__entityDsl_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_Entity2"):
                opp_val = getattr(old_value, "entityDsl_Entity2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_Entity2"):
                opp_val = getattr(value, "entityDsl_Entity2", None)
                if opp_val is None:
                    setattr(value, "entityDsl_Entity2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entityDsl_Attribute6(self):
        return self.__entityDsl_Attribute6

    @entityDsl_Attribute6.setter
    def entityDsl_Attribute6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_Attribute__entityDsl_Attribute6", None)
        self.__entityDsl_Attribute6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_Label"):
                opp_val = getattr(old_value, "entityDsl_Label", None)
                if opp_val == self:
                    setattr(old_value, "entityDsl_Label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_Label"):
                opp_val = getattr(value, "entityDsl_Label", None)
                setattr(value, "entityDsl_Label", self)

    @property
    def entityDsl_Attribute4(self):
        return self.__entityDsl_Attribute4

    @entityDsl_Attribute4.setter
    def entityDsl_Attribute4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_Attribute__entityDsl_Attribute4", None)
        self.__entityDsl_Attribute4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_WinFormControlType"):
                opp_val = getattr(old_value, "entityDsl_WinFormControlType", None)
                if opp_val == self:
                    setattr(old_value, "entityDsl_WinFormControlType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_WinFormControlType"):
                opp_val = getattr(value, "entityDsl_WinFormControlType", None)
                setattr(value, "entityDsl_WinFormControlType", self)

class entityDsl_Entity:

    def __init__(self, name: str, entityDsl_Entity: "entityDsl_Domainmodel" = None, entityDsl_Entity2: set["entityDsl_Attribute"] = None):
        self.name = name
        self.entityDsl_Entity = entityDsl_Entity
        self.entityDsl_Entity2 = entityDsl_Entity2 if entityDsl_Entity2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def entityDsl_Entity(self):
        return self.__entityDsl_Entity

    @entityDsl_Entity.setter
    def entityDsl_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_Entity__entityDsl_Entity", None)
        self.__entityDsl_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entityDsl_Domainmodel"):
                opp_val = getattr(old_value, "entityDsl_Domainmodel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entityDsl_Domainmodel"):
                opp_val = getattr(value, "entityDsl_Domainmodel", None)
                if opp_val is None:
                    setattr(value, "entityDsl_Domainmodel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entityDsl_Entity2(self):
        return self.__entityDsl_Entity2

    @entityDsl_Entity2.setter
    def entityDsl_Entity2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_Entity__entityDsl_Entity2", None)
        self.__entityDsl_Entity2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entityDsl_Attribute"):
                    opp_val = getattr(item, "entityDsl_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "entityDsl_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entityDsl_Attribute"):
                    opp_val = getattr(item, "entityDsl_Attribute", None)
                    
                    setattr(item, "entityDsl_Attribute", self)
                    

class entityDsl_Domainmodel:

    def __init__(self, applicationName: str, entityDsl_Domainmodel: set["entityDsl_Entity"] = None):
        self.applicationName = applicationName
        self.entityDsl_Domainmodel = entityDsl_Domainmodel if entityDsl_Domainmodel is not None else set()
        
    @property
    def applicationName(self) -> str:
        return self.__applicationName

    @applicationName.setter
    def applicationName(self, applicationName: str):
        self.__applicationName = applicationName

    @property
    def entityDsl_Domainmodel(self):
        return self.__entityDsl_Domainmodel

    @entityDsl_Domainmodel.setter
    def entityDsl_Domainmodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_entityDsl_Domainmodel__entityDsl_Domainmodel", None)
        self.__entityDsl_Domainmodel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entityDsl_Entity"):
                    opp_val = getattr(item, "entityDsl_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "entityDsl_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entityDsl_Entity"):
                    opp_val = getattr(item, "entityDsl_Entity", None)
                    
                    setattr(item, "entityDsl_Entity", self)
                    
