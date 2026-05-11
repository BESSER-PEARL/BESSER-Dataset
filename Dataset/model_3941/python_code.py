from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class UmlMM_Parameter:

    def __init__(self, name: str, parameter: "UmlMM_Operation" = None, Parameter: "UmlMM_Operation" = None, UmlMM_Parameter: "UmlMM_Classifier" = None):
        self.name = name
        self.parameter = parameter
        self.Parameter = Parameter
        self.UmlMM_Parameter = UmlMM_Parameter
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def UmlMM_Parameter(self):
        return self.__UmlMM_Parameter

    @UmlMM_Parameter.setter
    def UmlMM_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_Parameter__UmlMM_Parameter", None)
        self.__UmlMM_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UmlMM_Classifier"):
                opp_val = getattr(old_value, "UmlMM_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "UmlMM_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UmlMM_Classifier"):
                opp_val = getattr(value, "UmlMM_Classifier", None)
                setattr(value, "UmlMM_Classifier", self)

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_Parameter__parameter", None)
        self.__parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation9"):
                opp_val = getattr(old_value, "Operation9", None)
                if opp_val == self:
                    setattr(old_value, "Operation9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation9"):
                opp_val = getattr(value, "Operation9", None)
                setattr(value, "Operation9", self)

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_Operation"):
                opp_val = getattr(old_value, "_Operation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_Operation"):
                opp_val = getattr(value, "_Operation", None)
                if opp_val is None:
                    setattr(value, "_Operation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UmlMM_Property:

    def __init__(self, upper: int, lower: int, name: str, UmlMM_Property: "UmlMM_Classifier" = None, _property: "UmlMM_Class" = None, Property: "UmlMM_Class" = None):
        self.upper = upper
        self.lower = lower
        self.name = name
        self.UmlMM_Property = UmlMM_Property
        self._property = _property
        self.Property = Property
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower


    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_Property__Property", None)
        self.__Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_Class4"):
                opp_val = getattr(old_value, "_Class4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_Class4"):
                opp_val = getattr(value, "_Class4", None)
                if opp_val is None:
                    setattr(value, "_Class4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UmlMM_Property(self):
        return self.__UmlMM_Property

    @UmlMM_Property.setter
    def UmlMM_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_Property__UmlMM_Property", None)
        self.__UmlMM_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UmlMM_Classifier11"):
                opp_val = getattr(old_value, "UmlMM_Classifier11", None)
                if opp_val == self:
                    setattr(old_value, "UmlMM_Classifier11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UmlMM_Classifier11"):
                opp_val = getattr(value, "UmlMM_Classifier11", None)
                setattr(value, "UmlMM_Classifier11", self)

    @property
    def _property(self):
        return self.___property

    @_property.setter
    def _property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_Property___property", None)
        self.___property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class13"):
                opp_val = getattr(old_value, "Class13", None)
                if opp_val == self:
                    setattr(old_value, "Class13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class13"):
                opp_val = getattr(value, "Class13", None)
                setattr(value, "Class13", self)

class UmlMM_Operation:

    def __init__(self, name: str, Operation9: "UmlMM_Parameter" = None, Operation: "UmlMM_Class" = None, operation: "UmlMM_Class" = None, _Operation: set["UmlMM_Parameter"] = None):
        self.name = name
        self.Operation9 = Operation9
        self.Operation = Operation
        self.operation = operation
        self._Operation = _Operation if _Operation is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Operation(self):
        return self.__Operation

    @Operation.setter
    def Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_Operation__Operation", None)
        self.__Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_Class"):
                opp_val = getattr(old_value, "_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_Class"):
                opp_val = getattr(value, "_Class", None)
                if opp_val is None:
                    setattr(value, "_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def _Operation(self):
        return self.___Operation

    @_Operation.setter
    def _Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_Operation___Operation", None)
        self.___Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    @property
    def Operation9(self):
        return self.__Operation9

    @Operation9.setter
    def Operation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_Operation__Operation9", None)
        self.__Operation9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter"):
                opp_val = getattr(old_value, "parameter", None)
                if opp_val == self:
                    setattr(old_value, "parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter"):
                opp_val = getattr(value, "parameter", None)
                setattr(value, "parameter", self)

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_Operation__operation", None)
        self.__operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

class UmlMM_Classifier:

    pass
class UmlMM_UmlPackage:

    def __init__(self, name: str, _UmlPackage: set["UmlMM_Classifier"] = None, UmlPackage: "UmlMM_Classifier" = None):
        self.name = name
        self._UmlPackage = _UmlPackage if _UmlPackage is not None else set()
        self.UmlPackage = UmlPackage
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def UmlPackage(self):
        return self.__UmlPackage

    @UmlPackage.setter
    def UmlPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_UmlPackage__UmlPackage", None)
        self.__UmlPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elements"):
                opp_val = getattr(old_value, "elements", None)
                if opp_val == self:
                    setattr(old_value, "elements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elements"):
                opp_val = getattr(value, "elements", None)
                setattr(value, "elements", self)

    @property
    def _UmlPackage(self):
        return self.___UmlPackage

    @_UmlPackage.setter
    def _UmlPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_UmlPackage___UmlPackage", None)
        self.___UmlPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier"):
                    opp_val = getattr(item, "Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier"):
                    opp_val = getattr(item, "Classifier", None)
                    
                    setattr(item, "Classifier", self)
                    

class Classifier:

    pass
class UmlMM_Class(Classifier):

    def __init__(self, name: str, Class13: "UmlMM_Property" = None, _Class: set["UmlMM_Operation"] = None, _Class4: set["UmlMM_Property"] = None, Class: "UmlMM_Operation" = None):
        self.name = name
        self.Class13 = Class13
        self._Class = _Class if _Class is not None else set()
        self._Class4 = _Class4 if _Class4 is not None else set()
        self.Class = Class
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def _Class(self):
        return self.___Class

    @_Class.setter
    def _Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_Class___Class", None)
        self.___Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operation"):
                opp_val = getattr(old_value, "operation", None)
                if opp_val == self:
                    setattr(old_value, "operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operation"):
                opp_val = getattr(value, "operation", None)
                setattr(value, "operation", self)

    @property
    def Class13(self):
        return self.__Class13

    @Class13.setter
    def Class13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_Class__Class13", None)
        self.__Class13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_property"):
                opp_val = getattr(old_value, "_property", None)
                if opp_val == self:
                    setattr(old_value, "_property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_property"):
                opp_val = getattr(value, "_property", None)
                setattr(value, "_property", self)

    @property
    def _Class4(self):
        return self.___Class4

    @_Class4.setter
    def _Class4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UmlMM_Class___Class4", None)
        self.___Class4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

class UmlMM_DataType(Classifier):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

