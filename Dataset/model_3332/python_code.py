from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TrueFalseDefault(Enum):
    true = "true"
    false = "false"
    default = "default"
class VisibilityKind(Enum):
    public = "public"
    protected = "protected"
    private = "private"


############################################
# Definition of Classes
############################################

class JDTType:

    pass
class jdtmm_JDTEnum(JDTType):

    pass
class jdtmm_JDTInterface(JDTType):

    pass
class jdtmm_JDTClass(JDTType):

    pass
class JDTMethodBody:

    pass
class jdtmm_JDTOpaqueBody(JDTMethodBody):

    def __init__(self, _body: str):
        self._body = _body
        
    @property
    def _body(self) -> str:
        return self.___body

    @_body.setter
    def _body(self, _body: str):
        self.___body = _body

class jdtmm_JDTException:

    pass
class JDTTypeRoot:

    pass
class jdtmm_JDTCompilationUnit(JDTTypeRoot):

    pass
class jdtmm_JDTJavaElement(ABC):

    def __init__(self, elementType: str, comment: str, generated: str, elementName: str, children: "jdtmm_JDTParent" = None, JDTJavaElement: "jdtmm_JDTParent" = None):
        self.elementType = elementType
        self.comment = comment
        self.generated = generated
        self.elementName = elementName
        self.children = children
        self.JDTJavaElement = JDTJavaElement
        
    @property
    def elementName(self) -> str:
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

    @property
    def elementType(self) -> str:
        return self.__elementType

    @elementType.setter
    def elementType(self, elementType: str):
        self.__elementType = elementType

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def generated(self) -> str:
        return self.__generated

    @generated.setter
    def generated(self, generated: str):
        self.__generated = generated

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTJavaElement__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTParent"):
                opp_val = getattr(old_value, "JDTParent", None)
                if opp_val == self:
                    setattr(old_value, "JDTParent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTParent"):
                opp_val = getattr(value, "JDTParent", None)
                setattr(value, "JDTParent", self)

    @property
    def JDTJavaElement(self):
        return self.__JDTJavaElement

    @JDTJavaElement.setter
    def JDTJavaElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTJavaElement__JDTJavaElement", None)
        self.__JDTJavaElement = value
        
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

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

    def getJDTSignature(self) -> str:
        # TODO: Implement getJDTSignature method
        pass

    def getQualifiedName(self) -> str:
        # TODO: Implement getQualifiedName method
        pass

class JDTParentJavaElement:

    pass
class jdtmm_JDTTypeRoot(JDTParentJavaElement):

    pass
class jdtmm_JDTJavaModel(JDTParentJavaElement):

    pass
class jdtmm_JDTPackageFragment(JDTParentJavaElement):

    pass
class jdtmm_JDTImportContainer(JDTParentJavaElement):

    pass
class jdtmm_JDTPackageFragmentRoot(JDTParentJavaElement):

    pass
class jdtmm_JDTJavaProject(JDTParentJavaElement):

    pass
class jdtmm_JDTMember(JDTParentJavaElement):

    def __init__(self, visibility: str, explicitPlainTextRequiredImports: str, jdtmm_JDTMember: set["jdtmm_JDTType"] = None, declaringMember: set["jdtmm_JDTTypeParameter"] = None, JDTMember: "jdtmm_JDTTypeParameter" = None):
        self.visibility = visibility
        self.explicitPlainTextRequiredImports = explicitPlainTextRequiredImports
        self.jdtmm_JDTMember = jdtmm_JDTMember if jdtmm_JDTMember is not None else set()
        self.declaringMember = declaringMember if declaringMember is not None else set()
        self.JDTMember = JDTMember
        
    @property
    def explicitPlainTextRequiredImports(self) -> str:
        return self.__explicitPlainTextRequiredImports

    @explicitPlainTextRequiredImports.setter
    def explicitPlainTextRequiredImports(self, explicitPlainTextRequiredImports: str):
        self.__explicitPlainTextRequiredImports = explicitPlainTextRequiredImports

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def jdtmm_JDTMember(self):
        return self.__jdtmm_JDTMember

    @jdtmm_JDTMember.setter
    def jdtmm_JDTMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTMember__jdtmm_JDTMember", None)
        self.__jdtmm_JDTMember = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jdtmm_JDTType9"):
                    opp_val = getattr(item, "jdtmm_JDTType9", None)
                    
                    if opp_val == self:
                        setattr(item, "jdtmm_JDTType9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jdtmm_JDTType9"):
                    opp_val = getattr(item, "jdtmm_JDTType9", None)
                    
                    setattr(item, "jdtmm_JDTType9", self)
                    

    @property
    def declaringMember(self):
        return self.__declaringMember

    @declaringMember.setter
    def declaringMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTMember__declaringMember", None)
        self.__declaringMember = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTTypeParameter"):
                    opp_val = getattr(item, "JDTTypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTTypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTTypeParameter"):
                    opp_val = getattr(item, "JDTTypeParameter", None)
                    
                    setattr(item, "JDTTypeParameter", self)
                    

    @property
    def JDTMember(self):
        return self.__JDTMember

    @JDTMember.setter
    def JDTMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTMember__JDTMember", None)
        self.__JDTMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeParameters"):
                opp_val = getattr(old_value, "typeParameters", None)
                if opp_val == self:
                    setattr(old_value, "typeParameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeParameters"):
                opp_val = getattr(value, "typeParameters", None)
                setattr(value, "typeParameters", self)

class jdtmm_JDTParent(ABC):

    def __init__(self, flags: str, JDTParent: "jdtmm_JDTJavaElement" = None, parent: set["jdtmm_JDTJavaElement"] = None):
        self.flags = flags
        self.JDTParent = JDTParent
        self.parent = parent if parent is not None else set()
        
    @property
    def flags(self) -> str:
        return self.__flags

    @flags.setter
    def flags(self, flags: str):
        self.__flags = flags

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTParent__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTJavaElement"):
                    opp_val = getattr(item, "JDTJavaElement", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTJavaElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTJavaElement"):
                    opp_val = getattr(item, "JDTJavaElement", None)
                    
                    setattr(item, "JDTJavaElement", self)
                    

    @property
    def JDTParent(self):
        return self.__JDTParent

    @JDTParent.setter
    def JDTParent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTParent__JDTParent", None)
        self.__JDTParent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    def setFlag(self, value: str, flag: str):
        # TODO: Implement setFlag method
        pass

    def isFlagSet(self, flag: str) -> str:
        # TODO: Implement isFlagSet method
        pass

class JDTParent:

    pass
class JDTJavaElement:

    pass
class jdtmm_JDTTypeParameter(JDTJavaElement):

    pass
class jdtmm_JDTImportDeclaration(JDTJavaElement):

    pass
class jdtmm_JDTParentJavaElement(JDTJavaElement, JDTParent):

    pass
class JDTMember:

    pass
class jdtmm_JDTType(JDTMember):

    def __init__(self, class: str, interface: str, enum: str, abstract: str, final: str, static: str, superInterfaceNames: str, superClassName: str, JDTType: "jdtmm_JDTMethod" = None, jdtmm_JDTType9: "jdtmm_JDTMember" = None, jdtmm_JDTType: "jdtmm_JDTMethod" = None, types: "jdtmm_JDTCompilationUnit" = None, owner14: set["jdtmm_JDTMethod"] = None, owner17: set["jdtmm_JDTField"] = None, jdtmm_JDTType34: "jdtmm_JDTField" = None, JDTType22: "jdtmm_JDTType" = None, owner21: set["jdtmm_JDTType"] = None, JDTType26: "jdtmm_JDTType" = None, types25: "jdtmm_JDTType" = None, jdtmm_JDTType29: "jdtmm_JDTType" = None, jdtmm_JDTType27: set["jdtmm_JDTType"] = None, jdtmm_JDTType32: "jdtmm_JDTType" = None, jdtmm_JDTType30: "jdtmm_JDTType" = None, JDTType39: "jdtmm_JDTCompilationUnit" = None, JDTType36: "jdtmm_JDTField" = None, jdtmm_JDTType55: "jdtmm_JDTParameter" = None):
        self.class = class
        self.interface = interface
        self.enum = enum
        self.abstract = abstract
        self.final = final
        self.static = static
        self.superInterfaceNames = superInterfaceNames
        self.superClassName = superClassName
        self.JDTType = JDTType
        self.jdtmm_JDTType9 = jdtmm_JDTType9
        self.jdtmm_JDTType = jdtmm_JDTType
        self.types = types
        self.owner14 = owner14 if owner14 is not None else set()
        self.owner17 = owner17 if owner17 is not None else set()
        self.jdtmm_JDTType34 = jdtmm_JDTType34
        self.JDTType22 = JDTType22
        self.owner21 = owner21 if owner21 is not None else set()
        self.JDTType26 = JDTType26
        self.types25 = types25
        self.jdtmm_JDTType29 = jdtmm_JDTType29
        self.jdtmm_JDTType27 = jdtmm_JDTType27 if jdtmm_JDTType27 is not None else set()
        self.jdtmm_JDTType32 = jdtmm_JDTType32
        self.jdtmm_JDTType30 = jdtmm_JDTType30
        self.JDTType39 = JDTType39
        self.JDTType36 = JDTType36
        self.jdtmm_JDTType55 = jdtmm_JDTType55
        
    @property
    def interface(self) -> str:
        return self.__interface

    @interface.setter
    def interface(self, interface: str):
        self.__interface = interface

    @property
    def superInterfaceNames(self) -> str:
        return self.__superInterfaceNames

    @superInterfaceNames.setter
    def superInterfaceNames(self, superInterfaceNames: str):
        self.__superInterfaceNames = superInterfaceNames

    @property
    def abstract(self) -> str:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def superClassName(self) -> str:
        return self.__superClassName

    @superClassName.setter
    def superClassName(self, superClassName: str):
        self.__superClassName = superClassName

    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def enum(self) -> str:
        return self.__enum

    @enum.setter
    def enum(self, enum: str):
        self.__enum = enum

    @property
    def final(self) -> str:
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final

    @property
    def jdtmm_JDTType9(self):
        return self.__jdtmm_JDTType9

    @jdtmm_JDTType9.setter
    def jdtmm_JDTType9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__jdtmm_JDTType9", None)
        self.__jdtmm_JDTType9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jdtmm_JDTMember"):
                opp_val = getattr(old_value, "jdtmm_JDTMember", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jdtmm_JDTMember"):
                opp_val = getattr(value, "jdtmm_JDTMember", None)
                if opp_val is None:
                    setattr(value, "jdtmm_JDTMember", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jdtmm_JDTType55(self):
        return self.__jdtmm_JDTType55

    @jdtmm_JDTType55.setter
    def jdtmm_JDTType55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__jdtmm_JDTType55", None)
        self.__jdtmm_JDTType55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jdtmm_JDTParameter"):
                opp_val = getattr(old_value, "jdtmm_JDTParameter", None)
                if opp_val == self:
                    setattr(old_value, "jdtmm_JDTParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jdtmm_JDTParameter"):
                opp_val = getattr(value, "jdtmm_JDTParameter", None)
                setattr(value, "jdtmm_JDTParameter", self)

    @property
    def jdtmm_JDTType30(self):
        return self.__jdtmm_JDTType30

    @jdtmm_JDTType30.setter
    def jdtmm_JDTType30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__jdtmm_JDTType30", None)
        self.__jdtmm_JDTType30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jdtmm_JDTType32"):
                opp_val = getattr(old_value, "jdtmm_JDTType32", None)
                if opp_val == self:
                    setattr(old_value, "jdtmm_JDTType32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jdtmm_JDTType32"):
                opp_val = getattr(value, "jdtmm_JDTType32", None)
                setattr(value, "jdtmm_JDTType32", self)

    @property
    def owner17(self):
        return self.__owner17

    @owner17.setter
    def owner17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__owner17", None)
        self.__owner17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTField"):
                    opp_val = getattr(item, "JDTField", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTField", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTField"):
                    opp_val = getattr(item, "JDTField", None)
                    
                    setattr(item, "JDTField", self)
                    

    @property
    def JDTType22(self):
        return self.__JDTType22

    @JDTType22.setter
    def JDTType22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__JDTType22", None)
        self.__JDTType22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner21"):
                opp_val = getattr(old_value, "owner21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner21"):
                opp_val = getattr(value, "owner21", None)
                if opp_val is None:
                    setattr(value, "owner21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jdtmm_JDTType32(self):
        return self.__jdtmm_JDTType32

    @jdtmm_JDTType32.setter
    def jdtmm_JDTType32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__jdtmm_JDTType32", None)
        self.__jdtmm_JDTType32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jdtmm_JDTType30"):
                opp_val = getattr(old_value, "jdtmm_JDTType30", None)
                if opp_val == self:
                    setattr(old_value, "jdtmm_JDTType30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jdtmm_JDTType30"):
                opp_val = getattr(value, "jdtmm_JDTType30", None)
                setattr(value, "jdtmm_JDTType30", self)

    @property
    def JDTType(self):
        return self.__JDTType

    @JDTType.setter
    def JDTType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__JDTType", None)
        self.__JDTType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methods"):
                opp_val = getattr(old_value, "methods", None)
                if opp_val == self:
                    setattr(old_value, "methods", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methods"):
                opp_val = getattr(value, "methods", None)
                setattr(value, "methods", self)

    @property
    def JDTType26(self):
        return self.__JDTType26

    @JDTType26.setter
    def JDTType26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__JDTType26", None)
        self.__JDTType26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types25"):
                opp_val = getattr(old_value, "types25", None)
                if opp_val == self:
                    setattr(old_value, "types25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types25"):
                opp_val = getattr(value, "types25", None)
                setattr(value, "types25", self)

    @property
    def jdtmm_JDTType27(self):
        return self.__jdtmm_JDTType27

    @jdtmm_JDTType27.setter
    def jdtmm_JDTType27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__jdtmm_JDTType27", None)
        self.__jdtmm_JDTType27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jdtmm_JDTType29"):
                    opp_val = getattr(item, "jdtmm_JDTType29", None)
                    
                    if opp_val == self:
                        setattr(item, "jdtmm_JDTType29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jdtmm_JDTType29"):
                    opp_val = getattr(item, "jdtmm_JDTType29", None)
                    
                    setattr(item, "jdtmm_JDTType29", self)
                    

    @property
    def jdtmm_JDTType(self):
        return self.__jdtmm_JDTType

    @jdtmm_JDTType.setter
    def jdtmm_JDTType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__jdtmm_JDTType", None)
        self.__jdtmm_JDTType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jdtmm_JDTMethod"):
                opp_val = getattr(old_value, "jdtmm_JDTMethod", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jdtmm_JDTMethod"):
                opp_val = getattr(value, "jdtmm_JDTMethod", None)
                if opp_val is None:
                    setattr(value, "jdtmm_JDTMethod", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTType36(self):
        return self.__JDTType36

    @JDTType36.setter
    def JDTType36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__JDTType36", None)
        self.__JDTType36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fields"):
                opp_val = getattr(old_value, "fields", None)
                if opp_val == self:
                    setattr(old_value, "fields", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fields"):
                opp_val = getattr(value, "fields", None)
                setattr(value, "fields", self)

    @property
    def JDTType39(self):
        return self.__JDTType39

    @JDTType39.setter
    def JDTType39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__JDTType39", None)
        self.__JDTType39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compilationUnit"):
                opp_val = getattr(old_value, "compilationUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compilationUnit"):
                opp_val = getattr(value, "compilationUnit", None)
                if opp_val is None:
                    setattr(value, "compilationUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types25(self):
        return self.__types25

    @types25.setter
    def types25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__types25", None)
        self.__types25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTType26"):
                opp_val = getattr(old_value, "JDTType26", None)
                if opp_val == self:
                    setattr(old_value, "JDTType26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTType26"):
                opp_val = getattr(value, "JDTType26", None)
                setattr(value, "JDTType26", self)

    @property
    def types(self):
        return self.__types

    @types.setter
    def types(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__types", None)
        self.__types = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTCompilationUnit"):
                opp_val = getattr(old_value, "JDTCompilationUnit", None)
                if opp_val == self:
                    setattr(old_value, "JDTCompilationUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTCompilationUnit"):
                opp_val = getattr(value, "JDTCompilationUnit", None)
                setattr(value, "JDTCompilationUnit", self)

    @property
    def jdtmm_JDTType29(self):
        return self.__jdtmm_JDTType29

    @jdtmm_JDTType29.setter
    def jdtmm_JDTType29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__jdtmm_JDTType29", None)
        self.__jdtmm_JDTType29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jdtmm_JDTType27"):
                opp_val = getattr(old_value, "jdtmm_JDTType27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jdtmm_JDTType27"):
                opp_val = getattr(value, "jdtmm_JDTType27", None)
                if opp_val is None:
                    setattr(value, "jdtmm_JDTType27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owner21(self):
        return self.__owner21

    @owner21.setter
    def owner21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__owner21", None)
        self.__owner21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTType22"):
                    opp_val = getattr(item, "JDTType22", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTType22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTType22"):
                    opp_val = getattr(item, "JDTType22", None)
                    
                    setattr(item, "JDTType22", self)
                    

    @property
    def jdtmm_JDTType34(self):
        return self.__jdtmm_JDTType34

    @jdtmm_JDTType34.setter
    def jdtmm_JDTType34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__jdtmm_JDTType34", None)
        self.__jdtmm_JDTType34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jdtmm_JDTField"):
                opp_val = getattr(old_value, "jdtmm_JDTField", None)
                if opp_val == self:
                    setattr(old_value, "jdtmm_JDTField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jdtmm_JDTField"):
                opp_val = getattr(value, "jdtmm_JDTField", None)
                setattr(value, "jdtmm_JDTField", self)

    @property
    def owner14(self):
        return self.__owner14

    @owner14.setter
    def owner14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTType__owner14", None)
        self.__owner14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTMethod15"):
                    opp_val = getattr(item, "JDTMethod15", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTMethod15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTMethod15"):
                    opp_val = getattr(item, "JDTMethod15", None)
                    
                    setattr(item, "JDTMethod15", self)
                    

class jdtmm_JDTField(JDTMember):

    def __init__(self, abstract: str, final: str, static: str, isMultiValued: str, value: str, generateGetter: str, generateSetter: str, JDTField: "jdtmm_JDTType" = None, jdtmm_JDTField: "jdtmm_JDTType" = None, fields: "jdtmm_JDTType" = None):
        self.abstract = abstract
        self.final = final
        self.static = static
        self.isMultiValued = isMultiValued
        self.value = value
        self.generateGetter = generateGetter
        self.generateSetter = generateSetter
        self.JDTField = JDTField
        self.jdtmm_JDTField = jdtmm_JDTField
        self.fields = fields
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def isMultiValued(self) -> str:
        return self.__isMultiValued

    @isMultiValued.setter
    def isMultiValued(self, isMultiValued: str):
        self.__isMultiValued = isMultiValued

    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def abstract(self) -> str:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract

    @property
    def generateSetter(self) -> str:
        return self.__generateSetter

    @generateSetter.setter
    def generateSetter(self, generateSetter: str):
        self.__generateSetter = generateSetter

    @property
    def final(self) -> str:
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final

    @property
    def generateGetter(self) -> str:
        return self.__generateGetter

    @generateGetter.setter
    def generateGetter(self, generateGetter: str):
        self.__generateGetter = generateGetter

    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTField__fields", None)
        self.__fields = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTType36"):
                opp_val = getattr(old_value, "JDTType36", None)
                if opp_val == self:
                    setattr(old_value, "JDTType36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTType36"):
                opp_val = getattr(value, "JDTType36", None)
                setattr(value, "JDTType36", self)

    @property
    def jdtmm_JDTField(self):
        return self.__jdtmm_JDTField

    @jdtmm_JDTField.setter
    def jdtmm_JDTField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTField__jdtmm_JDTField", None)
        self.__jdtmm_JDTField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jdtmm_JDTType34"):
                opp_val = getattr(old_value, "jdtmm_JDTType34", None)
                if opp_val == self:
                    setattr(old_value, "jdtmm_JDTType34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jdtmm_JDTType34"):
                opp_val = getattr(value, "jdtmm_JDTType34", None)
                setattr(value, "jdtmm_JDTType34", self)

    @property
    def JDTField(self):
        return self.__JDTField

    @JDTField.setter
    def JDTField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTField__JDTField", None)
        self.__JDTField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner17"):
                opp_val = getattr(old_value, "owner17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner17"):
                opp_val = getattr(value, "owner17", None)
                if opp_val is None:
                    setattr(value, "owner17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jdtmm_JDTMethod(JDTMember):

    def __init__(self, abstract: str, final: str, static: str, synchronized: str, constructor: str, methods: "jdtmm_JDTType" = None, returnOwner: "jdtmm_JDTParameter" = None, parameterOwner: set["jdtmm_JDTParameter"] = None, JDTMethod: "jdtmm_JDTMethodBody" = None, jdtmm_JDTMethod: set["jdtmm_JDTType"] = None, owner: set["jdtmm_JDTMethodBody"] = None, JDTMethod15: "jdtmm_JDTType" = None, JDTMethod53: "jdtmm_JDTParameter" = None, JDTMethod57: "jdtmm_JDTParameter" = None):
        self.abstract = abstract
        self.final = final
        self.static = static
        self.synchronized = synchronized
        self.constructor = constructor
        self.methods = methods
        self.returnOwner = returnOwner
        self.parameterOwner = parameterOwner if parameterOwner is not None else set()
        self.JDTMethod = JDTMethod
        self.jdtmm_JDTMethod = jdtmm_JDTMethod if jdtmm_JDTMethod is not None else set()
        self.owner = owner if owner is not None else set()
        self.JDTMethod15 = JDTMethod15
        self.JDTMethod53 = JDTMethod53
        self.JDTMethod57 = JDTMethod57
        
    @property
    def constructor(self) -> str:
        return self.__constructor

    @constructor.setter
    def constructor(self, constructor: str):
        self.__constructor = constructor

    @property
    def final(self) -> str:
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final

    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def abstract(self) -> str:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract

    @property
    def synchronized(self) -> str:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: str):
        self.__synchronized = synchronized

    @property
    def JDTMethod57(self):
        return self.__JDTMethod57

    @JDTMethod57.setter
    def JDTMethod57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTMethod__JDTMethod57", None)
        self.__JDTMethod57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "returnType"):
                opp_val = getattr(old_value, "returnType", None)
                if opp_val == self:
                    setattr(old_value, "returnType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "returnType"):
                opp_val = getattr(value, "returnType", None)
                setattr(value, "returnType", self)

    @property
    def JDTMethod(self):
        return self.__JDTMethod

    @JDTMethod.setter
    def JDTMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTMethod__JDTMethod", None)
        self.__JDTMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bodies"):
                opp_val = getattr(old_value, "bodies", None)
                if opp_val == self:
                    setattr(old_value, "bodies", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bodies"):
                opp_val = getattr(value, "bodies", None)
                setattr(value, "bodies", self)

    @property
    def JDTMethod53(self):
        return self.__JDTMethod53

    @JDTMethod53.setter
    def JDTMethod53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTMethod__JDTMethod53", None)
        self.__JDTMethod53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters"):
                opp_val = getattr(old_value, "parameters", None)
                if opp_val == self:
                    setattr(old_value, "parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters"):
                opp_val = getattr(value, "parameters", None)
                setattr(value, "parameters", self)

    @property
    def methods(self):
        return self.__methods

    @methods.setter
    def methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTMethod__methods", None)
        self.__methods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTType"):
                opp_val = getattr(old_value, "JDTType", None)
                if opp_val == self:
                    setattr(old_value, "JDTType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTType"):
                opp_val = getattr(value, "JDTType", None)
                setattr(value, "JDTType", self)

    @property
    def parameterOwner(self):
        return self.__parameterOwner

    @parameterOwner.setter
    def parameterOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTMethod__parameterOwner", None)
        self.__parameterOwner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTParameter4"):
                    opp_val = getattr(item, "JDTParameter4", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTParameter4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTParameter4"):
                    opp_val = getattr(item, "JDTParameter4", None)
                    
                    setattr(item, "JDTParameter4", self)
                    

    @property
    def jdtmm_JDTMethod(self):
        return self.__jdtmm_JDTMethod

    @jdtmm_JDTMethod.setter
    def jdtmm_JDTMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTMethod__jdtmm_JDTMethod", None)
        self.__jdtmm_JDTMethod = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jdtmm_JDTType"):
                    opp_val = getattr(item, "jdtmm_JDTType", None)
                    
                    if opp_val == self:
                        setattr(item, "jdtmm_JDTType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jdtmm_JDTType"):
                    opp_val = getattr(item, "jdtmm_JDTType", None)
                    
                    setattr(item, "jdtmm_JDTType", self)
                    

    @property
    def returnOwner(self):
        return self.__returnOwner

    @returnOwner.setter
    def returnOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTMethod__returnOwner", None)
        self.__returnOwner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTParameter"):
                opp_val = getattr(old_value, "JDTParameter", None)
                if opp_val == self:
                    setattr(old_value, "JDTParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTParameter"):
                opp_val = getattr(value, "JDTParameter", None)
                setattr(value, "JDTParameter", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTMethod__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JDTMethodBody"):
                    opp_val = getattr(item, "JDTMethodBody", None)
                    
                    if opp_val == self:
                        setattr(item, "JDTMethodBody", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JDTMethodBody"):
                    opp_val = getattr(item, "JDTMethodBody", None)
                    
                    setattr(item, "JDTMethodBody", self)
                    

    @property
    def JDTMethod15(self):
        return self.__JDTMethod15

    @JDTMethod15.setter
    def JDTMethod15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTMethod__JDTMethod15", None)
        self.__JDTMethod15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner14"):
                opp_val = getattr(old_value, "owner14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner14"):
                opp_val = getattr(value, "owner14", None)
                if opp_val is None:
                    setattr(value, "owner14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jdtmm_JDTMethodBody(ABC):

    def __init__(self, bodies: "jdtmm_JDTMethod" = None, JDTMethodBody: "jdtmm_JDTMethod" = None):
        self.bodies = bodies
        self.JDTMethodBody = JDTMethodBody
        
    @property
    def bodies(self):
        return self.__bodies

    @bodies.setter
    def bodies(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTMethodBody__bodies", None)
        self.__bodies = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTMethod"):
                opp_val = getattr(old_value, "JDTMethod", None)
                if opp_val == self:
                    setattr(old_value, "JDTMethod", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTMethod"):
                opp_val = getattr(value, "JDTMethod", None)
                setattr(value, "JDTMethod", self)

    @property
    def JDTMethodBody(self):
        return self.__JDTMethodBody

    @JDTMethodBody.setter
    def JDTMethodBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTMethodBody__JDTMethodBody", None)
        self.__JDTMethodBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def asText(self) -> str:
        # TODO: Implement asText method
        pass

class jdtmm_JDTParameter(JDTMember):

    def __init__(self, final: str, isMultiValued: str, JDTParameter: "jdtmm_JDTMethod" = None, JDTParameter4: "jdtmm_JDTMethod" = None, parameters: "jdtmm_JDTMethod" = None, jdtmm_JDTParameter: "jdtmm_JDTType" = None, returnType: "jdtmm_JDTMethod" = None):
        self.final = final
        self.isMultiValued = isMultiValued
        self.JDTParameter = JDTParameter
        self.JDTParameter4 = JDTParameter4
        self.parameters = parameters
        self.jdtmm_JDTParameter = jdtmm_JDTParameter
        self.returnType = returnType
        
    @property
    def isMultiValued(self) -> str:
        return self.__isMultiValued

    @isMultiValued.setter
    def isMultiValued(self, isMultiValued: str):
        self.__isMultiValued = isMultiValued

    @property
    def final(self) -> str:
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTParameter__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTMethod53"):
                opp_val = getattr(old_value, "JDTMethod53", None)
                if opp_val == self:
                    setattr(old_value, "JDTMethod53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTMethod53"):
                opp_val = getattr(value, "JDTMethod53", None)
                setattr(value, "JDTMethod53", self)

    @property
    def jdtmm_JDTParameter(self):
        return self.__jdtmm_JDTParameter

    @jdtmm_JDTParameter.setter
    def jdtmm_JDTParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTParameter__jdtmm_JDTParameter", None)
        self.__jdtmm_JDTParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jdtmm_JDTType55"):
                opp_val = getattr(old_value, "jdtmm_JDTType55", None)
                if opp_val == self:
                    setattr(old_value, "jdtmm_JDTType55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jdtmm_JDTType55"):
                opp_val = getattr(value, "jdtmm_JDTType55", None)
                setattr(value, "jdtmm_JDTType55", self)

    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTParameter__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JDTMethod57"):
                opp_val = getattr(old_value, "JDTMethod57", None)
                if opp_val == self:
                    setattr(old_value, "JDTMethod57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JDTMethod57"):
                opp_val = getattr(value, "JDTMethod57", None)
                setattr(value, "JDTMethod57", self)

    @property
    def JDTParameter4(self):
        return self.__JDTParameter4

    @JDTParameter4.setter
    def JDTParameter4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTParameter__JDTParameter4", None)
        self.__JDTParameter4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterOwner"):
                opp_val = getattr(old_value, "parameterOwner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterOwner"):
                opp_val = getattr(value, "parameterOwner", None)
                if opp_val is None:
                    setattr(value, "parameterOwner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JDTParameter(self):
        return self.__JDTParameter

    @JDTParameter.setter
    def JDTParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jdtmm_JDTParameter__JDTParameter", None)
        self.__JDTParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "returnOwner"):
                opp_val = getattr(old_value, "returnOwner", None)
                if opp_val == self:
                    setattr(old_value, "returnOwner", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "returnOwner"):
                opp_val = getattr(value, "returnOwner", None)
                setattr(value, "returnOwner", self)
