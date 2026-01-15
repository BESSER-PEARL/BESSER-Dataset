from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class uml_package_:

    def __init__(self, name: str, oID: str, kind: str, uml_package_: "uml_DocumentRoot" = None, uml_package_61: "uml_packages" = None, uml_package_57: "uml_classifiersAndAssociations" = None):
        self.name = name
        self.oID = oID
        self.kind = kind
        self.uml_package_ = uml_package_
        self.uml_package_61 = uml_package_61
        self.uml_package_57 = uml_package_57
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def oID(self) -> str:
        return self.__oID

    @oID.setter
    def oID(self, oID: str):
        self.__oID = oID

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uml_package_(self):
        return self.__uml_package_

    @uml_package_.setter
    def uml_package_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_package___uml_package_", None)
        self.__uml_package_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_DocumentRoot39"):
                opp_val = getattr(old_value, "uml_DocumentRoot39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_DocumentRoot39"):
                opp_val = getattr(value, "uml_DocumentRoot39", None)
                if opp_val is None:
                    setattr(value, "uml_DocumentRoot39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_package_57(self):
        return self.__uml_package_57

    @uml_package_57.setter
    def uml_package_57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_package___uml_package_57", None)
        self.__uml_package_57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_classifiersAndAssociations58"):
                opp_val = getattr(old_value, "uml_classifiersAndAssociations58", None)
                if opp_val == self:
                    setattr(old_value, "uml_classifiersAndAssociations58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_classifiersAndAssociations58"):
                opp_val = getattr(value, "uml_classifiersAndAssociations58", None)
                setattr(value, "uml_classifiersAndAssociations58", self)

    @property
    def uml_package_61(self):
        return self.__uml_package_61

    @uml_package_61.setter
    def uml_package_61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_package___uml_package_61", None)
        self.__uml_package_61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_packages60"):
                opp_val = getattr(old_value, "uml_packages60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_packages60"):
                opp_val = getattr(value, "uml_packages60", None)
                if opp_val is None:
                    setattr(value, "uml_packages60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_UML:

    pass
class uml_packages:

    def __init__(self, group: str, uml_packages: "uml_DocumentRoot" = None, uml_packages60: set["uml_package_"] = None, uml_packages64: "uml_UML" = None):
        self.group = group
        self.uml_packages = uml_packages
        self.uml_packages60 = uml_packages60 if uml_packages60 is not None else set()
        self.uml_packages64 = uml_packages64
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def uml_packages60(self):
        return self.__uml_packages60

    @uml_packages60.setter
    def uml_packages60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_packages__uml_packages60", None)
        self.__uml_packages60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_package_61"):
                    opp_val = getattr(item, "uml_package_61", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_package_61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_package_61"):
                    opp_val = getattr(item, "uml_package_61", None)
                    
                    setattr(item, "uml_package_61", self)
                    

    @property
    def uml_packages64(self):
        return self.__uml_packages64

    @uml_packages64.setter
    def uml_packages64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_packages__uml_packages64", None)
        self.__uml_packages64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_UML63"):
                opp_val = getattr(old_value, "uml_UML63", None)
                if opp_val == self:
                    setattr(old_value, "uml_UML63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_UML63"):
                opp_val = getattr(value, "uml_UML63", None)
                setattr(value, "uml_UML63", self)

    @property
    def uml_packages(self):
        return self.__uml_packages

    @uml_packages.setter
    def uml_packages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_packages__uml_packages", None)
        self.__uml_packages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_DocumentRoot41"):
                opp_val = getattr(old_value, "uml_DocumentRoot41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_DocumentRoot41"):
                opp_val = getattr(value, "uml_DocumentRoot41", None)
                if opp_val is None:
                    setattr(value, "uml_DocumentRoot41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_primitiveDataType:

    def __init__(self, kind: str, name: str, oID: str, uml_primitiveDataType: "uml_classifiersAndAssociations" = None, uml_primitiveDataType44: "uml_DocumentRoot" = None, uml_primitiveDataType55: "uml_ownerClassifier" = None):
        self.kind = kind
        self.name = name
        self.oID = oID
        self.uml_primitiveDataType = uml_primitiveDataType
        self.uml_primitiveDataType44 = uml_primitiveDataType44
        self.uml_primitiveDataType55 = uml_primitiveDataType55
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def oID(self) -> str:
        return self.__oID

    @oID.setter
    def oID(self, oID: str):
        self.__oID = oID

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uml_primitiveDataType44(self):
        return self.__uml_primitiveDataType44

    @uml_primitiveDataType44.setter
    def uml_primitiveDataType44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_primitiveDataType__uml_primitiveDataType44", None)
        self.__uml_primitiveDataType44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_DocumentRoot43"):
                opp_val = getattr(old_value, "uml_DocumentRoot43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_DocumentRoot43"):
                opp_val = getattr(value, "uml_DocumentRoot43", None)
                if opp_val is None:
                    setattr(value, "uml_DocumentRoot43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_primitiveDataType55(self):
        return self.__uml_primitiveDataType55

    @uml_primitiveDataType55.setter
    def uml_primitiveDataType55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_primitiveDataType__uml_primitiveDataType55", None)
        self.__uml_primitiveDataType55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ownerClassifier54"):
                opp_val = getattr(old_value, "uml_ownerClassifier54", None)
                if opp_val == self:
                    setattr(old_value, "uml_ownerClassifier54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ownerClassifier54"):
                opp_val = getattr(value, "uml_ownerClassifier54", None)
                setattr(value, "uml_ownerClassifier54", self)

    @property
    def uml_primitiveDataType(self):
        return self.__uml_primitiveDataType

    @uml_primitiveDataType.setter
    def uml_primitiveDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_primitiveDataType__uml_primitiveDataType", None)
        self.__uml_primitiveDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_classifiersAndAssociations10"):
                opp_val = getattr(old_value, "uml_classifiersAndAssociations10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_classifiersAndAssociations10"):
                opp_val = getattr(value, "uml_classifiersAndAssociations10", None)
                if opp_val is None:
                    setattr(value, "uml_classifiersAndAssociations10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_EStringToStringMapEntry:

    pass
class uml_DocumentRoot:

    def __init__(self, mixed: str, uml_DocumentRoot: set["uml_EStringToStringMapEntry"] = None, uml_DocumentRoot15: set["uml_EStringToStringMapEntry"] = None, uml_DocumentRoot18: set["uml_association"] = None, uml_DocumentRoot21: set["uml_attribute"] = None, uml_DocumentRoot24: set["uml_attributes"] = None, uml_DocumentRoot27: set["uml_class_"] = None, uml_DocumentRoot30: set["uml_classifiersAndAssociations"] = None, uml_DocumentRoot33: set["uml_generalClass"] = None, uml_DocumentRoot41: set["uml_packages"] = None, uml_DocumentRoot43: set["uml_primitiveDataType"] = None, uml_DocumentRoot46: set["uml_UML"] = None, uml_DocumentRoot36: set["uml_ownerClassifier"] = None, uml_DocumentRoot39: set["uml_package_"] = None):
        self.mixed = mixed
        self.uml_DocumentRoot = uml_DocumentRoot if uml_DocumentRoot is not None else set()
        self.uml_DocumentRoot15 = uml_DocumentRoot15 if uml_DocumentRoot15 is not None else set()
        self.uml_DocumentRoot18 = uml_DocumentRoot18 if uml_DocumentRoot18 is not None else set()
        self.uml_DocumentRoot21 = uml_DocumentRoot21 if uml_DocumentRoot21 is not None else set()
        self.uml_DocumentRoot24 = uml_DocumentRoot24 if uml_DocumentRoot24 is not None else set()
        self.uml_DocumentRoot27 = uml_DocumentRoot27 if uml_DocumentRoot27 is not None else set()
        self.uml_DocumentRoot30 = uml_DocumentRoot30 if uml_DocumentRoot30 is not None else set()
        self.uml_DocumentRoot33 = uml_DocumentRoot33 if uml_DocumentRoot33 is not None else set()
        self.uml_DocumentRoot41 = uml_DocumentRoot41 if uml_DocumentRoot41 is not None else set()
        self.uml_DocumentRoot43 = uml_DocumentRoot43 if uml_DocumentRoot43 is not None else set()
        self.uml_DocumentRoot46 = uml_DocumentRoot46 if uml_DocumentRoot46 is not None else set()
        self.uml_DocumentRoot36 = uml_DocumentRoot36 if uml_DocumentRoot36 is not None else set()
        self.uml_DocumentRoot39 = uml_DocumentRoot39 if uml_DocumentRoot39 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def uml_DocumentRoot33(self):
        return self.__uml_DocumentRoot33

    @uml_DocumentRoot33.setter
    def uml_DocumentRoot33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DocumentRoot__uml_DocumentRoot33", None)
        self.__uml_DocumentRoot33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_generalClass34"):
                    opp_val = getattr(item, "uml_generalClass34", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_generalClass34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_generalClass34"):
                    opp_val = getattr(item, "uml_generalClass34", None)
                    
                    setattr(item, "uml_generalClass34", self)
                    

    @property
    def uml_DocumentRoot15(self):
        return self.__uml_DocumentRoot15

    @uml_DocumentRoot15.setter
    def uml_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DocumentRoot__uml_DocumentRoot15", None)
        self.__uml_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_EStringToStringMapEntry16"):
                    opp_val = getattr(item, "uml_EStringToStringMapEntry16", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_EStringToStringMapEntry16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_EStringToStringMapEntry16"):
                    opp_val = getattr(item, "uml_EStringToStringMapEntry16", None)
                    
                    setattr(item, "uml_EStringToStringMapEntry16", self)
                    

    @property
    def uml_DocumentRoot39(self):
        return self.__uml_DocumentRoot39

    @uml_DocumentRoot39.setter
    def uml_DocumentRoot39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DocumentRoot__uml_DocumentRoot39", None)
        self.__uml_DocumentRoot39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_package_"):
                    opp_val = getattr(item, "uml_package_", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_package_", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_package_"):
                    opp_val = getattr(item, "uml_package_", None)
                    
                    setattr(item, "uml_package_", self)
                    

    @property
    def uml_DocumentRoot27(self):
        return self.__uml_DocumentRoot27

    @uml_DocumentRoot27.setter
    def uml_DocumentRoot27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DocumentRoot__uml_DocumentRoot27", None)
        self.__uml_DocumentRoot27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_class_28"):
                    opp_val = getattr(item, "uml_class_28", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_class_28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_class_28"):
                    opp_val = getattr(item, "uml_class_28", None)
                    
                    setattr(item, "uml_class_28", self)
                    

    @property
    def uml_DocumentRoot24(self):
        return self.__uml_DocumentRoot24

    @uml_DocumentRoot24.setter
    def uml_DocumentRoot24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DocumentRoot__uml_DocumentRoot24", None)
        self.__uml_DocumentRoot24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_attributes25"):
                    opp_val = getattr(item, "uml_attributes25", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_attributes25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_attributes25"):
                    opp_val = getattr(item, "uml_attributes25", None)
                    
                    setattr(item, "uml_attributes25", self)
                    

    @property
    def uml_DocumentRoot30(self):
        return self.__uml_DocumentRoot30

    @uml_DocumentRoot30.setter
    def uml_DocumentRoot30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DocumentRoot__uml_DocumentRoot30", None)
        self.__uml_DocumentRoot30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_classifiersAndAssociations31"):
                    opp_val = getattr(item, "uml_classifiersAndAssociations31", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_classifiersAndAssociations31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_classifiersAndAssociations31"):
                    opp_val = getattr(item, "uml_classifiersAndAssociations31", None)
                    
                    setattr(item, "uml_classifiersAndAssociations31", self)
                    

    @property
    def uml_DocumentRoot46(self):
        return self.__uml_DocumentRoot46

    @uml_DocumentRoot46.setter
    def uml_DocumentRoot46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DocumentRoot__uml_DocumentRoot46", None)
        self.__uml_DocumentRoot46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_UML"):
                    opp_val = getattr(item, "uml_UML", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_UML", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_UML"):
                    opp_val = getattr(item, "uml_UML", None)
                    
                    setattr(item, "uml_UML", self)
                    

    @property
    def uml_DocumentRoot36(self):
        return self.__uml_DocumentRoot36

    @uml_DocumentRoot36.setter
    def uml_DocumentRoot36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DocumentRoot__uml_DocumentRoot36", None)
        self.__uml_DocumentRoot36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_ownerClassifier37"):
                    opp_val = getattr(item, "uml_ownerClassifier37", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_ownerClassifier37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_ownerClassifier37"):
                    opp_val = getattr(item, "uml_ownerClassifier37", None)
                    
                    setattr(item, "uml_ownerClassifier37", self)
                    

    @property
    def uml_DocumentRoot43(self):
        return self.__uml_DocumentRoot43

    @uml_DocumentRoot43.setter
    def uml_DocumentRoot43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DocumentRoot__uml_DocumentRoot43", None)
        self.__uml_DocumentRoot43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_primitiveDataType44"):
                    opp_val = getattr(item, "uml_primitiveDataType44", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_primitiveDataType44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_primitiveDataType44"):
                    opp_val = getattr(item, "uml_primitiveDataType44", None)
                    
                    setattr(item, "uml_primitiveDataType44", self)
                    

    @property
    def uml_DocumentRoot18(self):
        return self.__uml_DocumentRoot18

    @uml_DocumentRoot18.setter
    def uml_DocumentRoot18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DocumentRoot__uml_DocumentRoot18", None)
        self.__uml_DocumentRoot18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_association19"):
                    opp_val = getattr(item, "uml_association19", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_association19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_association19"):
                    opp_val = getattr(item, "uml_association19", None)
                    
                    setattr(item, "uml_association19", self)
                    

    @property
    def uml_DocumentRoot(self):
        return self.__uml_DocumentRoot

    @uml_DocumentRoot.setter
    def uml_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DocumentRoot__uml_DocumentRoot", None)
        self.__uml_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_EStringToStringMapEntry"):
                    opp_val = getattr(item, "uml_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_EStringToStringMapEntry"):
                    opp_val = getattr(item, "uml_EStringToStringMapEntry", None)
                    
                    setattr(item, "uml_EStringToStringMapEntry", self)
                    

    @property
    def uml_DocumentRoot21(self):
        return self.__uml_DocumentRoot21

    @uml_DocumentRoot21.setter
    def uml_DocumentRoot21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DocumentRoot__uml_DocumentRoot21", None)
        self.__uml_DocumentRoot21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_attribute22"):
                    opp_val = getattr(item, "uml_attribute22", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_attribute22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_attribute22"):
                    opp_val = getattr(item, "uml_attribute22", None)
                    
                    setattr(item, "uml_attribute22", self)
                    

    @property
    def uml_DocumentRoot41(self):
        return self.__uml_DocumentRoot41

    @uml_DocumentRoot41.setter
    def uml_DocumentRoot41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_DocumentRoot__uml_DocumentRoot41", None)
        self.__uml_DocumentRoot41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_packages"):
                    opp_val = getattr(item, "uml_packages", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_packages", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_packages"):
                    opp_val = getattr(item, "uml_packages", None)
                    
                    setattr(item, "uml_packages", self)
                    

class uml_classifiersAndAssociations:

    def __init__(self, group: str, uml_classifiersAndAssociations12: set["uml_association"] = None, uml_classifiersAndAssociations: set["uml_class_"] = None, uml_classifiersAndAssociations10: set["uml_primitiveDataType"] = None, uml_classifiersAndAssociations31: "uml_DocumentRoot" = None, uml_classifiersAndAssociations58: "uml_package_" = None):
        self.group = group
        self.uml_classifiersAndAssociations12 = uml_classifiersAndAssociations12 if uml_classifiersAndAssociations12 is not None else set()
        self.uml_classifiersAndAssociations = uml_classifiersAndAssociations if uml_classifiersAndAssociations is not None else set()
        self.uml_classifiersAndAssociations10 = uml_classifiersAndAssociations10 if uml_classifiersAndAssociations10 is not None else set()
        self.uml_classifiersAndAssociations31 = uml_classifiersAndAssociations31
        self.uml_classifiersAndAssociations58 = uml_classifiersAndAssociations58
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def uml_classifiersAndAssociations12(self):
        return self.__uml_classifiersAndAssociations12

    @uml_classifiersAndAssociations12.setter
    def uml_classifiersAndAssociations12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_classifiersAndAssociations__uml_classifiersAndAssociations12", None)
        self.__uml_classifiersAndAssociations12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_association"):
                    opp_val = getattr(item, "uml_association", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_association", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_association"):
                    opp_val = getattr(item, "uml_association", None)
                    
                    setattr(item, "uml_association", self)
                    

    @property
    def uml_classifiersAndAssociations10(self):
        return self.__uml_classifiersAndAssociations10

    @uml_classifiersAndAssociations10.setter
    def uml_classifiersAndAssociations10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_classifiersAndAssociations__uml_classifiersAndAssociations10", None)
        self.__uml_classifiersAndAssociations10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_primitiveDataType"):
                    opp_val = getattr(item, "uml_primitiveDataType", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_primitiveDataType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_primitiveDataType"):
                    opp_val = getattr(item, "uml_primitiveDataType", None)
                    
                    setattr(item, "uml_primitiveDataType", self)
                    

    @property
    def uml_classifiersAndAssociations58(self):
        return self.__uml_classifiersAndAssociations58

    @uml_classifiersAndAssociations58.setter
    def uml_classifiersAndAssociations58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_classifiersAndAssociations__uml_classifiersAndAssociations58", None)
        self.__uml_classifiersAndAssociations58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_package_57"):
                opp_val = getattr(old_value, "uml_package_57", None)
                if opp_val == self:
                    setattr(old_value, "uml_package_57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_package_57"):
                opp_val = getattr(value, "uml_package_57", None)
                setattr(value, "uml_package_57", self)

    @property
    def uml_classifiersAndAssociations(self):
        return self.__uml_classifiersAndAssociations

    @uml_classifiersAndAssociations.setter
    def uml_classifiersAndAssociations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_classifiersAndAssociations__uml_classifiersAndAssociations", None)
        self.__uml_classifiersAndAssociations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_class_8"):
                    opp_val = getattr(item, "uml_class_8", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_class_8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_class_8"):
                    opp_val = getattr(item, "uml_class_8", None)
                    
                    setattr(item, "uml_class_8", self)
                    

    @property
    def uml_classifiersAndAssociations31(self):
        return self.__uml_classifiersAndAssociations31

    @uml_classifiersAndAssociations31.setter
    def uml_classifiersAndAssociations31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_classifiersAndAssociations__uml_classifiersAndAssociations31", None)
        self.__uml_classifiersAndAssociations31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_DocumentRoot30"):
                opp_val = getattr(old_value, "uml_DocumentRoot30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_DocumentRoot30"):
                opp_val = getattr(value, "uml_DocumentRoot30", None)
                if opp_val is None:
                    setattr(value, "uml_DocumentRoot30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_generalClass:

    pass
class uml_class_:

    def __init__(self, kind: str, name: str, oID: str, uml_class_: "uml_generalClass" = None, uml_class_5: "uml_attributes" = None, uml_class_8: "uml_classifiersAndAssociations" = None, uml_class_28: "uml_DocumentRoot" = None, uml_class_49: "uml_generalClass" = None, uml_class_52: "uml_ownerClassifier" = None):
        self.kind = kind
        self.name = name
        self.oID = oID
        self.uml_class_ = uml_class_
        self.uml_class_5 = uml_class_5
        self.uml_class_8 = uml_class_8
        self.uml_class_28 = uml_class_28
        self.uml_class_49 = uml_class_49
        self.uml_class_52 = uml_class_52
        
    @property
    def oID(self) -> str:
        return self.__oID

    @oID.setter
    def oID(self, oID: str):
        self.__oID = oID

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uml_class_28(self):
        return self.__uml_class_28

    @uml_class_28.setter
    def uml_class_28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_class___uml_class_28", None)
        self.__uml_class_28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_DocumentRoot27"):
                opp_val = getattr(old_value, "uml_DocumentRoot27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_DocumentRoot27"):
                opp_val = getattr(value, "uml_DocumentRoot27", None)
                if opp_val is None:
                    setattr(value, "uml_DocumentRoot27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_class_(self):
        return self.__uml_class_

    @uml_class_.setter
    def uml_class_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_class___uml_class_", None)
        self.__uml_class_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_generalClass"):
                opp_val = getattr(old_value, "uml_generalClass", None)
                if opp_val == self:
                    setattr(old_value, "uml_generalClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_generalClass"):
                opp_val = getattr(value, "uml_generalClass", None)
                setattr(value, "uml_generalClass", self)

    @property
    def uml_class_8(self):
        return self.__uml_class_8

    @uml_class_8.setter
    def uml_class_8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_class___uml_class_8", None)
        self.__uml_class_8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_classifiersAndAssociations"):
                opp_val = getattr(old_value, "uml_classifiersAndAssociations", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_classifiersAndAssociations"):
                opp_val = getattr(value, "uml_classifiersAndAssociations", None)
                if opp_val is None:
                    setattr(value, "uml_classifiersAndAssociations", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_class_49(self):
        return self.__uml_class_49

    @uml_class_49.setter
    def uml_class_49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_class___uml_class_49", None)
        self.__uml_class_49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_generalClass48"):
                opp_val = getattr(old_value, "uml_generalClass48", None)
                if opp_val == self:
                    setattr(old_value, "uml_generalClass48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_generalClass48"):
                opp_val = getattr(value, "uml_generalClass48", None)
                setattr(value, "uml_generalClass48", self)

    @property
    def uml_class_52(self):
        return self.__uml_class_52

    @uml_class_52.setter
    def uml_class_52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_class___uml_class_52", None)
        self.__uml_class_52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ownerClassifier51"):
                opp_val = getattr(old_value, "uml_ownerClassifier51", None)
                if opp_val == self:
                    setattr(old_value, "uml_ownerClassifier51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ownerClassifier51"):
                opp_val = getattr(value, "uml_ownerClassifier51", None)
                setattr(value, "uml_ownerClassifier51", self)

    @property
    def uml_class_5(self):
        return self.__uml_class_5

    @uml_class_5.setter
    def uml_class_5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_class___uml_class_5", None)
        self.__uml_class_5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_attributes6"):
                opp_val = getattr(old_value, "uml_attributes6", None)
                if opp_val == self:
                    setattr(old_value, "uml_attributes6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_attributes6"):
                opp_val = getattr(value, "uml_attributes6", None)
                setattr(value, "uml_attributes6", self)

class uml_attributes:

    def __init__(self, group: str, uml_attributes: set["uml_attribute"] = None, uml_attributes6: "uml_class_" = None, uml_attributes25: "uml_DocumentRoot" = None):
        self.group = group
        self.uml_attributes = uml_attributes if uml_attributes is not None else set()
        self.uml_attributes6 = uml_attributes6
        self.uml_attributes25 = uml_attributes25
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def uml_attributes(self):
        return self.__uml_attributes

    @uml_attributes.setter
    def uml_attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_attributes__uml_attributes", None)
        self.__uml_attributes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml_attribute2"):
                    opp_val = getattr(item, "uml_attribute2", None)
                    
                    if opp_val == self:
                        setattr(item, "uml_attribute2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml_attribute2"):
                    opp_val = getattr(item, "uml_attribute2", None)
                    
                    setattr(item, "uml_attribute2", self)
                    

    @property
    def uml_attributes6(self):
        return self.__uml_attributes6

    @uml_attributes6.setter
    def uml_attributes6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_attributes__uml_attributes6", None)
        self.__uml_attributes6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_class_5"):
                opp_val = getattr(old_value, "uml_class_5", None)
                if opp_val == self:
                    setattr(old_value, "uml_class_5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_class_5"):
                opp_val = getattr(value, "uml_class_5", None)
                setattr(value, "uml_class_5", self)

    @property
    def uml_attributes25(self):
        return self.__uml_attributes25

    @uml_attributes25.setter
    def uml_attributes25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_attributes__uml_attributes25", None)
        self.__uml_attributes25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_DocumentRoot24"):
                opp_val = getattr(old_value, "uml_DocumentRoot24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_DocumentRoot24"):
                opp_val = getattr(value, "uml_DocumentRoot24", None)
                if opp_val is None:
                    setattr(value, "uml_DocumentRoot24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_ownerClassifier:

    pass
class uml_attribute:

    def __init__(self, kind: str, name: str, oID: str, uml_attribute: "uml_ownerClassifier" = None, uml_attribute2: "uml_attributes" = None, uml_attribute22: "uml_DocumentRoot" = None):
        self.kind = kind
        self.name = name
        self.oID = oID
        self.uml_attribute = uml_attribute
        self.uml_attribute2 = uml_attribute2
        self.uml_attribute22 = uml_attribute22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oID(self) -> str:
        return self.__oID

    @oID.setter
    def oID(self, oID: str):
        self.__oID = oID

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def uml_attribute2(self):
        return self.__uml_attribute2

    @uml_attribute2.setter
    def uml_attribute2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_attribute__uml_attribute2", None)
        self.__uml_attribute2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_attributes"):
                opp_val = getattr(old_value, "uml_attributes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_attributes"):
                opp_val = getattr(value, "uml_attributes", None)
                if opp_val is None:
                    setattr(value, "uml_attributes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_attribute(self):
        return self.__uml_attribute

    @uml_attribute.setter
    def uml_attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_attribute__uml_attribute", None)
        self.__uml_attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_ownerClassifier"):
                opp_val = getattr(old_value, "uml_ownerClassifier", None)
                if opp_val == self:
                    setattr(old_value, "uml_ownerClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_ownerClassifier"):
                opp_val = getattr(value, "uml_ownerClassifier", None)
                setattr(value, "uml_ownerClassifier", self)

    @property
    def uml_attribute22(self):
        return self.__uml_attribute22

    @uml_attribute22.setter
    def uml_attribute22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_attribute__uml_attribute22", None)
        self.__uml_attribute22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_DocumentRoot21"):
                opp_val = getattr(old_value, "uml_DocumentRoot21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_DocumentRoot21"):
                opp_val = getattr(value, "uml_DocumentRoot21", None)
                if opp_val is None:
                    setattr(value, "uml_DocumentRoot21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uml_association:

    def __init__(self, destination: str, kind: str, name: str, oID: str, source: str, uml_association: "uml_classifiersAndAssociations" = None, uml_association19: "uml_DocumentRoot" = None):
        self.destination = destination
        self.kind = kind
        self.name = name
        self.oID = oID
        self.source = source
        self.uml_association = uml_association
        self.uml_association19 = uml_association19
        
    @property
    def destination(self) -> str:
        return self.__destination

    @destination.setter
    def destination(self, destination: str):
        self.__destination = destination

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oID(self) -> str:
        return self.__oID

    @oID.setter
    def oID(self, oID: str):
        self.__oID = oID

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def uml_association19(self):
        return self.__uml_association19

    @uml_association19.setter
    def uml_association19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_association__uml_association19", None)
        self.__uml_association19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_DocumentRoot18"):
                opp_val = getattr(old_value, "uml_DocumentRoot18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_DocumentRoot18"):
                opp_val = getattr(value, "uml_DocumentRoot18", None)
                if opp_val is None:
                    setattr(value, "uml_DocumentRoot18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml_association(self):
        return self.__uml_association

    @uml_association.setter
    def uml_association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_association__uml_association", None)
        self.__uml_association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_classifiersAndAssociations12"):
                opp_val = getattr(old_value, "uml_classifiersAndAssociations12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_classifiersAndAssociations12"):
                opp_val = getattr(value, "uml_classifiersAndAssociations12", None)
                if opp_val is None:
                    setattr(value, "uml_classifiersAndAssociations12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
