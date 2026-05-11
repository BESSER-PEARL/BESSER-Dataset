from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class hutn_Spec:

    def __init__(self, modelFile: str, sourceFile: str, hutn_Spec: set["hutn_NsUri"] = None, hutn_Spec2: set["hutn_PackageObject"] = None):
        self.modelFile = modelFile
        self.sourceFile = sourceFile
        self.hutn_Spec = hutn_Spec if hutn_Spec is not None else set()
        self.hutn_Spec2 = hutn_Spec2 if hutn_Spec2 is not None else set()
        
        pass
    @property
    def modelFile(self):
        return self.__modelFile

    @modelFile.setter
    def modelFile(self, modelFile: str):
        self.__modelFile = modelFile


    @property
    def sourceFile(self):
        return self.__sourceFile

    @sourceFile.setter
    def sourceFile(self, sourceFile: str):
        self.__sourceFile = sourceFile


    @property
    def hutn_Spec2(self):
        return self.__hutn_Spec2

    @hutn_Spec2.setter
    def hutn_Spec2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hutn_Spec__hutn_Spec2", None)
        self.__hutn_Spec2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hutn_PackageObject"):
                    opp_val = getattr(item, "hutn_PackageObject", None)
                    
                    if opp_val == self:
                        setattr(item, "hutn_PackageObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hutn_PackageObject"):
                    opp_val = getattr(item, "hutn_PackageObject", None)
                    
                    setattr(item, "hutn_PackageObject", self)
                    

    @property
    def hutn_Spec(self):
        return self.__hutn_Spec

    @hutn_Spec.setter
    def hutn_Spec(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hutn_Spec__hutn_Spec", None)
        self.__hutn_Spec = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hutn_NsUri"):
                    opp_val = getattr(item, "hutn_NsUri", None)
                    
                    if opp_val == self:
                        setattr(item, "hutn_NsUri", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hutn_NsUri"):
                    opp_val = getattr(item, "hutn_NsUri", None)
                    
                    setattr(item, "hutn_NsUri", self)
                    

class hutn_ClassObjectSlot(ABC):

    def __init__(self):
        
        pass
    def getClassObjects(self) :
        # TODO: Implement getClassObjects method
        pass

    def setClassObjects(self, hutn_classObjects):
        # TODO: Implement setClassObjects method
        pass

    def addClassObject(self, hutn_classObject):
        # TODO: Implement addClassObject method
        pass

class hutn_AttributeSlot:

    pass
class hutn_ReferenceSlot:

    pass
class hutn_ContainmentSlot:

    pass
class hutn_ModelElement:

    def __init__(self, line: int, col: int):
        self.line = line
        self.col = col
        
        pass
    @property
    def col(self):
        return self.__col

    @col.setter
    def col(self, col: int):
        self.__col = col


    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, line: int):
        self.__line = line


class hutn_EPackage:

    pass
class Object:

    pass
class hutn_ClassObject(Object):

    def __init__(self, hutn_ClassObject: "hutn_PackageObject" = None, ClassObject: "hutn_Slot" = None, hutn_ClassObject9: "hutn_ContainmentSlot" = None):
        self.hutn_ClassObject = hutn_ClassObject
        self.ClassObject = ClassObject
        self.hutn_ClassObject9 = hutn_ClassObject9
        
        pass
    @property
    def hutn_ClassObject(self):
        return self.__hutn_ClassObject

    @hutn_ClassObject.setter
    def hutn_ClassObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hutn_ClassObject__hutn_ClassObject", None)
        self.__hutn_ClassObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hutn_PackageObject6"):
                opp_val = getattr(old_value, "hutn_PackageObject6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hutn_PackageObject6"):
                opp_val = getattr(value, "hutn_PackageObject6", None)
                if opp_val is None:
                    setattr(value, "hutn_PackageObject6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hutn_ClassObject9(self):
        return self.__hutn_ClassObject9

    @hutn_ClassObject9.setter
    def hutn_ClassObject9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hutn_ClassObject__hutn_ClassObject9", None)
        self.__hutn_ClassObject9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hutn_ContainmentSlot"):
                opp_val = getattr(old_value, "hutn_ContainmentSlot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hutn_ContainmentSlot"):
                opp_val = getattr(value, "hutn_ContainmentSlot", None)
                if opp_val is None:
                    setattr(value, "hutn_ContainmentSlot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassObject(self):
        return self.__ClassObject

    @ClassObject.setter
    def ClassObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hutn_ClassObject__ClassObject", None)
        self.__ClassObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "slots"):
                opp_val = getattr(old_value, "slots", None)
                if opp_val == self:
                    setattr(old_value, "slots", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "slots"):
                opp_val = getattr(value, "slots", None)
                setattr(value, "slots", self)

    def typeCompatibleWith(self, hutn_eClass) :
        # TODO: Implement typeCompatibleWith method
        pass

    def findSlot(self, hutn_feature):
        # TODO: Implement findSlot method
        pass

    def findOrCreateAttributeSlot(self, hutn_feature) :
        # TODO: Implement findOrCreateAttributeSlot method
        pass

    def hasEClass(self) :
        # TODO: Implement hasEClass method
        pass

    def getEClass(self) :
        # TODO: Implement getEClass method
        pass

    def findOrCreateReferenceSlot(self, hutn_feature) :
        # TODO: Implement findOrCreateReferenceSlot method
        pass

    def getPackageObject(self) :
        # TODO: Implement getPackageObject method
        pass

    def findOrCreateContainmentSlot(self, hutn_feature) :
        # TODO: Implement findOrCreateContainmentSlot method
        pass

class ModelElement:

    pass
class hutn_Object(ModelElement):

    def __init__(self, type: str, identifier: str):
        self.type = type
        self.identifier = identifier
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


class hutn_NsUri(ModelElement):

    def __init__(self, value: str, hutn_NsUri: "hutn_Spec" = None):
        self.value = value
        self.hutn_NsUri = hutn_NsUri
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def hutn_NsUri(self):
        return self.__hutn_NsUri

    @hutn_NsUri.setter
    def hutn_NsUri(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hutn_NsUri__hutn_NsUri", None)
        self.__hutn_NsUri = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hutn_Spec"):
                opp_val = getattr(old_value, "hutn_Spec", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hutn_Spec"):
                opp_val = getattr(value, "hutn_Spec", None)
                if opp_val is None:
                    setattr(value, "hutn_Spec", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hutn_Slot(ModelElement):

    def __init__(self, feature: str, values: str, slots: "hutn_ClassObject" = None):
        self.feature = feature
        self.values = values
        self.slots = slots
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature


    @property
    def slots(self):
        return self.__slots

    @slots.setter
    def slots(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hutn_Slot__slots", None)
        self.__slots = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassObject"):
                opp_val = getattr(old_value, "ClassObject", None)
                if opp_val == self:
                    setattr(old_value, "ClassObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassObject"):
                opp_val = getattr(value, "ClassObject", None)
                setattr(value, "ClassObject", self)

    def multiplicityCompatibleWith(self, hutn_eStructuralFeature) :
        # TODO: Implement multiplicityCompatibleWith method
        pass

    def compatibleWith(self, hutn_eStructuralFeature) :
        # TODO: Implement compatibleWith method
        pass

    def typeCompatibleWith(self, hutn_eStructuralFeature) :
        # TODO: Implement typeCompatibleWith method
        pass

    def getEStructuralFeature(self) :
        # TODO: Implement getEStructuralFeature method
        pass

    def hasEStructuralFeature(self) :
        # TODO: Implement hasEStructuralFeature method
        pass

    def setValues(self, hutn_values):
        # TODO: Implement setValues method
        pass

class hutn_PackageObject(Object):

    def __init__(self, hutn_PackageObject: "hutn_Spec" = None, hutn_PackageObject4: set["hutn_EPackage"] = None, hutn_PackageObject6: set["hutn_ClassObject"] = None):
        self.hutn_PackageObject = hutn_PackageObject
        self.hutn_PackageObject4 = hutn_PackageObject4 if hutn_PackageObject4 is not None else set()
        self.hutn_PackageObject6 = hutn_PackageObject6 if hutn_PackageObject6 is not None else set()
        
        pass
    @property
    def hutn_PackageObject(self):
        return self.__hutn_PackageObject

    @hutn_PackageObject.setter
    def hutn_PackageObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hutn_PackageObject__hutn_PackageObject", None)
        self.__hutn_PackageObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hutn_Spec2"):
                opp_val = getattr(old_value, "hutn_Spec2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hutn_Spec2"):
                opp_val = getattr(value, "hutn_Spec2", None)
                if opp_val is None:
                    setattr(value, "hutn_Spec2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hutn_PackageObject4(self):
        return self.__hutn_PackageObject4

    @hutn_PackageObject4.setter
    def hutn_PackageObject4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hutn_PackageObject__hutn_PackageObject4", None)
        self.__hutn_PackageObject4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hutn_EPackage"):
                    opp_val = getattr(item, "hutn_EPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "hutn_EPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hutn_EPackage"):
                    opp_val = getattr(item, "hutn_EPackage", None)
                    
                    setattr(item, "hutn_EPackage", self)
                    

    @property
    def hutn_PackageObject6(self):
        return self.__hutn_PackageObject6

    @hutn_PackageObject6.setter
    def hutn_PackageObject6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hutn_PackageObject__hutn_PackageObject6", None)
        self.__hutn_PackageObject6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hutn_ClassObject"):
                    opp_val = getattr(item, "hutn_ClassObject", None)
                    
                    if opp_val == self:
                        setattr(item, "hutn_ClassObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hutn_ClassObject"):
                    opp_val = getattr(item, "hutn_ClassObject", None)
                    
                    setattr(item, "hutn_ClassObject", self)
                    

    def getAllEClasses(self) :
        # TODO: Implement getAllEClasses method
        pass
