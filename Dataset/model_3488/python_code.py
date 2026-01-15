from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AttributeValue:

    pass
class fc_IntegerValue(AttributeValue):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class fc_BooleanValue(AttributeValue):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class fc_Attribute:

    pass
class fc_StringValue(AttributeValue):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class fc_DoubleValue(AttributeValue):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class fc_Feature:

    pass
class fc_AttributeValue(ABC):

    def __init__(self, comment: str, id: str, name: str, description: str, AttributeValue: "fc_Selection" = None, values: "fc_Selection" = None, fc_AttributeValue: "fc_Attribute" = None):
        self.comment = comment
        self.id = id
        self.name = name
        self.description = description
        self.AttributeValue = AttributeValue
        self.values = values
        self.fc_AttributeValue = fc_AttributeValue
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_AttributeValue__values", None)
        self.__values = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Selection18"):
                opp_val = getattr(old_value, "Selection18", None)
                if opp_val == self:
                    setattr(old_value, "Selection18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Selection18"):
                opp_val = getattr(value, "Selection18", None)
                setattr(value, "Selection18", self)

    @property
    def AttributeValue(self):
        return self.__AttributeValue

    @AttributeValue.setter
    def AttributeValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_AttributeValue__AttributeValue", None)
        self.__AttributeValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selection"):
                opp_val = getattr(old_value, "selection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selection"):
                opp_val = getattr(value, "selection", None)
                if opp_val is None:
                    setattr(value, "selection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fc_AttributeValue(self):
        return self.__fc_AttributeValue

    @fc_AttributeValue.setter
    def fc_AttributeValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_AttributeValue__fc_AttributeValue", None)
        self.__fc_AttributeValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fc_Attribute"):
                opp_val = getattr(old_value, "fc_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "fc_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fc_Attribute"):
                opp_val = getattr(value, "fc_Attribute", None)
                setattr(value, "fc_Attribute", self)

class fc_Selection:

    def __init__(self, description: str, comment: str, id: str, name: str, root: bool, present: bool, enabled: bool, fc_Selection: "fc_FeatureConfiguration" = None, Selection11: "fc_Selection" = None, parent: set["fc_Selection"] = None, Selection: "fc_Selection" = None, selections: "fc_Selection" = None, selection: set["fc_AttributeValue"] = None, Selection18: "fc_AttributeValue" = None, fc_Selection13: "fc_FeatureConfiguration" = None, fc_Selection16: "fc_Feature" = None):
        self.description = description
        self.comment = comment
        self.id = id
        self.name = name
        self.root = root
        self.present = present
        self.enabled = enabled
        self.fc_Selection = fc_Selection
        self.Selection11 = Selection11
        self.parent = parent if parent is not None else set()
        self.Selection = Selection
        self.selections = selections
        self.selection = selection if selection is not None else set()
        self.Selection18 = Selection18
        self.fc_Selection13 = fc_Selection13
        self.fc_Selection16 = fc_Selection16
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def present(self) -> bool:
        return self.__present

    @present.setter
    def present(self, present: bool):
        self.__present = present

    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

    @property
    def root(self) -> bool:
        return self.__root

    @root.setter
    def root(self, root: bool):
        self.__root = root

    @property
    def fc_Selection16(self):
        return self.__fc_Selection16

    @fc_Selection16.setter
    def fc_Selection16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_Selection__fc_Selection16", None)
        self.__fc_Selection16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fc_Feature"):
                opp_val = getattr(old_value, "fc_Feature", None)
                if opp_val == self:
                    setattr(old_value, "fc_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fc_Feature"):
                opp_val = getattr(value, "fc_Feature", None)
                setattr(value, "fc_Feature", self)

    @property
    def Selection(self):
        return self.__Selection

    @Selection.setter
    def Selection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_Selection__Selection", None)
        self.__Selection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selections"):
                opp_val = getattr(old_value, "selections", None)
                if opp_val == self:
                    setattr(old_value, "selections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selections"):
                opp_val = getattr(value, "selections", None)
                setattr(value, "selections", self)

    @property
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_Selection__selection", None)
        self.__selection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributeValue"):
                    opp_val = getattr(item, "AttributeValue", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeValue"):
                    opp_val = getattr(item, "AttributeValue", None)
                    
                    setattr(item, "AttributeValue", self)
                    

    @property
    def Selection11(self):
        return self.__Selection11

    @Selection11.setter
    def Selection11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_Selection__Selection11", None)
        self.__Selection11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def selections(self):
        return self.__selections

    @selections.setter
    def selections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_Selection__selections", None)
        self.__selections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Selection"):
                opp_val = getattr(old_value, "Selection", None)
                if opp_val == self:
                    setattr(old_value, "Selection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Selection"):
                opp_val = getattr(value, "Selection", None)
                setattr(value, "Selection", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_Selection__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Selection11"):
                    opp_val = getattr(item, "Selection11", None)
                    
                    if opp_val == self:
                        setattr(item, "Selection11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Selection11"):
                    opp_val = getattr(item, "Selection11", None)
                    
                    setattr(item, "Selection11", self)
                    

    @property
    def Selection18(self):
        return self.__Selection18

    @Selection18.setter
    def Selection18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_Selection__Selection18", None)
        self.__Selection18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "values"):
                opp_val = getattr(old_value, "values", None)
                if opp_val == self:
                    setattr(old_value, "values", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "values"):
                opp_val = getattr(value, "values", None)
                setattr(value, "values", self)

    @property
    def fc_Selection13(self):
        return self.__fc_Selection13

    @fc_Selection13.setter
    def fc_Selection13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_Selection__fc_Selection13", None)
        self.__fc_Selection13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fc_FeatureConfiguration14"):
                opp_val = getattr(old_value, "fc_FeatureConfiguration14", None)
                if opp_val == self:
                    setattr(old_value, "fc_FeatureConfiguration14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fc_FeatureConfiguration14"):
                opp_val = getattr(value, "fc_FeatureConfiguration14", None)
                setattr(value, "fc_FeatureConfiguration14", self)

    @property
    def fc_Selection(self):
        return self.__fc_Selection

    @fc_Selection.setter
    def fc_Selection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_Selection__fc_Selection", None)
        self.__fc_Selection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fc_FeatureConfiguration5"):
                opp_val = getattr(old_value, "fc_FeatureConfiguration5", None)
                if opp_val == self:
                    setattr(old_value, "fc_FeatureConfiguration5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fc_FeatureConfiguration5"):
                opp_val = getattr(value, "fc_FeatureConfiguration5", None)
                setattr(value, "fc_FeatureConfiguration5", self)

class fc_FeatureConfiguration:

    def __init__(self, comment: str, name: str, version: str, description: str, fc_FeatureConfiguration: "fc_FeatureModel" = None, fc_FeatureConfiguration2: "fc_FeatureModel" = None, fc_FeatureConfiguration5: "fc_Selection" = None, fc_FeatureConfiguration14: "fc_Selection" = None):
        self.comment = comment
        self.name = name
        self.version = version
        self.description = description
        self.fc_FeatureConfiguration = fc_FeatureConfiguration
        self.fc_FeatureConfiguration2 = fc_FeatureConfiguration2
        self.fc_FeatureConfiguration5 = fc_FeatureConfiguration5
        self.fc_FeatureConfiguration14 = fc_FeatureConfiguration14
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fc_FeatureConfiguration14(self):
        return self.__fc_FeatureConfiguration14

    @fc_FeatureConfiguration14.setter
    def fc_FeatureConfiguration14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_FeatureConfiguration__fc_FeatureConfiguration14", None)
        self.__fc_FeatureConfiguration14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fc_Selection13"):
                opp_val = getattr(old_value, "fc_Selection13", None)
                if opp_val == self:
                    setattr(old_value, "fc_Selection13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fc_Selection13"):
                opp_val = getattr(value, "fc_Selection13", None)
                setattr(value, "fc_Selection13", self)

    @property
    def fc_FeatureConfiguration2(self):
        return self.__fc_FeatureConfiguration2

    @fc_FeatureConfiguration2.setter
    def fc_FeatureConfiguration2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_FeatureConfiguration__fc_FeatureConfiguration2", None)
        self.__fc_FeatureConfiguration2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fc_FeatureModel3"):
                opp_val = getattr(old_value, "fc_FeatureModel3", None)
                if opp_val == self:
                    setattr(old_value, "fc_FeatureModel3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fc_FeatureModel3"):
                opp_val = getattr(value, "fc_FeatureModel3", None)
                setattr(value, "fc_FeatureModel3", self)

    @property
    def fc_FeatureConfiguration(self):
        return self.__fc_FeatureConfiguration

    @fc_FeatureConfiguration.setter
    def fc_FeatureConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_FeatureConfiguration__fc_FeatureConfiguration", None)
        self.__fc_FeatureConfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fc_FeatureModel"):
                opp_val = getattr(old_value, "fc_FeatureModel", None)
                if opp_val == self:
                    setattr(old_value, "fc_FeatureModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fc_FeatureModel"):
                opp_val = getattr(value, "fc_FeatureModel", None)
                setattr(value, "fc_FeatureModel", self)

    @property
    def fc_FeatureConfiguration5(self):
        return self.__fc_FeatureConfiguration5

    @fc_FeatureConfiguration5.setter
    def fc_FeatureConfiguration5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fc_FeatureConfiguration__fc_FeatureConfiguration5", None)
        self.__fc_FeatureConfiguration5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fc_Selection"):
                opp_val = getattr(old_value, "fc_Selection", None)
                if opp_val == self:
                    setattr(old_value, "fc_Selection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fc_Selection"):
                opp_val = getattr(value, "fc_Selection", None)
                setattr(value, "fc_Selection", self)

    def getSelectionsById(self, id: str):
        # TODO: Implement getSelectionsById method
        pass

class fc_FeatureModel:

    pass