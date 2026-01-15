from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FormMethodType(Enum):
    get = "get"
    post = "post"
class OrientationType(Enum):
    right = "right"
    left = "left"
class ContentStyle(Enum):
    hierarchical = "hierarchical"
    normal = "normal"
class ConditionalTemplateExpType(Enum):
    isNotEmpty = "isNotEmpty"
class ConditionType(Enum):
    equal = "equal"
    implies = "implies"
    dateLessEqual = "dateLessEqual"


############################################
# Definition of Classes
############################################

class Form:

    pass
class becontent_ExtendedForm(Form):

    def __init__(self, className: str):
        self.className = className
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

class NotStructuredElement:

    pass
class becontent_Year(NotStructuredElement):

    def __init__(self, name: str, label: str, start: int, end: int, isMandatory: bool):
        self.name = name
        self.label = label
        self.start = start
        self.end = end
        self.isMandatory = isMandatory
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def start(self) -> int:
        return self.__start

    @start.setter
    def start(self, start: int):
        self.__start = start

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def end(self) -> int:
        return self.__end

    @end.setter
    def end(self, end: int):
        self.__end = end

    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

class becontent_Date(NotStructuredElement):

    def __init__(self, name: str, label: str, isMandatory: bool):
        self.name = name
        self.label = label
        self.isMandatory = isMandatory
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

class becontent_RelationManager(NotStructuredElement):

    def __init__(self, name: str, label: str, orientation: str, restrictCondition: str):
        self.name = name
        self.label = label
        self.orientation = orientation
        self.restrictCondition = restrictCondition
        
    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def restrictCondition(self) -> str:
        return self.__restrictCondition

    @restrictCondition.setter
    def restrictCondition(self, restrictCondition: str):
        self.__restrictCondition = restrictCondition

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class becontent_Color(NotStructuredElement):

    def __init__(self, name: str, label: str, defaultColor: str):
        self.name = name
        self.label = label
        self.defaultColor = defaultColor
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def defaultColor(self) -> str:
        return self.__defaultColor

    @defaultColor.setter
    def defaultColor(self, defaultColor: str):
        self.__defaultColor = defaultColor

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class becontent_RadioButton(NotStructuredElement):

    def __init__(self, name: str, label: str, values: str):
        self.name = name
        self.label = label
        self.values = values
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class becontent_HierarchicalPosition(NotStructuredElement):

    def __init__(self, referenceField: str, size: int, name: str, label: str, controlledField: str):
        self.referenceField = referenceField
        self.size = size
        self.name = name
        self.label = label
        self.controlledField = controlledField
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def controlledField(self) -> str:
        return self.__controlledField

    @controlledField.setter
    def controlledField(self, controlledField: str):
        self.__controlledField = controlledField

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def referenceField(self) -> str:
        return self.__referenceField

    @referenceField.setter
    def referenceField(self, referenceField: str):
        self.__referenceField = referenceField

class becontent_File(NotStructuredElement):

    def __init__(self, isMandatory: bool, extension: str, extensionMessage: str, name: str, label: str):
        self.isMandatory = isMandatory
        self.extension = extension
        self.extensionMessage = extensionMessage
        self.name = name
        self.label = label
        
    @property
    def extensionMessage(self) -> str:
        return self.__extensionMessage

    @extensionMessage.setter
    def extensionMessage(self, extensionMessage: str):
        self.__extensionMessage = extensionMessage

    @property
    def extension(self) -> str:
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension

    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class becontent_Position(NotStructuredElement):

    def __init__(self, name: str, label: str, controlledField: str, size: int, isMandatory: bool):
        self.name = name
        self.label = label
        self.controlledField = controlledField
        self.size = size
        self.isMandatory = isMandatory
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def controlledField(self) -> str:
        return self.__controlledField

    @controlledField.setter
    def controlledField(self, controlledField: str):
        self.__controlledField = controlledField

class becontent_Password(NotStructuredElement):

    def __init__(self, name: str, label: str, size: int, isMandatory: bool, maxLength: int):
        self.name = name
        self.label = label
        self.size = size
        self.isMandatory = isMandatory
        self.maxLength = maxLength
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def maxLength(self) -> int:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: int):
        self.__maxLength = maxLength

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class becontent_FileToFolder(NotStructuredElement):

    def __init__(self, name: str, label: str, isMandatory: bool, extension: str, extensionMessage: str):
        self.name = name
        self.label = label
        self.isMandatory = isMandatory
        self.extension = extension
        self.extensionMessage = extensionMessage
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def extension(self) -> str:
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extensionMessage(self) -> str:
        return self.__extensionMessage

    @extensionMessage.setter
    def extensionMessage(self, extensionMessage: str):
        self.__extensionMessage = extensionMessage

class becontent_Select(NotStructuredElement):

    def __init__(self, name: str, label: str, values: str, isMandatory: bool):
        self.name = name
        self.label = label
        self.values = values
        self.isMandatory = isMandatory
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class becontent_Link(NotStructuredElement):

    def __init__(self, name: str, label: str, size: int, isMandatory: bool, maxLength: int):
        self.name = name
        self.label = label
        self.size = size
        self.isMandatory = isMandatory
        self.maxLength = maxLength
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def maxLength(self) -> int:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: int):
        self.__maxLength = maxLength

class becontent_Textarea(NotStructuredElement):

    def __init__(self, name: str, label: str, rows: int, columns: int, isMandatory: bool):
        self.name = name
        self.label = label
        self.rows = rows
        self.columns = columns
        self.isMandatory = isMandatory
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def columns(self) -> int:
        return self.__columns

    @columns.setter
    def columns(self, columns: int):
        self.__columns = columns

    @property
    def rows(self) -> int:
        return self.__rows

    @rows.setter
    def rows(self, rows: int):
        self.__rows = rows

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class becontent_Text(NotStructuredElement):

    def __init__(self, name: str, label: str, size: int, isMandatory: bool, maxLength: int):
        self.name = name
        self.label = label
        self.size = size
        self.isMandatory = isMandatory
        self.maxLength = maxLength
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def maxLength(self) -> int:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: int):
        self.__maxLength = maxLength

class becontent_LongDate(NotStructuredElement):

    def __init__(self, name: str, label: str, isMandatory: bool):
        self.name = name
        self.label = label
        self.isMandatory = isMandatory
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class becontent_Editor(NotStructuredElement):

    def __init__(self, isMandatory: bool, name: str, label: str, rows: int, columns: int):
        self.isMandatory = isMandatory
        self.name = name
        self.label = label
        self.rows = rows
        self.columns = columns
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def columns(self) -> int:
        return self.__columns

    @columns.setter
    def columns(self, columns: int):
        self.__columns = columns

    @property
    def rows(self) -> int:
        return self.__rows

    @rows.setter
    def rows(self, rows: int):
        self.__rows = rows

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class becontent_SelectFromReference(NotStructuredElement):

    def __init__(self, name: str, label: str, isMandatory: bool, restrictCondition: str, becontent_SelectFromReference: "becontent_Entity" = None):
        self.name = name
        self.label = label
        self.isMandatory = isMandatory
        self.restrictCondition = restrictCondition
        self.becontent_SelectFromReference = becontent_SelectFromReference
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def restrictCondition(self) -> str:
        return self.__restrictCondition

    @restrictCondition.setter
    def restrictCondition(self, restrictCondition: str):
        self.__restrictCondition = restrictCondition

    @property
    def becontent_SelectFromReference(self):
        return self.__becontent_SelectFromReference

    @becontent_SelectFromReference.setter
    def becontent_SelectFromReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_SelectFromReference__becontent_SelectFromReference", None)
        self.__becontent_SelectFromReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Entity71"):
                opp_val = getattr(old_value, "becontent_Entity71", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Entity71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Entity71"):
                opp_val = getattr(value, "becontent_Entity71", None)
                setattr(value, "becontent_Entity71", self)

class becontent_Hidden(NotStructuredElement):

    def __init__(self, name: str, values: str):
        self.name = name
        self.values = values
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class becontent_Checkbox(NotStructuredElement):

    def __init__(self, name: str, label: str, value: str, isChecked: bool):
        self.name = name
        self.label = label
        self.value = value
        self.isChecked = isChecked
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isChecked(self) -> bool:
        return self.__isChecked

    @isChecked.setter
    def isChecked(self, isChecked: bool):
        self.__isChecked = isChecked

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class becontent_Image(NotStructuredElement):

    def __init__(self, name: str, label: str, isMandatory: bool):
        self.name = name
        self.label = label
        self.isMandatory = isMandatory
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class becontent_RadioFromReference(NotStructuredElement):

    def __init__(self, name: str, label: str, isMandatory: bool, restrictCondition: str, becontent_RadioFromReference: "becontent_Entity" = None):
        self.name = name
        self.label = label
        self.isMandatory = isMandatory
        self.restrictCondition = restrictCondition
        self.becontent_RadioFromReference = becontent_RadioFromReference
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def restrictCondition(self) -> str:
        return self.__restrictCondition

    @restrictCondition.setter
    def restrictCondition(self, restrictCondition: str):
        self.__restrictCondition = restrictCondition

    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def becontent_RadioFromReference(self):
        return self.__becontent_RadioFromReference

    @becontent_RadioFromReference.setter
    def becontent_RadioFromReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_RadioFromReference__becontent_RadioFromReference", None)
        self.__becontent_RadioFromReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Entity73"):
                opp_val = getattr(old_value, "becontent_Entity73", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Entity73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Entity73"):
                opp_val = getattr(value, "becontent_Entity73", None)
                setattr(value, "becontent_Entity73", self)

class becontent_Section(NotStructuredElement):

    def __init__(self, name: str, text: str):
        self.name = name
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ApplyCommand:

    pass
class becontent_ApplyIndexed(ApplyCommand):

    pass
class becontent_ApplyItem(ApplyCommand):

    def __init__(self, key: str, prefix: str):
        self.key = key
        self.prefix = prefix
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

class becontent_Apply(ApplyCommand):

    def __init__(self, prefix: str):
        self.prefix = prefix
        
    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

class FormElement:

    pass
class becontent_Form(FormElement):

    def __init__(self, name: str, method: str, description: str, becontent_Form: "becontent_EntityManagerPage" = None, becontent_Form56: "becontent_DefinitionItem" = None, becontent_Form58: set["becontent_FormElement"] = None, becontent_Form60: "becontent_CustomPager" = None, becontent_Form63: set["becontent_Validation"] = None):
        self.name = name
        self.method = method
        self.description = description
        self.becontent_Form = becontent_Form
        self.becontent_Form56 = becontent_Form56
        self.becontent_Form58 = becontent_Form58 if becontent_Form58 is not None else set()
        self.becontent_Form60 = becontent_Form60
        self.becontent_Form63 = becontent_Form63 if becontent_Form63 is not None else set()
        
    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def becontent_Form58(self):
        return self.__becontent_Form58

    @becontent_Form58.setter
    def becontent_Form58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Form__becontent_Form58", None)
        self.__becontent_Form58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "becontent_FormElement"):
                    opp_val = getattr(item, "becontent_FormElement", None)
                    
                    if opp_val == self:
                        setattr(item, "becontent_FormElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "becontent_FormElement"):
                    opp_val = getattr(item, "becontent_FormElement", None)
                    
                    setattr(item, "becontent_FormElement", self)
                    

    @property
    def becontent_Form(self):
        return self.__becontent_Form

    @becontent_Form.setter
    def becontent_Form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Form__becontent_Form", None)
        self.__becontent_Form = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_EntityManagerPage"):
                opp_val = getattr(old_value, "becontent_EntityManagerPage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_EntityManagerPage"):
                opp_val = getattr(value, "becontent_EntityManagerPage", None)
                if opp_val is None:
                    setattr(value, "becontent_EntityManagerPage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def becontent_Form63(self):
        return self.__becontent_Form63

    @becontent_Form63.setter
    def becontent_Form63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Form__becontent_Form63", None)
        self.__becontent_Form63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "becontent_Validation64"):
                    opp_val = getattr(item, "becontent_Validation64", None)
                    
                    if opp_val == self:
                        setattr(item, "becontent_Validation64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "becontent_Validation64"):
                    opp_val = getattr(item, "becontent_Validation64", None)
                    
                    setattr(item, "becontent_Validation64", self)
                    

    @property
    def becontent_Form56(self):
        return self.__becontent_Form56

    @becontent_Form56.setter
    def becontent_Form56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Form__becontent_Form56", None)
        self.__becontent_Form56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_DefinitionItem"):
                opp_val = getattr(old_value, "becontent_DefinitionItem", None)
                if opp_val == self:
                    setattr(old_value, "becontent_DefinitionItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_DefinitionItem"):
                opp_val = getattr(value, "becontent_DefinitionItem", None)
                setattr(value, "becontent_DefinitionItem", self)

    @property
    def becontent_Form60(self):
        return self.__becontent_Form60

    @becontent_Form60.setter
    def becontent_Form60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Form__becontent_Form60", None)
        self.__becontent_Form60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_CustomPager61"):
                opp_val = getattr(old_value, "becontent_CustomPager61", None)
                if opp_val == self:
                    setattr(old_value, "becontent_CustomPager61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_CustomPager61"):
                opp_val = getattr(value, "becontent_CustomPager61", None)
                setattr(value, "becontent_CustomPager61", self)

class becontent_NotStructuredElement(FormElement):

    def __init__(self, helper: str, becontent_NotStructuredElement: "becontent_Validation" = None, becontent_NotStructuredElement69: "becontent_Validation" = None):
        self.helper = helper
        self.becontent_NotStructuredElement = becontent_NotStructuredElement
        self.becontent_NotStructuredElement69 = becontent_NotStructuredElement69
        
    @property
    def helper(self) -> str:
        return self.__helper

    @helper.setter
    def helper(self, helper: str):
        self.__helper = helper

    @property
    def becontent_NotStructuredElement69(self):
        return self.__becontent_NotStructuredElement69

    @becontent_NotStructuredElement69.setter
    def becontent_NotStructuredElement69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_NotStructuredElement__becontent_NotStructuredElement69", None)
        self.__becontent_NotStructuredElement69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Validation68"):
                opp_val = getattr(old_value, "becontent_Validation68", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Validation68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Validation68"):
                opp_val = getattr(value, "becontent_Validation68", None)
                setattr(value, "becontent_Validation68", self)

    @property
    def becontent_NotStructuredElement(self):
        return self.__becontent_NotStructuredElement

    @becontent_NotStructuredElement.setter
    def becontent_NotStructuredElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_NotStructuredElement__becontent_NotStructuredElement", None)
        self.__becontent_NotStructuredElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Validation66"):
                opp_val = getattr(old_value, "becontent_Validation66", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Validation66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Validation66"):
                opp_val = getattr(value, "becontent_Validation66", None)
                setattr(value, "becontent_Validation66", self)

class becontent_FormElement(ABC):

    pass
class becontent_Validation:

    def __init__(self, condition: str, message: str, _id_model: str, becontent_Validation: "becontent_EntityManagerPage" = None, becontent_Validation66: "becontent_NotStructuredElement" = None, becontent_Validation68: "becontent_NotStructuredElement" = None, becontent_Validation64: "becontent_Form" = None):
        self.condition = condition
        self.message = message
        self._id_model = _id_model
        self.becontent_Validation = becontent_Validation
        self.becontent_Validation66 = becontent_Validation66
        self.becontent_Validation68 = becontent_Validation68
        self.becontent_Validation64 = becontent_Validation64
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def _id_model(self) -> str:
        return self.___id_model

    @_id_model.setter
    def _id_model(self, _id_model: str):
        self.___id_model = _id_model

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def becontent_Validation64(self):
        return self.__becontent_Validation64

    @becontent_Validation64.setter
    def becontent_Validation64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Validation__becontent_Validation64", None)
        self.__becontent_Validation64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Form63"):
                opp_val = getattr(old_value, "becontent_Form63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Form63"):
                opp_val = getattr(value, "becontent_Form63", None)
                if opp_val is None:
                    setattr(value, "becontent_Form63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def becontent_Validation(self):
        return self.__becontent_Validation

    @becontent_Validation.setter
    def becontent_Validation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Validation__becontent_Validation", None)
        self.__becontent_Validation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_EntityManagerPage54"):
                opp_val = getattr(old_value, "becontent_EntityManagerPage54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_EntityManagerPage54"):
                opp_val = getattr(value, "becontent_EntityManagerPage54", None)
                if opp_val is None:
                    setattr(value, "becontent_EntityManagerPage54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def becontent_Validation66(self):
        return self.__becontent_Validation66

    @becontent_Validation66.setter
    def becontent_Validation66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Validation__becontent_Validation66", None)
        self.__becontent_Validation66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_NotStructuredElement"):
                opp_val = getattr(old_value, "becontent_NotStructuredElement", None)
                if opp_val == self:
                    setattr(old_value, "becontent_NotStructuredElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_NotStructuredElement"):
                opp_val = getattr(value, "becontent_NotStructuredElement", None)
                setattr(value, "becontent_NotStructuredElement", self)

    @property
    def becontent_Validation68(self):
        return self.__becontent_Validation68

    @becontent_Validation68.setter
    def becontent_Validation68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Validation__becontent_Validation68", None)
        self.__becontent_Validation68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_NotStructuredElement69"):
                opp_val = getattr(old_value, "becontent_NotStructuredElement69", None)
                if opp_val == self:
                    setattr(old_value, "becontent_NotStructuredElement69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_NotStructuredElement69"):
                opp_val = getattr(value, "becontent_NotStructuredElement69", None)
                setattr(value, "becontent_NotStructuredElement69", self)

class becontent_CustomPager:

    def __init__(self, _id_model: str, className: str, length: int, template: str, query: str, filter: str, order: str, becontent_CustomPager: "becontent_EntityManagerPage" = None, becontent_CustomPager61: "becontent_Form" = None):
        self._id_model = _id_model
        self.className = className
        self.length = length
        self.template = template
        self.query = query
        self.filter = filter
        self.order = order
        self.becontent_CustomPager = becontent_CustomPager
        self.becontent_CustomPager61 = becontent_CustomPager61
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def template(self) -> str:
        return self.__template

    @template.setter
    def template(self, template: str):
        self.__template = template

    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def query(self) -> str:
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query

    @property
    def _id_model(self) -> str:
        return self.___id_model

    @_id_model.setter
    def _id_model(self, _id_model: str):
        self.___id_model = _id_model

    @property
    def order(self) -> str:
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def becontent_CustomPager61(self):
        return self.__becontent_CustomPager61

    @becontent_CustomPager61.setter
    def becontent_CustomPager61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_CustomPager__becontent_CustomPager61", None)
        self.__becontent_CustomPager61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Form60"):
                opp_val = getattr(old_value, "becontent_Form60", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Form60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Form60"):
                opp_val = getattr(value, "becontent_Form60", None)
                setattr(value, "becontent_Form60", self)

    @property
    def becontent_CustomPager(self):
        return self.__becontent_CustomPager

    @becontent_CustomPager.setter
    def becontent_CustomPager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_CustomPager__becontent_CustomPager", None)
        self.__becontent_CustomPager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_EntityManagerPage52"):
                opp_val = getattr(old_value, "becontent_EntityManagerPage52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_EntityManagerPage52"):
                opp_val = getattr(value, "becontent_EntityManagerPage52", None)
                if opp_val is None:
                    setattr(value, "becontent_EntityManagerPage52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class becontent_ConditionalTemplate:

    def __init__(self, _id_model: str, trueTemplate: str, falseTemplate: str, conditionExp: str, fieldName: str, becontent_ConditionalTemplate: "becontent_Content" = None):
        self._id_model = _id_model
        self.trueTemplate = trueTemplate
        self.falseTemplate = falseTemplate
        self.conditionExp = conditionExp
        self.fieldName = fieldName
        self.becontent_ConditionalTemplate = becontent_ConditionalTemplate
        
    @property
    def conditionExp(self) -> str:
        return self.__conditionExp

    @conditionExp.setter
    def conditionExp(self, conditionExp: str):
        self.__conditionExp = conditionExp

    @property
    def falseTemplate(self) -> str:
        return self.__falseTemplate

    @falseTemplate.setter
    def falseTemplate(self, falseTemplate: str):
        self.__falseTemplate = falseTemplate

    @property
    def _id_model(self) -> str:
        return self.___id_model

    @_id_model.setter
    def _id_model(self, _id_model: str):
        self.___id_model = _id_model

    @property
    def fieldName(self) -> str:
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName

    @property
    def trueTemplate(self) -> str:
        return self.__trueTemplate

    @trueTemplate.setter
    def trueTemplate(self, trueTemplate: str):
        self.__trueTemplate = trueTemplate

    @property
    def becontent_ConditionalTemplate(self):
        return self.__becontent_ConditionalTemplate

    @becontent_ConditionalTemplate.setter
    def becontent_ConditionalTemplate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_ConditionalTemplate__becontent_ConditionalTemplate", None)
        self.__becontent_ConditionalTemplate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Content41"):
                opp_val = getattr(old_value, "becontent_Content41", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Content41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Content41"):
                opp_val = getattr(value, "becontent_Content41", None)
                setattr(value, "becontent_Content41", self)

class becontent_ContentCommand(ABC):

    def __init__(self, _id_model: str, becontent_ContentCommand: "becontent_Content" = None):
        self._id_model = _id_model
        self.becontent_ContentCommand = becontent_ContentCommand
        
    @property
    def _id_model(self) -> str:
        return self.___id_model

    @_id_model.setter
    def _id_model(self, _id_model: str):
        self.___id_model = _id_model

    @property
    def becontent_ContentCommand(self):
        return self.__becontent_ContentCommand

    @becontent_ContentCommand.setter
    def becontent_ContentCommand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_ContentCommand__becontent_ContentCommand", None)
        self.__becontent_ContentCommand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Content39"):
                opp_val = getattr(old_value, "becontent_Content39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Content39"):
                opp_val = getattr(value, "becontent_Content39", None)
                if opp_val is None:
                    setattr(value, "becontent_Content39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ContentCommand:

    pass
class becontent_Trigger(ContentCommand):

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
        
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

class becontent_Copy(ContentCommand):

    def __init__(self, fieldName1: str, fieldName2: str):
        self.fieldName1 = fieldName1
        self.fieldName2 = fieldName2
        
    @property
    def fieldName1(self) -> str:
        return self.__fieldName1

    @fieldName1.setter
    def fieldName1(self, fieldName1: str):
        self.__fieldName1 = fieldName1

    @property
    def fieldName2(self) -> str:
        return self.__fieldName2

    @fieldName2.setter
    def fieldName2(self, fieldName2: str):
        self.__fieldName2 = fieldName2

class becontent_ApplyCommand(ContentCommand):

    pass
class becontent_Propagate(ContentCommand):

    def __init__(self, fieldName1: str, fieldName2: str):
        self.fieldName1 = fieldName1
        self.fieldName2 = fieldName2
        
    @property
    def fieldName1(self) -> str:
        return self.__fieldName1

    @fieldName1.setter
    def fieldName1(self, fieldName1: str):
        self.__fieldName1 = fieldName1

    @property
    def fieldName2(self) -> str:
        return self.__fieldName2

    @fieldName2.setter
    def fieldName2(self, fieldName2: str):
        self.__fieldName2 = fieldName2

class becontent_UnsetParameter(ContentCommand):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class becontent_Parameter(ContentCommand):

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
        
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

class becontent_ViewItem(ABC):

    pass
class becontent_JoinEntity:

    def __init__(self, _id_model: str, becontent_JoinEntity: "becontent_Content" = None, becontent_JoinEntity44: "becontent_JoinEntity" = None, becontent_JoinEntity42: "becontent_JoinEntity" = None, becontent_JoinEntity46: "becontent_Entity" = None):
        self._id_model = _id_model
        self.becontent_JoinEntity = becontent_JoinEntity
        self.becontent_JoinEntity44 = becontent_JoinEntity44
        self.becontent_JoinEntity42 = becontent_JoinEntity42
        self.becontent_JoinEntity46 = becontent_JoinEntity46
        
    @property
    def _id_model(self) -> str:
        return self.___id_model

    @_id_model.setter
    def _id_model(self, _id_model: str):
        self.___id_model = _id_model

    @property
    def becontent_JoinEntity42(self):
        return self.__becontent_JoinEntity42

    @becontent_JoinEntity42.setter
    def becontent_JoinEntity42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_JoinEntity__becontent_JoinEntity42", None)
        self.__becontent_JoinEntity42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_JoinEntity44"):
                opp_val = getattr(old_value, "becontent_JoinEntity44", None)
                if opp_val == self:
                    setattr(old_value, "becontent_JoinEntity44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_JoinEntity44"):
                opp_val = getattr(value, "becontent_JoinEntity44", None)
                setattr(value, "becontent_JoinEntity44", self)

    @property
    def becontent_JoinEntity46(self):
        return self.__becontent_JoinEntity46

    @becontent_JoinEntity46.setter
    def becontent_JoinEntity46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_JoinEntity__becontent_JoinEntity46", None)
        self.__becontent_JoinEntity46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Entity47"):
                opp_val = getattr(old_value, "becontent_Entity47", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Entity47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Entity47"):
                opp_val = getattr(value, "becontent_Entity47", None)
                setattr(value, "becontent_Entity47", self)

    @property
    def becontent_JoinEntity44(self):
        return self.__becontent_JoinEntity44

    @becontent_JoinEntity44.setter
    def becontent_JoinEntity44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_JoinEntity__becontent_JoinEntity44", None)
        self.__becontent_JoinEntity44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_JoinEntity42"):
                opp_val = getattr(old_value, "becontent_JoinEntity42", None)
                if opp_val == self:
                    setattr(old_value, "becontent_JoinEntity42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_JoinEntity42"):
                opp_val = getattr(value, "becontent_JoinEntity42", None)
                setattr(value, "becontent_JoinEntity42", self)

    @property
    def becontent_JoinEntity(self):
        return self.__becontent_JoinEntity

    @becontent_JoinEntity.setter
    def becontent_JoinEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_JoinEntity__becontent_JoinEntity", None)
        self.__becontent_JoinEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Content37"):
                opp_val = getattr(old_value, "becontent_Content37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Content37"):
                opp_val = getattr(value, "becontent_Content37", None)
                if opp_val is None:
                    setattr(value, "becontent_Content37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ViewItem:

    pass
class becontent_Content(ViewItem):

    def __init__(self, template: str, presentationFields: str, orderFields: str, joinCondition: str, filter: str, limit: int, style: str, _id_model: str, becontent_Content: "becontent_Entity" = None, becontent_Content37: set["becontent_JoinEntity"] = None, becontent_Content39: set["becontent_ContentCommand"] = None, becontent_Content41: "becontent_ConditionalTemplate" = None):
        self.template = template
        self.presentationFields = presentationFields
        self.orderFields = orderFields
        self.joinCondition = joinCondition
        self.filter = filter
        self.limit = limit
        self.style = style
        self._id_model = _id_model
        self.becontent_Content = becontent_Content
        self.becontent_Content37 = becontent_Content37 if becontent_Content37 is not None else set()
        self.becontent_Content39 = becontent_Content39 if becontent_Content39 is not None else set()
        self.becontent_Content41 = becontent_Content41
        
    @property
    def joinCondition(self) -> str:
        return self.__joinCondition

    @joinCondition.setter
    def joinCondition(self, joinCondition: str):
        self.__joinCondition = joinCondition

    @property
    def presentationFields(self) -> str:
        return self.__presentationFields

    @presentationFields.setter
    def presentationFields(self, presentationFields: str):
        self.__presentationFields = presentationFields

    @property
    def _id_model(self) -> str:
        return self.___id_model

    @_id_model.setter
    def _id_model(self, _id_model: str):
        self.___id_model = _id_model

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def limit(self) -> int:
        return self.__limit

    @limit.setter
    def limit(self, limit: int):
        self.__limit = limit

    @property
    def template(self) -> str:
        return self.__template

    @template.setter
    def template(self, template: str):
        self.__template = template

    @property
    def orderFields(self) -> str:
        return self.__orderFields

    @orderFields.setter
    def orderFields(self, orderFields: str):
        self.__orderFields = orderFields

    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def becontent_Content41(self):
        return self.__becontent_Content41

    @becontent_Content41.setter
    def becontent_Content41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Content__becontent_Content41", None)
        self.__becontent_Content41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_ConditionalTemplate"):
                opp_val = getattr(old_value, "becontent_ConditionalTemplate", None)
                if opp_val == self:
                    setattr(old_value, "becontent_ConditionalTemplate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_ConditionalTemplate"):
                opp_val = getattr(value, "becontent_ConditionalTemplate", None)
                setattr(value, "becontent_ConditionalTemplate", self)

    @property
    def becontent_Content39(self):
        return self.__becontent_Content39

    @becontent_Content39.setter
    def becontent_Content39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Content__becontent_Content39", None)
        self.__becontent_Content39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "becontent_ContentCommand"):
                    opp_val = getattr(item, "becontent_ContentCommand", None)
                    
                    if opp_val == self:
                        setattr(item, "becontent_ContentCommand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "becontent_ContentCommand"):
                    opp_val = getattr(item, "becontent_ContentCommand", None)
                    
                    setattr(item, "becontent_ContentCommand", self)
                    

    @property
    def becontent_Content(self):
        return self.__becontent_Content

    @becontent_Content.setter
    def becontent_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Content__becontent_Content", None)
        self.__becontent_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Entity35"):
                opp_val = getattr(old_value, "becontent_Entity35", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Entity35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Entity35"):
                opp_val = getattr(value, "becontent_Entity35", None)
                setattr(value, "becontent_Entity35", self)

    @property
    def becontent_Content37(self):
        return self.__becontent_Content37

    @becontent_Content37.setter
    def becontent_Content37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Content__becontent_Content37", None)
        self.__becontent_Content37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "becontent_JoinEntity"):
                    opp_val = getattr(item, "becontent_JoinEntity", None)
                    
                    if opp_val == self:
                        setattr(item, "becontent_JoinEntity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "becontent_JoinEntity"):
                    opp_val = getattr(item, "becontent_JoinEntity", None)
                    
                    setattr(item, "becontent_JoinEntity", self)
                    

class becontent_Skinlet(ViewItem):

    def __init__(self, template: str, _id_model: str):
        self.template = template
        self._id_model = _id_model
        
    @property
    def template(self) -> str:
        return self.__template

    @template.setter
    def template(self, template: str):
        self.__template = template

    @property
    def _id_model(self) -> str:
        return self.___id_model

    @_id_model.setter
    def _id_model(self, _id_model: str):
        self.___id_model = _id_model

class becontent_Skin(ViewItem):

    def __init__(self, name: str, becontent_Skin: "becontent_Handler" = None):
        self.name = name
        self.becontent_Skin = becontent_Skin
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def becontent_Skin(self):
        return self.__becontent_Skin

    @becontent_Skin.setter
    def becontent_Skin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Skin__becontent_Skin", None)
        self.__becontent_Skin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Handler30"):
                opp_val = getattr(old_value, "becontent_Handler30", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Handler30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Handler30"):
                opp_val = getattr(value, "becontent_Handler30", None)
                setattr(value, "becontent_Handler30", self)

class becontent_Template(ViewItem):

    def __init__(self, path: str, _id_model: str):
        self.path = path
        self._id_model = _id_model
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def _id_model(self) -> str:
        return self.___id_model

    @_id_model.setter
    def _id_model(self, _id_model: str):
        self.___id_model = _id_model

class TypedSystemAttribute:

    pass
class becontent_SystemAttributePassword(TypedSystemAttribute):

    pass
class becontent_SystemAttributeText(TypedSystemAttribute):

    pass
class becontent_SystemAttributeLongDate(TypedSystemAttribute):

    pass
class becontent_SystemAttributeDate(TypedSystemAttribute):

    pass
class becontent_SystemAttributeColor(TypedSystemAttribute):

    pass
class SystemEntityField:

    pass
class becontent_TypedSystemAttribute(SystemEntityField):

    def __init__(self, name: str, isMandatory: bool):
        self.name = name
        self.isMandatory = isMandatory
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class becontent_SystemReference(SystemEntityField):

    def __init__(self, name: str, becontent_SystemReference: "becontent_SystemEntity" = None):
        self.name = name
        self.becontent_SystemReference = becontent_SystemReference
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def becontent_SystemReference(self):
        return self.__becontent_SystemReference

    @becontent_SystemReference.setter
    def becontent_SystemReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_SystemReference__becontent_SystemReference", None)
        self.__becontent_SystemReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_SystemEntity21"):
                opp_val = getattr(old_value, "becontent_SystemEntity21", None)
                if opp_val == self:
                    setattr(old_value, "becontent_SystemEntity21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_SystemEntity21"):
                opp_val = getattr(value, "becontent_SystemEntity21", None)
                setattr(value, "becontent_SystemEntity21", self)

class becontent_SystemAttributeFileToFolder(TypedSystemAttribute):

    pass
class becontent_SystemAttributeFile(TypedSystemAttribute):

    pass
class becontent_SystemAttributeVarchar(TypedSystemAttribute):

    def __init__(self, length: int, isPrimaryKey: bool):
        self.length = length
        self.isPrimaryKey = isPrimaryKey
        
    @property
    def isPrimaryKey(self) -> bool:
        return self.__isPrimaryKey

    @isPrimaryKey.setter
    def isPrimaryKey(self, isPrimaryKey: bool):
        self.__isPrimaryKey = isPrimaryKey

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

class becontent_SystemAttributeInteger(TypedSystemAttribute):

    def __init__(self, isPrimaryKey: bool):
        self.isPrimaryKey = isPrimaryKey
        
    @property
    def isPrimaryKey(self) -> bool:
        return self.__isPrimaryKey

    @isPrimaryKey.setter
    def isPrimaryKey(self, isPrimaryKey: bool):
        self.__isPrimaryKey = isPrimaryKey

class becontent_SystemAttributeImage(TypedSystemAttribute):

    pass
class becontent_SystemAttributePosition(TypedSystemAttribute):

    pass
class EntityField:

    pass
class becontent_TypedAttribute(EntityField):

    def __init__(self, name: str, isMandatory: bool):
        self.name = name
        self.isMandatory = isMandatory
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

class becontent_Reference(EntityField):

    def __init__(self, name: str, becontent_Reference: "becontent_Entity" = None):
        self.name = name
        self.becontent_Reference = becontent_Reference
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def becontent_Reference(self):
        return self.__becontent_Reference

    @becontent_Reference.setter
    def becontent_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Reference__becontent_Reference", None)
        self.__becontent_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Entity18"):
                opp_val = getattr(old_value, "becontent_Entity18", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Entity18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Entity18"):
                opp_val = getattr(value, "becontent_Entity18", None)
                setattr(value, "becontent_Entity18", self)

class TypedAttribute:

    pass
class becontent_AttributeColor(TypedAttribute):

    pass
class becontent_AttributeImage(TypedAttribute):

    pass
class becontent_AttributeInteger(TypedAttribute):

    def __init__(self, isPrimaryKey: bool):
        self.isPrimaryKey = isPrimaryKey
        
    @property
    def isPrimaryKey(self) -> bool:
        return self.__isPrimaryKey

    @isPrimaryKey.setter
    def isPrimaryKey(self, isPrimaryKey: bool):
        self.__isPrimaryKey = isPrimaryKey

class becontent_AttributePosition(TypedAttribute):

    pass
class becontent_AttributePassword(TypedAttribute):

    pass
class becontent_AttributeDate(TypedAttribute):

    pass
class becontent_AttributeVarchar(TypedAttribute):

    def __init__(self, length: int, isPrimaryKey: bool):
        self.length = length
        self.isPrimaryKey = isPrimaryKey
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def isPrimaryKey(self) -> bool:
        return self.__isPrimaryKey

    @isPrimaryKey.setter
    def isPrimaryKey(self, isPrimaryKey: bool):
        self.__isPrimaryKey = isPrimaryKey

class becontent_AttributeFile(TypedAttribute):

    pass
class becontent_AttributeText(TypedAttribute):

    pass
class becontent_AttributeLongDate(TypedAttribute):

    pass
class becontent_AttributeFileToFolder(TypedAttribute):

    pass
class Entity:

    pass
class becontent_SystemEntity(Entity):

    pass
class becontent_CustomEntity(Entity):

    pass
class becontent_EntityField(ABC):

    def __init__(self, isPresented: bool, isTextSearch: bool, isSearchPresentationHead: bool, isSearchPresentationBody: bool, becontent_EntityField: "becontent_Entity" = None):
        self.isPresented = isPresented
        self.isTextSearch = isTextSearch
        self.isSearchPresentationHead = isSearchPresentationHead
        self.isSearchPresentationBody = isSearchPresentationBody
        self.becontent_EntityField = becontent_EntityField
        
    @property
    def isSearchPresentationHead(self) -> bool:
        return self.__isSearchPresentationHead

    @isSearchPresentationHead.setter
    def isSearchPresentationHead(self, isSearchPresentationHead: bool):
        self.__isSearchPresentationHead = isSearchPresentationHead

    @property
    def isSearchPresentationBody(self) -> bool:
        return self.__isSearchPresentationBody

    @isSearchPresentationBody.setter
    def isSearchPresentationBody(self, isSearchPresentationBody: bool):
        self.__isSearchPresentationBody = isSearchPresentationBody

    @property
    def isTextSearch(self) -> bool:
        return self.__isTextSearch

    @isTextSearch.setter
    def isTextSearch(self, isTextSearch: bool):
        self.__isTextSearch = isTextSearch

    @property
    def isPresented(self) -> bool:
        return self.__isPresented

    @isPresented.setter
    def isPresented(self, isPresented: bool):
        self.__isPresented = isPresented

    @property
    def becontent_EntityField(self):
        return self.__becontent_EntityField

    @becontent_EntityField.setter
    def becontent_EntityField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_EntityField__becontent_EntityField", None)
        self.__becontent_EntityField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Entity"):
                opp_val = getattr(old_value, "becontent_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Entity"):
                opp_val = getattr(value, "becontent_Entity", None)
                if opp_val is None:
                    setattr(value, "becontent_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Relation:

    pass
class becontent_SystemRelation(Relation):

    pass
class becontent_CustomRelation(Relation):

    pass
class becontent_SystemEntityField(ABC):

    def __init__(self, isPresented: bool, isTextSearch: bool, isSearchPresentationHead: bool, isSearchPresentationBody: bool, becontent_SystemEntityField: "becontent_SystemEntity" = None):
        self.isPresented = isPresented
        self.isTextSearch = isTextSearch
        self.isSearchPresentationHead = isSearchPresentationHead
        self.isSearchPresentationBody = isSearchPresentationBody
        self.becontent_SystemEntityField = becontent_SystemEntityField
        
    @property
    def isPresented(self) -> bool:
        return self.__isPresented

    @isPresented.setter
    def isPresented(self, isPresented: bool):
        self.__isPresented = isPresented

    @property
    def isSearchPresentationHead(self) -> bool:
        return self.__isSearchPresentationHead

    @isSearchPresentationHead.setter
    def isSearchPresentationHead(self, isSearchPresentationHead: bool):
        self.__isSearchPresentationHead = isSearchPresentationHead

    @property
    def isSearchPresentationBody(self) -> bool:
        return self.__isSearchPresentationBody

    @isSearchPresentationBody.setter
    def isSearchPresentationBody(self, isSearchPresentationBody: bool):
        self.__isSearchPresentationBody = isSearchPresentationBody

    @property
    def isTextSearch(self) -> bool:
        return self.__isTextSearch

    @isTextSearch.setter
    def isTextSearch(self, isTextSearch: bool):
        self.__isTextSearch = isTextSearch

    @property
    def becontent_SystemEntityField(self):
        return self.__becontent_SystemEntityField

    @becontent_SystemEntityField.setter
    def becontent_SystemEntityField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_SystemEntityField__becontent_SystemEntityField", None)
        self.__becontent_SystemEntityField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_SystemEntity"):
                opp_val = getattr(old_value, "becontent_SystemEntity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_SystemEntity"):
                opp_val = getattr(value, "becontent_SystemEntity", None)
                if opp_val is None:
                    setattr(value, "becontent_SystemEntity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DefinitionItem:

    pass
class becontent_Relation(DefinitionItem):

    def __init__(self, name: str, variableName: str):
        self.name = name
        self.variableName = variableName
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

class becontent_Entity(DefinitionItem):

    def __init__(self, name: str, variableName: str, isOwned: bool, presentationString: str, rssFilter: str, becontent_Entity8: "becontent_CustomRelation" = None, becontent_Entity11: "becontent_CustomRelation" = None, becontent_Entity: set["becontent_EntityField"] = None, becontent_Entity3: "becontent_Channel" = None, becontent_Entity5: "becontent_Handler" = None, becontent_Entity18: "becontent_Reference" = None, becontent_Entity26: "becontent_Channel" = None, becontent_Entity35: "becontent_Content" = None, becontent_Entity47: "becontent_JoinEntity" = None, becontent_Entity71: "becontent_SelectFromReference" = None, becontent_Entity73: "becontent_RadioFromReference" = None):
        self.name = name
        self.variableName = variableName
        self.isOwned = isOwned
        self.presentationString = presentationString
        self.rssFilter = rssFilter
        self.becontent_Entity8 = becontent_Entity8
        self.becontent_Entity11 = becontent_Entity11
        self.becontent_Entity = becontent_Entity if becontent_Entity is not None else set()
        self.becontent_Entity3 = becontent_Entity3
        self.becontent_Entity5 = becontent_Entity5
        self.becontent_Entity18 = becontent_Entity18
        self.becontent_Entity26 = becontent_Entity26
        self.becontent_Entity35 = becontent_Entity35
        self.becontent_Entity47 = becontent_Entity47
        self.becontent_Entity71 = becontent_Entity71
        self.becontent_Entity73 = becontent_Entity73
        
    @property
    def isOwned(self) -> bool:
        return self.__isOwned

    @isOwned.setter
    def isOwned(self, isOwned: bool):
        self.__isOwned = isOwned

    @property
    def rssFilter(self) -> str:
        return self.__rssFilter

    @rssFilter.setter
    def rssFilter(self, rssFilter: str):
        self.__rssFilter = rssFilter

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

    @property
    def presentationString(self) -> str:
        return self.__presentationString

    @presentationString.setter
    def presentationString(self, presentationString: str):
        self.__presentationString = presentationString

    @property
    def becontent_Entity18(self):
        return self.__becontent_Entity18

    @becontent_Entity18.setter
    def becontent_Entity18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Entity__becontent_Entity18", None)
        self.__becontent_Entity18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Reference"):
                opp_val = getattr(old_value, "becontent_Reference", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Reference"):
                opp_val = getattr(value, "becontent_Reference", None)
                setattr(value, "becontent_Reference", self)

    @property
    def becontent_Entity47(self):
        return self.__becontent_Entity47

    @becontent_Entity47.setter
    def becontent_Entity47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Entity__becontent_Entity47", None)
        self.__becontent_Entity47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_JoinEntity46"):
                opp_val = getattr(old_value, "becontent_JoinEntity46", None)
                if opp_val == self:
                    setattr(old_value, "becontent_JoinEntity46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_JoinEntity46"):
                opp_val = getattr(value, "becontent_JoinEntity46", None)
                setattr(value, "becontent_JoinEntity46", self)

    @property
    def becontent_Entity8(self):
        return self.__becontent_Entity8

    @becontent_Entity8.setter
    def becontent_Entity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Entity__becontent_Entity8", None)
        self.__becontent_Entity8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_CustomRelation"):
                opp_val = getattr(old_value, "becontent_CustomRelation", None)
                if opp_val == self:
                    setattr(old_value, "becontent_CustomRelation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_CustomRelation"):
                opp_val = getattr(value, "becontent_CustomRelation", None)
                setattr(value, "becontent_CustomRelation", self)

    @property
    def becontent_Entity71(self):
        return self.__becontent_Entity71

    @becontent_Entity71.setter
    def becontent_Entity71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Entity__becontent_Entity71", None)
        self.__becontent_Entity71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_SelectFromReference"):
                opp_val = getattr(old_value, "becontent_SelectFromReference", None)
                if opp_val == self:
                    setattr(old_value, "becontent_SelectFromReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_SelectFromReference"):
                opp_val = getattr(value, "becontent_SelectFromReference", None)
                setattr(value, "becontent_SelectFromReference", self)

    @property
    def becontent_Entity(self):
        return self.__becontent_Entity

    @becontent_Entity.setter
    def becontent_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Entity__becontent_Entity", None)
        self.__becontent_Entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "becontent_EntityField"):
                    opp_val = getattr(item, "becontent_EntityField", None)
                    
                    if opp_val == self:
                        setattr(item, "becontent_EntityField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "becontent_EntityField"):
                    opp_val = getattr(item, "becontent_EntityField", None)
                    
                    setattr(item, "becontent_EntityField", self)
                    

    @property
    def becontent_Entity26(self):
        return self.__becontent_Entity26

    @becontent_Entity26.setter
    def becontent_Entity26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Entity__becontent_Entity26", None)
        self.__becontent_Entity26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Channel25"):
                opp_val = getattr(old_value, "becontent_Channel25", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Channel25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Channel25"):
                opp_val = getattr(value, "becontent_Channel25", None)
                setattr(value, "becontent_Channel25", self)

    @property
    def becontent_Entity5(self):
        return self.__becontent_Entity5

    @becontent_Entity5.setter
    def becontent_Entity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Entity__becontent_Entity5", None)
        self.__becontent_Entity5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Handler"):
                opp_val = getattr(old_value, "becontent_Handler", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Handler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Handler"):
                opp_val = getattr(value, "becontent_Handler", None)
                setattr(value, "becontent_Handler", self)

    @property
    def becontent_Entity11(self):
        return self.__becontent_Entity11

    @becontent_Entity11.setter
    def becontent_Entity11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Entity__becontent_Entity11", None)
        self.__becontent_Entity11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_CustomRelation10"):
                opp_val = getattr(old_value, "becontent_CustomRelation10", None)
                if opp_val == self:
                    setattr(old_value, "becontent_CustomRelation10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_CustomRelation10"):
                opp_val = getattr(value, "becontent_CustomRelation10", None)
                setattr(value, "becontent_CustomRelation10", self)

    @property
    def becontent_Entity3(self):
        return self.__becontent_Entity3

    @becontent_Entity3.setter
    def becontent_Entity3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Entity__becontent_Entity3", None)
        self.__becontent_Entity3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Channel"):
                opp_val = getattr(old_value, "becontent_Channel", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Channel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Channel"):
                opp_val = getattr(value, "becontent_Channel", None)
                setattr(value, "becontent_Channel", self)

    @property
    def becontent_Entity35(self):
        return self.__becontent_Entity35

    @becontent_Entity35.setter
    def becontent_Entity35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Entity__becontent_Entity35", None)
        self.__becontent_Entity35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Content"):
                opp_val = getattr(old_value, "becontent_Content", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Content", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Content"):
                opp_val = getattr(value, "becontent_Content", None)
                setattr(value, "becontent_Content", self)

    @property
    def becontent_Entity73(self):
        return self.__becontent_Entity73

    @becontent_Entity73.setter
    def becontent_Entity73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Entity__becontent_Entity73", None)
        self.__becontent_Entity73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_RadioFromReference"):
                opp_val = getattr(old_value, "becontent_RadioFromReference", None)
                if opp_val == self:
                    setattr(old_value, "becontent_RadioFromReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_RadioFromReference"):
                opp_val = getattr(value, "becontent_RadioFromReference", None)
                setattr(value, "becontent_RadioFromReference", self)

class BeContentElement:

    pass
class becontent_FileToFolderExtension(BeContentElement):

    def __init__(self, extensionKey: str, extensionValue: str, _id_model: str, becontent_FileToFolderExtension: "becontent_AttributeFileToFolder" = None, becontent_FileToFolderExtension23: "becontent_SystemAttributeFileToFolder" = None):
        self.extensionKey = extensionKey
        self.extensionValue = extensionValue
        self._id_model = _id_model
        self.becontent_FileToFolderExtension = becontent_FileToFolderExtension
        self.becontent_FileToFolderExtension23 = becontent_FileToFolderExtension23
        
    @property
    def extensionKey(self) -> str:
        return self.__extensionKey

    @extensionKey.setter
    def extensionKey(self, extensionKey: str):
        self.__extensionKey = extensionKey

    @property
    def _id_model(self) -> str:
        return self.___id_model

    @_id_model.setter
    def _id_model(self, _id_model: str):
        self.___id_model = _id_model

    @property
    def extensionValue(self) -> str:
        return self.__extensionValue

    @extensionValue.setter
    def extensionValue(self, extensionValue: str):
        self.__extensionValue = extensionValue

    @property
    def becontent_FileToFolderExtension23(self):
        return self.__becontent_FileToFolderExtension23

    @becontent_FileToFolderExtension23.setter
    def becontent_FileToFolderExtension23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_FileToFolderExtension__becontent_FileToFolderExtension23", None)
        self.__becontent_FileToFolderExtension23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_SystemAttributeFileToFolder"):
                opp_val = getattr(old_value, "becontent_SystemAttributeFileToFolder", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_SystemAttributeFileToFolder"):
                opp_val = getattr(value, "becontent_SystemAttributeFileToFolder", None)
                if opp_val is None:
                    setattr(value, "becontent_SystemAttributeFileToFolder", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def becontent_FileToFolderExtension(self):
        return self.__becontent_FileToFolderExtension

    @becontent_FileToFolderExtension.setter
    def becontent_FileToFolderExtension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_FileToFolderExtension__becontent_FileToFolderExtension", None)
        self.__becontent_FileToFolderExtension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_AttributeFileToFolder"):
                opp_val = getattr(old_value, "becontent_AttributeFileToFolder", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_AttributeFileToFolder"):
                opp_val = getattr(value, "becontent_AttributeFileToFolder", None)
                if opp_val is None:
                    setattr(value, "becontent_AttributeFileToFolder", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class becontent_EntityManagerPage(BeContentElement):

    def __init__(self, fileName: str, skin: str, becontent_EntityManagerPage: set["becontent_Form"] = None, becontent_EntityManagerPage52: set["becontent_CustomPager"] = None, becontent_EntityManagerPage54: set["becontent_Validation"] = None):
        self.fileName = fileName
        self.skin = skin
        self.becontent_EntityManagerPage = becontent_EntityManagerPage if becontent_EntityManagerPage is not None else set()
        self.becontent_EntityManagerPage52 = becontent_EntityManagerPage52 if becontent_EntityManagerPage52 is not None else set()
        self.becontent_EntityManagerPage54 = becontent_EntityManagerPage54 if becontent_EntityManagerPage54 is not None else set()
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def skin(self) -> str:
        return self.__skin

    @skin.setter
    def skin(self, skin: str):
        self.__skin = skin

    @property
    def becontent_EntityManagerPage54(self):
        return self.__becontent_EntityManagerPage54

    @becontent_EntityManagerPage54.setter
    def becontent_EntityManagerPage54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_EntityManagerPage__becontent_EntityManagerPage54", None)
        self.__becontent_EntityManagerPage54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "becontent_Validation"):
                    opp_val = getattr(item, "becontent_Validation", None)
                    
                    if opp_val == self:
                        setattr(item, "becontent_Validation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "becontent_Validation"):
                    opp_val = getattr(item, "becontent_Validation", None)
                    
                    setattr(item, "becontent_Validation", self)
                    

    @property
    def becontent_EntityManagerPage52(self):
        return self.__becontent_EntityManagerPage52

    @becontent_EntityManagerPage52.setter
    def becontent_EntityManagerPage52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_EntityManagerPage__becontent_EntityManagerPage52", None)
        self.__becontent_EntityManagerPage52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "becontent_CustomPager"):
                    opp_val = getattr(item, "becontent_CustomPager", None)
                    
                    if opp_val == self:
                        setattr(item, "becontent_CustomPager", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "becontent_CustomPager"):
                    opp_val = getattr(item, "becontent_CustomPager", None)
                    
                    setattr(item, "becontent_CustomPager", self)
                    

    @property
    def becontent_EntityManagerPage(self):
        return self.__becontent_EntityManagerPage

    @becontent_EntityManagerPage.setter
    def becontent_EntityManagerPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_EntityManagerPage__becontent_EntityManagerPage", None)
        self.__becontent_EntityManagerPage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "becontent_Form"):
                    opp_val = getattr(item, "becontent_Form", None)
                    
                    if opp_val == self:
                        setattr(item, "becontent_Form", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "becontent_Form"):
                    opp_val = getattr(item, "becontent_Form", None)
                    
                    setattr(item, "becontent_Form", self)
                    

class becontent_Handler(BeContentElement):

    def __init__(self, fileName: str, mainSkinWithPager: bool, mainSkinPagerLength: int, mainSkinPlaceholder: str, becontent_Handler: "becontent_Entity" = None, becontent_Handler28: set["becontent_ViewItem"] = None, becontent_Handler30: "becontent_Skin" = None, becontent_Handler32: "becontent_ViewItem" = None):
        self.fileName = fileName
        self.mainSkinWithPager = mainSkinWithPager
        self.mainSkinPagerLength = mainSkinPagerLength
        self.mainSkinPlaceholder = mainSkinPlaceholder
        self.becontent_Handler = becontent_Handler
        self.becontent_Handler28 = becontent_Handler28 if becontent_Handler28 is not None else set()
        self.becontent_Handler30 = becontent_Handler30
        self.becontent_Handler32 = becontent_Handler32
        
    @property
    def mainSkinWithPager(self) -> bool:
        return self.__mainSkinWithPager

    @mainSkinWithPager.setter
    def mainSkinWithPager(self, mainSkinWithPager: bool):
        self.__mainSkinWithPager = mainSkinWithPager

    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def mainSkinPagerLength(self) -> int:
        return self.__mainSkinPagerLength

    @mainSkinPagerLength.setter
    def mainSkinPagerLength(self, mainSkinPagerLength: int):
        self.__mainSkinPagerLength = mainSkinPagerLength

    @property
    def mainSkinPlaceholder(self) -> str:
        return self.__mainSkinPlaceholder

    @mainSkinPlaceholder.setter
    def mainSkinPlaceholder(self, mainSkinPlaceholder: str):
        self.__mainSkinPlaceholder = mainSkinPlaceholder

    @property
    def becontent_Handler30(self):
        return self.__becontent_Handler30

    @becontent_Handler30.setter
    def becontent_Handler30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Handler__becontent_Handler30", None)
        self.__becontent_Handler30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Skin"):
                opp_val = getattr(old_value, "becontent_Skin", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Skin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Skin"):
                opp_val = getattr(value, "becontent_Skin", None)
                setattr(value, "becontent_Skin", self)

    @property
    def becontent_Handler32(self):
        return self.__becontent_Handler32

    @becontent_Handler32.setter
    def becontent_Handler32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Handler__becontent_Handler32", None)
        self.__becontent_Handler32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_ViewItem33"):
                opp_val = getattr(old_value, "becontent_ViewItem33", None)
                if opp_val == self:
                    setattr(old_value, "becontent_ViewItem33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_ViewItem33"):
                opp_val = getattr(value, "becontent_ViewItem33", None)
                setattr(value, "becontent_ViewItem33", self)

    @property
    def becontent_Handler28(self):
        return self.__becontent_Handler28

    @becontent_Handler28.setter
    def becontent_Handler28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Handler__becontent_Handler28", None)
        self.__becontent_Handler28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "becontent_ViewItem"):
                    opp_val = getattr(item, "becontent_ViewItem", None)
                    
                    if opp_val == self:
                        setattr(item, "becontent_ViewItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "becontent_ViewItem"):
                    opp_val = getattr(item, "becontent_ViewItem", None)
                    
                    setattr(item, "becontent_ViewItem", self)
                    

    @property
    def becontent_Handler(self):
        return self.__becontent_Handler

    @becontent_Handler.setter
    def becontent_Handler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Handler__becontent_Handler", None)
        self.__becontent_Handler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Entity5"):
                opp_val = getattr(old_value, "becontent_Entity5", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Entity5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Entity5"):
                opp_val = getattr(value, "becontent_Entity5", None)
                setattr(value, "becontent_Entity5", self)

class becontent_Channel(BeContentElement):

    def __init__(self, parameters: str, _id_model: str, becontent_Channel: "becontent_Entity" = None, becontent_Channel25: "becontent_Entity" = None):
        self.parameters = parameters
        self._id_model = _id_model
        self.becontent_Channel = becontent_Channel
        self.becontent_Channel25 = becontent_Channel25
        
    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def _id_model(self) -> str:
        return self.___id_model

    @_id_model.setter
    def _id_model(self, _id_model: str):
        self.___id_model = _id_model

    @property
    def becontent_Channel25(self):
        return self.__becontent_Channel25

    @becontent_Channel25.setter
    def becontent_Channel25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Channel__becontent_Channel25", None)
        self.__becontent_Channel25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Entity26"):
                opp_val = getattr(old_value, "becontent_Entity26", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Entity26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Entity26"):
                opp_val = getattr(value, "becontent_Entity26", None)
                setattr(value, "becontent_Entity26", self)

    @property
    def becontent_Channel(self):
        return self.__becontent_Channel

    @becontent_Channel.setter
    def becontent_Channel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_becontent_Channel__becontent_Channel", None)
        self.__becontent_Channel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "becontent_Entity3"):
                opp_val = getattr(old_value, "becontent_Entity3", None)
                if opp_val == self:
                    setattr(old_value, "becontent_Entity3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "becontent_Entity3"):
                opp_val = getattr(value, "becontent_Entity3", None)
                setattr(value, "becontent_Entity3", self)

class becontent_DefinitionItem(BeContentElement):

    pass
class becontent_BeContentElement(ABC):

    pass
class becontent_BeContentModel:

    pass