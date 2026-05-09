from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FileEncoding(Enum):
    US_ASCII = "US_ASCII"
    ISO_8859_1 = "ISO_8859_1"
    UTF_8 = "UTF_8"
    UTF_16 = "UTF_16"
    UTF_16BE = "UTF_16BE"
    UTF_16LE = "UTF_16LE"


############################################
# Definition of Classes
############################################

class file_FileOwner(ABC):

    pass
class FileOwner:

    pass
class file_Files(FileOwner):

    def __init__(self, Name: str):
        self.Name = Name
        
        pass
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name


class file_FileOutput(FileOwner):

    pass
class file_FileHandler(FileOwner):

    pass
class FileHandler:

    pass
class file_FileReaderWriter(FileHandler):

    def __init__(self, ReadFeedback: str, CloseFeedback: str, Open: bool, WriteFeedback: str):
        self.ReadFeedback = ReadFeedback
        self.CloseFeedback = CloseFeedback
        self.Open = Open
        self.WriteFeedback = WriteFeedback
        
        pass
    @property
    def Open(self):
        return self.__Open

    @Open.setter
    def Open(self, Open: bool):
        self.__Open = Open


    @property
    def CloseFeedback(self):
        return self.__CloseFeedback

    @CloseFeedback.setter
    def CloseFeedback(self, CloseFeedback: str):
        self.__CloseFeedback = CloseFeedback


    @property
    def WriteFeedback(self):
        return self.__WriteFeedback

    @WriteFeedback.setter
    def WriteFeedback(self, WriteFeedback: str):
        self.__WriteFeedback = WriteFeedback


    @property
    def ReadFeedback(self):
        return self.__ReadFeedback

    @ReadFeedback.setter
    def ReadFeedback(self, ReadFeedback: str):
        self.__ReadFeedback = ReadFeedback


    def writeFile(self, file_file):
        # TODO: Implement writeFile method
        pass

    def close(self):
        # TODO: Implement close method
        pass

    def readFile(self, file_file):
        # TODO: Implement readFile method
        pass

    def getWriteFeedback(self, file_file) :
        # TODO: Implement getWriteFeedback method
        pass

    def getReadFeedback(self, file_file) :
        # TODO: Implement getReadFeedback method
        pass

class File:

    pass
class file_ByteFile(File):

    def __init__(self, Encoding: str):
        self.Encoding = Encoding
        
        pass
    @property
    def Encoding(self):
        return self.__Encoding

    @Encoding.setter
    def Encoding(self, Encoding: str):
        self.__Encoding = Encoding


class file_FileInMemory(File):

    def __init__(self, Content: str):
        self.Content = Content
        
        pass
    @property
    def Content(self):
        return self.__Content

    @Content.setter
    def Content(self, Content: str):
        self.__Content = Content


class ByteFile:

    pass
class file_FileRemote(ByteFile):

    def __init__(self, URL: str):
        self.URL = URL
        
        pass
    @property
    def URL(self):
        return self.__URL

    @URL.setter
    def URL(self, URL: str):
        self.__URL = URL


class file_FileLocal(ByteFile):

    def __init__(self, FilePath: str):
        self.FilePath = FilePath
        
        pass
    @property
    def FilePath(self):
        return self.__FilePath

    @FilePath.setter
    def FilePath(self, FilePath: str):
        self.__FilePath = FilePath


class file_File(ABC):

    def __init__(self, Name: str, file_File: "file_FileHandler" = None, file_File3: "file_FileHandler" = None, file_File5: "file_FileOwner" = None, file_File7: "file_FileOutput" = None):
        self.Name = Name
        self.file_File = file_File
        self.file_File3 = file_File3
        self.file_File5 = file_File5
        self.file_File7 = file_File7
        
        pass
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name


    @property
    def file_File7(self):
        return self.__file_File7

    @file_File7.setter
    def file_File7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_file_File__file_File7", None)
        self.__file_File7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "file_FileOutput"):
                opp_val = getattr(old_value, "file_FileOutput", None)
                if opp_val == self:
                    setattr(old_value, "file_FileOutput", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "file_FileOutput"):
                opp_val = getattr(value, "file_FileOutput", None)
                setattr(value, "file_FileOutput", self)

    @property
    def file_File(self):
        return self.__file_File

    @file_File.setter
    def file_File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_file_File__file_File", None)
        self.__file_File = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "file_FileHandler"):
                opp_val = getattr(old_value, "file_FileHandler", None)
                if opp_val == self:
                    setattr(old_value, "file_FileHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "file_FileHandler"):
                opp_val = getattr(value, "file_FileHandler", None)
                setattr(value, "file_FileHandler", self)

    @property
    def file_File3(self):
        return self.__file_File3

    @file_File3.setter
    def file_File3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_file_File__file_File3", None)
        self.__file_File3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "file_FileHandler2"):
                opp_val = getattr(old_value, "file_FileHandler2", None)
                if opp_val == self:
                    setattr(old_value, "file_FileHandler2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "file_FileHandler2"):
                opp_val = getattr(value, "file_FileHandler2", None)
                setattr(value, "file_FileHandler2", self)

    @property
    def file_File5(self):
        return self.__file_File5

    @file_File5.setter
    def file_File5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_file_File__file_File5", None)
        self.__file_File5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "file_FileOwner"):
                opp_val = getattr(old_value, "file_FileOwner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "file_FileOwner"):
                opp_val = getattr(value, "file_FileOwner", None)
                if opp_val is None:
                    setattr(value, "file_FileOwner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
