from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LoopStatementKind(Enum):
    FOREACH = "FOREACH"
    WHILE = "WHILE"
    DOWHILE = "DOWHILE"
    FOR = "FOR"
class GlobalFunctionKind(Enum):
    NORMAL = "NORMAL"
    UNITINITIALIZER = "UNITINITIALIZER"
    UNITFINALIZER = "UNITFINALIZER"
class JumpStatementKind(Enum):
    JUMP = "JUMP"
    RETURN = "RETURN"
    THROW = "THROW"
class Status(Enum):
    NORMAL = "NORMAL"
    LIBRARY = "LIBRARY"
    IMPLICIT = "IMPLICIT"
    FAILEDDEP = "FAILEDDEP"
class Visibilities(Enum):
    VISIBILITYSTRICTPROTECTED = "VISIBILITYSTRICTPROTECTED"
    VISIBILITYPUBLIC = "VISIBILITYPUBLIC"
    VISIBILITYPACKAGE = "VISIBILITYPACKAGE"
    VISIBILITYPROTECTED = "VISIBILITYPROTECTED"
    VISIBILITYPRIVAT = "VISIBILITYPRIVAT"


############################################
# Definition of Classes
############################################

class TypeParameterClass:

    pass
class TypeAlias:

    pass
class GlobalVariable:

    pass
class GlobalFunction:

    pass
class Delegate:

    pass
class Access:

    pass
class GASTClass:

    pass
class NamedModelElement:

    pass
class gast_core_Package(NamedModelElement):

    def __init__(self, linesOfComments: int, linesOfCode: int, qualifiedName: str, gast_core_Package: set["GASTClass"] = None, gast_core_Package53: set["GASTClass"] = None, gast_core_Package56: set["GASTClass"] = None, gast_core_Package59: set["GASTClass"] = None, gast_core_Package62: set["Access"] = None, surroundingPackage: set["Delegate"] = None, surroundingPackage65: set["GlobalFunction"] = None, surroundingPackage67: set["GlobalVariable"] = None, packages: "Root" = None, surroundingPackage71: set["GASTClass"] = None, subPackages: "Package" = None, gast_core_Package78: set["Package"] = None, surroundingPackage81: set["TypeAlias"] = None, surroundingPackage74: set["Package"] = None):
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.qualifiedName = qualifiedName
        self.gast_core_Package = gast_core_Package if gast_core_Package is not None else set()
        self.gast_core_Package53 = gast_core_Package53 if gast_core_Package53 is not None else set()
        self.gast_core_Package56 = gast_core_Package56 if gast_core_Package56 is not None else set()
        self.gast_core_Package59 = gast_core_Package59 if gast_core_Package59 is not None else set()
        self.gast_core_Package62 = gast_core_Package62 if gast_core_Package62 is not None else set()
        self.surroundingPackage = surroundingPackage if surroundingPackage is not None else set()
        self.surroundingPackage65 = surroundingPackage65 if surroundingPackage65 is not None else set()
        self.surroundingPackage67 = surroundingPackage67 if surroundingPackage67 is not None else set()
        self.packages = packages
        self.surroundingPackage71 = surroundingPackage71 if surroundingPackage71 is not None else set()
        self.subPackages = subPackages
        self.gast_core_Package78 = gast_core_Package78 if gast_core_Package78 is not None else set()
        self.surroundingPackage81 = surroundingPackage81 if surroundingPackage81 is not None else set()
        self.surroundingPackage74 = surroundingPackage74 if surroundingPackage74 is not None else set()
        
        pass
    @property
    def qualifiedName(self):
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName


    @property
    def linesOfComments(self):
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments


    @property
    def linesOfCode(self):
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode


    @property
    def gast_core_Package59(self):
        return self.__gast_core_Package59

    @gast_core_Package59.setter
    def gast_core_Package59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package59", None)
        self.__gast_core_Package59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass60"):
                    opp_val = getattr(item, "GASTClass60", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass60"):
                    opp_val = getattr(item, "GASTClass60", None)
                    
                    setattr(item, "GASTClass60", self)
                    

    @property
    def packages(self):
        return self.__packages

    @packages.setter
    def packages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__packages", None)
        self.__packages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root69"):
                opp_val = getattr(old_value, "Root69", None)
                if opp_val == self:
                    setattr(old_value, "Root69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root69"):
                opp_val = getattr(value, "Root69", None)
                setattr(value, "Root69", self)

    @property
    def surroundingPackage(self):
        return self.__surroundingPackage

    @surroundingPackage.setter
    def surroundingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage", None)
        self.__surroundingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Delegate"):
                    opp_val = getattr(item, "Delegate", None)
                    
                    if opp_val == self:
                        setattr(item, "Delegate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Delegate"):
                    opp_val = getattr(item, "Delegate", None)
                    
                    setattr(item, "Delegate", self)
                    

    @property
    def gast_core_Package56(self):
        return self.__gast_core_Package56

    @gast_core_Package56.setter
    def gast_core_Package56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package56", None)
        self.__gast_core_Package56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass57"):
                    opp_val = getattr(item, "GASTClass57", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass57"):
                    opp_val = getattr(item, "GASTClass57", None)
                    
                    setattr(item, "GASTClass57", self)
                    

    @property
    def gast_core_Package62(self):
        return self.__gast_core_Package62

    @gast_core_Package62.setter
    def gast_core_Package62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package62", None)
        self.__gast_core_Package62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Access"):
                    opp_val = getattr(item, "Access", None)
                    
                    if opp_val == self:
                        setattr(item, "Access", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access"):
                    opp_val = getattr(item, "Access", None)
                    
                    setattr(item, "Access", self)
                    

    @property
    def surroundingPackage71(self):
        return self.__surroundingPackage71

    @surroundingPackage71.setter
    def surroundingPackage71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage71", None)
        self.__surroundingPackage71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass72"):
                    opp_val = getattr(item, "GASTClass72", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass72"):
                    opp_val = getattr(item, "GASTClass72", None)
                    
                    setattr(item, "GASTClass72", self)
                    

    @property
    def surroundingPackage74(self):
        return self.__surroundingPackage74

    @surroundingPackage74.setter
    def surroundingPackage74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage74", None)
        self.__surroundingPackage74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    if opp_val == self:
                        setattr(item, "Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    setattr(item, "Package", self)
                    

    @property
    def surroundingPackage65(self):
        return self.__surroundingPackage65

    @surroundingPackage65.setter
    def surroundingPackage65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage65", None)
        self.__surroundingPackage65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalFunction"):
                    opp_val = getattr(item, "GlobalFunction", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction"):
                    opp_val = getattr(item, "GlobalFunction", None)
                    
                    setattr(item, "GlobalFunction", self)
                    

    @property
    def subPackages(self):
        return self.__subPackages

    @subPackages.setter
    def subPackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__subPackages", None)
        self.__subPackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package76"):
                opp_val = getattr(old_value, "Package76", None)
                if opp_val == self:
                    setattr(old_value, "Package76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package76"):
                opp_val = getattr(value, "Package76", None)
                setattr(value, "Package76", self)

    @property
    def surroundingPackage67(self):
        return self.__surroundingPackage67

    @surroundingPackage67.setter
    def surroundingPackage67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage67", None)
        self.__surroundingPackage67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalVariable"):
                    opp_val = getattr(item, "GlobalVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable"):
                    opp_val = getattr(item, "GlobalVariable", None)
                    
                    setattr(item, "GlobalVariable", self)
                    

    @property
    def gast_core_Package(self):
        return self.__gast_core_Package

    @gast_core_Package.setter
    def gast_core_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package", None)
        self.__gast_core_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass"):
                    opp_val = getattr(item, "GASTClass", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass"):
                    opp_val = getattr(item, "GASTClass", None)
                    
                    setattr(item, "GASTClass", self)
                    

    @property
    def gast_core_Package53(self):
        return self.__gast_core_Package53

    @gast_core_Package53.setter
    def gast_core_Package53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package53", None)
        self.__gast_core_Package53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass54"):
                    opp_val = getattr(item, "GASTClass54", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass54"):
                    opp_val = getattr(item, "GASTClass54", None)
                    
                    setattr(item, "GASTClass54", self)
                    

    @property
    def gast_core_Package78(self):
        return self.__gast_core_Package78

    @gast_core_Package78.setter
    def gast_core_Package78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package78", None)
        self.__gast_core_Package78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package79"):
                    opp_val = getattr(item, "Package79", None)
                    
                    if opp_val == self:
                        setattr(item, "Package79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package79"):
                    opp_val = getattr(item, "Package79", None)
                    
                    setattr(item, "Package79", self)
                    

    @property
    def surroundingPackage81(self):
        return self.__surroundingPackage81

    @surroundingPackage81.setter
    def surroundingPackage81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage81", None)
        self.__surroundingPackage81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeAlias"):
                    opp_val = getattr(item, "TypeAlias", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeAlias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeAlias"):
                    opp_val = getattr(item, "TypeAlias", None)
                    
                    setattr(item, "TypeAlias", self)
                    

class gast_core_Identifier(ABC):

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    def idHasToBeUnique(self, gast_context, gast_diagnostics) :
        # TODO: Implement idHasToBeUnique method
        pass

class CatchParameter:

    pass
class ModelAnnotation:

    pass
class Identifier:

    pass
class gast_core_ModelElement(Identifier):

    def __init__(self, status: str, sissyId: int, gast_core_ModelElement: set["ModelAnnotation"] = None):
        self.status = status
        self.sissyId = sissyId
        self.gast_core_ModelElement = gast_core_ModelElement if gast_core_ModelElement is not None else set()
        
        pass
    @property
    def sissyId(self):
        return self.__sissyId

    @sissyId.setter
    def sissyId(self, sissyId: int):
        self.__sissyId = sissyId


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def gast_core_ModelElement(self):
        return self.__gast_core_ModelElement

    @gast_core_ModelElement.setter
    def gast_core_ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_ModelElement__gast_core_ModelElement", None)
        self.__gast_core_ModelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelAnnotation"):
                    opp_val = getattr(item, "ModelAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelAnnotation"):
                    opp_val = getattr(item, "ModelAnnotation", None)
                    
                    setattr(item, "ModelAnnotation", self)
                    

class Directory:

    pass
class Root:

    pass
class ModelElement:

    pass
class gast_core_GenericEntity(ModelElement):

    pass
class gast_core_NamedModelElement(ModelElement):

    def __init__(self, simpleName: str, ModelElement112: "gast_core_Root" = None, ModelElement270: "gast_accesses_Access" = None, ModelElement: "gast_core_Root" = None):
        self.simpleName = simpleName
        
        pass
    @property
    def simpleName(self):
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName


class gast_core_Root(ModelElement):

    def __init__(self, linesOfComments: int, linesOfCode: int, gast_core_Root: set["Access"] = None, gast_core_Root86: set["GASTClass"] = None, gast_core_Root89: set["GASTClass"] = None, gast_core_Root92: set["GASTClass"] = None, gast_core_Root95: set["GASTClass"] = None, gast_core_Root100: set["GlobalVariable"] = None, root: set["Package"] = None, root105: set["Clone"] = None, gast_core_Root107: set["StructuralAbstraction"] = None, gast_core_Root109: set["GASTType"] = None, gast_core_Root111: set["ModelElement"] = None, root114: set["BasePath"] = None, gast_core_Root98: set["ModelElement"] = None, root116: set["GlobalFunction"] = None, ModelElement112: "gast_core_Root" = None, ModelElement270: "gast_accesses_Access" = None, ModelElement: "gast_core_Root" = None):
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.gast_core_Root = gast_core_Root if gast_core_Root is not None else set()
        self.gast_core_Root86 = gast_core_Root86 if gast_core_Root86 is not None else set()
        self.gast_core_Root89 = gast_core_Root89 if gast_core_Root89 is not None else set()
        self.gast_core_Root92 = gast_core_Root92 if gast_core_Root92 is not None else set()
        self.gast_core_Root95 = gast_core_Root95 if gast_core_Root95 is not None else set()
        self.gast_core_Root100 = gast_core_Root100 if gast_core_Root100 is not None else set()
        self.root = root if root is not None else set()
        self.root105 = root105 if root105 is not None else set()
        self.gast_core_Root107 = gast_core_Root107 if gast_core_Root107 is not None else set()
        self.gast_core_Root109 = gast_core_Root109 if gast_core_Root109 is not None else set()
        self.gast_core_Root111 = gast_core_Root111 if gast_core_Root111 is not None else set()
        self.root114 = root114 if root114 is not None else set()
        self.gast_core_Root98 = gast_core_Root98 if gast_core_Root98 is not None else set()
        self.root116 = root116 if root116 is not None else set()
        
        pass
    @property
    def linesOfCode(self):
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode


    @property
    def linesOfComments(self):
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments


    @property
    def gast_core_Root111(self):
        return self.__gast_core_Root111

    @gast_core_Root111.setter
    def gast_core_Root111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root111", None)
        self.__gast_core_Root111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElement112"):
                    opp_val = getattr(item, "ModelElement112", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElement112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElement112"):
                    opp_val = getattr(item, "ModelElement112", None)
                    
                    setattr(item, "ModelElement112", self)
                    

    @property
    def gast_core_Root100(self):
        return self.__gast_core_Root100

    @gast_core_Root100.setter
    def gast_core_Root100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root100", None)
        self.__gast_core_Root100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalVariable101"):
                    opp_val = getattr(item, "GlobalVariable101", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable101"):
                    opp_val = getattr(item, "GlobalVariable101", None)
                    
                    setattr(item, "GlobalVariable101", self)
                    

    @property
    def gast_core_Root98(self):
        return self.__gast_core_Root98

    @gast_core_Root98.setter
    def gast_core_Root98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root98", None)
        self.__gast_core_Root98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElement"):
                    opp_val = getattr(item, "ModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElement"):
                    opp_val = getattr(item, "ModelElement", None)
                    
                    setattr(item, "ModelElement", self)
                    

    @property
    def gast_core_Root109(self):
        return self.__gast_core_Root109

    @gast_core_Root109.setter
    def gast_core_Root109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root109", None)
        self.__gast_core_Root109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTType"):
                    opp_val = getattr(item, "GASTType", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTType"):
                    opp_val = getattr(item, "GASTType", None)
                    
                    setattr(item, "GASTType", self)
                    

    @property
    def gast_core_Root92(self):
        return self.__gast_core_Root92

    @gast_core_Root92.setter
    def gast_core_Root92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root92", None)
        self.__gast_core_Root92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass93"):
                    opp_val = getattr(item, "GASTClass93", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass93"):
                    opp_val = getattr(item, "GASTClass93", None)
                    
                    setattr(item, "GASTClass93", self)
                    

    @property
    def root105(self):
        return self.__root105

    @root105.setter
    def root105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__root105", None)
        self.__root105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Clone"):
                    opp_val = getattr(item, "Clone", None)
                    
                    if opp_val == self:
                        setattr(item, "Clone", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Clone"):
                    opp_val = getattr(item, "Clone", None)
                    
                    setattr(item, "Clone", self)
                    

    @property
    def gast_core_Root(self):
        return self.__gast_core_Root

    @gast_core_Root.setter
    def gast_core_Root(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root", None)
        self.__gast_core_Root = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Access84"):
                    opp_val = getattr(item, "Access84", None)
                    
                    if opp_val == self:
                        setattr(item, "Access84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access84"):
                    opp_val = getattr(item, "Access84", None)
                    
                    setattr(item, "Access84", self)
                    

    @property
    def gast_core_Root86(self):
        return self.__gast_core_Root86

    @gast_core_Root86.setter
    def gast_core_Root86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root86", None)
        self.__gast_core_Root86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass87"):
                    opp_val = getattr(item, "GASTClass87", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass87"):
                    opp_val = getattr(item, "GASTClass87", None)
                    
                    setattr(item, "GASTClass87", self)
                    

    @property
    def root116(self):
        return self.__root116

    @root116.setter
    def root116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__root116", None)
        self.__root116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalFunction117"):
                    opp_val = getattr(item, "GlobalFunction117", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction117"):
                    opp_val = getattr(item, "GlobalFunction117", None)
                    
                    setattr(item, "GlobalFunction117", self)
                    

    @property
    def gast_core_Root95(self):
        return self.__gast_core_Root95

    @gast_core_Root95.setter
    def gast_core_Root95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root95", None)
        self.__gast_core_Root95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass96"):
                    opp_val = getattr(item, "GASTClass96", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass96"):
                    opp_val = getattr(item, "GASTClass96", None)
                    
                    setattr(item, "GASTClass96", self)
                    

    @property
    def gast_core_Root89(self):
        return self.__gast_core_Root89

    @gast_core_Root89.setter
    def gast_core_Root89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root89", None)
        self.__gast_core_Root89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass90"):
                    opp_val = getattr(item, "GASTClass90", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass90"):
                    opp_val = getattr(item, "GASTClass90", None)
                    
                    setattr(item, "GASTClass90", self)
                    

    @property
    def root114(self):
        return self.__root114

    @root114.setter
    def root114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__root114", None)
        self.__root114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasePath"):
                    opp_val = getattr(item, "BasePath", None)
                    
                    if opp_val == self:
                        setattr(item, "BasePath", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasePath"):
                    opp_val = getattr(item, "BasePath", None)
                    
                    setattr(item, "BasePath", self)
                    

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__root", None)
        self.__root = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package103"):
                    opp_val = getattr(item, "Package103", None)
                    
                    if opp_val == self:
                        setattr(item, "Package103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package103"):
                    opp_val = getattr(item, "Package103", None)
                    
                    setattr(item, "Package103", self)
                    

    @property
    def gast_core_Root107(self):
        return self.__gast_core_Root107

    @gast_core_Root107.setter
    def gast_core_Root107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root107", None)
        self.__gast_core_Root107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StructuralAbstraction"):
                    opp_val = getattr(item, "StructuralAbstraction", None)
                    
                    if opp_val == self:
                        setattr(item, "StructuralAbstraction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StructuralAbstraction"):
                    opp_val = getattr(item, "StructuralAbstraction", None)
                    
                    setattr(item, "StructuralAbstraction", self)
                    

    def getPackageByName(self, gast_name) :
        # TODO: Implement getPackageByName method
        pass

    def getPackageByQualifiedName(self, gast_qualifiedName) :
        # TODO: Implement getPackageByQualifiedName method
        pass

class gast_core_BasePath(ModelElement):

    def __init__(self, path: str, basePaths: "Root" = None, basePath: set["Directory"] = None, ModelElement112: "gast_core_Root" = None, ModelElement270: "gast_accesses_Access" = None, ModelElement: "gast_core_Root" = None):
        self.path = path
        self.basePaths = basePaths
        self.basePath = basePath if basePath is not None else set()
        
        pass
    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path


    @property
    def basePaths(self):
        return self.__basePaths

    @basePaths.setter
    def basePaths(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_BasePath__basePaths", None)
        self.__basePaths = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root"):
                opp_val = getattr(old_value, "Root", None)
                if opp_val == self:
                    setattr(old_value, "Root", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root"):
                opp_val = getattr(value, "Root", None)
                setattr(value, "Root", self)

    @property
    def basePath(self):
        return self.__basePath

    @basePath.setter
    def basePath(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_BasePath__basePath", None)
        self.__basePath = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Directory"):
                    opp_val = getattr(item, "Directory", None)
                    
                    if opp_val == self:
                        setattr(item, "Directory", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Directory"):
                    opp_val = getattr(item, "Directory", None)
                    
                    setattr(item, "Directory", self)
                    

class gast_statements_Exit:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Exit:

    pass
class gast_statements_GASTBehaviour:

    pass
class BranchStatement:

    pass
class GASTExpression:

    pass
class Function:

    pass
class LoopStatement:

    pass
class Branch:

    pass
class CloneInstance:

    pass
class BaseAccess:

    pass
class variables_Field:

    pass
class variables_Variable:

    pass
class FormalParameter:

    pass
class ThrowTypeAccess:

    pass
class LocalVariable:

    pass
class DeclarationTypeAccess:

    pass
class functions_Constructor:

    pass
class functions_Method:

    pass
class gast_functions_GlobalFunction(Function):

    def __init__(self, kind: str, globalFunctions: "Package" = None, globalFunctions287: "Root" = None, Function223: "gast_types_GASTClass" = None, Function311: "gast_variables_FormalParameter" = None, Function202: "gast_types_GASTClass" = None, Function263: "gast_accesses_FunctionAccess" = None, Function255: "gast_accesses_DelegateAccess" = None, Function: "gast_statements_BlockStatement" = None, Function275: "gast_functions_Delegate" = None, Function248: "gast_accesses_BaseAccess" = None, Function319: "gast_variables_LocalVariable" = None, Function252: "gast_accesses_DeclarationTypeAccess" = None):
        self.kind = kind
        self.globalFunctions = globalFunctions
        self.globalFunctions287 = globalFunctions287
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def globalFunctions(self):
        return self.__globalFunctions

    @globalFunctions.setter
    def globalFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_GlobalFunction__globalFunctions", None)
        self.__globalFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package285"):
                opp_val = getattr(old_value, "Package285", None)
                if opp_val == self:
                    setattr(old_value, "Package285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package285"):
                opp_val = getattr(value, "Package285", None)
                setattr(value, "Package285", self)

    @property
    def globalFunctions287(self):
        return self.__globalFunctions287

    @globalFunctions287.setter
    def globalFunctions287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_GlobalFunction__globalFunctions287", None)
        self.__globalFunctions287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root288"):
                opp_val = getattr(old_value, "Root288", None)
                if opp_val == self:
                    setattr(old_value, "Root288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root288"):
                opp_val = getattr(value, "Root288", None)
                setattr(value, "Root288", self)

class functions_GlobalFunction:

    pass
class gast_accesses_Access(BaseAccess):

    pass
class functions_Function:

    pass
class gast_accesses_FunctionAccess(Access):

    pass
class VariableAccess:

    pass
class gast_accesses_PropertyAccess(VariableAccess):

    pass
class gast_accesses_SelfAccess(VariableAccess):

    def __init__(self, super: bool):
        self.super = super
        
        pass
    @property
    def super(self):
        return self.__super

    @super.setter
    def super(self, super: bool):
        self.__super = super


class gast_accesses_VariableAccess(Access):

    def __init__(self, write: bool, gast_accesses_VariableAccess: "Variable" = None, Access: "gast_core_Package" = None, Access228: "gast_types_GASTClass" = None, Access303: "gast_functions_Function" = None, Access84: "gast_core_Root" = None):
        self.write = write
        self.gast_accesses_VariableAccess = gast_accesses_VariableAccess
        
        pass
    @property
    def write(self):
        return self.__write

    @write.setter
    def write(self, write: bool):
        self.__write = write


    @property
    def gast_accesses_VariableAccess(self):
        return self.__gast_accesses_VariableAccess

    @gast_accesses_VariableAccess.setter
    def gast_accesses_VariableAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_accesses_VariableAccess__gast_accesses_VariableAccess", None)
        self.__gast_accesses_VariableAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable265"):
                opp_val = getattr(old_value, "Variable265", None)
                if opp_val == self:
                    setattr(old_value, "Variable265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable265"):
                opp_val = getattr(value, "Variable265", None)
                setattr(value, "Variable265", self)

class FunctionAccess:

    pass
class gast_accesses_DelegateAccess(FunctionAccess):

    pass
class Variable:

    pass
class gast_variables_CatchParameter(Variable):

    def __init__(self, rethrown: bool, Variable: "gast_accesses_DeclarationTypeAccess" = None, Variable265: "gast_accesses_VariableAccess" = None):
        self.rethrown = rethrown
        
        pass
    @property
    def rethrown(self):
        return self.__rethrown

    @rethrown.setter
    def rethrown(self, rethrown: bool):
        self.__rethrown = rethrown


class gast_variables_LocalVariable(Variable):

    pass
class gast_variables_GlobalVariable(Variable):

    pass
class gast_variables_FormalParameter(Variable):

    def __init__(self, passedByReference: bool, formalParameters: "Function" = None, Variable: "gast_accesses_DeclarationTypeAccess" = None, Variable265: "gast_accesses_VariableAccess" = None):
        self.passedByReference = passedByReference
        self.formalParameters = formalParameters
        
        pass
    @property
    def passedByReference(self):
        return self.__passedByReference

    @passedByReference.setter
    def passedByReference(self, passedByReference: bool):
        self.__passedByReference = passedByReference


    @property
    def formalParameters(self):
        return self.__formalParameters

    @formalParameters.setter
    def formalParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_FormalParameter__formalParameters", None)
        self.__formalParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Function311"):
                opp_val = getattr(old_value, "Function311", None)
                if opp_val == self:
                    setattr(old_value, "Function311", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Function311"):
                opp_val = getattr(value, "Function311", None)
                setattr(value, "Function311", self)

class CompositeAccess:

    pass
class InheritanceTypeAccess:

    pass
class gast_accesses_CompositeAccess(BaseAccess):

    pass
class gast_accesses_TypeAccess(Access):

    pass
class TypeAccess:

    pass
class gast_accesses_CastTypeAccess(TypeAccess):

    pass
class gast_accesses_DeclarationTypeAccess(TypeAccess):

    pass
class gast_accesses_ThrowTypeAccess(TypeAccess):

    def __init__(self, declared: bool):
        self.declared = declared
        
        pass
    @property
    def declared(self):
        return self.__declared

    @declared.setter
    def declared(self, declared: bool):
        self.__declared = declared


class gast_accesses_RunTimeTypeAccess(TypeAccess):

    pass
class gast_accesses_StaticTypeAccess(TypeAccess):

    pass
class gast_accesses_InheritanceTypeAccess(TypeAccess):

    def __init__(self, implementationInheritance: bool):
        self.implementationInheritance = implementationInheritance
        
        pass
    @property
    def implementationInheritance(self):
        return self.__implementationInheritance

    @implementationInheritance.setter
    def implementationInheritance(self, implementationInheritance: bool):
        self.__implementationInheritance = implementationInheritance


class gast_accesses_ParameterInstantiationTypeAccess(TypeAccess):

    pass
class Property:

    pass
class Method:

    pass
class Field:

    pass
class Destructor:

    pass
class Constructor:

    pass
class types_GASTType:

    pass
class gast_types_GASTUnion(GASTClass):

    pass
class gast_types_GASTStruct(GASTClass):

    pass
class gast_types_GASTEnumeration(GASTClass):

    pass
class core_GenericEntity:

    pass
class gast_functions_GenericMethod(functions_Method, core_GenericEntity):

    pass
class gast_functions_GenericFunction(core_GenericEntity, functions_GlobalFunction):

    pass
class gast_functions_GenericConstructor(core_GenericEntity, functions_Constructor):

    pass
class gast_types_TypeParameterClass(GASTClass):

    pass
class Member:

    pass
class types_TypeDecorator:

    pass
class types_Member:

    pass
class gast_functions_Delegate(types_GASTType, functions_Function, types_Member):

    def __init__(self, innerDelegate: bool, gast_functions_Delegate: "GASTClass" = None, gast_functions_Delegate274: set["Function"] = None, innerDelegates: "GASTClass" = None, delegates: "Package" = None):
        self.innerDelegate = innerDelegate
        self.gast_functions_Delegate = gast_functions_Delegate
        self.gast_functions_Delegate274 = gast_functions_Delegate274 if gast_functions_Delegate274 is not None else set()
        self.innerDelegates = innerDelegates
        self.delegates = delegates
        
        pass
    @property
    def innerDelegate(self):
        return self.__innerDelegate

    @innerDelegate.setter
    def innerDelegate(self, innerDelegate: bool):
        self.__innerDelegate = innerDelegate


    @property
    def gast_functions_Delegate274(self):
        return self.__gast_functions_Delegate274

    @gast_functions_Delegate274.setter
    def gast_functions_Delegate274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__gast_functions_Delegate274", None)
        self.__gast_functions_Delegate274 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function275"):
                    opp_val = getattr(item, "Function275", None)
                    
                    if opp_val == self:
                        setattr(item, "Function275", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function275"):
                    opp_val = getattr(item, "Function275", None)
                    
                    setattr(item, "Function275", self)
                    

    @property
    def gast_functions_Delegate(self):
        return self.__gast_functions_Delegate

    @gast_functions_Delegate.setter
    def gast_functions_Delegate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__gast_functions_Delegate", None)
        self.__gast_functions_Delegate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass272"):
                opp_val = getattr(old_value, "GASTClass272", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass272"):
                opp_val = getattr(value, "GASTClass272", None)
                setattr(value, "GASTClass272", self)

    @property
    def delegates(self):
        return self.__delegates

    @delegates.setter
    def delegates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__delegates", None)
        self.__delegates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package279"):
                opp_val = getattr(old_value, "Package279", None)
                if opp_val == self:
                    setattr(old_value, "Package279", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package279"):
                opp_val = getattr(value, "Package279", None)
                setattr(value, "Package279", self)

    @property
    def innerDelegates(self):
        return self.__innerDelegates

    @innerDelegates.setter
    def innerDelegates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__innerDelegates", None)
        self.__innerDelegates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass277"):
                opp_val = getattr(old_value, "GASTClass277", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass277"):
                opp_val = getattr(value, "GASTClass277", None)
                setattr(value, "GASTClass277", self)

class gast_variables_Field(variables_Variable, types_Member):

    def __init__(self, propertyField: bool, fields: "GASTClass" = None):
        self.propertyField = propertyField
        self.fields = fields
        
        pass
    @property
    def propertyField(self):
        return self.__propertyField

    @propertyField.setter
    def propertyField(self, propertyField: bool):
        self.__propertyField = propertyField


    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_Field__fields", None)
        self.__fields = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass317"):
                opp_val = getattr(old_value, "GASTClass317", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass317", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass317"):
                opp_val = getattr(value, "GASTClass317", None)
                setattr(value, "GASTClass317", self)

class gast_functions_Constructor(functions_Function, types_Member):

    def __init__(self, initializer: bool, constructors: "GASTClass" = None):
        self.initializer = initializer
        self.constructors = constructors
        
        pass
    @property
    def initializer(self):
        return self.__initializer

    @initializer.setter
    def initializer(self, initializer: bool):
        self.__initializer = initializer


    @property
    def constructors(self):
        return self.__constructors

    @constructors.setter
    def constructors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Constructor__constructors", None)
        self.__constructors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass281"):
                opp_val = getattr(old_value, "GASTClass281", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass281"):
                opp_val = getattr(value, "GASTClass281", None)
                setattr(value, "GASTClass281", self)

class gast_types_GASTClass(types_GASTType, types_Member):

    def __init__(self, linesOfComments: int, local: bool, primitive: bool, interface: bool, anonymous: bool, inner: bool, surroundingClass: set["TypeAlias"] = None, surroundingClass194: set["Constructor"] = None, surroundingClass196: set["Destructor"] = None, surroundingClass198: set["Field"] = None, surroundingClass200: set["Method"] = None, localClasses: "Function" = None, classes: "Package" = None, gast_types_GASTClass: set["GASTClass"] = None, surroundingClass208: set["GASTClass"] = None, innerClasses: "GASTClass" = None, surroundingClass191: set["Delegate"] = None, gast_types_GASTClass215: "Field" = None, gastClass: set["GASTClass"] = None, friendClasses: "GASTClass" = None, gast_types_GASTClass213: set["InheritanceTypeAccess"] = None, gast_types_GASTClass222: set["Function"] = None, gast_types_GASTClass225: set["Property"] = None, gast_types_GASTClass227: set["Access"] = None, gast_types_GASTClass230: set["GASTClass"] = None):
        self.linesOfComments = linesOfComments
        self.local = local
        self.primitive = primitive
        self.interface = interface
        self.anonymous = anonymous
        self.inner = inner
        self.surroundingClass = surroundingClass if surroundingClass is not None else set()
        self.surroundingClass194 = surroundingClass194 if surroundingClass194 is not None else set()
        self.surroundingClass196 = surroundingClass196 if surroundingClass196 is not None else set()
        self.surroundingClass198 = surroundingClass198 if surroundingClass198 is not None else set()
        self.surroundingClass200 = surroundingClass200 if surroundingClass200 is not None else set()
        self.localClasses = localClasses
        self.classes = classes
        self.gast_types_GASTClass = gast_types_GASTClass if gast_types_GASTClass is not None else set()
        self.surroundingClass208 = surroundingClass208 if surroundingClass208 is not None else set()
        self.innerClasses = innerClasses
        self.surroundingClass191 = surroundingClass191 if surroundingClass191 is not None else set()
        self.gast_types_GASTClass215 = gast_types_GASTClass215
        self.gastClass = gastClass if gastClass is not None else set()
        self.friendClasses = friendClasses
        self.gast_types_GASTClass213 = gast_types_GASTClass213 if gast_types_GASTClass213 is not None else set()
        self.gast_types_GASTClass222 = gast_types_GASTClass222 if gast_types_GASTClass222 is not None else set()
        self.gast_types_GASTClass225 = gast_types_GASTClass225 if gast_types_GASTClass225 is not None else set()
        self.gast_types_GASTClass227 = gast_types_GASTClass227 if gast_types_GASTClass227 is not None else set()
        self.gast_types_GASTClass230 = gast_types_GASTClass230 if gast_types_GASTClass230 is not None else set()
        
        pass
    @property
    def inner(self):
        return self.__inner

    @inner.setter
    def inner(self, inner: bool):
        self.__inner = inner


    @property
    def linesOfComments(self):
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments


    @property
    def interface(self):
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface


    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, local: bool):
        self.__local = local


    @property
    def anonymous(self):
        return self.__anonymous

    @anonymous.setter
    def anonymous(self, anonymous: bool):
        self.__anonymous = anonymous


    @property
    def primitive(self):
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: bool):
        self.__primitive = primitive


    @property
    def surroundingClass194(self):
        return self.__surroundingClass194

    @surroundingClass194.setter
    def surroundingClass194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass194", None)
        self.__surroundingClass194 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constructor"):
                    opp_val = getattr(item, "Constructor", None)
                    
                    if opp_val == self:
                        setattr(item, "Constructor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constructor"):
                    opp_val = getattr(item, "Constructor", None)
                    
                    setattr(item, "Constructor", self)
                    

    @property
    def surroundingClass191(self):
        return self.__surroundingClass191

    @surroundingClass191.setter
    def surroundingClass191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass191", None)
        self.__surroundingClass191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Delegate192"):
                    opp_val = getattr(item, "Delegate192", None)
                    
                    if opp_val == self:
                        setattr(item, "Delegate192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Delegate192"):
                    opp_val = getattr(item, "Delegate192", None)
                    
                    setattr(item, "Delegate192", self)
                    

    @property
    def surroundingClass208(self):
        return self.__surroundingClass208

    @surroundingClass208.setter
    def surroundingClass208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass208", None)
        self.__surroundingClass208 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass209"):
                    opp_val = getattr(item, "GASTClass209", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass209", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass209"):
                    opp_val = getattr(item, "GASTClass209", None)
                    
                    setattr(item, "GASTClass209", self)
                    

    @property
    def innerClasses(self):
        return self.__innerClasses

    @innerClasses.setter
    def innerClasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__innerClasses", None)
        self.__innerClasses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass211"):
                opp_val = getattr(old_value, "GASTClass211", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass211"):
                opp_val = getattr(value, "GASTClass211", None)
                setattr(value, "GASTClass211", self)

    @property
    def gast_types_GASTClass215(self):
        return self.__gast_types_GASTClass215

    @gast_types_GASTClass215.setter
    def gast_types_GASTClass215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass215", None)
        self.__gast_types_GASTClass215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Field216"):
                opp_val = getattr(old_value, "Field216", None)
                if opp_val == self:
                    setattr(old_value, "Field216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Field216"):
                opp_val = getattr(value, "Field216", None)
                setattr(value, "Field216", self)

    @property
    def gast_types_GASTClass227(self):
        return self.__gast_types_GASTClass227

    @gast_types_GASTClass227.setter
    def gast_types_GASTClass227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass227", None)
        self.__gast_types_GASTClass227 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Access228"):
                    opp_val = getattr(item, "Access228", None)
                    
                    if opp_val == self:
                        setattr(item, "Access228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access228"):
                    opp_val = getattr(item, "Access228", None)
                    
                    setattr(item, "Access228", self)
                    

    @property
    def classes(self):
        return self.__classes

    @classes.setter
    def classes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__classes", None)
        self.__classes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package204"):
                opp_val = getattr(old_value, "Package204", None)
                if opp_val == self:
                    setattr(old_value, "Package204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package204"):
                opp_val = getattr(value, "Package204", None)
                setattr(value, "Package204", self)

    @property
    def gast_types_GASTClass(self):
        return self.__gast_types_GASTClass

    @gast_types_GASTClass.setter
    def gast_types_GASTClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass", None)
        self.__gast_types_GASTClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass206"):
                    opp_val = getattr(item, "GASTClass206", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass206", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass206"):
                    opp_val = getattr(item, "GASTClass206", None)
                    
                    setattr(item, "GASTClass206", self)
                    

    @property
    def gast_types_GASTClass225(self):
        return self.__gast_types_GASTClass225

    @gast_types_GASTClass225.setter
    def gast_types_GASTClass225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass225", None)
        self.__gast_types_GASTClass225 = value if value is not None else set()
        
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
                    

    @property
    def surroundingClass200(self):
        return self.__surroundingClass200

    @surroundingClass200.setter
    def surroundingClass200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass200", None)
        self.__surroundingClass200 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    if opp_val == self:
                        setattr(item, "Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    setattr(item, "Method", self)
                    

    @property
    def friendClasses(self):
        return self.__friendClasses

    @friendClasses.setter
    def friendClasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__friendClasses", None)
        self.__friendClasses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass220"):
                opp_val = getattr(old_value, "GASTClass220", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass220"):
                opp_val = getattr(value, "GASTClass220", None)
                setattr(value, "GASTClass220", self)

    @property
    def gast_types_GASTClass222(self):
        return self.__gast_types_GASTClass222

    @gast_types_GASTClass222.setter
    def gast_types_GASTClass222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass222", None)
        self.__gast_types_GASTClass222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function223"):
                    opp_val = getattr(item, "Function223", None)
                    
                    if opp_val == self:
                        setattr(item, "Function223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function223"):
                    opp_val = getattr(item, "Function223", None)
                    
                    setattr(item, "Function223", self)
                    

    @property
    def localClasses(self):
        return self.__localClasses

    @localClasses.setter
    def localClasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__localClasses", None)
        self.__localClasses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Function202"):
                opp_val = getattr(old_value, "Function202", None)
                if opp_val == self:
                    setattr(old_value, "Function202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Function202"):
                opp_val = getattr(value, "Function202", None)
                setattr(value, "Function202", self)

    @property
    def surroundingClass198(self):
        return self.__surroundingClass198

    @surroundingClass198.setter
    def surroundingClass198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass198", None)
        self.__surroundingClass198 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Field"):
                    opp_val = getattr(item, "Field", None)
                    
                    if opp_val == self:
                        setattr(item, "Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Field"):
                    opp_val = getattr(item, "Field", None)
                    
                    setattr(item, "Field", self)
                    

    @property
    def surroundingClass(self):
        return self.__surroundingClass

    @surroundingClass.setter
    def surroundingClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass", None)
        self.__surroundingClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeAlias189"):
                    opp_val = getattr(item, "TypeAlias189", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeAlias189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeAlias189"):
                    opp_val = getattr(item, "TypeAlias189", None)
                    
                    setattr(item, "TypeAlias189", self)
                    

    @property
    def gastClass(self):
        return self.__gastClass

    @gastClass.setter
    def gastClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gastClass", None)
        self.__gastClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass218"):
                    opp_val = getattr(item, "GASTClass218", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass218", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass218"):
                    opp_val = getattr(item, "GASTClass218", None)
                    
                    setattr(item, "GASTClass218", self)
                    

    @property
    def surroundingClass196(self):
        return self.__surroundingClass196

    @surroundingClass196.setter
    def surroundingClass196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass196", None)
        self.__surroundingClass196 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Destructor"):
                    opp_val = getattr(item, "Destructor", None)
                    
                    if opp_val == self:
                        setattr(item, "Destructor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Destructor"):
                    opp_val = getattr(item, "Destructor", None)
                    
                    setattr(item, "Destructor", self)
                    

    @property
    def gast_types_GASTClass213(self):
        return self.__gast_types_GASTClass213

    @gast_types_GASTClass213.setter
    def gast_types_GASTClass213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass213", None)
        self.__gast_types_GASTClass213 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InheritanceTypeAccess"):
                    opp_val = getattr(item, "InheritanceTypeAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "InheritanceTypeAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InheritanceTypeAccess"):
                    opp_val = getattr(item, "InheritanceTypeAccess", None)
                    
                    setattr(item, "InheritanceTypeAccess", self)
                    

    @property
    def gast_types_GASTClass230(self):
        return self.__gast_types_GASTClass230

    @gast_types_GASTClass230.setter
    def gast_types_GASTClass230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass230", None)
        self.__gast_types_GASTClass230 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass231"):
                    opp_val = getattr(item, "GASTClass231", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass231", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass231"):
                    opp_val = getattr(item, "GASTClass231", None)
                    
                    setattr(item, "GASTClass231", self)
                    

class gast_functions_Method(functions_Function, types_Member):

    def __init__(self, propertyMethod: bool, gast_functions_Method: "Property" = None, methods: "GASTClass" = None):
        self.propertyMethod = propertyMethod
        self.gast_functions_Method = gast_functions_Method
        self.methods = methods
        
        pass
    @property
    def propertyMethod(self):
        return self.__propertyMethod

    @propertyMethod.setter
    def propertyMethod(self, propertyMethod: bool):
        self.__propertyMethod = propertyMethod


    @property
    def gast_functions_Method(self):
        return self.__gast_functions_Method

    @gast_functions_Method.setter
    def gast_functions_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Method__gast_functions_Method", None)
        self.__gast_functions_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property290"):
                opp_val = getattr(old_value, "Property290", None)
                if opp_val == self:
                    setattr(old_value, "Property290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property290"):
                opp_val = getattr(value, "Property290", None)
                setattr(value, "Property290", self)

    @property
    def methods(self):
        return self.__methods

    @methods.setter
    def methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Method__methods", None)
        self.__methods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass292"):
                opp_val = getattr(old_value, "GASTClass292", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass292"):
                opp_val = getattr(value, "GASTClass292", None)
                setattr(value, "GASTClass292", self)

class gast_variables_Property(types_Member, variables_Field):

    pass
class gast_functions_Destructor(functions_Function, types_Member):

    pass
class gast_types_TypeAlias(types_TypeDecorator, types_Member):

    def __init__(self, innerTypeAlias: bool, gast_types_TypeAlias: "GASTType" = None, innerTypeAliases: "GASTClass" = None, typeAliases: "Package" = None):
        self.innerTypeAlias = innerTypeAlias
        self.gast_types_TypeAlias = gast_types_TypeAlias
        self.innerTypeAliases = innerTypeAliases
        self.typeAliases = typeAliases
        
        pass
    @property
    def innerTypeAlias(self):
        return self.__innerTypeAlias

    @innerTypeAlias.setter
    def innerTypeAlias(self, innerTypeAlias: bool):
        self.__innerTypeAlias = innerTypeAlias


    @property
    def gast_types_TypeAlias(self):
        return self.__gast_types_TypeAlias

    @gast_types_TypeAlias.setter
    def gast_types_TypeAlias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_TypeAlias__gast_types_TypeAlias", None)
        self.__gast_types_TypeAlias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTType180"):
                opp_val = getattr(old_value, "GASTType180", None)
                if opp_val == self:
                    setattr(old_value, "GASTType180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType180"):
                opp_val = getattr(value, "GASTType180", None)
                setattr(value, "GASTType180", self)

    @property
    def innerTypeAliases(self):
        return self.__innerTypeAliases

    @innerTypeAliases.setter
    def innerTypeAliases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_TypeAlias__innerTypeAliases", None)
        self.__innerTypeAliases = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass182"):
                opp_val = getattr(old_value, "GASTClass182", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass182"):
                opp_val = getattr(value, "GASTClass182", None)
                setattr(value, "GASTClass182", self)

    @property
    def typeAliases(self):
        return self.__typeAliases

    @typeAliases.setter
    def typeAliases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_TypeAlias__typeAliases", None)
        self.__typeAliases = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package184"):
                opp_val = getattr(old_value, "Package184", None)
                if opp_val == self:
                    setattr(old_value, "Package184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package184"):
                opp_val = getattr(value, "Package184", None)
                setattr(value, "Package184", self)

class gast_types_GASTType(NamedModelElement):

    def __init__(self, qualifiedName: str, referenceType: bool):
        self.qualifiedName = qualifiedName
        self.referenceType = referenceType
        
        pass
    @property
    def referenceType(self):
        return self.__referenceType

    @referenceType.setter
    def referenceType(self, referenceType: bool):
        self.__referenceType = referenceType


    @property
    def qualifiedName(self):
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName


class TypeDecorator:

    pass
class gast_types_GASTArray(TypeDecorator):

    def __init__(self, dimensions: int, gast_types_GASTArray: "GASTType" = None):
        self.dimensions = dimensions
        self.gast_types_GASTArray = gast_types_GASTArray
        
        pass
    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: int):
        self.__dimensions = dimensions


    @property
    def gast_types_GASTArray(self):
        return self.__gast_types_GASTArray

    @gast_types_GASTArray.setter
    def gast_types_GASTArray(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTArray__gast_types_GASTArray", None)
        self.__gast_types_GASTArray = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTType178"):
                opp_val = getattr(old_value, "GASTType178", None)
                if opp_val == self:
                    setattr(old_value, "GASTType178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType178"):
                opp_val = getattr(value, "GASTType178", None)
                setattr(value, "GASTType178", self)

class gast_types_Reference(TypeDecorator):

    def __init__(self, explicit: bool, gast_types_Reference: "GASTType" = None):
        self.explicit = explicit
        self.gast_types_Reference = gast_types_Reference
        
        pass
    @property
    def explicit(self):
        return self.__explicit

    @explicit.setter
    def explicit(self, explicit: bool):
        self.__explicit = explicit


    @property
    def gast_types_Reference(self):
        return self.__gast_types_Reference

    @gast_types_Reference.setter
    def gast_types_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_Reference__gast_types_Reference", None)
        self.__gast_types_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTType171"):
                opp_val = getattr(old_value, "GASTType171", None)
                if opp_val == self:
                    setattr(old_value, "GASTType171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType171"):
                opp_val = getattr(value, "GASTType171", None)
                setattr(value, "GASTType171", self)

class gast_annotations_ModelAnnotation(ABC):

    pass
class core_SourceEntity:

    pass
class core_NamedModelElement:

    pass
class gast_functions_Function(core_NamedModelElement, core_SourceEntity):

    def __init__(self, numberOfStatements: int, maximumNestingLevel: int, linesOfComments: int, linesOfCode: int, numberOfEdgesInCFG: int, numberOfNodesInCFG: int, operator: bool, function: "DeclarationTypeAccess" = None, surroundingFunction296: set["LocalVariable"] = None, gast_functions_Function: set["Statement"] = None, gast_functions_Function300: set["ThrowTypeAccess"] = None, gast_functions_Function302: set["Access"] = None, surroundingFunction305: "BlockStatement" = None, surroundingFunction308: set["GASTClass"] = None, surroundingFunction: set["FormalParameter"] = None):
        self.numberOfStatements = numberOfStatements
        self.maximumNestingLevel = maximumNestingLevel
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.numberOfEdgesInCFG = numberOfEdgesInCFG
        self.numberOfNodesInCFG = numberOfNodesInCFG
        self.operator = operator
        self.function = function
        self.surroundingFunction296 = surroundingFunction296 if surroundingFunction296 is not None else set()
        self.gast_functions_Function = gast_functions_Function if gast_functions_Function is not None else set()
        self.gast_functions_Function300 = gast_functions_Function300 if gast_functions_Function300 is not None else set()
        self.gast_functions_Function302 = gast_functions_Function302 if gast_functions_Function302 is not None else set()
        self.surroundingFunction305 = surroundingFunction305
        self.surroundingFunction308 = surroundingFunction308 if surroundingFunction308 is not None else set()
        self.surroundingFunction = surroundingFunction if surroundingFunction is not None else set()
        
        pass
    @property
    def linesOfComments(self):
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments


    @property
    def maximumNestingLevel(self):
        return self.__maximumNestingLevel

    @maximumNestingLevel.setter
    def maximumNestingLevel(self, maximumNestingLevel: int):
        self.__maximumNestingLevel = maximumNestingLevel


    @property
    def numberOfStatements(self):
        return self.__numberOfStatements

    @numberOfStatements.setter
    def numberOfStatements(self, numberOfStatements: int):
        self.__numberOfStatements = numberOfStatements


    @property
    def linesOfCode(self):
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode


    @property
    def numberOfNodesInCFG(self):
        return self.__numberOfNodesInCFG

    @numberOfNodesInCFG.setter
    def numberOfNodesInCFG(self, numberOfNodesInCFG: int):
        self.__numberOfNodesInCFG = numberOfNodesInCFG


    @property
    def numberOfEdgesInCFG(self):
        return self.__numberOfEdgesInCFG

    @numberOfEdgesInCFG.setter
    def numberOfEdgesInCFG(self, numberOfEdgesInCFG: int):
        self.__numberOfEdgesInCFG = numberOfEdgesInCFG


    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator


    @property
    def gast_functions_Function300(self):
        return self.__gast_functions_Function300

    @gast_functions_Function300.setter
    def gast_functions_Function300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__gast_functions_Function300", None)
        self.__gast_functions_Function300 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ThrowTypeAccess"):
                    opp_val = getattr(item, "ThrowTypeAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "ThrowTypeAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ThrowTypeAccess"):
                    opp_val = getattr(item, "ThrowTypeAccess", None)
                    
                    setattr(item, "ThrowTypeAccess", self)
                    

    @property
    def surroundingFunction308(self):
        return self.__surroundingFunction308

    @surroundingFunction308.setter
    def surroundingFunction308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__surroundingFunction308", None)
        self.__surroundingFunction308 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass309"):
                    opp_val = getattr(item, "GASTClass309", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass309", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass309"):
                    opp_val = getattr(item, "GASTClass309", None)
                    
                    setattr(item, "GASTClass309", self)
                    

    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__function", None)
        self.__function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DeclarationTypeAccess"):
                opp_val = getattr(old_value, "DeclarationTypeAccess", None)
                if opp_val == self:
                    setattr(old_value, "DeclarationTypeAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DeclarationTypeAccess"):
                opp_val = getattr(value, "DeclarationTypeAccess", None)
                setattr(value, "DeclarationTypeAccess", self)

    @property
    def gast_functions_Function302(self):
        return self.__gast_functions_Function302

    @gast_functions_Function302.setter
    def gast_functions_Function302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__gast_functions_Function302", None)
        self.__gast_functions_Function302 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Access303"):
                    opp_val = getattr(item, "Access303", None)
                    
                    if opp_val == self:
                        setattr(item, "Access303", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access303"):
                    opp_val = getattr(item, "Access303", None)
                    
                    setattr(item, "Access303", self)
                    

    @property
    def surroundingFunction305(self):
        return self.__surroundingFunction305

    @surroundingFunction305.setter
    def surroundingFunction305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__surroundingFunction305", None)
        self.__surroundingFunction305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BlockStatement306"):
                opp_val = getattr(old_value, "BlockStatement306", None)
                if opp_val == self:
                    setattr(old_value, "BlockStatement306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BlockStatement306"):
                opp_val = getattr(value, "BlockStatement306", None)
                setattr(value, "BlockStatement306", self)

    @property
    def surroundingFunction296(self):
        return self.__surroundingFunction296

    @surroundingFunction296.setter
    def surroundingFunction296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__surroundingFunction296", None)
        self.__surroundingFunction296 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LocalVariable"):
                    opp_val = getattr(item, "LocalVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "LocalVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LocalVariable"):
                    opp_val = getattr(item, "LocalVariable", None)
                    
                    setattr(item, "LocalVariable", self)
                    

    @property
    def gast_functions_Function(self):
        return self.__gast_functions_Function

    @gast_functions_Function.setter
    def gast_functions_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__gast_functions_Function", None)
        self.__gast_functions_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement298"):
                    opp_val = getattr(item, "Statement298", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement298", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement298"):
                    opp_val = getattr(item, "Statement298", None)
                    
                    setattr(item, "Statement298", self)
                    

    @property
    def surroundingFunction(self):
        return self.__surroundingFunction

    @surroundingFunction.setter
    def surroundingFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__surroundingFunction", None)
        self.__surroundingFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FormalParameter"):
                    opp_val = getattr(item, "FormalParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "FormalParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FormalParameter"):
                    opp_val = getattr(item, "FormalParameter", None)
                    
                    setattr(item, "FormalParameter", self)
                    

class gast_variables_Variable(core_NamedModelElement, core_SourceEntity):

    def __init__(self, const: bool, gast_variables_Variable: "GASTType" = None, surroundingVariable: "DeclarationTypeAccess" = None):
        self.const = const
        self.gast_variables_Variable = gast_variables_Variable
        self.surroundingVariable = surroundingVariable
        
        pass
    @property
    def const(self):
        return self.__const

    @const.setter
    def const(self, const: bool):
        self.__const = const


    @property
    def gast_variables_Variable(self):
        return self.__gast_variables_Variable

    @gast_variables_Variable.setter
    def gast_variables_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_Variable__gast_variables_Variable", None)
        self.__gast_variables_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTType313"):
                opp_val = getattr(old_value, "GASTType313", None)
                if opp_val == self:
                    setattr(old_value, "GASTType313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType313"):
                opp_val = getattr(value, "GASTType313", None)
                setattr(value, "GASTType313", self)

    @property
    def surroundingVariable(self):
        return self.__surroundingVariable

    @surroundingVariable.setter
    def surroundingVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_Variable__surroundingVariable", None)
        self.__surroundingVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DeclarationTypeAccess315"):
                opp_val = getattr(old_value, "DeclarationTypeAccess315", None)
                if opp_val == self:
                    setattr(old_value, "DeclarationTypeAccess315", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DeclarationTypeAccess315"):
                opp_val = getattr(value, "DeclarationTypeAccess315", None)
                setattr(value, "DeclarationTypeAccess315", self)

class core_ModelElement:

    pass
class annotations_ModelAnnotation:

    pass
class gast_annotations_CloneInstance(annotations_ModelAnnotation, core_ModelElement):

    pass
class gast_annotations_Clone(annotations_ModelAnnotation, core_ModelElement):

    pass
class gast_annotations_Comment(annotations_ModelAnnotation, core_SourceEntity):

    def __init__(self, todo: bool, formal: bool, todoCount: int, texts: str):
        self.todo = todo
        self.formal = formal
        self.todoCount = todoCount
        self.texts = texts
        
        pass
    @property
    def formal(self):
        return self.__formal

    @formal.setter
    def formal(self, formal: bool):
        self.__formal = formal


    @property
    def todo(self):
        return self.__todo

    @todo.setter
    def todo(self, todo: bool):
        self.__todo = todo


    @property
    def todoCount(self):
        return self.__todoCount

    @todoCount.setter
    def todoCount(self, todoCount: int):
        self.__todoCount = todoCount


    @property
    def texts(self):
        return self.__texts

    @texts.setter
    def texts(self, texts: str):
        self.__texts = texts


    def OCLtodo(self, gast_context, gast_diagnostics) :
        # TODO: Implement OCLtodo method
        pass

class gast_annotations_StructuralAbstraction(annotations_ModelAnnotation, core_NamedModelElement):

    pass
class types_GASTClass:

    pass
class gast_types_GenericClass(core_GenericEntity, types_GASTClass):

    pass
class gast_annotations_Attribute(annotations_ModelAnnotation, types_GASTClass):

    pass
class Position:

    pass
class gast_core_SourceEntity(ModelElement):

    pass
class gast_core_Position:

    def __init__(self, endColumn: int, endLine: int, startLine: int, startColumn: int, gast_core_Position: "File" = None, gast_core_Position156: "File" = None, position: "SourceEntity" = None):
        self.endColumn = endColumn
        self.endLine = endLine
        self.startLine = startLine
        self.startColumn = startColumn
        self.gast_core_Position = gast_core_Position
        self.gast_core_Position156 = gast_core_Position156
        self.position = position
        
        pass
    @property
    def endColumn(self):
        return self.__endColumn

    @endColumn.setter
    def endColumn(self, endColumn: int):
        self.__endColumn = endColumn


    @property
    def startColumn(self):
        return self.__startColumn

    @startColumn.setter
    def startColumn(self, startColumn: int):
        self.__startColumn = startColumn


    @property
    def endLine(self):
        return self.__endLine

    @endLine.setter
    def endLine(self, endLine: int):
        self.__endLine = endLine


    @property
    def startLine(self):
        return self.__startLine

    @startLine.setter
    def startLine(self, startLine: int):
        self.__startLine = startLine


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Position__position", None)
        self.__position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SourceEntity"):
                opp_val = getattr(old_value, "SourceEntity", None)
                if opp_val == self:
                    setattr(old_value, "SourceEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SourceEntity"):
                opp_val = getattr(value, "SourceEntity", None)
                setattr(value, "SourceEntity", self)

    @property
    def gast_core_Position156(self):
        return self.__gast_core_Position156

    @gast_core_Position156.setter
    def gast_core_Position156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Position__gast_core_Position156", None)
        self.__gast_core_Position156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "File157"):
                opp_val = getattr(old_value, "File157", None)
                if opp_val == self:
                    setattr(old_value, "File157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File157"):
                opp_val = getattr(value, "File157", None)
                setattr(value, "File157", self)

    @property
    def gast_core_Position(self):
        return self.__gast_core_Position

    @gast_core_Position.setter
    def gast_core_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Position__gast_core_Position", None)
        self.__gast_core_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "File154"):
                opp_val = getattr(old_value, "File154", None)
                if opp_val == self:
                    setattr(old_value, "File154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File154"):
                opp_val = getattr(value, "File154", None)
                setattr(value, "File154", self)

    def EitherAssemblyFileOrSourceFileSet(self, gast_context, gast_diagnostics) :
        # TODO: Implement EitherAssemblyFileOrSourceFileSet method
        pass

class gast_core_File(NamedModelElement):

    def __init__(self, sourceFile: bool, assemblyFile: bool, linesOfCode: int, size: str, fullQualifiedPath: str, fileSystemPath: str, gast_core_File134: set["GlobalVariable"] = None, gast_core_File137: set["GlobalFunction"] = None, gast_core_File140: set["GlobalFunction"] = None, gast_core_File143: set["GlobalVariable"] = None, gast_core_File146: set["Package"] = None, gast_core_File149: set["File"] = None, files: "Directory" = None, gast_core_File131: set["GASTType"] = None, gast_core_File: "Root" = None, gast_core_File128: set["GASTType"] = None):
        self.sourceFile = sourceFile
        self.assemblyFile = assemblyFile
        self.linesOfCode = linesOfCode
        self.size = size
        self.fullQualifiedPath = fullQualifiedPath
        self.fileSystemPath = fileSystemPath
        self.gast_core_File134 = gast_core_File134 if gast_core_File134 is not None else set()
        self.gast_core_File137 = gast_core_File137 if gast_core_File137 is not None else set()
        self.gast_core_File140 = gast_core_File140 if gast_core_File140 is not None else set()
        self.gast_core_File143 = gast_core_File143 if gast_core_File143 is not None else set()
        self.gast_core_File146 = gast_core_File146 if gast_core_File146 is not None else set()
        self.gast_core_File149 = gast_core_File149 if gast_core_File149 is not None else set()
        self.files = files
        self.gast_core_File131 = gast_core_File131 if gast_core_File131 is not None else set()
        self.gast_core_File = gast_core_File
        self.gast_core_File128 = gast_core_File128 if gast_core_File128 is not None else set()
        
        pass
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def fullQualifiedPath(self):
        return self.__fullQualifiedPath

    @fullQualifiedPath.setter
    def fullQualifiedPath(self, fullQualifiedPath: str):
        self.__fullQualifiedPath = fullQualifiedPath


    @property
    def linesOfCode(self):
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode


    @property
    def assemblyFile(self):
        return self.__assemblyFile

    @assemblyFile.setter
    def assemblyFile(self, assemblyFile: bool):
        self.__assemblyFile = assemblyFile


    @property
    def sourceFile(self):
        return self.__sourceFile

    @sourceFile.setter
    def sourceFile(self, sourceFile: bool):
        self.__sourceFile = sourceFile


    @property
    def fileSystemPath(self):
        return self.__fileSystemPath

    @fileSystemPath.setter
    def fileSystemPath(self, fileSystemPath: str):
        self.__fileSystemPath = fileSystemPath


    @property
    def gast_core_File(self):
        return self.__gast_core_File

    @gast_core_File.setter
    def gast_core_File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File", None)
        self.__gast_core_File = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root126"):
                opp_val = getattr(old_value, "Root126", None)
                if opp_val == self:
                    setattr(old_value, "Root126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root126"):
                opp_val = getattr(value, "Root126", None)
                setattr(value, "Root126", self)

    @property
    def gast_core_File146(self):
        return self.__gast_core_File146

    @gast_core_File146.setter
    def gast_core_File146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File146", None)
        self.__gast_core_File146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package147"):
                    opp_val = getattr(item, "Package147", None)
                    
                    if opp_val == self:
                        setattr(item, "Package147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package147"):
                    opp_val = getattr(item, "Package147", None)
                    
                    setattr(item, "Package147", self)
                    

    @property
    def files(self):
        return self.__files

    @files.setter
    def files(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__files", None)
        self.__files = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Directory152"):
                opp_val = getattr(old_value, "Directory152", None)
                if opp_val == self:
                    setattr(old_value, "Directory152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Directory152"):
                opp_val = getattr(value, "Directory152", None)
                setattr(value, "Directory152", self)

    @property
    def gast_core_File137(self):
        return self.__gast_core_File137

    @gast_core_File137.setter
    def gast_core_File137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File137", None)
        self.__gast_core_File137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalFunction138"):
                    opp_val = getattr(item, "GlobalFunction138", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction138"):
                    opp_val = getattr(item, "GlobalFunction138", None)
                    
                    setattr(item, "GlobalFunction138", self)
                    

    @property
    def gast_core_File134(self):
        return self.__gast_core_File134

    @gast_core_File134.setter
    def gast_core_File134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File134", None)
        self.__gast_core_File134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalVariable135"):
                    opp_val = getattr(item, "GlobalVariable135", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable135"):
                    opp_val = getattr(item, "GlobalVariable135", None)
                    
                    setattr(item, "GlobalVariable135", self)
                    

    @property
    def gast_core_File143(self):
        return self.__gast_core_File143

    @gast_core_File143.setter
    def gast_core_File143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File143", None)
        self.__gast_core_File143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalVariable144"):
                    opp_val = getattr(item, "GlobalVariable144", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable144"):
                    opp_val = getattr(item, "GlobalVariable144", None)
                    
                    setattr(item, "GlobalVariable144", self)
                    

    @property
    def gast_core_File128(self):
        return self.__gast_core_File128

    @gast_core_File128.setter
    def gast_core_File128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File128", None)
        self.__gast_core_File128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTType129"):
                    opp_val = getattr(item, "GASTType129", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTType129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTType129"):
                    opp_val = getattr(item, "GASTType129", None)
                    
                    setattr(item, "GASTType129", self)
                    

    @property
    def gast_core_File149(self):
        return self.__gast_core_File149

    @gast_core_File149.setter
    def gast_core_File149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File149", None)
        self.__gast_core_File149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "File150"):
                    opp_val = getattr(item, "File150", None)
                    
                    if opp_val == self:
                        setattr(item, "File150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "File150"):
                    opp_val = getattr(item, "File150", None)
                    
                    setattr(item, "File150", self)
                    

    @property
    def gast_core_File140(self):
        return self.__gast_core_File140

    @gast_core_File140.setter
    def gast_core_File140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File140", None)
        self.__gast_core_File140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalFunction141"):
                    opp_val = getattr(item, "GlobalFunction141", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction141", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction141"):
                    opp_val = getattr(item, "GlobalFunction141", None)
                    
                    setattr(item, "GlobalFunction141", self)
                    

    @property
    def gast_core_File131(self):
        return self.__gast_core_File131

    @gast_core_File131.setter
    def gast_core_File131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File131", None)
        self.__gast_core_File131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTType132"):
                    opp_val = getattr(item, "GASTType132", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTType132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTType132"):
                    opp_val = getattr(item, "GASTType132", None)
                    
                    setattr(item, "GASTType132", self)
                    

class File:

    pass
class gast_core_Directory(NamedModelElement):

    def __init__(self, fullQualifiedPath: str, fileSystemPath: str, parentDirectory: set["Directory"] = None, subDirectory: "Directory" = None, directory: set["File"] = None, directories: "BasePath" = None):
        self.fullQualifiedPath = fullQualifiedPath
        self.fileSystemPath = fileSystemPath
        self.parentDirectory = parentDirectory if parentDirectory is not None else set()
        self.subDirectory = subDirectory
        self.directory = directory if directory is not None else set()
        self.directories = directories
        
        pass
    @property
    def fileSystemPath(self):
        return self.__fileSystemPath

    @fileSystemPath.setter
    def fileSystemPath(self, fileSystemPath: str):
        self.__fileSystemPath = fileSystemPath


    @property
    def fullQualifiedPath(self):
        return self.__fullQualifiedPath

    @fullQualifiedPath.setter
    def fullQualifiedPath(self, fullQualifiedPath: str):
        self.__fullQualifiedPath = fullQualifiedPath


    @property
    def subDirectory(self):
        return self.__subDirectory

    @subDirectory.setter
    def subDirectory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__subDirectory", None)
        self.__subDirectory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Directory121"):
                opp_val = getattr(old_value, "Directory121", None)
                if opp_val == self:
                    setattr(old_value, "Directory121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Directory121"):
                opp_val = getattr(value, "Directory121", None)
                setattr(value, "Directory121", self)

    @property
    def parentDirectory(self):
        return self.__parentDirectory

    @parentDirectory.setter
    def parentDirectory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__parentDirectory", None)
        self.__parentDirectory = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Directory119"):
                    opp_val = getattr(item, "Directory119", None)
                    
                    if opp_val == self:
                        setattr(item, "Directory119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Directory119"):
                    opp_val = getattr(item, "Directory119", None)
                    
                    setattr(item, "Directory119", self)
                    

    @property
    def directories(self):
        return self.__directories

    @directories.setter
    def directories(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__directories", None)
        self.__directories = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasePath124"):
                opp_val = getattr(old_value, "BasePath124", None)
                if opp_val == self:
                    setattr(old_value, "BasePath124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasePath124"):
                opp_val = getattr(value, "BasePath124", None)
                setattr(value, "BasePath124", self)

    @property
    def directory(self):
        return self.__directory

    @directory.setter
    def directory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__directory", None)
        self.__directory = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "File"):
                    opp_val = getattr(item, "File", None)
                    
                    if opp_val == self:
                        setattr(item, "File", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "File"):
                    opp_val = getattr(item, "File", None)
                    
                    setattr(item, "File", self)
                    

class BasePath:

    pass
class GASTType:

    pass
class gast_types_TypeDecorator(GASTType):

    pass
class StructuralAbstraction:

    pass
class gast_annotations_Layer(StructuralAbstraction):

    pass
class gast_annotations_Subsystem(StructuralAbstraction):

    pass
class Clone:

    pass
class Package:

    pass
class gast_core_PackageAlias(Package):

    pass
class SourceEntity:

    pass
class gast_types_Member(SourceEntity):

    def __init__(self, visibility: str, abstract: bool, extern: bool, introspectable: bool, override: bool, static: bool, typeParameterClassMember: bool, virtual: bool, final: bool, internal: bool, gast_types_Member: "Member" = None, SourceEntity: "gast_core_Position" = None):
        self.visibility = visibility
        self.abstract = abstract
        self.extern = extern
        self.introspectable = introspectable
        self.override = override
        self.static = static
        self.typeParameterClassMember = typeParameterClassMember
        self.virtual = virtual
        self.final = final
        self.internal = internal
        self.gast_types_Member = gast_types_Member
        
        pass
    @property
    def virtual(self):
        return self.__virtual

    @virtual.setter
    def virtual(self, virtual: bool):
        self.__virtual = virtual


    @property
    def internal(self):
        return self.__internal

    @internal.setter
    def internal(self, internal: bool):
        self.__internal = internal


    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract


    @property
    def typeParameterClassMember(self):
        return self.__typeParameterClassMember

    @typeParameterClassMember.setter
    def typeParameterClassMember(self, typeParameterClassMember: bool):
        self.__typeParameterClassMember = typeParameterClassMember


    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final


    @property
    def override(self):
        return self.__override

    @override.setter
    def override(self, override: bool):
        self.__override = override


    @property
    def introspectable(self):
        return self.__introspectable

    @introspectable.setter
    def introspectable(self, introspectable: bool):
        self.__introspectable = introspectable


    @property
    def extern(self):
        return self.__extern

    @extern.setter
    def extern(self, extern: bool):
        self.__extern = extern


    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


    @property
    def gast_types_Member(self):
        return self.__gast_types_Member

    @gast_types_Member.setter
    def gast_types_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_Member__gast_types_Member", None)
        self.__gast_types_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Member"):
                opp_val = getattr(old_value, "Member", None)
                if opp_val == self:
                    setattr(old_value, "Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Member"):
                opp_val = getattr(value, "Member", None)
                setattr(value, "Member", self)

    def getSurroundingClass(self) :
        # TODO: Implement getSurroundingClass method
        pass

class gast_statements_Branch(SourceEntity):

    pass
class gast_accesses_BaseAccess(SourceEntity):

    pass
class gast_statements_GASTExpression(SourceEntity):

    pass
class gast_statements_Statement(SourceEntity):

    def __init__(self, numberOfComments: int, linesOfCode: int, numberOfEdgesInCFG: int, numberOfStatements: int, maximumNestingLevel: int, numberOfNodesInCFG: int, parentStatement: set["BaseAccess"] = None, statements: "CloneInstance" = None, statements9: "BlockStatement" = None, gast_statements_Statement: "Statement" = None, statement: "Branch" = None, body: "LoopStatement" = None, gast_statements_Statement15: set["Statement"] = None, gast_statements_Statement18: set["Statement"] = None, SourceEntity: "gast_core_Position" = None):
        self.numberOfComments = numberOfComments
        self.linesOfCode = linesOfCode
        self.numberOfEdgesInCFG = numberOfEdgesInCFG
        self.numberOfStatements = numberOfStatements
        self.maximumNestingLevel = maximumNestingLevel
        self.numberOfNodesInCFG = numberOfNodesInCFG
        self.parentStatement = parentStatement if parentStatement is not None else set()
        self.statements = statements
        self.statements9 = statements9
        self.gast_statements_Statement = gast_statements_Statement
        self.statement = statement
        self.body = body
        self.gast_statements_Statement15 = gast_statements_Statement15 if gast_statements_Statement15 is not None else set()
        self.gast_statements_Statement18 = gast_statements_Statement18 if gast_statements_Statement18 is not None else set()
        
        pass
    @property
    def numberOfComments(self):
        return self.__numberOfComments

    @numberOfComments.setter
    def numberOfComments(self, numberOfComments: int):
        self.__numberOfComments = numberOfComments


    @property
    def numberOfNodesInCFG(self):
        return self.__numberOfNodesInCFG

    @numberOfNodesInCFG.setter
    def numberOfNodesInCFG(self, numberOfNodesInCFG: int):
        self.__numberOfNodesInCFG = numberOfNodesInCFG


    @property
    def numberOfEdgesInCFG(self):
        return self.__numberOfEdgesInCFG

    @numberOfEdgesInCFG.setter
    def numberOfEdgesInCFG(self, numberOfEdgesInCFG: int):
        self.__numberOfEdgesInCFG = numberOfEdgesInCFG


    @property
    def maximumNestingLevel(self):
        return self.__maximumNestingLevel

    @maximumNestingLevel.setter
    def maximumNestingLevel(self, maximumNestingLevel: int):
        self.__maximumNestingLevel = maximumNestingLevel


    @property
    def numberOfStatements(self):
        return self.__numberOfStatements

    @numberOfStatements.setter
    def numberOfStatements(self, numberOfStatements: int):
        self.__numberOfStatements = numberOfStatements


    @property
    def linesOfCode(self):
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode


    @property
    def gast_statements_Statement18(self):
        return self.__gast_statements_Statement18

    @gast_statements_Statement18.setter
    def gast_statements_Statement18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__gast_statements_Statement18", None)
        self.__gast_statements_Statement18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement19"):
                    opp_val = getattr(item, "Statement19", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement19"):
                    opp_val = getattr(item, "Statement19", None)
                    
                    setattr(item, "Statement19", self)
                    

    @property
    def statement(self):
        return self.__statement

    @statement.setter
    def statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__statement", None)
        self.__statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Branch"):
                opp_val = getattr(old_value, "Branch", None)
                if opp_val == self:
                    setattr(old_value, "Branch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Branch"):
                opp_val = getattr(value, "Branch", None)
                setattr(value, "Branch", self)

    @property
    def statements9(self):
        return self.__statements9

    @statements9.setter
    def statements9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__statements9", None)
        self.__statements9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BlockStatement10"):
                opp_val = getattr(old_value, "BlockStatement10", None)
                if opp_val == self:
                    setattr(old_value, "BlockStatement10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BlockStatement10"):
                opp_val = getattr(value, "BlockStatement10", None)
                setattr(value, "BlockStatement10", self)

    @property
    def statements(self):
        return self.__statements

    @statements.setter
    def statements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__statements", None)
        self.__statements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CloneInstance"):
                opp_val = getattr(old_value, "CloneInstance", None)
                if opp_val == self:
                    setattr(old_value, "CloneInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CloneInstance"):
                opp_val = getattr(value, "CloneInstance", None)
                setattr(value, "CloneInstance", self)

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__body", None)
        self.__body = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LoopStatement"):
                opp_val = getattr(old_value, "LoopStatement", None)
                if opp_val == self:
                    setattr(old_value, "LoopStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LoopStatement"):
                opp_val = getattr(value, "LoopStatement", None)
                setattr(value, "LoopStatement", self)

    @property
    def gast_statements_Statement15(self):
        return self.__gast_statements_Statement15

    @gast_statements_Statement15.setter
    def gast_statements_Statement15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__gast_statements_Statement15", None)
        self.__gast_statements_Statement15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement16"):
                    opp_val = getattr(item, "Statement16", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement16"):
                    opp_val = getattr(item, "Statement16", None)
                    
                    setattr(item, "Statement16", self)
                    

    @property
    def gast_statements_Statement(self):
        return self.__gast_statements_Statement

    @gast_statements_Statement.setter
    def gast_statements_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__gast_statements_Statement", None)
        self.__gast_statements_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Statement"):
                opp_val = getattr(old_value, "Statement", None)
                if opp_val == self:
                    setattr(old_value, "Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Statement"):
                opp_val = getattr(value, "Statement", None)
                setattr(value, "Statement", self)

    @property
    def parentStatement(self):
        return self.__parentStatement

    @parentStatement.setter
    def parentStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__parentStatement", None)
        self.__parentStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BaseAccess"):
                    opp_val = getattr(item, "BaseAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "BaseAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BaseAccess"):
                    opp_val = getattr(item, "BaseAccess", None)
                    
                    setattr(item, "BaseAccess", self)
                    

class BlockStatement:

    pass
class gast_statements_Methods(BlockStatement):

    def __init__(self, methodName: str, gast_statements_Methods: "Exit" = None, BlockStatement: "gast_statements_ExceptionHandler" = None, BlockStatement10: "gast_statements_Statement" = None, BlockStatement306: "gast_functions_Function" = None, BlockStatement5: "gast_statements_ExceptionHandler" = None, BlockStatement46: "gast_statements_GASTBehaviour" = None):
        self.methodName = methodName
        self.gast_statements_Methods = gast_statements_Methods
        
        pass
    @property
    def methodName(self):
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName


    @property
    def gast_statements_Methods(self):
        return self.__gast_statements_Methods

    @gast_statements_Methods.setter
    def gast_statements_Methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Methods__gast_statements_Methods", None)
        self.__gast_statements_Methods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Exit"):
                opp_val = getattr(old_value, "Exit", None)
                if opp_val == self:
                    setattr(old_value, "Exit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Exit"):
                opp_val = getattr(value, "Exit", None)
                setattr(value, "Exit", self)

class gast_statements_CatchBlock(BlockStatement):

    pass
class CatchBlock:

    pass
class Statement:

    pass
class gast_statements_LoopStatement(Statement):

    def __init__(self, kind: str, gast_statements_LoopStatement: "GASTExpression" = None, gast_statements_LoopStatement33: "GASTExpression" = None, gast_statements_LoopStatement36: "GASTExpression" = None, loopstatement: "Statement" = None, Statement27: "gast_statements_Branch" = None, Statement298: "gast_functions_Function" = None, Statement: "gast_statements_Statement" = None, Statement16: "gast_statements_Statement" = None, Statement21: "gast_statements_BlockStatement" = None, Statement39: "gast_statements_LoopStatement" = None, Statement240: "gast_accesses_BaseAccess" = None, Statement167: "gast_annotations_CloneInstance" = None, Statement19: "gast_statements_Statement" = None, Statement242: "gast_accesses_BaseAccess" = None):
        self.kind = kind
        self.gast_statements_LoopStatement = gast_statements_LoopStatement
        self.gast_statements_LoopStatement33 = gast_statements_LoopStatement33
        self.gast_statements_LoopStatement36 = gast_statements_LoopStatement36
        self.loopstatement = loopstatement
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def loopstatement(self):
        return self.__loopstatement

    @loopstatement.setter
    def loopstatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__loopstatement", None)
        self.__loopstatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Statement39"):
                opp_val = getattr(old_value, "Statement39", None)
                if opp_val == self:
                    setattr(old_value, "Statement39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Statement39"):
                opp_val = getattr(value, "Statement39", None)
                setattr(value, "Statement39", self)

    @property
    def gast_statements_LoopStatement(self):
        return self.__gast_statements_LoopStatement

    @gast_statements_LoopStatement.setter
    def gast_statements_LoopStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__gast_statements_LoopStatement", None)
        self.__gast_statements_LoopStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTExpression31"):
                opp_val = getattr(old_value, "GASTExpression31", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression31"):
                opp_val = getattr(value, "GASTExpression31", None)
                setattr(value, "GASTExpression31", self)

    @property
    def gast_statements_LoopStatement36(self):
        return self.__gast_statements_LoopStatement36

    @gast_statements_LoopStatement36.setter
    def gast_statements_LoopStatement36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__gast_statements_LoopStatement36", None)
        self.__gast_statements_LoopStatement36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTExpression37"):
                opp_val = getattr(old_value, "GASTExpression37", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression37"):
                opp_val = getattr(value, "GASTExpression37", None)
                setattr(value, "GASTExpression37", self)

    @property
    def gast_statements_LoopStatement33(self):
        return self.__gast_statements_LoopStatement33

    @gast_statements_LoopStatement33.setter
    def gast_statements_LoopStatement33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__gast_statements_LoopStatement33", None)
        self.__gast_statements_LoopStatement33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTExpression34"):
                opp_val = getattr(old_value, "GASTExpression34", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression34"):
                opp_val = getattr(value, "GASTExpression34", None)
                setattr(value, "GASTExpression34", self)

class gast_statements_BranchStatement(Statement):

    pass
class gast_statements_JumpStatement(Statement):

    def __init__(self, kind: str, gast_statements_JumpStatement: "GASTExpression" = None, Statement27: "gast_statements_Branch" = None, Statement298: "gast_functions_Function" = None, Statement: "gast_statements_Statement" = None, Statement16: "gast_statements_Statement" = None, Statement21: "gast_statements_BlockStatement" = None, Statement39: "gast_statements_LoopStatement" = None, Statement240: "gast_accesses_BaseAccess" = None, Statement167: "gast_annotations_CloneInstance" = None, Statement19: "gast_statements_Statement" = None, Statement242: "gast_accesses_BaseAccess" = None):
        self.kind = kind
        self.gast_statements_JumpStatement = gast_statements_JumpStatement
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def gast_statements_JumpStatement(self):
        return self.__gast_statements_JumpStatement

    @gast_statements_JumpStatement.setter
    def gast_statements_JumpStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_JumpStatement__gast_statements_JumpStatement", None)
        self.__gast_statements_JumpStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTExpression42"):
                opp_val = getattr(old_value, "GASTExpression42", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression42"):
                opp_val = getattr(value, "GASTExpression42", None)
                setattr(value, "GASTExpression42", self)

class gast_statements_SimpleStatement(Statement):

    pass
class gast_statements_BlockStatement(Statement):

    def __init__(self, synchronized: bool, blockstatement: set["Statement"] = None, body23: "Function" = None, Statement27: "gast_statements_Branch" = None, Statement298: "gast_functions_Function" = None, Statement: "gast_statements_Statement" = None, Statement16: "gast_statements_Statement" = None, Statement21: "gast_statements_BlockStatement" = None, Statement39: "gast_statements_LoopStatement" = None, Statement240: "gast_accesses_BaseAccess" = None, Statement167: "gast_annotations_CloneInstance" = None, Statement19: "gast_statements_Statement" = None, Statement242: "gast_accesses_BaseAccess" = None):
        self.synchronized = synchronized
        self.blockstatement = blockstatement if blockstatement is not None else set()
        self.body23 = body23
        
        pass
    @property
    def synchronized(self):
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized


    @property
    def body23(self):
        return self.__body23

    @body23.setter
    def body23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_BlockStatement__body23", None)
        self.__body23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Function"):
                opp_val = getattr(old_value, "Function", None)
                if opp_val == self:
                    setattr(old_value, "Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Function"):
                opp_val = getattr(value, "Function", None)
                setattr(value, "Function", self)

    @property
    def blockstatement(self):
        return self.__blockstatement

    @blockstatement.setter
    def blockstatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_BlockStatement__blockstatement", None)
        self.__blockstatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement21"):
                    opp_val = getattr(item, "Statement21", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement21"):
                    opp_val = getattr(item, "Statement21", None)
                    
                    setattr(item, "Statement21", self)
                    

class gast_statements_ExceptionHandler(Statement):

    pass