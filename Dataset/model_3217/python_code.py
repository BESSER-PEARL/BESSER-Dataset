from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Modifiers(Enum):
    bridge = "bridge"
    default = "default"
    deprecated = "deprecated"
    enum = "enum"
    final = "final"
    interface = "interface"
    native = "native"
    private = "private"
    protected = "protected"
    public = "public"
    static = "static"
    abstract = "abstract"
    annotation = "annotation"
    strictfp = "strictfp"
    super = "super"
    synchronized = "synchronized"
    synthetic = "synthetic"
    transient = "transient"
    varargs = "varargs"
    volatile = "volatile"


############################################
# Definition of Classes
############################################

class Core_Parameter:

    def __init__(self, name: str, type: str, Core_Parameter: "Core_IMethod" = None):
        self.name = name
        self.type = type
        self.Core_Parameter = Core_Parameter
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Core_Parameter(self):
        return self.__Core_Parameter

    @Core_Parameter.setter
    def Core_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_Parameter__Core_Parameter", None)
        self.__Core_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_IMethod50"):
                opp_val = getattr(old_value, "Core_IMethod50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_IMethod50"):
                opp_val = getattr(value, "Core_IMethod50", None)
                if opp_val is None:
                    setattr(value, "Core_IMethod50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Core_ISourceRange:

    def __init__(self, length: str, offset: str, Core_ISourceRange34: "Core_IMember" = None, Core_ISourceRange37: "Core_IMember" = None, Core_ISourceRange: "Core_ISourceReference" = None):
        self.length = length
        self.offset = offset
        self.Core_ISourceRange34 = Core_ISourceRange34
        self.Core_ISourceRange37 = Core_ISourceRange37
        self.Core_ISourceRange = Core_ISourceRange
        
    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def offset(self) -> str:
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset

    @property
    def Core_ISourceRange37(self):
        return self.__Core_ISourceRange37

    @Core_ISourceRange37.setter
    def Core_ISourceRange37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ISourceRange__Core_ISourceRange37", None)
        self.__Core_ISourceRange37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_IMember36"):
                opp_val = getattr(old_value, "Core_IMember36", None)
                if opp_val == self:
                    setattr(old_value, "Core_IMember36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_IMember36"):
                opp_val = getattr(value, "Core_IMember36", None)
                setattr(value, "Core_IMember36", self)

    @property
    def Core_ISourceRange(self):
        return self.__Core_ISourceRange

    @Core_ISourceRange.setter
    def Core_ISourceRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ISourceRange__Core_ISourceRange", None)
        self.__Core_ISourceRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_ISourceReference"):
                opp_val = getattr(old_value, "Core_ISourceReference", None)
                if opp_val == self:
                    setattr(old_value, "Core_ISourceReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_ISourceReference"):
                opp_val = getattr(value, "Core_ISourceReference", None)
                setattr(value, "Core_ISourceReference", self)

    @property
    def Core_ISourceRange34(self):
        return self.__Core_ISourceRange34

    @Core_ISourceRange34.setter
    def Core_ISourceRange34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ISourceRange__Core_ISourceRange34", None)
        self.__Core_ISourceRange34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_IMember"):
                opp_val = getattr(old_value, "Core_IMember", None)
                if opp_val == self:
                    setattr(old_value, "Core_IMember", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_IMember"):
                opp_val = getattr(value, "Core_IMember", None)
                setattr(value, "Core_IMember", self)

class Core_ISourceReference(ABC):

    def __init__(self, source: str, Core_ISourceReference: "Core_ISourceRange" = None):
        self.source = source
        self.Core_ISourceReference = Core_ISourceReference
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def Core_ISourceReference(self):
        return self.__Core_ISourceReference

    @Core_ISourceReference.setter
    def Core_ISourceReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ISourceReference__Core_ISourceReference", None)
        self.__Core_ISourceReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_ISourceRange"):
                opp_val = getattr(old_value, "Core_ISourceRange", None)
                if opp_val == self:
                    setattr(old_value, "Core_ISourceRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_ISourceRange"):
                opp_val = getattr(value, "Core_ISourceRange", None)
                setattr(value, "Core_ISourceRange", self)

class IMember:

    pass
class Core_IField(IMember):

    def __init__(self, constant: str, isEnumConstant: str, typeSignature: str, isVolatile: str, isTransient: str, Core_IField: "Core_IType" = None):
        self.constant = constant
        self.isEnumConstant = isEnumConstant
        self.typeSignature = typeSignature
        self.isVolatile = isVolatile
        self.isTransient = isTransient
        self.Core_IField = Core_IField
        
    @property
    def constant(self) -> str:
        return self.__constant

    @constant.setter
    def constant(self, constant: str):
        self.__constant = constant

    @property
    def isEnumConstant(self) -> str:
        return self.__isEnumConstant

    @isEnumConstant.setter
    def isEnumConstant(self, isEnumConstant: str):
        self.__isEnumConstant = isEnumConstant

    @property
    def isVolatile(self) -> str:
        return self.__isVolatile

    @isVolatile.setter
    def isVolatile(self, isVolatile: str):
        self.__isVolatile = isVolatile

    @property
    def typeSignature(self) -> str:
        return self.__typeSignature

    @typeSignature.setter
    def typeSignature(self, typeSignature: str):
        self.__typeSignature = typeSignature

    @property
    def isTransient(self) -> str:
        return self.__isTransient

    @isTransient.setter
    def isTransient(self, isTransient: str):
        self.__isTransient = isTransient

    @property
    def Core_IField(self):
        return self.__Core_IField

    @Core_IField.setter
    def Core_IField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IField__Core_IField", None)
        self.__Core_IField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_IType41"):
                opp_val = getattr(old_value, "Core_IType41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_IType41"):
                opp_val = getattr(value, "Core_IType41", None)
                if opp_val is None:
                    setattr(value, "Core_IType41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Core_IInitializer(IMember):

    pass
class Core_IMethod(IMember):

    def __init__(self, returnType: str, isConstructor: str, isMainMethod: str, exceptionTypes: str, Core_IMethod: "Core_IType" = None, Core_IMethod50: set["Core_Parameter"] = None):
        self.returnType = returnType
        self.isConstructor = isConstructor
        self.isMainMethod = isMainMethod
        self.exceptionTypes = exceptionTypes
        self.Core_IMethod = Core_IMethod
        self.Core_IMethod50 = Core_IMethod50 if Core_IMethod50 is not None else set()
        
    @property
    def exceptionTypes(self) -> str:
        return self.__exceptionTypes

    @exceptionTypes.setter
    def exceptionTypes(self, exceptionTypes: str):
        self.__exceptionTypes = exceptionTypes

    @property
    def isMainMethod(self) -> str:
        return self.__isMainMethod

    @isMainMethod.setter
    def isMainMethod(self, isMainMethod: str):
        self.__isMainMethod = isMainMethod

    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

    @property
    def isConstructor(self) -> str:
        return self.__isConstructor

    @isConstructor.setter
    def isConstructor(self, isConstructor: str):
        self.__isConstructor = isConstructor

    @property
    def Core_IMethod50(self):
        return self.__Core_IMethod50

    @Core_IMethod50.setter
    def Core_IMethod50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IMethod__Core_IMethod50", None)
        self.__Core_IMethod50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_Parameter"):
                    opp_val = getattr(item, "Core_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_Parameter"):
                    opp_val = getattr(item, "Core_Parameter", None)
                    
                    setattr(item, "Core_Parameter", self)
                    

    @property
    def Core_IMethod(self):
        return self.__Core_IMethod

    @Core_IMethod.setter
    def Core_IMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IMethod__Core_IMethod", None)
        self.__Core_IMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_IType43"):
                opp_val = getattr(old_value, "Core_IType43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_IType43"):
                opp_val = getattr(value, "Core_IType43", None)
                if opp_val is None:
                    setattr(value, "Core_IType43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Core_IType(IMember):

    def __init__(self, fullyQualifiedName: str, fullyQualifiedParametrizedName: str, Core_IType31: "Core_IClassFile" = None, Core_IType: "Core_ICompilationUnit" = None, Core_IType23: "Core_ICompilationUnit" = None, Core_IType39: set["Core_IInitializer"] = None, Core_IType41: set["Core_IField"] = None, Core_IType43: set["Core_IMethod"] = None, Core_IType46: "Core_IType" = None, Core_IType44: set["Core_IType"] = None, Core_IType48: set["Core_ITypeParameter"] = None):
        self.fullyQualifiedName = fullyQualifiedName
        self.fullyQualifiedParametrizedName = fullyQualifiedParametrizedName
        self.Core_IType31 = Core_IType31
        self.Core_IType = Core_IType
        self.Core_IType23 = Core_IType23
        self.Core_IType39 = Core_IType39 if Core_IType39 is not None else set()
        self.Core_IType41 = Core_IType41 if Core_IType41 is not None else set()
        self.Core_IType43 = Core_IType43 if Core_IType43 is not None else set()
        self.Core_IType46 = Core_IType46
        self.Core_IType44 = Core_IType44 if Core_IType44 is not None else set()
        self.Core_IType48 = Core_IType48 if Core_IType48 is not None else set()
        
    @property
    def fullyQualifiedParametrizedName(self) -> str:
        return self.__fullyQualifiedParametrizedName

    @fullyQualifiedParametrizedName.setter
    def fullyQualifiedParametrizedName(self, fullyQualifiedParametrizedName: str):
        self.__fullyQualifiedParametrizedName = fullyQualifiedParametrizedName

    @property
    def fullyQualifiedName(self) -> str:
        return self.__fullyQualifiedName

    @fullyQualifiedName.setter
    def fullyQualifiedName(self, fullyQualifiedName: str):
        self.__fullyQualifiedName = fullyQualifiedName

    @property
    def Core_IType46(self):
        return self.__Core_IType46

    @Core_IType46.setter
    def Core_IType46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType46", None)
        self.__Core_IType46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_IType44"):
                opp_val = getattr(old_value, "Core_IType44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_IType44"):
                opp_val = getattr(value, "Core_IType44", None)
                if opp_val is None:
                    setattr(value, "Core_IType44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Core_IType23(self):
        return self.__Core_IType23

    @Core_IType23.setter
    def Core_IType23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType23", None)
        self.__Core_IType23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_ICompilationUnit22"):
                opp_val = getattr(old_value, "Core_ICompilationUnit22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_ICompilationUnit22"):
                opp_val = getattr(value, "Core_ICompilationUnit22", None)
                if opp_val is None:
                    setattr(value, "Core_ICompilationUnit22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Core_IType44(self):
        return self.__Core_IType44

    @Core_IType44.setter
    def Core_IType44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType44", None)
        self.__Core_IType44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IType46"):
                    opp_val = getattr(item, "Core_IType46", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IType46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IType46"):
                    opp_val = getattr(item, "Core_IType46", None)
                    
                    setattr(item, "Core_IType46", self)
                    

    @property
    def Core_IType48(self):
        return self.__Core_IType48

    @Core_IType48.setter
    def Core_IType48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType48", None)
        self.__Core_IType48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_ITypeParameter"):
                    opp_val = getattr(item, "Core_ITypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_ITypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_ITypeParameter"):
                    opp_val = getattr(item, "Core_ITypeParameter", None)
                    
                    setattr(item, "Core_ITypeParameter", self)
                    

    @property
    def Core_IType43(self):
        return self.__Core_IType43

    @Core_IType43.setter
    def Core_IType43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType43", None)
        self.__Core_IType43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IMethod"):
                    opp_val = getattr(item, "Core_IMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IMethod"):
                    opp_val = getattr(item, "Core_IMethod", None)
                    
                    setattr(item, "Core_IMethod", self)
                    

    @property
    def Core_IType(self):
        return self.__Core_IType

    @Core_IType.setter
    def Core_IType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType", None)
        self.__Core_IType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_ICompilationUnit18"):
                opp_val = getattr(old_value, "Core_ICompilationUnit18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_ICompilationUnit18"):
                opp_val = getattr(value, "Core_ICompilationUnit18", None)
                if opp_val is None:
                    setattr(value, "Core_ICompilationUnit18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Core_IType39(self):
        return self.__Core_IType39

    @Core_IType39.setter
    def Core_IType39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType39", None)
        self.__Core_IType39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IInitializer"):
                    opp_val = getattr(item, "Core_IInitializer", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IInitializer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IInitializer"):
                    opp_val = getattr(item, "Core_IInitializer", None)
                    
                    setattr(item, "Core_IInitializer", self)
                    

    @property
    def Core_IType41(self):
        return self.__Core_IType41

    @Core_IType41.setter
    def Core_IType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType41", None)
        self.__Core_IType41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IField"):
                    opp_val = getattr(item, "Core_IField", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IField"):
                    opp_val = getattr(item, "Core_IField", None)
                    
                    setattr(item, "Core_IField", self)
                    

    @property
    def Core_IType31(self):
        return self.__Core_IType31

    @Core_IType31.setter
    def Core_IType31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IType__Core_IType31", None)
        self.__Core_IType31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_IClassFile30"):
                opp_val = getattr(old_value, "Core_IClassFile30", None)
                if opp_val == self:
                    setattr(old_value, "Core_IClassFile30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_IClassFile30"):
                opp_val = getattr(value, "Core_IClassFile30", None)
                setattr(value, "Core_IClassFile30", self)

class ITypeRoot:

    pass
class ISourceReference:

    pass
class Core_ICompilationUnit(ITypeRoot):

    pass
class Core_CompilationUnit:

    pass
class IPackageFragmentRoot:

    pass
class Core_SourcePackageFragmentRoot(IPackageFragmentRoot):

    pass
class Core_BinaryPackageFragmentRoot(IPackageFragmentRoot):

    pass
class Core_IClassFile(ITypeRoot):

    def __init__(self, isClass: str, isInterface: str, Core_IClassFile: "Core_IPackageFragment" = None, Core_IClassFile30: "Core_IType" = None):
        self.isClass = isClass
        self.isInterface = isInterface
        self.Core_IClassFile = Core_IClassFile
        self.Core_IClassFile30 = Core_IClassFile30
        
    @property
    def isClass(self) -> str:
        return self.__isClass

    @isClass.setter
    def isClass(self, isClass: str):
        self.__isClass = isClass

    @property
    def isInterface(self) -> str:
        return self.__isInterface

    @isInterface.setter
    def isInterface(self, isInterface: str):
        self.__isInterface = isInterface

    @property
    def Core_IClassFile(self):
        return self.__Core_IClassFile

    @Core_IClassFile.setter
    def Core_IClassFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IClassFile__Core_IClassFile", None)
        self.__Core_IClassFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_IPackageFragment"):
                opp_val = getattr(old_value, "Core_IPackageFragment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_IPackageFragment"):
                opp_val = getattr(value, "Core_IPackageFragment", None)
                if opp_val is None:
                    setattr(value, "Core_IPackageFragment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Core_IClassFile30(self):
        return self.__Core_IClassFile30

    @Core_IClassFile30.setter
    def Core_IClassFile30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IClassFile__Core_IClassFile30", None)
        self.__Core_IClassFile30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_IType31"):
                opp_val = getattr(old_value, "Core_IType31", None)
                if opp_val == self:
                    setattr(old_value, "Core_IType31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_IType31"):
                opp_val = getattr(value, "Core_IType31", None)
                setattr(value, "Core_IType31", self)

class PhysicalElement:

    pass
class Core_IJavaModel(PhysicalElement):

    pass
class Core_PhysicalElement(ABC):

    def __init__(self, path: str, isReadOnly: str):
        self.path = path
        self.isReadOnly = isReadOnly
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

class Core_IJavaElement(ABC):

    def __init__(self, elementName: str):
        self.elementName = elementName
        
    @property
    def elementName(self) -> str:
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

class IJavaElement:

    pass
class Core_IPackageFragment(IJavaElement, PhysicalElement):

    def __init__(self, isDefaultPackage: str, packageFragments: "Core_IPackageFragmentRoot" = None, Core_IPackageFragment: set["Core_IClassFile"] = None, IPackageFragment: "Core_IPackageFragmentRoot" = None, Core_IPackageFragment16: set["Core_ICompilationUnit"] = None):
        self.isDefaultPackage = isDefaultPackage
        self.packageFragments = packageFragments
        self.Core_IPackageFragment = Core_IPackageFragment if Core_IPackageFragment is not None else set()
        self.IPackageFragment = IPackageFragment
        self.Core_IPackageFragment16 = Core_IPackageFragment16 if Core_IPackageFragment16 is not None else set()
        
    @property
    def isDefaultPackage(self) -> str:
        return self.__isDefaultPackage

    @isDefaultPackage.setter
    def isDefaultPackage(self, isDefaultPackage: str):
        self.__isDefaultPackage = isDefaultPackage

    @property
    def Core_IPackageFragment16(self):
        return self.__Core_IPackageFragment16

    @Core_IPackageFragment16.setter
    def Core_IPackageFragment16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IPackageFragment__Core_IPackageFragment16", None)
        self.__Core_IPackageFragment16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_ICompilationUnit"):
                    opp_val = getattr(item, "Core_ICompilationUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_ICompilationUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_ICompilationUnit"):
                    opp_val = getattr(item, "Core_ICompilationUnit", None)
                    
                    setattr(item, "Core_ICompilationUnit", self)
                    

    @property
    def packageFragments(self):
        return self.__packageFragments

    @packageFragments.setter
    def packageFragments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IPackageFragment__packageFragments", None)
        self.__packageFragments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IPackageFragmentRoot"):
                opp_val = getattr(old_value, "IPackageFragmentRoot", None)
                if opp_val == self:
                    setattr(old_value, "IPackageFragmentRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IPackageFragmentRoot"):
                opp_val = getattr(value, "IPackageFragmentRoot", None)
                setattr(value, "IPackageFragmentRoot", self)

    @property
    def IPackageFragment(self):
        return self.__IPackageFragment

    @IPackageFragment.setter
    def IPackageFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IPackageFragment__IPackageFragment", None)
        self.__IPackageFragment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packageFragmentRoot"):
                opp_val = getattr(old_value, "packageFragmentRoot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packageFragmentRoot"):
                opp_val = getattr(value, "packageFragmentRoot", None)
                if opp_val is None:
                    setattr(value, "packageFragmentRoot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Core_IPackageFragment(self):
        return self.__Core_IPackageFragment

    @Core_IPackageFragment.setter
    def Core_IPackageFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IPackageFragment__Core_IPackageFragment", None)
        self.__Core_IPackageFragment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Core_IClassFile"):
                    opp_val = getattr(item, "Core_IClassFile", None)
                    
                    if opp_val == self:
                        setattr(item, "Core_IClassFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Core_IClassFile"):
                    opp_val = getattr(item, "Core_IClassFile", None)
                    
                    setattr(item, "Core_IClassFile", self)
                    

class Core_IImportDeclaration(IJavaElement, ISourceReference):

    def __init__(self, isOnDemand: str, isStatic: str, Core_IImportDeclaration: "Core_ICompilationUnit" = None):
        self.isOnDemand = isOnDemand
        self.isStatic = isStatic
        self.Core_IImportDeclaration = Core_IImportDeclaration
        
    @property
    def isOnDemand(self) -> str:
        return self.__isOnDemand

    @isOnDemand.setter
    def isOnDemand(self, isOnDemand: str):
        self.__isOnDemand = isOnDemand

    @property
    def isStatic(self) -> str:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic

    @property
    def Core_IImportDeclaration(self):
        return self.__Core_IImportDeclaration

    @Core_IImportDeclaration.setter
    def Core_IImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_IImportDeclaration__Core_IImportDeclaration", None)
        self.__Core_IImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_ICompilationUnit20"):
                opp_val = getattr(old_value, "Core_ICompilationUnit20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_ICompilationUnit20"):
                opp_val = getattr(value, "Core_ICompilationUnit20", None)
                if opp_val is None:
                    setattr(value, "Core_ICompilationUnit20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Core_ITypeParameter(IJavaElement, ISourceReference):

    def __init__(self, bounds: str, Core_ITypeParameter: "Core_IType" = None):
        self.bounds = bounds
        self.Core_ITypeParameter = Core_ITypeParameter
        
    @property
    def bounds(self) -> str:
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds

    @property
    def Core_ITypeParameter(self):
        return self.__Core_ITypeParameter

    @Core_ITypeParameter.setter
    def Core_ITypeParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ITypeParameter__Core_ITypeParameter", None)
        self.__Core_ITypeParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Core_IType48"):
                opp_val = getattr(old_value, "Core_IType48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Core_IType48"):
                opp_val = getattr(value, "Core_IType48", None)
                if opp_val is None:
                    setattr(value, "Core_IType48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Core_ITypeRoot(IJavaElement, PhysicalElement, ISourceReference):

    pass
class Core_IMember(IJavaElement, ISourceReference):

    pass
class Core_IPackageFragmentRoot(IJavaElement, PhysicalElement):

    pass
class Core_IJavaProject(IJavaElement, PhysicalElement):

    pass