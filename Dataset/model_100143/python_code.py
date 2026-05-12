from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FieldType(Enum):
    RELATIVE = "RELATIVE"
    ABSOLUTE = "ABSOLUTE"


############################################
# Definition of Classes
############################################

class Task:

    pass
class model_TaskExport(Task):

    pass
class model_TaskFile(Task):

    pass
class model_TaskSQL(Task):

    pass
class model_TaskImport(Task):

    pass
class IFile:

    pass
class SeparatedElement:

    pass
class model_File(IFile, SeparatedElement):

    def __init__(self, files: str, numberOfHeaderLines: str, model_File: set["model_Field"] = None, model_File58: "model_TaskFile" = None, model_File61: "model_TaskFile" = None):
        self.files = files
        self.numberOfHeaderLines = numberOfHeaderLines
        self.model_File = model_File if model_File is not None else set()
        self.model_File58 = model_File58
        self.model_File61 = model_File61
        
        pass
    @property
    def numberOfHeaderLines(self):
        return self.__numberOfHeaderLines

    @numberOfHeaderLines.setter
    def numberOfHeaderLines(self, numberOfHeaderLines: str):
        self.__numberOfHeaderLines = numberOfHeaderLines


    @property
    def files(self):
        return self.__files

    @files.setter
    def files(self, files: str):
        self.__files = files


    @property
    def model_File58(self):
        return self.__model_File58

    @model_File58.setter
    def model_File58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_File__model_File58", None)
        self.__model_File58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TaskFile"):
                opp_val = getattr(old_value, "model_TaskFile", None)
                if opp_val == self:
                    setattr(old_value, "model_TaskFile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TaskFile"):
                opp_val = getattr(value, "model_TaskFile", None)
                setattr(value, "model_TaskFile", self)

    @property
    def model_File61(self):
        return self.__model_File61

    @model_File61.setter
    def model_File61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_File__model_File61", None)
        self.__model_File61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TaskFile60"):
                opp_val = getattr(old_value, "model_TaskFile60", None)
                if opp_val == self:
                    setattr(old_value, "model_TaskFile60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TaskFile60"):
                opp_val = getattr(value, "model_TaskFile60", None)
                setattr(value, "model_TaskFile60", self)

    @property
    def model_File(self):
        return self.__model_File

    @model_File.setter
    def model_File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_File__model_File", None)
        self.__model_File = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Field"):
                    opp_val = getattr(item, "model_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Field"):
                    opp_val = getattr(item, "model_Field", None)
                    
                    setattr(item, "model_Field", self)
                    

class Mapping:

    pass
class model_MappingExport(Mapping):

    pass
class model_MappingSQL(Mapping):

    pass
class model_MappingFile(Mapping):

    pass
class model_MappingImport(Mapping):

    pass
class model_Mapping:

    def __init__(self, expression: str):
        self.expression = expression
        
        pass
    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


class model_SCTFile(IFile):

    def __init__(self, file: str, model_SCTFile: set["model_Column"] = None, model_SCTFile21: set["model_Domain"] = None):
        self.file = file
        self.model_SCTFile = model_SCTFile if model_SCTFile is not None else set()
        self.model_SCTFile21 = model_SCTFile21 if model_SCTFile21 is not None else set()
        
        pass
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def model_SCTFile21(self):
        return self.__model_SCTFile21

    @model_SCTFile21.setter
    def model_SCTFile21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_SCTFile__model_SCTFile21", None)
        self.__model_SCTFile21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Domain22"):
                    opp_val = getattr(item, "model_Domain22", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Domain22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Domain22"):
                    opp_val = getattr(item, "model_Domain22", None)
                    
                    setattr(item, "model_Domain22", self)
                    

    @property
    def model_SCTFile(self):
        return self.__model_SCTFile

    @model_SCTFile.setter
    def model_SCTFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_SCTFile__model_SCTFile", None)
        self.__model_SCTFile = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Column19"):
                    opp_val = getattr(item, "model_Column19", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Column19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Column19"):
                    opp_val = getattr(item, "model_Column19", None)
                    
                    setattr(item, "model_Column19", self)
                    

class FQNamedElement:

    pass
class IColumn:

    pass
class model_Field(SeparatedElement, IColumn):

    def __init__(self, type: str, length: str, position: str, model_Field28: "model_MappingFile" = None, model_Field31: "model_MappingFile" = None, model_Field: "model_File" = None):
        self.type = type
        self.length = length
        self.position = position
        self.model_Field28 = model_Field28
        self.model_Field31 = model_Field31
        self.model_Field = model_Field
        
        pass
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def model_Field(self):
        return self.__model_Field

    @model_Field.setter
    def model_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Field__model_Field", None)
        self.__model_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_File"):
                opp_val = getattr(old_value, "model_File", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_File"):
                opp_val = getattr(value, "model_File", None)
                if opp_val is None:
                    setattr(value, "model_File", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Field31(self):
        return self.__model_Field31

    @model_Field31.setter
    def model_Field31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Field__model_Field31", None)
        self.__model_Field31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MappingFile30"):
                opp_val = getattr(old_value, "model_MappingFile30", None)
                if opp_val == self:
                    setattr(old_value, "model_MappingFile30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MappingFile30"):
                opp_val = getattr(value, "model_MappingFile30", None)
                setattr(value, "model_MappingFile30", self)

    @property
    def model_Field28(self):
        return self.__model_Field28

    @model_Field28.setter
    def model_Field28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Field__model_Field28", None)
        self.__model_Field28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_MappingFile"):
                opp_val = getattr(old_value, "model_MappingFile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_MappingFile"):
                opp_val = getattr(value, "model_MappingFile", None)
                if opp_val is None:
                    setattr(value, "model_MappingFile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Column(IColumn):

    pass
class model_SeparatedElement:

    def __init__(self, separator: str):
        self.separator = separator
        
        pass
    @property
    def separator(self):
        return self.__separator

    @separator.setter
    def separator(self, separator: str):
        self.__separator = separator


class model_FQNamedElement:

    def __init__(self):
        
        pass
    def getFQName(self) :
        # TODO: Implement getFQName method
        pass

class model_DescribedElement:

    def __init__(self, description: str):
        self.description = description
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


class model_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Type:

    pass
class model_Domain(FQNamedElement, Type):

    def __init__(self, type: str, model_Domain: "model_Schema" = None, model_Domain22: "model_SCTFile" = None):
        self.type = type
        self.model_Domain = model_Domain
        self.model_Domain22 = model_Domain22
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def model_Domain(self):
        return self.__model_Domain

    @model_Domain.setter
    def model_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Domain__model_Domain", None)
        self.__model_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Schema7"):
                opp_val = getattr(old_value, "model_Schema7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Schema7"):
                opp_val = getattr(value, "model_Schema7", None)
                if opp_val is None:
                    setattr(value, "model_Schema7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Domain22(self):
        return self.__model_Domain22

    @model_Domain22.setter
    def model_Domain22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Domain__model_Domain22", None)
        self.__model_Domain22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_SCTFile21"):
                opp_val = getattr(old_value, "model_SCTFile21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_SCTFile21"):
                opp_val = getattr(value, "model_SCTFile21", None)
                if opp_val is None:
                    setattr(value, "model_SCTFile21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_NativeSQLType(Type):

    pass
class DescribedElement:

    pass
class NamedElement:

    pass
class model_Table(NamedElement, DescribedElement, FQNamedElement):

    pass
class model_Task(NamedElement, DescribedElement):

    def __init__(self, fileName: str, model_Task48: "model_Task" = None, model_Task46: set["model_Task"] = None, model_Task: "model_TaskSet" = None, model_Task45: "model_TaskSet" = None):
        self.fileName = fileName
        self.model_Task48 = model_Task48
        self.model_Task46 = model_Task46 if model_Task46 is not None else set()
        self.model_Task = model_Task
        self.model_Task45 = model_Task45
        
        pass
    @property
    def fileName(self):
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName


    @property
    def model_Task45(self):
        return self.__model_Task45

    @model_Task45.setter
    def model_Task45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Task__model_Task45", None)
        self.__model_Task45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TaskSet44"):
                opp_val = getattr(old_value, "model_TaskSet44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TaskSet44"):
                opp_val = getattr(value, "model_TaskSet44", None)
                if opp_val is None:
                    setattr(value, "model_TaskSet44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Task48(self):
        return self.__model_Task48

    @model_Task48.setter
    def model_Task48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Task__model_Task48", None)
        self.__model_Task48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Task46"):
                opp_val = getattr(old_value, "model_Task46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Task46"):
                opp_val = getattr(value, "model_Task46", None)
                if opp_val is None:
                    setattr(value, "model_Task46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Task46(self):
        return self.__model_Task46

    @model_Task46.setter
    def model_Task46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Task__model_Task46", None)
        self.__model_Task46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Task48"):
                    opp_val = getattr(item, "model_Task48", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Task48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Task48"):
                    opp_val = getattr(item, "model_Task48", None)
                    
                    setattr(item, "model_Task48", self)
                    

    @property
    def model_Task(self):
        return self.__model_Task

    @model_Task.setter
    def model_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Task__model_Task", None)
        self.__model_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TaskSet"):
                opp_val = getattr(old_value, "model_TaskSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TaskSet"):
                opp_val = getattr(value, "model_TaskSet", None)
                if opp_val is None:
                    setattr(value, "model_TaskSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_IColumn(NamedElement, DescribedElement, FQNamedElement):

    pass
class model_IFile(NamedElement, DescribedElement):

    pass
class model_User(NamedElement, DescribedElement, FQNamedElement):

    def __init__(self, password: str, model_User: "model_Database" = None, model_User4: "model_Schema" = None):
        self.password = password
        self.model_User = model_User
        self.model_User4 = model_User4
        
        pass
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def model_User4(self):
        return self.__model_User4

    @model_User4.setter
    def model_User4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_User__model_User4", None)
        self.__model_User4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Schema5"):
                opp_val = getattr(old_value, "model_Schema5", None)
                if opp_val == self:
                    setattr(old_value, "model_Schema5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Schema5"):
                opp_val = getattr(value, "model_Schema5", None)
                setattr(value, "model_Schema5", self)

    @property
    def model_User(self):
        return self.__model_User

    @model_User.setter
    def model_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_User__model_User", None)
        self.__model_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Database"):
                opp_val = getattr(old_value, "model_Database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Database"):
                opp_val = getattr(value, "model_Database", None)
                if opp_val is None:
                    setattr(value, "model_Database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Database(NamedElement, DescribedElement):

    def __init__(self, dsn: str, model_Database: set["model_User"] = None, model_Database2: set["model_Schema"] = None, model_Database82: "model_Site" = None):
        self.dsn = dsn
        self.model_Database = model_Database if model_Database is not None else set()
        self.model_Database2 = model_Database2 if model_Database2 is not None else set()
        self.model_Database82 = model_Database82
        
        pass
    @property
    def dsn(self):
        return self.__dsn

    @dsn.setter
    def dsn(self, dsn: str):
        self.__dsn = dsn


    @property
    def model_Database(self):
        return self.__model_Database

    @model_Database.setter
    def model_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Database__model_Database", None)
        self.__model_Database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_User"):
                    opp_val = getattr(item, "model_User", None)
                    
                    if opp_val == self:
                        setattr(item, "model_User", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_User"):
                    opp_val = getattr(item, "model_User", None)
                    
                    setattr(item, "model_User", self)
                    

    @property
    def model_Database82(self):
        return self.__model_Database82

    @model_Database82.setter
    def model_Database82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Database__model_Database82", None)
        self.__model_Database82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Site"):
                opp_val = getattr(old_value, "model_Site", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Site"):
                opp_val = getattr(value, "model_Site", None)
                if opp_val is None:
                    setattr(value, "model_Site", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Database2(self):
        return self.__model_Database2

    @model_Database2.setter
    def model_Database2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Database__model_Database2", None)
        self.__model_Database2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Schema"):
                    opp_val = getattr(item, "model_Schema", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Schema", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Schema"):
                    opp_val = getattr(item, "model_Schema", None)
                    
                    setattr(item, "model_Schema", self)
                    

class model_FileSet(NamedElement, DescribedElement):

    def __init__(self, hostname: str, model_FileSet: set["model_IFile"] = None, model_FileSet85: "model_Site" = None):
        self.hostname = hostname
        self.model_FileSet = model_FileSet if model_FileSet is not None else set()
        self.model_FileSet85 = model_FileSet85
        
        pass
    @property
    def hostname(self):
        return self.__hostname

    @hostname.setter
    def hostname(self, hostname: str):
        self.__hostname = hostname


    @property
    def model_FileSet85(self):
        return self.__model_FileSet85

    @model_FileSet85.setter
    def model_FileSet85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FileSet__model_FileSet85", None)
        self.__model_FileSet85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Site84"):
                opp_val = getattr(old_value, "model_Site84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Site84"):
                opp_val = getattr(value, "model_Site84", None)
                if opp_val is None:
                    setattr(value, "model_Site84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_FileSet(self):
        return self.__model_FileSet

    @model_FileSet.setter
    def model_FileSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FileSet__model_FileSet", None)
        self.__model_FileSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_IFile"):
                    opp_val = getattr(item, "model_IFile", None)
                    
                    if opp_val == self:
                        setattr(item, "model_IFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_IFile"):
                    opp_val = getattr(item, "model_IFile", None)
                    
                    setattr(item, "model_IFile", self)
                    

class model_Site(NamedElement, DescribedElement):

    pass
class model_TaskSet(NamedElement, DescribedElement):

    pass
class model_View(NamedElement, FQNamedElement, DescribedElement):

    def __init__(self, sql: str, model_View: "model_Schema" = None):
        self.sql = sql
        self.model_View = model_View
        
        pass
    @property
    def sql(self):
        return self.__sql

    @sql.setter
    def sql(self, sql: str):
        self.__sql = sql


    @property
    def model_View(self):
        return self.__model_View

    @model_View.setter
    def model_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_View__model_View", None)
        self.__model_View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Schema11"):
                opp_val = getattr(old_value, "model_Schema11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Schema11"):
                opp_val = getattr(value, "model_Schema11", None)
                if opp_val is None:
                    setattr(value, "model_Schema11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Schema(NamedElement, DescribedElement):

    pass
class model_Type(NamedElement, DescribedElement):

    pass