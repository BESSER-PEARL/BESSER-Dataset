from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class filetree_User:

    def __init__(self, userId: str, password: str, pin: str, rootDir: str, filetree_User: "filetree_FileTree" = None):
        self.userId = userId
        self.password = password
        self.pin = pin
        self.rootDir = rootDir
        self.filetree_User = filetree_User
        
    @property
    def rootDir(self) -> str:
        return self.__rootDir

    @rootDir.setter
    def rootDir(self, rootDir: str):
        self.__rootDir = rootDir

    @property
    def userId(self) -> str:
        return self.__userId

    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def pin(self) -> str:
        return self.__pin

    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def filetree_User(self):
        return self.__filetree_User

    @filetree_User.setter
    def filetree_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_filetree_User__filetree_User", None)
        self.__filetree_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "filetree_FileTree5"):
                opp_val = getattr(old_value, "filetree_FileTree5", None)
                if opp_val == self:
                    setattr(old_value, "filetree_FileTree5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "filetree_FileTree5"):
                opp_val = getattr(value, "filetree_FileTree5", None)
                setattr(value, "filetree_FileTree5", self)

class FileTreeElement:

    pass
class filetree_Container(FileTreeElement):

    pass
class filetree_H2HFile(FileTreeElement):

    pass
class filetree_AccessRight:

    def __init__(self, readPermission: bool, writePermission: bool, userId: str, filetree_AccessRight: "filetree_FileTreeElement" = None):
        self.readPermission = readPermission
        self.writePermission = writePermission
        self.userId = userId
        self.filetree_AccessRight = filetree_AccessRight
        
    @property
    def writePermission(self) -> bool:
        return self.__writePermission

    @writePermission.setter
    def writePermission(self, writePermission: bool):
        self.__writePermission = writePermission

    @property
    def readPermission(self) -> bool:
        return self.__readPermission

    @readPermission.setter
    def readPermission(self, readPermission: bool):
        self.__readPermission = readPermission

    @property
    def userId(self) -> str:
        return self.__userId

    @userId.setter
    def userId(self, userId: str):
        self.__userId = userId

    @property
    def filetree_AccessRight(self):
        return self.__filetree_AccessRight

    @filetree_AccessRight.setter
    def filetree_AccessRight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_filetree_AccessRight__filetree_AccessRight", None)
        self.__filetree_AccessRight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "filetree_FileTreeElement"):
                opp_val = getattr(old_value, "filetree_FileTreeElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "filetree_FileTreeElement"):
                opp_val = getattr(value, "filetree_FileTreeElement", None)
                if opp_val is None:
                    setattr(value, "filetree_FileTreeElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class filetree_FileTreeElement(ABC):

    def __init__(self, path: str, name: str, file: str, filetree_FileTreeElement: set["filetree_AccessRight"] = None, FileTreeElement: "filetree_Container" = None, children: "filetree_Container" = None, filetree_FileTreeElement8: "filetree_PathToTreeElementMap" = None):
        self.path = path
        self.name = name
        self.file = file
        self.filetree_FileTreeElement = filetree_FileTreeElement if filetree_FileTreeElement is not None else set()
        self.FileTreeElement = FileTreeElement
        self.children = children
        self.filetree_FileTreeElement8 = filetree_FileTreeElement8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_filetree_FileTreeElement__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Container"):
                opp_val = getattr(old_value, "Container", None)
                if opp_val == self:
                    setattr(old_value, "Container", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Container"):
                opp_val = getattr(value, "Container", None)
                setattr(value, "Container", self)

    @property
    def FileTreeElement(self):
        return self.__FileTreeElement

    @FileTreeElement.setter
    def FileTreeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_filetree_FileTreeElement__FileTreeElement", None)
        self.__FileTreeElement = value
        
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
    def filetree_FileTreeElement8(self):
        return self.__filetree_FileTreeElement8

    @filetree_FileTreeElement8.setter
    def filetree_FileTreeElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_filetree_FileTreeElement__filetree_FileTreeElement8", None)
        self.__filetree_FileTreeElement8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "filetree_PathToTreeElementMap7"):
                opp_val = getattr(old_value, "filetree_PathToTreeElementMap7", None)
                if opp_val == self:
                    setattr(old_value, "filetree_PathToTreeElementMap7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "filetree_PathToTreeElementMap7"):
                opp_val = getattr(value, "filetree_PathToTreeElementMap7", None)
                setattr(value, "filetree_PathToTreeElementMap7", self)

    @property
    def filetree_FileTreeElement(self):
        return self.__filetree_FileTreeElement

    @filetree_FileTreeElement.setter
    def filetree_FileTreeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_filetree_FileTreeElement__filetree_FileTreeElement", None)
        self.__filetree_FileTreeElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "filetree_AccessRight"):
                    opp_val = getattr(item, "filetree_AccessRight", None)
                    
                    if opp_val == self:
                        setattr(item, "filetree_AccessRight", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "filetree_AccessRight"):
                    opp_val = getattr(item, "filetree_AccessRight", None)
                    
                    setattr(item, "filetree_AccessRight", self)
                    

class filetree_PathToTreeElementMap:

    def __init__(self, key: str, filetree_PathToTreeElementMap: "filetree_FileTree" = None, filetree_PathToTreeElementMap7: "filetree_FileTreeElement" = None):
        self.key = key
        self.filetree_PathToTreeElementMap = filetree_PathToTreeElementMap
        self.filetree_PathToTreeElementMap7 = filetree_PathToTreeElementMap7
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def filetree_PathToTreeElementMap(self):
        return self.__filetree_PathToTreeElementMap

    @filetree_PathToTreeElementMap.setter
    def filetree_PathToTreeElementMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_filetree_PathToTreeElementMap__filetree_PathToTreeElementMap", None)
        self.__filetree_PathToTreeElementMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "filetree_FileTree"):
                opp_val = getattr(old_value, "filetree_FileTree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "filetree_FileTree"):
                opp_val = getattr(value, "filetree_FileTree", None)
                if opp_val is None:
                    setattr(value, "filetree_FileTree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def filetree_PathToTreeElementMap7(self):
        return self.__filetree_PathToTreeElementMap7

    @filetree_PathToTreeElementMap7.setter
    def filetree_PathToTreeElementMap7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_filetree_PathToTreeElementMap__filetree_PathToTreeElementMap7", None)
        self.__filetree_PathToTreeElementMap7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "filetree_FileTreeElement8"):
                opp_val = getattr(old_value, "filetree_FileTreeElement8", None)
                if opp_val == self:
                    setattr(old_value, "filetree_FileTreeElement8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "filetree_FileTreeElement8"):
                opp_val = getattr(value, "filetree_FileTreeElement8", None)
                setattr(value, "filetree_FileTreeElement8", self)

class Container:

    pass
class filetree_Directory(Container):

    pass
class filetree_FileTree(Container):

    pass