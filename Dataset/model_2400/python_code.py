from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class PhotosMetaModel_Files:

    def __init__(self, type: str, extension: str, PhotosMetaModel_Files: "PhotosMetaModel_SegmentStructure" = None, PhotosMetaModel_Files198: "PhotosMetaModel_Directories" = None):
        self.type = type
        self.extension = extension
        self.PhotosMetaModel_Files = PhotosMetaModel_Files
        self.PhotosMetaModel_Files198 = PhotosMetaModel_Files198
        
    @property
    def extension(self) -> str:
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def PhotosMetaModel_Files(self):
        return self.__PhotosMetaModel_Files

    @PhotosMetaModel_Files.setter
    def PhotosMetaModel_Files(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Files__PhotosMetaModel_Files", None)
        self.__PhotosMetaModel_Files = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_SegmentStructure195"):
                opp_val = getattr(old_value, "PhotosMetaModel_SegmentStructure195", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_SegmentStructure195"):
                opp_val = getattr(value, "PhotosMetaModel_SegmentStructure195", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_SegmentStructure195", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhotosMetaModel_Files198(self):
        return self.__PhotosMetaModel_Files198

    @PhotosMetaModel_Files198.setter
    def PhotosMetaModel_Files198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Files__PhotosMetaModel_Files198", None)
        self.__PhotosMetaModel_Files198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Directories197"):
                opp_val = getattr(old_value, "PhotosMetaModel_Directories197", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_Directories197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Directories197"):
                opp_val = getattr(value, "PhotosMetaModel_Directories197", None)
                setattr(value, "PhotosMetaModel_Directories197", self)

class PhotosMetaModel_Directories:

    pass
class Logic:

    pass
class PhotosMetaModel_Structure(Logic):

    pass
class PhotosMetaModel_Router(Logic):

    pass
class PhotosMetaModel_State:

    def __init__(self, active: str, PhotosMetaModel_State: "PhotosMetaModel_ReactClasses" = None):
        self.active = active
        self.PhotosMetaModel_State = PhotosMetaModel_State
        
    @property
    def active(self) -> str:
        return self.__active

    @active.setter
    def active(self, active: str):
        self.__active = active

    @property
    def PhotosMetaModel_State(self):
        return self.__PhotosMetaModel_State

    @PhotosMetaModel_State.setter
    def PhotosMetaModel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_State__PhotosMetaModel_State", None)
        self.__PhotosMetaModel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_ReactClasses188"):
                opp_val = getattr(old_value, "PhotosMetaModel_ReactClasses188", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_ReactClasses188"):
                opp_val = getattr(value, "PhotosMetaModel_ReactClasses188", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_ReactClasses188", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Actions:

    pass
class PhotosMetaModel_Services(Actions):

    pass
class PhotosMetaModel_Request(Actions):

    pass
class UI:

    pass
class PhotosMetaModel_ViewComponents(UI):

    pass
class PhotosMetaModel_Subcomponents(UI):

    pass
class Components:

    pass
class PhotosMetaModel_Logic(Components):

    pass
class ReactConfiguration:

    pass
class PhotosMetaModel_Dependencies(ReactConfiguration):

    pass
class PhotosMetaModel_ReactDOM(ReactConfiguration):

    def __init__(self, isRoute: str, isConstant: str, isStruct: str):
        self.isRoute = isRoute
        self.isConstant = isConstant
        self.isStruct = isStruct
        
    @property
    def isRoute(self) -> str:
        return self.__isRoute

    @isRoute.setter
    def isRoute(self, isRoute: str):
        self.__isRoute = isRoute

    @property
    def isStruct(self) -> str:
        return self.__isStruct

    @isStruct.setter
    def isStruct(self, isStruct: str):
        self.__isStruct = isStruct

    @property
    def isConstant(self) -> str:
        return self.__isConstant

    @isConstant.setter
    def isConstant(self, isConstant: str):
        self.__isConstant = isConstant

class PhotosMetaModel_Props:

    def __init__(self, type: str, dataType: str, PhotosMetaModel_Props: "PhotosMetaModel_ReactClasses" = None):
        self.type = type
        self.dataType = dataType
        self.PhotosMetaModel_Props = PhotosMetaModel_Props
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def PhotosMetaModel_Props(self):
        return self.__PhotosMetaModel_Props

    @PhotosMetaModel_Props.setter
    def PhotosMetaModel_Props(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Props__PhotosMetaModel_Props", None)
        self.__PhotosMetaModel_Props = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_ReactClasses186"):
                opp_val = getattr(old_value, "PhotosMetaModel_ReactClasses186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_ReactClasses186"):
                opp_val = getattr(value, "PhotosMetaModel_ReactClasses186", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_ReactClasses186", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PhotosMetaModel_UI(Components):

    pass
class Access:

    pass
class PhotosMetaModel_OnlyAuthorized(Access):

    pass
class PhotosMetaModel_ObjectsPublic(Access):

    pass
class PhotosMetaModel_BucketObjectsNotPublic(Access):

    pass
class PhotosMetaModel_Public(Access):

    pass
class PhotosMetaModel_Folder_a:

    def __init__(self, name: str, PhotosMetaModel_Folder_a: "PhotosMetaModel_Bucket" = None, PhotosMetaModel_Folder_a181: set["PhotosMetaModel_File_a"] = None):
        self.name = name
        self.PhotosMetaModel_Folder_a = PhotosMetaModel_Folder_a
        self.PhotosMetaModel_Folder_a181 = PhotosMetaModel_Folder_a181 if PhotosMetaModel_Folder_a181 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_Folder_a(self):
        return self.__PhotosMetaModel_Folder_a

    @PhotosMetaModel_Folder_a.setter
    def PhotosMetaModel_Folder_a(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Folder_a__PhotosMetaModel_Folder_a", None)
        self.__PhotosMetaModel_Folder_a = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Bucket177"):
                opp_val = getattr(old_value, "PhotosMetaModel_Bucket177", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Bucket177"):
                opp_val = getattr(value, "PhotosMetaModel_Bucket177", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_Bucket177", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhotosMetaModel_Folder_a181(self):
        return self.__PhotosMetaModel_Folder_a181

    @PhotosMetaModel_Folder_a181.setter
    def PhotosMetaModel_Folder_a181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Folder_a__PhotosMetaModel_Folder_a181", None)
        self.__PhotosMetaModel_Folder_a181 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_File_a182"):
                    opp_val = getattr(item, "PhotosMetaModel_File_a182", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_File_a182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_File_a182"):
                    opp_val = getattr(item, "PhotosMetaModel_File_a182", None)
                    
                    setattr(item, "PhotosMetaModel_File_a182", self)
                    

class PhotosMetaModel_MetaData:

    pass
class PhotosMetaModel_BatchOperation:

    pass
class PhotosMetaModel_Bucket:

    def __init__(self, name: str, PhotosMetaModel_Bucket173: "PhotosMetaModel_Access" = None, PhotosMetaModel_Bucket175: set["PhotosMetaModel_File_a"] = None, PhotosMetaModel_Bucket: "PhotosMetaModel_AmazonSimpleStorageService" = None, PhotosMetaModel_Bucket177: set["PhotosMetaModel_Folder_a"] = None):
        self.name = name
        self.PhotosMetaModel_Bucket173 = PhotosMetaModel_Bucket173
        self.PhotosMetaModel_Bucket175 = PhotosMetaModel_Bucket175 if PhotosMetaModel_Bucket175 is not None else set()
        self.PhotosMetaModel_Bucket = PhotosMetaModel_Bucket
        self.PhotosMetaModel_Bucket177 = PhotosMetaModel_Bucket177 if PhotosMetaModel_Bucket177 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_Bucket177(self):
        return self.__PhotosMetaModel_Bucket177

    @PhotosMetaModel_Bucket177.setter
    def PhotosMetaModel_Bucket177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Bucket__PhotosMetaModel_Bucket177", None)
        self.__PhotosMetaModel_Bucket177 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Folder_a"):
                    opp_val = getattr(item, "PhotosMetaModel_Folder_a", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Folder_a", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Folder_a"):
                    opp_val = getattr(item, "PhotosMetaModel_Folder_a", None)
                    
                    setattr(item, "PhotosMetaModel_Folder_a", self)
                    

    @property
    def PhotosMetaModel_Bucket(self):
        return self.__PhotosMetaModel_Bucket

    @PhotosMetaModel_Bucket.setter
    def PhotosMetaModel_Bucket(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Bucket__PhotosMetaModel_Bucket", None)
        self.__PhotosMetaModel_Bucket = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_AmazonSimpleStorageService169"):
                opp_val = getattr(old_value, "PhotosMetaModel_AmazonSimpleStorageService169", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_AmazonSimpleStorageService169"):
                opp_val = getattr(value, "PhotosMetaModel_AmazonSimpleStorageService169", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_AmazonSimpleStorageService169", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhotosMetaModel_Bucket175(self):
        return self.__PhotosMetaModel_Bucket175

    @PhotosMetaModel_Bucket175.setter
    def PhotosMetaModel_Bucket175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Bucket__PhotosMetaModel_Bucket175", None)
        self.__PhotosMetaModel_Bucket175 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_File_a"):
                    opp_val = getattr(item, "PhotosMetaModel_File_a", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_File_a", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_File_a"):
                    opp_val = getattr(item, "PhotosMetaModel_File_a", None)
                    
                    setattr(item, "PhotosMetaModel_File_a", self)
                    

    @property
    def PhotosMetaModel_Bucket173(self):
        return self.__PhotosMetaModel_Bucket173

    @PhotosMetaModel_Bucket173.setter
    def PhotosMetaModel_Bucket173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Bucket__PhotosMetaModel_Bucket173", None)
        self.__PhotosMetaModel_Bucket173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Access"):
                opp_val = getattr(old_value, "PhotosMetaModel_Access", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_Access", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Access"):
                opp_val = getattr(value, "PhotosMetaModel_Access", None)
                setattr(value, "PhotosMetaModel_Access", self)

class ReactFunctions:

    pass
class PhotosMetaModel_CoreFunctions(ReactFunctions):

    pass
class PhotosMetaModel_Constructor(ReactFunctions):

    pass
class PhotosMetaModel_LifeCycle(ReactFunctions):

    pass
class PhotosMetaModel_Render(ReactFunctions):

    pass
class PhotosMetaModel_ReactFunctions:

    def __init__(self, name: str, PhotosMetaModel_ReactFunctions: "PhotosMetaModel_ReactClasses" = None):
        self.name = name
        self.PhotosMetaModel_ReactFunctions = PhotosMetaModel_ReactFunctions
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_ReactFunctions(self):
        return self.__PhotosMetaModel_ReactFunctions

    @PhotosMetaModel_ReactFunctions.setter
    def PhotosMetaModel_ReactFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_ReactFunctions__PhotosMetaModel_ReactFunctions", None)
        self.__PhotosMetaModel_ReactFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_ReactClasses184"):
                opp_val = getattr(old_value, "PhotosMetaModel_ReactClasses184", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_ReactClasses184"):
                opp_val = getattr(value, "PhotosMetaModel_ReactClasses184", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_ReactClasses184", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PhotosMetaModel_File_a:

    def __init__(self, Onwer: str, size: str, ObjectURL: str, PhotosMetaModel_File_a: "PhotosMetaModel_Bucket" = None, PhotosMetaModel_File_a179: set["PhotosMetaModel_MetaData"] = None, PhotosMetaModel_File_a182: "PhotosMetaModel_Folder_a" = None):
        self.Onwer = Onwer
        self.size = size
        self.ObjectURL = ObjectURL
        self.PhotosMetaModel_File_a = PhotosMetaModel_File_a
        self.PhotosMetaModel_File_a179 = PhotosMetaModel_File_a179 if PhotosMetaModel_File_a179 is not None else set()
        self.PhotosMetaModel_File_a182 = PhotosMetaModel_File_a182
        
    @property
    def Onwer(self) -> str:
        return self.__Onwer

    @Onwer.setter
    def Onwer(self, Onwer: str):
        self.__Onwer = Onwer

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def ObjectURL(self) -> str:
        return self.__ObjectURL

    @ObjectURL.setter
    def ObjectURL(self, ObjectURL: str):
        self.__ObjectURL = ObjectURL

    @property
    def PhotosMetaModel_File_a182(self):
        return self.__PhotosMetaModel_File_a182

    @PhotosMetaModel_File_a182.setter
    def PhotosMetaModel_File_a182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_File_a__PhotosMetaModel_File_a182", None)
        self.__PhotosMetaModel_File_a182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Folder_a181"):
                opp_val = getattr(old_value, "PhotosMetaModel_Folder_a181", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Folder_a181"):
                opp_val = getattr(value, "PhotosMetaModel_Folder_a181", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_Folder_a181", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhotosMetaModel_File_a179(self):
        return self.__PhotosMetaModel_File_a179

    @PhotosMetaModel_File_a179.setter
    def PhotosMetaModel_File_a179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_File_a__PhotosMetaModel_File_a179", None)
        self.__PhotosMetaModel_File_a179 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_MetaData"):
                    opp_val = getattr(item, "PhotosMetaModel_MetaData", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_MetaData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_MetaData"):
                    opp_val = getattr(item, "PhotosMetaModel_MetaData", None)
                    
                    setattr(item, "PhotosMetaModel_MetaData", self)
                    

    @property
    def PhotosMetaModel_File_a(self):
        return self.__PhotosMetaModel_File_a

    @PhotosMetaModel_File_a.setter
    def PhotosMetaModel_File_a(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_File_a__PhotosMetaModel_File_a", None)
        self.__PhotosMetaModel_File_a = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Bucket175"):
                opp_val = getattr(old_value, "PhotosMetaModel_Bucket175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Bucket175"):
                opp_val = getattr(value, "PhotosMetaModel_Bucket175", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_Bucket175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PhotosMetaModel_Access:

    pass
class DataSegment:

    pass
class PhotosMetaModel_PostgreSQL_a(DataSegment):

    pass
class BusinessLogicSegment:

    pass
class PhotosMetaModel_Model_a(BusinessLogicSegment):

    pass
class PhotosMetaModel_Repository_a(BusinessLogicSegment):

    pass
class PhotosMetaModel_Security_a(BusinessLogicSegment):

    pass
class PhotosMetaModel_Controller_a(BusinessLogicSegment):

    pass
class PresentationSegment:

    pass
class PhotosMetaModel_Component_a(PresentationSegment):

    pass
class PhotosMetaModel_Action_a(PresentationSegment):

    pass
class PhotosMetaModel_View_a(PresentationSegment):

    pass
class PhotosMetaModel_ReactClasses:

    pass
class Modules:

    pass
class PhotosMetaModel_Actions(Modules):

    pass
class PhotosMetaModel_Information(Modules):

    def __init__(self, fileType: str):
        self.fileType = fileType
        
    @property
    def fileType(self) -> str:
        return self.__fileType

    @fileType.setter
    def fileType(self, fileType: str):
        self.__fileType = fileType

class PhotosMetaModel_ReactConfiguration(Modules):

    pass
class PhotosMetaModel_Libraries(Modules):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class PhotosMetaModel_Components(Modules):

    pass
class PhotosMetaModel_AmazonS3Storage(DataSegment):

    pass
class PhotosMetaModel_DataSegment:

    pass
class PhotosMetaModel_BusinessLogicSegment:

    pass
class PhotosMetaModel_PresentationSegment:

    pass
class Layer:

    pass
class PhotosMetaModel_Data(Layer):

    pass
class PhotosMetaModel_BusinessLogic(Layer):

    pass
class PhotosMetaModel_Presentation(Layer):

    pass
class PhotosMetaModel_SegmentStructure:

    def __init__(self, name: str, PhotosMetaModel_SegmentStructure: "PhotosMetaModel_PresentationSegment" = None, PhotosMetaModel_SegmentStructure160: "PhotosMetaModel_BusinessLogicSegment" = None, PhotosMetaModel_SegmentStructure163: "PhotosMetaModel_DataSegment" = None, PhotosMetaModel_SegmentStructure193: set["PhotosMetaModel_Directories"] = None, PhotosMetaModel_SegmentStructure195: set["PhotosMetaModel_Files"] = None):
        self.name = name
        self.PhotosMetaModel_SegmentStructure = PhotosMetaModel_SegmentStructure
        self.PhotosMetaModel_SegmentStructure160 = PhotosMetaModel_SegmentStructure160
        self.PhotosMetaModel_SegmentStructure163 = PhotosMetaModel_SegmentStructure163
        self.PhotosMetaModel_SegmentStructure193 = PhotosMetaModel_SegmentStructure193 if PhotosMetaModel_SegmentStructure193 is not None else set()
        self.PhotosMetaModel_SegmentStructure195 = PhotosMetaModel_SegmentStructure195 if PhotosMetaModel_SegmentStructure195 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_SegmentStructure195(self):
        return self.__PhotosMetaModel_SegmentStructure195

    @PhotosMetaModel_SegmentStructure195.setter
    def PhotosMetaModel_SegmentStructure195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_SegmentStructure__PhotosMetaModel_SegmentStructure195", None)
        self.__PhotosMetaModel_SegmentStructure195 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Files"):
                    opp_val = getattr(item, "PhotosMetaModel_Files", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Files", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Files"):
                    opp_val = getattr(item, "PhotosMetaModel_Files", None)
                    
                    setattr(item, "PhotosMetaModel_Files", self)
                    

    @property
    def PhotosMetaModel_SegmentStructure163(self):
        return self.__PhotosMetaModel_SegmentStructure163

    @PhotosMetaModel_SegmentStructure163.setter
    def PhotosMetaModel_SegmentStructure163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_SegmentStructure__PhotosMetaModel_SegmentStructure163", None)
        self.__PhotosMetaModel_SegmentStructure163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_DataSegment162"):
                opp_val = getattr(old_value, "PhotosMetaModel_DataSegment162", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_DataSegment162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_DataSegment162"):
                opp_val = getattr(value, "PhotosMetaModel_DataSegment162", None)
                setattr(value, "PhotosMetaModel_DataSegment162", self)

    @property
    def PhotosMetaModel_SegmentStructure160(self):
        return self.__PhotosMetaModel_SegmentStructure160

    @PhotosMetaModel_SegmentStructure160.setter
    def PhotosMetaModel_SegmentStructure160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_SegmentStructure__PhotosMetaModel_SegmentStructure160", None)
        self.__PhotosMetaModel_SegmentStructure160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_BusinessLogicSegment159"):
                opp_val = getattr(old_value, "PhotosMetaModel_BusinessLogicSegment159", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_BusinessLogicSegment159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_BusinessLogicSegment159"):
                opp_val = getattr(value, "PhotosMetaModel_BusinessLogicSegment159", None)
                setattr(value, "PhotosMetaModel_BusinessLogicSegment159", self)

    @property
    def PhotosMetaModel_SegmentStructure193(self):
        return self.__PhotosMetaModel_SegmentStructure193

    @PhotosMetaModel_SegmentStructure193.setter
    def PhotosMetaModel_SegmentStructure193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_SegmentStructure__PhotosMetaModel_SegmentStructure193", None)
        self.__PhotosMetaModel_SegmentStructure193 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Directories"):
                    opp_val = getattr(item, "PhotosMetaModel_Directories", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Directories", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Directories"):
                    opp_val = getattr(item, "PhotosMetaModel_Directories", None)
                    
                    setattr(item, "PhotosMetaModel_Directories", self)
                    

    @property
    def PhotosMetaModel_SegmentStructure(self):
        return self.__PhotosMetaModel_SegmentStructure

    @PhotosMetaModel_SegmentStructure.setter
    def PhotosMetaModel_SegmentStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_SegmentStructure__PhotosMetaModel_SegmentStructure", None)
        self.__PhotosMetaModel_SegmentStructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_PresentationSegment157"):
                opp_val = getattr(old_value, "PhotosMetaModel_PresentationSegment157", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_PresentationSegment157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_PresentationSegment157"):
                opp_val = getattr(value, "PhotosMetaModel_PresentationSegment157", None)
                setattr(value, "PhotosMetaModel_PresentationSegment157", self)

class Relation:

    pass
class PhotosMetaModel_AllowedToUse(Relation):

    pass
class Connection:

    pass
class PhotosMetaModel_PostgreSQLConnection(Connection):

    def __init__(self, port: int, username: str, password: str, url: str):
        self.port = port
        self.username = username
        self.password = password
        self.url = url
        
    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

class PhotosMetaModel_REST(Connection):

    pass
class PhotosMetaModel_Relation:

    pass
class PhotosMetaModel_AmazonS3API(Connection):

    def __init__(self, endpointUrl: str, accessKey: str, secretKey: str, bucketName: str):
        self.endpointUrl = endpointUrl
        self.accessKey = accessKey
        self.secretKey = secretKey
        self.bucketName = bucketName
        
    @property
    def bucketName(self) -> str:
        return self.__bucketName

    @bucketName.setter
    def bucketName(self, bucketName: str):
        self.__bucketName = bucketName

    @property
    def accessKey(self) -> str:
        return self.__accessKey

    @accessKey.setter
    def accessKey(self, accessKey: str):
        self.__accessKey = accessKey

    @property
    def endpointUrl(self) -> str:
        return self.__endpointUrl

    @endpointUrl.setter
    def endpointUrl(self, endpointUrl: str):
        self.__endpointUrl = endpointUrl

    @property
    def secretKey(self) -> str:
        return self.__secretKey

    @secretKey.setter
    def secretKey(self, secretKey: str):
        self.__secretKey = secretKey

class PhotosMetaModel_Connection:

    pass
class PhotosMetaModel_AmazonElasticComputeCloud:

    pass
class PhotosMetaModel_AmazonSimpleStorageService:

    pass
class PhotosMetaModel_Layer:

    pass
class Functionalities:

    pass
class PhotosMetaModel_ProfileManagement(Functionalities):

    pass
class PhotosMetaModel_AppAccess(Functionalities):

    pass
class Entities:

    pass
class PhotosMetaModel_Photo(Entities):

    def __init__(self, name: str, PhotosMetaModel_Photo: "PhotosMetaModel_PhotoActions" = None):
        self.name = name
        self.PhotosMetaModel_Photo = PhotosMetaModel_Photo
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_Photo(self):
        return self.__PhotosMetaModel_Photo

    @PhotosMetaModel_Photo.setter
    def PhotosMetaModel_Photo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Photo__PhotosMetaModel_Photo", None)
        self.__PhotosMetaModel_Photo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_PhotoActions128"):
                opp_val = getattr(old_value, "PhotosMetaModel_PhotoActions128", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_PhotoActions128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_PhotoActions128"):
                opp_val = getattr(value, "PhotosMetaModel_PhotoActions128", None)
                setattr(value, "PhotosMetaModel_PhotoActions128", self)

class PhotosMetaModel_Album(Entities):

    def __init__(self, url: str, name: str, PhotosMetaModel_Album: "PhotosMetaModel_AlbumManagement" = None):
        self.url = url
        self.name = name
        self.PhotosMetaModel_Album = PhotosMetaModel_Album
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_Album(self):
        return self.__PhotosMetaModel_Album

    @PhotosMetaModel_Album.setter
    def PhotosMetaModel_Album(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Album__PhotosMetaModel_Album", None)
        self.__PhotosMetaModel_Album = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_AlbumManagement130"):
                opp_val = getattr(old_value, "PhotosMetaModel_AlbumManagement130", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_AlbumManagement130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_AlbumManagement130"):
                opp_val = getattr(value, "PhotosMetaModel_AlbumManagement130", None)
                setattr(value, "PhotosMetaModel_AlbumManagement130", self)

class PhotosMetaModel_User_d(Entities):

    def __init__(self, first_name: str, last_name: str, profile_description: str, username: str, password: str, email: str, PhotosMetaModel_User_d: "PhotosMetaModel_Functionalities" = None):
        self.first_name = first_name
        self.last_name = last_name
        self.profile_description = profile_description
        self.username = username
        self.password = password
        self.email = email
        self.PhotosMetaModel_User_d = PhotosMetaModel_User_d
        
    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self.__last_name = last_name

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name

    @property
    def profile_description(self) -> str:
        return self.__profile_description

    @profile_description.setter
    def profile_description(self, profile_description: str):
        self.__profile_description = profile_description

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def PhotosMetaModel_User_d(self):
        return self.__PhotosMetaModel_User_d

    @PhotosMetaModel_User_d.setter
    def PhotosMetaModel_User_d(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_User_d__PhotosMetaModel_User_d", None)
        self.__PhotosMetaModel_User_d = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Functionalities125"):
                opp_val = getattr(old_value, "PhotosMetaModel_Functionalities125", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_Functionalities125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Functionalities125"):
                opp_val = getattr(value, "PhotosMetaModel_Functionalities125", None)
                setattr(value, "PhotosMetaModel_Functionalities125", self)

class PhotosMetaModel_Index:

    pass
class PhotosMetaModel_PhotoActions(Functionalities):

    pass
class PhotosMetaModel_AlbumManagement(Functionalities):

    pass
class PhotosMetaModel_Column:

    pass
class PhotosMetaModel_Policy:

    pass
class PhotosMetaModel_Privilege:

    pass
class PhotosMetaModel_Scheme:

    def __init__(self, name: str, PhotosMetaModel_Scheme: "PhotosMetaModel_Database" = None, PhotosMetaModel_Scheme97: set["PhotosMetaModel_Table_p"] = None, PhotosMetaModel_Scheme100: set["PhotosMetaModel_View"] = None, PhotosMetaModel_Scheme102: set["PhotosMetaModel_Index_p"] = None, PhotosMetaModel_Scheme104: set["PhotosMetaModel_Trigger"] = None, PhotosMetaModel_Scheme106: set["PhotosMetaModel_Function_p"] = None):
        self.name = name
        self.PhotosMetaModel_Scheme = PhotosMetaModel_Scheme
        self.PhotosMetaModel_Scheme97 = PhotosMetaModel_Scheme97 if PhotosMetaModel_Scheme97 is not None else set()
        self.PhotosMetaModel_Scheme100 = PhotosMetaModel_Scheme100 if PhotosMetaModel_Scheme100 is not None else set()
        self.PhotosMetaModel_Scheme102 = PhotosMetaModel_Scheme102 if PhotosMetaModel_Scheme102 is not None else set()
        self.PhotosMetaModel_Scheme104 = PhotosMetaModel_Scheme104 if PhotosMetaModel_Scheme104 is not None else set()
        self.PhotosMetaModel_Scheme106 = PhotosMetaModel_Scheme106 if PhotosMetaModel_Scheme106 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_Scheme(self):
        return self.__PhotosMetaModel_Scheme

    @PhotosMetaModel_Scheme.setter
    def PhotosMetaModel_Scheme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Scheme__PhotosMetaModel_Scheme", None)
        self.__PhotosMetaModel_Scheme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Database"):
                opp_val = getattr(old_value, "PhotosMetaModel_Database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Database"):
                opp_val = getattr(value, "PhotosMetaModel_Database", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_Database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhotosMetaModel_Scheme104(self):
        return self.__PhotosMetaModel_Scheme104

    @PhotosMetaModel_Scheme104.setter
    def PhotosMetaModel_Scheme104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Scheme__PhotosMetaModel_Scheme104", None)
        self.__PhotosMetaModel_Scheme104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Trigger"):
                    opp_val = getattr(item, "PhotosMetaModel_Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Trigger"):
                    opp_val = getattr(item, "PhotosMetaModel_Trigger", None)
                    
                    setattr(item, "PhotosMetaModel_Trigger", self)
                    

    @property
    def PhotosMetaModel_Scheme97(self):
        return self.__PhotosMetaModel_Scheme97

    @PhotosMetaModel_Scheme97.setter
    def PhotosMetaModel_Scheme97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Scheme__PhotosMetaModel_Scheme97", None)
        self.__PhotosMetaModel_Scheme97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Table_p98"):
                    opp_val = getattr(item, "PhotosMetaModel_Table_p98", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Table_p98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Table_p98"):
                    opp_val = getattr(item, "PhotosMetaModel_Table_p98", None)
                    
                    setattr(item, "PhotosMetaModel_Table_p98", self)
                    

    @property
    def PhotosMetaModel_Scheme102(self):
        return self.__PhotosMetaModel_Scheme102

    @PhotosMetaModel_Scheme102.setter
    def PhotosMetaModel_Scheme102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Scheme__PhotosMetaModel_Scheme102", None)
        self.__PhotosMetaModel_Scheme102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Index_p"):
                    opp_val = getattr(item, "PhotosMetaModel_Index_p", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Index_p", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Index_p"):
                    opp_val = getattr(item, "PhotosMetaModel_Index_p", None)
                    
                    setattr(item, "PhotosMetaModel_Index_p", self)
                    

    @property
    def PhotosMetaModel_Scheme100(self):
        return self.__PhotosMetaModel_Scheme100

    @PhotosMetaModel_Scheme100.setter
    def PhotosMetaModel_Scheme100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Scheme__PhotosMetaModel_Scheme100", None)
        self.__PhotosMetaModel_Scheme100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_View"):
                    opp_val = getattr(item, "PhotosMetaModel_View", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_View", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_View"):
                    opp_val = getattr(item, "PhotosMetaModel_View", None)
                    
                    setattr(item, "PhotosMetaModel_View", self)
                    

    @property
    def PhotosMetaModel_Scheme106(self):
        return self.__PhotosMetaModel_Scheme106

    @PhotosMetaModel_Scheme106.setter
    def PhotosMetaModel_Scheme106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Scheme__PhotosMetaModel_Scheme106", None)
        self.__PhotosMetaModel_Scheme106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Function_p"):
                    opp_val = getattr(item, "PhotosMetaModel_Function_p", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Function_p", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Function_p"):
                    opp_val = getattr(item, "PhotosMetaModel_Function_p", None)
                    
                    setattr(item, "PhotosMetaModel_Function_p", self)
                    

class PhotosMetaModel_User_p:

    def __init__(self, username: str, password: str, PhotosMetaModel_User_p: set["PhotosMetaModel_Query"] = None, PhotosMetaModel_User_p110: set["PhotosMetaModel_Privilege"] = None, PhotosMetaModel_User_p116: "PhotosMetaModel_Cluster" = None):
        self.username = username
        self.password = password
        self.PhotosMetaModel_User_p = PhotosMetaModel_User_p if PhotosMetaModel_User_p is not None else set()
        self.PhotosMetaModel_User_p110 = PhotosMetaModel_User_p110 if PhotosMetaModel_User_p110 is not None else set()
        self.PhotosMetaModel_User_p116 = PhotosMetaModel_User_p116
        
    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def PhotosMetaModel_User_p110(self):
        return self.__PhotosMetaModel_User_p110

    @PhotosMetaModel_User_p110.setter
    def PhotosMetaModel_User_p110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_User_p__PhotosMetaModel_User_p110", None)
        self.__PhotosMetaModel_User_p110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Privilege"):
                    opp_val = getattr(item, "PhotosMetaModel_Privilege", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Privilege", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Privilege"):
                    opp_val = getattr(item, "PhotosMetaModel_Privilege", None)
                    
                    setattr(item, "PhotosMetaModel_Privilege", self)
                    

    @property
    def PhotosMetaModel_User_p(self):
        return self.__PhotosMetaModel_User_p

    @PhotosMetaModel_User_p.setter
    def PhotosMetaModel_User_p(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_User_p__PhotosMetaModel_User_p", None)
        self.__PhotosMetaModel_User_p = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Query108"):
                    opp_val = getattr(item, "PhotosMetaModel_Query108", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Query108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Query108"):
                    opp_val = getattr(item, "PhotosMetaModel_Query108", None)
                    
                    setattr(item, "PhotosMetaModel_Query108", self)
                    

    @property
    def PhotosMetaModel_User_p116(self):
        return self.__PhotosMetaModel_User_p116

    @PhotosMetaModel_User_p116.setter
    def PhotosMetaModel_User_p116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_User_p__PhotosMetaModel_User_p116", None)
        self.__PhotosMetaModel_User_p116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Cluster115"):
                opp_val = getattr(old_value, "PhotosMetaModel_Cluster115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Cluster115"):
                opp_val = getattr(value, "PhotosMetaModel_Cluster115", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_Cluster115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PhotosMetaModel_Row:

    def __init__(self, name: str, PhotosMetaModel_Row: "PhotosMetaModel_Table_p" = None, PhotosMetaModel_Row118: set["PhotosMetaModel_Policy"] = None):
        self.name = name
        self.PhotosMetaModel_Row = PhotosMetaModel_Row
        self.PhotosMetaModel_Row118 = PhotosMetaModel_Row118 if PhotosMetaModel_Row118 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_Row(self):
        return self.__PhotosMetaModel_Row

    @PhotosMetaModel_Row.setter
    def PhotosMetaModel_Row(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Row__PhotosMetaModel_Row", None)
        self.__PhotosMetaModel_Row = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Table_p85"):
                opp_val = getattr(old_value, "PhotosMetaModel_Table_p85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Table_p85"):
                opp_val = getattr(value, "PhotosMetaModel_Table_p85", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_Table_p85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhotosMetaModel_Row118(self):
        return self.__PhotosMetaModel_Row118

    @PhotosMetaModel_Row118.setter
    def PhotosMetaModel_Row118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Row__PhotosMetaModel_Row118", None)
        self.__PhotosMetaModel_Row118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Policy"):
                    opp_val = getattr(item, "PhotosMetaModel_Policy", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Policy", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Policy"):
                    opp_val = getattr(item, "PhotosMetaModel_Policy", None)
                    
                    setattr(item, "PhotosMetaModel_Policy", self)
                    

class PhotosMetaModel_Index_p:

    pass
class PhotosMetaModel_View:

    pass
class PhotosMetaModel_Trigger:

    pass
class PhotosMetaModel_Table_p:

    def __init__(self, name: str, PhotosMetaModel_Table_p: "PhotosMetaModel_ForeignKey" = None, PhotosMetaModel_Table_p82: set["PhotosMetaModel_Column_p"] = None, PhotosMetaModel_Table_p85: set["PhotosMetaModel_Row"] = None, PhotosMetaModel_Table_p87: set["PhotosMetaModel_ForeignKey"] = None, PhotosMetaModel_Table_p90: set["PhotosMetaModel_Column_p"] = None, PhotosMetaModel_Table_p94: "PhotosMetaModel_Table_p" = None, PhotosMetaModel_Table_p92: "PhotosMetaModel_Table_p" = None, PhotosMetaModel_Table_p98: "PhotosMetaModel_Scheme" = None):
        self.name = name
        self.PhotosMetaModel_Table_p = PhotosMetaModel_Table_p
        self.PhotosMetaModel_Table_p82 = PhotosMetaModel_Table_p82 if PhotosMetaModel_Table_p82 is not None else set()
        self.PhotosMetaModel_Table_p85 = PhotosMetaModel_Table_p85 if PhotosMetaModel_Table_p85 is not None else set()
        self.PhotosMetaModel_Table_p87 = PhotosMetaModel_Table_p87 if PhotosMetaModel_Table_p87 is not None else set()
        self.PhotosMetaModel_Table_p90 = PhotosMetaModel_Table_p90 if PhotosMetaModel_Table_p90 is not None else set()
        self.PhotosMetaModel_Table_p94 = PhotosMetaModel_Table_p94
        self.PhotosMetaModel_Table_p92 = PhotosMetaModel_Table_p92
        self.PhotosMetaModel_Table_p98 = PhotosMetaModel_Table_p98
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_Table_p92(self):
        return self.__PhotosMetaModel_Table_p92

    @PhotosMetaModel_Table_p92.setter
    def PhotosMetaModel_Table_p92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Table_p__PhotosMetaModel_Table_p92", None)
        self.__PhotosMetaModel_Table_p92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Table_p94"):
                opp_val = getattr(old_value, "PhotosMetaModel_Table_p94", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_Table_p94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Table_p94"):
                opp_val = getattr(value, "PhotosMetaModel_Table_p94", None)
                setattr(value, "PhotosMetaModel_Table_p94", self)

    @property
    def PhotosMetaModel_Table_p94(self):
        return self.__PhotosMetaModel_Table_p94

    @PhotosMetaModel_Table_p94.setter
    def PhotosMetaModel_Table_p94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Table_p__PhotosMetaModel_Table_p94", None)
        self.__PhotosMetaModel_Table_p94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Table_p92"):
                opp_val = getattr(old_value, "PhotosMetaModel_Table_p92", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_Table_p92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Table_p92"):
                opp_val = getattr(value, "PhotosMetaModel_Table_p92", None)
                setattr(value, "PhotosMetaModel_Table_p92", self)

    @property
    def PhotosMetaModel_Table_p98(self):
        return self.__PhotosMetaModel_Table_p98

    @PhotosMetaModel_Table_p98.setter
    def PhotosMetaModel_Table_p98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Table_p__PhotosMetaModel_Table_p98", None)
        self.__PhotosMetaModel_Table_p98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Scheme97"):
                opp_val = getattr(old_value, "PhotosMetaModel_Scheme97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Scheme97"):
                opp_val = getattr(value, "PhotosMetaModel_Scheme97", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_Scheme97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhotosMetaModel_Table_p82(self):
        return self.__PhotosMetaModel_Table_p82

    @PhotosMetaModel_Table_p82.setter
    def PhotosMetaModel_Table_p82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Table_p__PhotosMetaModel_Table_p82", None)
        self.__PhotosMetaModel_Table_p82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Column_p83"):
                    opp_val = getattr(item, "PhotosMetaModel_Column_p83", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Column_p83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Column_p83"):
                    opp_val = getattr(item, "PhotosMetaModel_Column_p83", None)
                    
                    setattr(item, "PhotosMetaModel_Column_p83", self)
                    

    @property
    def PhotosMetaModel_Table_p85(self):
        return self.__PhotosMetaModel_Table_p85

    @PhotosMetaModel_Table_p85.setter
    def PhotosMetaModel_Table_p85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Table_p__PhotosMetaModel_Table_p85", None)
        self.__PhotosMetaModel_Table_p85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Row"):
                    opp_val = getattr(item, "PhotosMetaModel_Row", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Row", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Row"):
                    opp_val = getattr(item, "PhotosMetaModel_Row", None)
                    
                    setattr(item, "PhotosMetaModel_Row", self)
                    

    @property
    def PhotosMetaModel_Table_p90(self):
        return self.__PhotosMetaModel_Table_p90

    @PhotosMetaModel_Table_p90.setter
    def PhotosMetaModel_Table_p90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Table_p__PhotosMetaModel_Table_p90", None)
        self.__PhotosMetaModel_Table_p90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Column_p91"):
                    opp_val = getattr(item, "PhotosMetaModel_Column_p91", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Column_p91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Column_p91"):
                    opp_val = getattr(item, "PhotosMetaModel_Column_p91", None)
                    
                    setattr(item, "PhotosMetaModel_Column_p91", self)
                    

    @property
    def PhotosMetaModel_Table_p(self):
        return self.__PhotosMetaModel_Table_p

    @PhotosMetaModel_Table_p.setter
    def PhotosMetaModel_Table_p(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Table_p__PhotosMetaModel_Table_p", None)
        self.__PhotosMetaModel_Table_p = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_ForeignKey80"):
                opp_val = getattr(old_value, "PhotosMetaModel_ForeignKey80", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_ForeignKey80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_ForeignKey80"):
                opp_val = getattr(value, "PhotosMetaModel_ForeignKey80", None)
                setattr(value, "PhotosMetaModel_ForeignKey80", self)

    @property
    def PhotosMetaModel_Table_p87(self):
        return self.__PhotosMetaModel_Table_p87

    @PhotosMetaModel_Table_p87.setter
    def PhotosMetaModel_Table_p87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Table_p__PhotosMetaModel_Table_p87", None)
        self.__PhotosMetaModel_Table_p87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_ForeignKey88"):
                    opp_val = getattr(item, "PhotosMetaModel_ForeignKey88", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_ForeignKey88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_ForeignKey88"):
                    opp_val = getattr(item, "PhotosMetaModel_ForeignKey88", None)
                    
                    setattr(item, "PhotosMetaModel_ForeignKey88", self)
                    

class PhotosMetaModel_Database:

    def __init__(self, name: str, PhotosMetaModel_Database: set["PhotosMetaModel_Scheme"] = None, PhotosMetaModel_Database113: "PhotosMetaModel_Cluster" = None):
        self.name = name
        self.PhotosMetaModel_Database = PhotosMetaModel_Database if PhotosMetaModel_Database is not None else set()
        self.PhotosMetaModel_Database113 = PhotosMetaModel_Database113
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_Database113(self):
        return self.__PhotosMetaModel_Database113

    @PhotosMetaModel_Database113.setter
    def PhotosMetaModel_Database113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Database__PhotosMetaModel_Database113", None)
        self.__PhotosMetaModel_Database113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Cluster112"):
                opp_val = getattr(old_value, "PhotosMetaModel_Cluster112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Cluster112"):
                opp_val = getattr(value, "PhotosMetaModel_Cluster112", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_Cluster112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhotosMetaModel_Database(self):
        return self.__PhotosMetaModel_Database

    @PhotosMetaModel_Database.setter
    def PhotosMetaModel_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Database__PhotosMetaModel_Database", None)
        self.__PhotosMetaModel_Database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Scheme"):
                    opp_val = getattr(item, "PhotosMetaModel_Scheme", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Scheme", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Scheme"):
                    opp_val = getattr(item, "PhotosMetaModel_Scheme", None)
                    
                    setattr(item, "PhotosMetaModel_Scheme", self)
                    

class PhotosMetaModel_Function_p:

    pass
class PhotosMetaModel_Clause:

    pass
class PhotosMetaModel_Query:

    pass
class PhotosMetaModel_Cluster:

    pass
class PhotosMetaModel_Order_s:

    pass
class PhotosMetaModel_EnableGlobalMethodSecurity:

    pass
class PhotosMetaModel_EnableAuthorizationServer:

    pass
class PhotosMetaModel_ForeignKey:

    pass
class PhotosMetaModel_Bean:

    pass
class PhotosMetaModel_Predicate:

    pass
class PhotosMetaModel_SearchCriteria:

    pass
class PhotosMetaModel_DataType:

    def __init__(self, name: str, PhotosMetaModel_DataType: "PhotosMetaModel_Column_p" = None, PhotosMetaModel_DataType120: "PhotosMetaModel_Column" = None):
        self.name = name
        self.PhotosMetaModel_DataType = PhotosMetaModel_DataType
        self.PhotosMetaModel_DataType120 = PhotosMetaModel_DataType120
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_DataType(self):
        return self.__PhotosMetaModel_DataType

    @PhotosMetaModel_DataType.setter
    def PhotosMetaModel_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_DataType__PhotosMetaModel_DataType", None)
        self.__PhotosMetaModel_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Column_p57"):
                opp_val = getattr(old_value, "PhotosMetaModel_Column_p57", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_Column_p57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Column_p57"):
                opp_val = getattr(value, "PhotosMetaModel_Column_p57", None)
                setattr(value, "PhotosMetaModel_Column_p57", self)

    @property
    def PhotosMetaModel_DataType120(self):
        return self.__PhotosMetaModel_DataType120

    @PhotosMetaModel_DataType120.setter
    def PhotosMetaModel_DataType120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_DataType__PhotosMetaModel_DataType120", None)
        self.__PhotosMetaModel_DataType120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Column"):
                opp_val = getattr(old_value, "PhotosMetaModel_Column", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_Column", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Column"):
                opp_val = getattr(value, "PhotosMetaModel_Column", None)
                setattr(value, "PhotosMetaModel_Column", self)

class PhotosMetaModel_Constraint:

    pass
class PhotosMetaModel_Column_p:

    def __init__(self, name: str, PhotosMetaModel_Column_p: set["PhotosMetaModel_Constraint"] = None, PhotosMetaModel_Column_p57: "PhotosMetaModel_DataType" = None, PhotosMetaModel_Column_p78: "PhotosMetaModel_ForeignKey" = None, PhotosMetaModel_Column_p83: "PhotosMetaModel_Table_p" = None, PhotosMetaModel_Column_p91: "PhotosMetaModel_Table_p" = None):
        self.name = name
        self.PhotosMetaModel_Column_p = PhotosMetaModel_Column_p if PhotosMetaModel_Column_p is not None else set()
        self.PhotosMetaModel_Column_p57 = PhotosMetaModel_Column_p57
        self.PhotosMetaModel_Column_p78 = PhotosMetaModel_Column_p78
        self.PhotosMetaModel_Column_p83 = PhotosMetaModel_Column_p83
        self.PhotosMetaModel_Column_p91 = PhotosMetaModel_Column_p91
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_Column_p78(self):
        return self.__PhotosMetaModel_Column_p78

    @PhotosMetaModel_Column_p78.setter
    def PhotosMetaModel_Column_p78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Column_p__PhotosMetaModel_Column_p78", None)
        self.__PhotosMetaModel_Column_p78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_ForeignKey"):
                opp_val = getattr(old_value, "PhotosMetaModel_ForeignKey", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_ForeignKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_ForeignKey"):
                opp_val = getattr(value, "PhotosMetaModel_ForeignKey", None)
                setattr(value, "PhotosMetaModel_ForeignKey", self)

    @property
    def PhotosMetaModel_Column_p83(self):
        return self.__PhotosMetaModel_Column_p83

    @PhotosMetaModel_Column_p83.setter
    def PhotosMetaModel_Column_p83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Column_p__PhotosMetaModel_Column_p83", None)
        self.__PhotosMetaModel_Column_p83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Table_p82"):
                opp_val = getattr(old_value, "PhotosMetaModel_Table_p82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Table_p82"):
                opp_val = getattr(value, "PhotosMetaModel_Table_p82", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_Table_p82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhotosMetaModel_Column_p(self):
        return self.__PhotosMetaModel_Column_p

    @PhotosMetaModel_Column_p.setter
    def PhotosMetaModel_Column_p(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Column_p__PhotosMetaModel_Column_p", None)
        self.__PhotosMetaModel_Column_p = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Constraint"):
                    opp_val = getattr(item, "PhotosMetaModel_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Constraint"):
                    opp_val = getattr(item, "PhotosMetaModel_Constraint", None)
                    
                    setattr(item, "PhotosMetaModel_Constraint", self)
                    

    @property
    def PhotosMetaModel_Column_p57(self):
        return self.__PhotosMetaModel_Column_p57

    @PhotosMetaModel_Column_p57.setter
    def PhotosMetaModel_Column_p57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Column_p__PhotosMetaModel_Column_p57", None)
        self.__PhotosMetaModel_Column_p57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_DataType"):
                opp_val = getattr(old_value, "PhotosMetaModel_DataType", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_DataType"):
                opp_val = getattr(value, "PhotosMetaModel_DataType", None)
                setattr(value, "PhotosMetaModel_DataType", self)

    @property
    def PhotosMetaModel_Column_p91(self):
        return self.__PhotosMetaModel_Column_p91

    @PhotosMetaModel_Column_p91.setter
    def PhotosMetaModel_Column_p91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Column_p__PhotosMetaModel_Column_p91", None)
        self.__PhotosMetaModel_Column_p91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Table_p90"):
                opp_val = getattr(old_value, "PhotosMetaModel_Table_p90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Table_p90"):
                opp_val = getattr(value, "PhotosMetaModel_Table_p90", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_Table_p90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PhotosMetaModel_EnableResourceServer:

    pass
class PhotosMetaModel_EnableWebSecurity:

    pass
class PhotosMetaModel_Id:

    pass
class PhotosMetaModel_Column_s:

    def __init__(self, name: str, PhotosMetaModel_Column_s: "PhotosMetaModel_Table_s" = None):
        self.name = name
        self.PhotosMetaModel_Column_s = PhotosMetaModel_Column_s
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_Column_s(self):
        return self.__PhotosMetaModel_Column_s

    @PhotosMetaModel_Column_s.setter
    def PhotosMetaModel_Column_s(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Column_s__PhotosMetaModel_Column_s", None)
        self.__PhotosMetaModel_Column_s = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Table_s50"):
                opp_val = getattr(old_value, "PhotosMetaModel_Table_s50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Table_s50"):
                opp_val = getattr(value, "PhotosMetaModel_Table_s50", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_Table_s50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PhotosMetaModel_NamedNativeQuery:

    pass
class PhotosMetaModel_Table_s:

    def __init__(self, name: str, PhotosMetaModel_Table_s: "PhotosMetaModel_Entity" = None, PhotosMetaModel_Table_s50: set["PhotosMetaModel_Column_s"] = None, PhotosMetaModel_Table_s52: "PhotosMetaModel_Id" = None):
        self.name = name
        self.PhotosMetaModel_Table_s = PhotosMetaModel_Table_s
        self.PhotosMetaModel_Table_s50 = PhotosMetaModel_Table_s50 if PhotosMetaModel_Table_s50 is not None else set()
        self.PhotosMetaModel_Table_s52 = PhotosMetaModel_Table_s52
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_Table_s52(self):
        return self.__PhotosMetaModel_Table_s52

    @PhotosMetaModel_Table_s52.setter
    def PhotosMetaModel_Table_s52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Table_s__PhotosMetaModel_Table_s52", None)
        self.__PhotosMetaModel_Table_s52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Id"):
                opp_val = getattr(old_value, "PhotosMetaModel_Id", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_Id", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Id"):
                opp_val = getattr(value, "PhotosMetaModel_Id", None)
                setattr(value, "PhotosMetaModel_Id", self)

    @property
    def PhotosMetaModel_Table_s(self):
        return self.__PhotosMetaModel_Table_s

    @PhotosMetaModel_Table_s.setter
    def PhotosMetaModel_Table_s(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Table_s__PhotosMetaModel_Table_s", None)
        self.__PhotosMetaModel_Table_s = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Entity46"):
                opp_val = getattr(old_value, "PhotosMetaModel_Entity46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Entity46"):
                opp_val = getattr(value, "PhotosMetaModel_Entity46", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_Entity46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PhotosMetaModel_Table_s50(self):
        return self.__PhotosMetaModel_Table_s50

    @PhotosMetaModel_Table_s50.setter
    def PhotosMetaModel_Table_s50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Table_s__PhotosMetaModel_Table_s50", None)
        self.__PhotosMetaModel_Table_s50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Column_s"):
                    opp_val = getattr(item, "PhotosMetaModel_Column_s", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Column_s", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Column_s"):
                    opp_val = getattr(item, "PhotosMetaModel_Column_s", None)
                    
                    setattr(item, "PhotosMetaModel_Column_s", self)
                    

class PhotosMetaModel_Exception:

    pass
class PhotosMetaModel_GeneratedValue:

    pass
class RequestMapping:

    pass
class PhotosMetaModel_DeleteMapping(RequestMapping):

    pass
class PhotosMetaModel_PostMapping(RequestMapping):

    pass
class PhotosMetaModel_RequestPart:

    pass
class PhotosMetaModel_Configuration:

    pass
class PhotosMetaModel_Component:

    pass
class PhotosMetaModel_PutMapping(RequestMapping):

    pass
class PhotosMetaModel_GetMapping(RequestMapping):

    pass
class PhotosMetaModel_Specification:

    pass
class PhotosMetaModel_Autowired:

    pass
class PhotosMetaModel_ExceptionHandler:

    pass
class PhotosMetaModel_RequestMapping:

    pass
class PhotosMetaModel_RestController:

    def __init__(self, name: str, PhotosMetaModel_RestController34: "PhotosMetaModel_SpringBootApplication" = None, PhotosMetaModel_RestController: set["PhotosMetaModel_RequestMapping"] = None, PhotosMetaModel_RestController25: set["PhotosMetaModel_ExceptionHandler"] = None, PhotosMetaModel_RestController27: set["PhotosMetaModel_Autowired"] = None, PhotosMetaModel_RestController29: set["PhotosMetaModel_Specification"] = None):
        self.name = name
        self.PhotosMetaModel_RestController34 = PhotosMetaModel_RestController34
        self.PhotosMetaModel_RestController = PhotosMetaModel_RestController if PhotosMetaModel_RestController is not None else set()
        self.PhotosMetaModel_RestController25 = PhotosMetaModel_RestController25 if PhotosMetaModel_RestController25 is not None else set()
        self.PhotosMetaModel_RestController27 = PhotosMetaModel_RestController27 if PhotosMetaModel_RestController27 is not None else set()
        self.PhotosMetaModel_RestController29 = PhotosMetaModel_RestController29 if PhotosMetaModel_RestController29 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_RestController(self):
        return self.__PhotosMetaModel_RestController

    @PhotosMetaModel_RestController.setter
    def PhotosMetaModel_RestController(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_RestController__PhotosMetaModel_RestController", None)
        self.__PhotosMetaModel_RestController = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_RequestMapping"):
                    opp_val = getattr(item, "PhotosMetaModel_RequestMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_RequestMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_RequestMapping"):
                    opp_val = getattr(item, "PhotosMetaModel_RequestMapping", None)
                    
                    setattr(item, "PhotosMetaModel_RequestMapping", self)
                    

    @property
    def PhotosMetaModel_RestController25(self):
        return self.__PhotosMetaModel_RestController25

    @PhotosMetaModel_RestController25.setter
    def PhotosMetaModel_RestController25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_RestController__PhotosMetaModel_RestController25", None)
        self.__PhotosMetaModel_RestController25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_ExceptionHandler"):
                    opp_val = getattr(item, "PhotosMetaModel_ExceptionHandler", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_ExceptionHandler", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_ExceptionHandler"):
                    opp_val = getattr(item, "PhotosMetaModel_ExceptionHandler", None)
                    
                    setattr(item, "PhotosMetaModel_ExceptionHandler", self)
                    

    @property
    def PhotosMetaModel_RestController27(self):
        return self.__PhotosMetaModel_RestController27

    @PhotosMetaModel_RestController27.setter
    def PhotosMetaModel_RestController27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_RestController__PhotosMetaModel_RestController27", None)
        self.__PhotosMetaModel_RestController27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Autowired"):
                    opp_val = getattr(item, "PhotosMetaModel_Autowired", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Autowired", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Autowired"):
                    opp_val = getattr(item, "PhotosMetaModel_Autowired", None)
                    
                    setattr(item, "PhotosMetaModel_Autowired", self)
                    

    @property
    def PhotosMetaModel_RestController29(self):
        return self.__PhotosMetaModel_RestController29

    @PhotosMetaModel_RestController29.setter
    def PhotosMetaModel_RestController29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_RestController__PhotosMetaModel_RestController29", None)
        self.__PhotosMetaModel_RestController29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PhotosMetaModel_Specification"):
                    opp_val = getattr(item, "PhotosMetaModel_Specification", None)
                    
                    if opp_val == self:
                        setattr(item, "PhotosMetaModel_Specification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PhotosMetaModel_Specification"):
                    opp_val = getattr(item, "PhotosMetaModel_Specification", None)
                    
                    setattr(item, "PhotosMetaModel_Specification", self)
                    

    @property
    def PhotosMetaModel_RestController34(self):
        return self.__PhotosMetaModel_RestController34

    @PhotosMetaModel_RestController34.setter
    def PhotosMetaModel_RestController34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_RestController__PhotosMetaModel_RestController34", None)
        self.__PhotosMetaModel_RestController34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_SpringBootApplication33"):
                opp_val = getattr(old_value, "PhotosMetaModel_SpringBootApplication33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_SpringBootApplication33"):
                opp_val = getattr(value, "PhotosMetaModel_SpringBootApplication33", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_SpringBootApplication33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PhotosMetaModel_Repository:

    pass
class PhotosMetaModel_Modules:

    def __init__(self, name: str, PhotosMetaModel_Modules: "PhotosMetaModel_React" = None, PhotosMetaModel_Modules167: "PhotosMetaModel_Components" = None):
        self.name = name
        self.PhotosMetaModel_Modules = PhotosMetaModel_Modules
        self.PhotosMetaModel_Modules167 = PhotosMetaModel_Modules167
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PhotosMetaModel_Modules167(self):
        return self.__PhotosMetaModel_Modules167

    @PhotosMetaModel_Modules167.setter
    def PhotosMetaModel_Modules167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Modules__PhotosMetaModel_Modules167", None)
        self.__PhotosMetaModel_Modules167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Components166"):
                opp_val = getattr(old_value, "PhotosMetaModel_Components166", None)
                if opp_val == self:
                    setattr(old_value, "PhotosMetaModel_Components166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Components166"):
                opp_val = getattr(value, "PhotosMetaModel_Components166", None)
                setattr(value, "PhotosMetaModel_Components166", self)

    @property
    def PhotosMetaModel_Modules(self):
        return self.__PhotosMetaModel_Modules

    @PhotosMetaModel_Modules.setter
    def PhotosMetaModel_Modules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Modules__PhotosMetaModel_Modules", None)
        self.__PhotosMetaModel_Modules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_React22"):
                opp_val = getattr(old_value, "PhotosMetaModel_React22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_React22"):
                opp_val = getattr(value, "PhotosMetaModel_React22", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_React22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PhotosMetaModel_SpringBootApplication:

    pass
class PhotosMetaModel_AmazonWebServices:

    pass
class PhotosMetaModel_React:

    pass
class PhotosMetaModel_PostgreSQL:

    pass
class PhotosMetaModel_Spring:

    pass
class PhotosMetaModel_NTier:

    pass
class PhotosMetaModel_Entity:

    pass
class PhotosMetaModel_Technology:

    pass
class PhotosMetaModel_Architecture:

    pass
class PhotosMetaModel_Domain:

    pass
class PhotosMetaModel_SoftGallery:

    pass
class PhotosMetaModel_Entities:

    def __init__(self, id: str, PhotosMetaModel_Entities: "PhotosMetaModel_Domain" = None):
        self.id = id
        self.PhotosMetaModel_Entities = PhotosMetaModel_Entities
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def PhotosMetaModel_Entities(self):
        return self.__PhotosMetaModel_Entities

    @PhotosMetaModel_Entities.setter
    def PhotosMetaModel_Entities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PhotosMetaModel_Entities__PhotosMetaModel_Entities", None)
        self.__PhotosMetaModel_Entities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PhotosMetaModel_Domain8"):
                opp_val = getattr(old_value, "PhotosMetaModel_Domain8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PhotosMetaModel_Domain8"):
                opp_val = getattr(value, "PhotosMetaModel_Domain8", None)
                if opp_val is None:
                    setattr(value, "PhotosMetaModel_Domain8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PhotosMetaModel_Functionalities:

    pass