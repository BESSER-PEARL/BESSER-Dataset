from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class OCLType:

    pass
class OCLPackageParent:

    pass
class OCLRoot:

    pass
class library_OCLLibrary(OCLRoot, OCLPackageParent):

    pass
class OCLNamedElement:

    pass
class library_OCLTypedElement(OCLNamedElement):

    pass
class library_OCLType(OCLNamedElement):

    pass
class library_OCLPackageParent(OCLNamedElement):

    pass
class library_OCLPackage(OCLPackageParent):

    pass
class library_OCLTypeParameter(OCLType):

    pass
class OCLElement:

    pass
class library_OCLTypeValue(OCLElement):

    pass
class library_OCLNamedElement(OCLElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class OCLTypedElement:

    pass
class library_OCLLibraryProperty(OCLTypedElement):

    def __init__(self, isStatic: bool, class: str, library_OCLLibraryProperty: "library_OCLTypeDefinition" = None):
        self.isStatic = isStatic
        self.class = class
        self.library_OCLLibraryProperty = library_OCLLibraryProperty
        
    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def library_OCLLibraryProperty(self):
        return self.__library_OCLLibraryProperty

    @library_OCLLibraryProperty.setter
    def library_OCLLibraryProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_OCLLibraryProperty__library_OCLLibraryProperty", None)
        self.__library_OCLLibraryProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_OCLTypeDefinition26"):
                opp_val = getattr(old_value, "library_OCLTypeDefinition26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_OCLTypeDefinition26"):
                opp_val = getattr(value, "library_OCLTypeDefinition26", None)
                if opp_val is None:
                    setattr(value, "library_OCLTypeDefinition26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_OCLLibraryOperation(OCLTypedElement):

    def __init__(self, isStatic: bool, class: str, library_OCLLibraryOperation: set["library_OCLTypeParameter"] = None, library_OCLLibraryOperation7: set["library_OCLParameter"] = None, library_OCLLibraryOperation24: "library_OCLTypeDefinition" = None):
        self.isStatic = isStatic
        self.class = class
        self.library_OCLLibraryOperation = library_OCLLibraryOperation if library_OCLLibraryOperation is not None else set()
        self.library_OCLLibraryOperation7 = library_OCLLibraryOperation7 if library_OCLLibraryOperation7 is not None else set()
        self.library_OCLLibraryOperation24 = library_OCLLibraryOperation24
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def library_OCLLibraryOperation(self):
        return self.__library_OCLLibraryOperation

    @library_OCLLibraryOperation.setter
    def library_OCLLibraryOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_OCLLibraryOperation__library_OCLLibraryOperation", None)
        self.__library_OCLLibraryOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_OCLTypeParameter"):
                    opp_val = getattr(item, "library_OCLTypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "library_OCLTypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_OCLTypeParameter"):
                    opp_val = getattr(item, "library_OCLTypeParameter", None)
                    
                    setattr(item, "library_OCLTypeParameter", self)
                    

    @property
    def library_OCLLibraryOperation7(self):
        return self.__library_OCLLibraryOperation7

    @library_OCLLibraryOperation7.setter
    def library_OCLLibraryOperation7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_OCLLibraryOperation__library_OCLLibraryOperation7", None)
        self.__library_OCLLibraryOperation7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_OCLParameter"):
                    opp_val = getattr(item, "library_OCLParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "library_OCLParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_OCLParameter"):
                    opp_val = getattr(item, "library_OCLParameter", None)
                    
                    setattr(item, "library_OCLParameter", self)
                    

    @property
    def library_OCLLibraryOperation24(self):
        return self.__library_OCLLibraryOperation24

    @library_OCLLibraryOperation24.setter
    def library_OCLLibraryOperation24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_OCLLibraryOperation__library_OCLLibraryOperation24", None)
        self.__library_OCLLibraryOperation24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_OCLTypeDefinition23"):
                opp_val = getattr(old_value, "library_OCLTypeDefinition23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_OCLTypeDefinition23"):
                opp_val = getattr(value, "library_OCLTypeDefinition23", None)
                if opp_val is None:
                    setattr(value, "library_OCLTypeDefinition23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_OCLParameter(OCLTypedElement):

    pass
class library_OCLLibraryIteration(OCLTypedElement):

    def __init__(self, iterator: str, iterators: bool, class: str, library_OCLLibraryIteration: "library_OCLTypeDefinition" = None):
        self.iterator = iterator
        self.iterators = iterators
        self.class = class
        self.library_OCLLibraryIteration = library_OCLLibraryIteration
        
    @property
    def iterator(self) -> str:
        return self.__iterator

    @iterator.setter
    def iterator(self, iterator: str):
        self.__iterator = iterator

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def iterators(self) -> bool:
        return self.__iterators

    @iterators.setter
    def iterators(self, iterators: bool):
        self.__iterators = iterators

    @property
    def library_OCLLibraryIteration(self):
        return self.__library_OCLLibraryIteration

    @library_OCLLibraryIteration.setter
    def library_OCLLibraryIteration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_OCLLibraryIteration__library_OCLLibraryIteration", None)
        self.__library_OCLLibraryIteration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_OCLTypeDefinition21"):
                opp_val = getattr(old_value, "library_OCLTypeDefinition21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_OCLTypeDefinition21"):
                opp_val = getattr(value, "library_OCLTypeDefinition21", None)
                if opp_val is None:
                    setattr(value, "library_OCLTypeDefinition21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_OCLElement:

    pass
class library_OCLTypeBinding(OCLElement):

    pass
class library_OCLTypeDefinition(OCLType):

    pass
class OCLTypeValue:

    pass
class library_OCLTypeReference(OCLTypeValue):

    pass
class library_OCLBoundType(OCLTypeValue):

    pass
class library_OCLRoot:

    pass