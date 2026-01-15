from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class softGalleryLanguage_BucketAccess:

    pass
class softGalleryLanguage_Bucket:

    def __init__(self, name: str, softGalleryLanguage_Bucket: set["softGalleryLanguage_EObject"] = None):
        self.name = name
        self.softGalleryLanguage_Bucket = softGalleryLanguage_Bucket if softGalleryLanguage_Bucket is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_Bucket(self):
        return self.__softGalleryLanguage_Bucket

    @softGalleryLanguage_Bucket.setter
    def softGalleryLanguage_Bucket(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Bucket__softGalleryLanguage_Bucket", None)
        self.__softGalleryLanguage_Bucket = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_EObject257"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject257", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_EObject257", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_EObject257"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject257", None)
                    
                    setattr(item, "softGalleryLanguage_EObject257", self)
                    

class softGalleryLanguage_BatchOperation:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_AmazonSimpleStorageService:

    pass
class softGalleryLanguage_Clause:

    def __init__(self, name: str, softGalleryLanguage_Clause: "softGalleryLanguage_Query" = None):
        self.name = name
        self.softGalleryLanguage_Clause = softGalleryLanguage_Clause
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_Clause(self):
        return self.__softGalleryLanguage_Clause

    @softGalleryLanguage_Clause.setter
    def softGalleryLanguage_Clause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Clause__softGalleryLanguage_Clause", None)
        self.__softGalleryLanguage_Clause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_Query"):
                opp_val = getattr(old_value, "softGalleryLanguage_Query", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_Query"):
                opp_val = getattr(value, "softGalleryLanguage_Query", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_Query", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_Query:

    pass
class softGalleryLanguage_Privilege:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_AmazonElasticComputeCloud:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_Metadata:

    def __init__(self, name: str, softGalleryLanguage_Metadata: "softGalleryLanguage_AmazonFile" = None):
        self.name = name
        self.softGalleryLanguage_Metadata = softGalleryLanguage_Metadata
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_Metadata(self):
        return self.__softGalleryLanguage_Metadata

    @softGalleryLanguage_Metadata.setter
    def softGalleryLanguage_Metadata(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Metadata__softGalleryLanguage_Metadata", None)
        self.__softGalleryLanguage_Metadata = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_AmazonFile"):
                opp_val = getattr(old_value, "softGalleryLanguage_AmazonFile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_AmazonFile"):
                opp_val = getattr(value, "softGalleryLanguage_AmazonFile", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_AmazonFile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_AmazonFile:

    pass
class softGalleryLanguage_AmazonFolder:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_OnlyAuthorized:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_BucketObjectsNotPublic:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_ObjectsPublic:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_PublicAccess:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_ColumnP:

    def __init__(self, name: str, softGalleryLanguage_ColumnP: set["softGalleryLanguage_EObject"] = None):
        self.name = name
        self.softGalleryLanguage_ColumnP = softGalleryLanguage_ColumnP if softGalleryLanguage_ColumnP is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_ColumnP(self):
        return self.__softGalleryLanguage_ColumnP

    @softGalleryLanguage_ColumnP.setter
    def softGalleryLanguage_ColumnP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ColumnP__softGalleryLanguage_ColumnP", None)
        self.__softGalleryLanguage_ColumnP = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_EObject246"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject246", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_EObject246", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_EObject246"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject246", None)
                    
                    setattr(item, "softGalleryLanguage_EObject246", self)
                    

class softGalleryLanguage_RefTable_p:

    def __init__(self, name: str, softGalleryLanguage_RefTable_p: "softGalleryLanguage_ForeignKeyRef" = None):
        self.name = name
        self.softGalleryLanguage_RefTable_p = softGalleryLanguage_RefTable_p
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_RefTable_p(self):
        return self.__softGalleryLanguage_RefTable_p

    @softGalleryLanguage_RefTable_p.setter
    def softGalleryLanguage_RefTable_p(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_RefTable_p__softGalleryLanguage_RefTable_p", None)
        self.__softGalleryLanguage_RefTable_p = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ForeignKeyRef"):
                opp_val = getattr(old_value, "softGalleryLanguage_ForeignKeyRef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ForeignKeyRef"):
                opp_val = getattr(value, "softGalleryLanguage_ForeignKeyRef", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ForeignKeyRef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ForeignKeyRef:

    pass
class softGalleryLanguage_ForeignKey_n:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_ForeignKey:

    pass
class softGalleryLanguage_Table_p:

    def __init__(self, name: str, softGalleryLanguage_Table_p: set["softGalleryLanguage_EObject"] = None):
        self.name = name
        self.softGalleryLanguage_Table_p = softGalleryLanguage_Table_p if softGalleryLanguage_Table_p is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_Table_p(self):
        return self.__softGalleryLanguage_Table_p

    @softGalleryLanguage_Table_p.setter
    def softGalleryLanguage_Table_p(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Table_p__softGalleryLanguage_Table_p", None)
        self.__softGalleryLanguage_Table_p = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_EObject241"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject241", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_EObject241", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_EObject241"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject241", None)
                    
                    setattr(item, "softGalleryLanguage_EObject241", self)
                    

class softGalleryLanguage_ViewSchema:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_Index_p:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_PostgresUser:

    def __init__(self, name: str, softGalleryLanguage_PostgresUser: set["softGalleryLanguage_EObject"] = None):
        self.name = name
        self.softGalleryLanguage_PostgresUser = softGalleryLanguage_PostgresUser if softGalleryLanguage_PostgresUser is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_PostgresUser(self):
        return self.__softGalleryLanguage_PostgresUser

    @softGalleryLanguage_PostgresUser.setter
    def softGalleryLanguage_PostgresUser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_PostgresUser__softGalleryLanguage_PostgresUser", None)
        self.__softGalleryLanguage_PostgresUser = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_EObject249"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject249", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_EObject249", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_EObject249"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject249", None)
                    
                    setattr(item, "softGalleryLanguage_EObject249", self)
                    

class softGalleryLanguage_Function:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_Trigger:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_Policy:

    def __init__(self, name: str, softGalleryLanguage_Policy: "softGalleryLanguage_Row" = None):
        self.name = name
        self.softGalleryLanguage_Policy = softGalleryLanguage_Policy
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_Policy(self):
        return self.__softGalleryLanguage_Policy

    @softGalleryLanguage_Policy.setter
    def softGalleryLanguage_Policy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Policy__softGalleryLanguage_Policy", None)
        self.__softGalleryLanguage_Policy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_Row"):
                opp_val = getattr(old_value, "softGalleryLanguage_Row", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_Row"):
                opp_val = getattr(value, "softGalleryLanguage_Row", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_Row", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_Row:

    def __init__(self, name: str, softGalleryLanguage_Row: set["softGalleryLanguage_Policy"] = None):
        self.name = name
        self.softGalleryLanguage_Row = softGalleryLanguage_Row if softGalleryLanguage_Row is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_Row(self):
        return self.__softGalleryLanguage_Row

    @softGalleryLanguage_Row.setter
    def softGalleryLanguage_Row(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Row__softGalleryLanguage_Row", None)
        self.__softGalleryLanguage_Row = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_Policy"):
                    opp_val = getattr(item, "softGalleryLanguage_Policy", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_Policy", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_Policy"):
                    opp_val = getattr(item, "softGalleryLanguage_Policy", None)
                    
                    setattr(item, "softGalleryLanguage_Policy", self)
                    

class softGalleryLanguage_Constraint:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_DatatypeDB:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_ReactLibrary:

    def __init__(self, name: str, softGalleryLanguage_ReactLibrary: "softGalleryLanguage_ReactLibraries" = None):
        self.name = name
        self.softGalleryLanguage_ReactLibrary = softGalleryLanguage_ReactLibrary
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_ReactLibrary(self):
        return self.__softGalleryLanguage_ReactLibrary

    @softGalleryLanguage_ReactLibrary.setter
    def softGalleryLanguage_ReactLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactLibrary__softGalleryLanguage_ReactLibrary", None)
        self.__softGalleryLanguage_ReactLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ReactLibraries228"):
                opp_val = getattr(old_value, "softGalleryLanguage_ReactLibraries228", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ReactLibraries228"):
                opp_val = getattr(value, "softGalleryLanguage_ReactLibraries228", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ReactLibraries228", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ReactsRelationServ:

    def __init__(self, name: str, softGalleryLanguage_ReactsRelationServ: "softGalleryLanguage_ReactServicesRelation" = None, softGalleryLanguage_ReactsRelationServ225: set["softGalleryLanguage_ReactServicesType"] = None):
        self.name = name
        self.softGalleryLanguage_ReactsRelationServ = softGalleryLanguage_ReactsRelationServ
        self.softGalleryLanguage_ReactsRelationServ225 = softGalleryLanguage_ReactsRelationServ225 if softGalleryLanguage_ReactsRelationServ225 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_ReactsRelationServ225(self):
        return self.__softGalleryLanguage_ReactsRelationServ225

    @softGalleryLanguage_ReactsRelationServ225.setter
    def softGalleryLanguage_ReactsRelationServ225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactsRelationServ__softGalleryLanguage_ReactsRelationServ225", None)
        self.__softGalleryLanguage_ReactsRelationServ225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_ReactServicesType226"):
                    opp_val = getattr(item, "softGalleryLanguage_ReactServicesType226", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_ReactServicesType226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_ReactServicesType226"):
                    opp_val = getattr(item, "softGalleryLanguage_ReactServicesType226", None)
                    
                    setattr(item, "softGalleryLanguage_ReactServicesType226", self)
                    

    @property
    def softGalleryLanguage_ReactsRelationServ(self):
        return self.__softGalleryLanguage_ReactsRelationServ

    @softGalleryLanguage_ReactsRelationServ.setter
    def softGalleryLanguage_ReactsRelationServ(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactsRelationServ__softGalleryLanguage_ReactsRelationServ", None)
        self.__softGalleryLanguage_ReactsRelationServ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ReactServicesRelation223"):
                opp_val = getattr(old_value, "softGalleryLanguage_ReactServicesRelation223", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ReactServicesRelation223"):
                opp_val = getattr(value, "softGalleryLanguage_ReactServicesRelation223", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ReactServicesRelation223", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ReactServiceRequestProps:

    def __init__(self, reqPropName: str, reqPropDescription: str, softGalleryLanguage_ReactServiceRequestProps: "softGalleryLanguage_ReactServiceContRequest" = None):
        self.reqPropName = reqPropName
        self.reqPropDescription = reqPropDescription
        self.softGalleryLanguage_ReactServiceRequestProps = softGalleryLanguage_ReactServiceRequestProps
        
    @property
    def reqPropDescription(self) -> str:
        return self.__reqPropDescription

    @reqPropDescription.setter
    def reqPropDescription(self, reqPropDescription: str):
        self.__reqPropDescription = reqPropDescription

    @property
    def reqPropName(self) -> str:
        return self.__reqPropName

    @reqPropName.setter
    def reqPropName(self, reqPropName: str):
        self.__reqPropName = reqPropName

    @property
    def softGalleryLanguage_ReactServiceRequestProps(self):
        return self.__softGalleryLanguage_ReactServiceRequestProps

    @softGalleryLanguage_ReactServiceRequestProps.setter
    def softGalleryLanguage_ReactServiceRequestProps(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactServiceRequestProps__softGalleryLanguage_ReactServiceRequestProps", None)
        self.__softGalleryLanguage_ReactServiceRequestProps = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ReactServiceContRequest221"):
                opp_val = getattr(old_value, "softGalleryLanguage_ReactServiceContRequest221", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ReactServiceContRequest221"):
                opp_val = getattr(value, "softGalleryLanguage_ReactServiceContRequest221", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ReactServiceContRequest221", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ReactServiceContRequest:

    pass
class softGalleryLanguage_Schema:

    pass
class softGalleryLanguage_Database:

    def __init__(self, name: str, softGalleryLanguage_Database: set["softGalleryLanguage_Schema"] = None):
        self.name = name
        self.softGalleryLanguage_Database = softGalleryLanguage_Database if softGalleryLanguage_Database is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_Database(self):
        return self.__softGalleryLanguage_Database

    @softGalleryLanguage_Database.setter
    def softGalleryLanguage_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Database__softGalleryLanguage_Database", None)
        self.__softGalleryLanguage_Database = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_Schema"):
                    opp_val = getattr(item, "softGalleryLanguage_Schema", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_Schema", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_Schema"):
                    opp_val = getattr(item, "softGalleryLanguage_Schema", None)
                    
                    setattr(item, "softGalleryLanguage_Schema", self)
                    

class softGalleryLanguage_Cluster:

    pass
class softGalleryLanguage_ReactInformation:

    def __init__(self, name: str, softGalleryLanguage_ReactInformation: "softGalleryLanguage_ReactInfo" = None):
        self.name = name
        self.softGalleryLanguage_ReactInformation = softGalleryLanguage_ReactInformation
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_ReactInformation(self):
        return self.__softGalleryLanguage_ReactInformation

    @softGalleryLanguage_ReactInformation.setter
    def softGalleryLanguage_ReactInformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactInformation__softGalleryLanguage_ReactInformation", None)
        self.__softGalleryLanguage_ReactInformation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ReactInfo230"):
                opp_val = getattr(old_value, "softGalleryLanguage_ReactInfo230", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ReactInfo230"):
                opp_val = getattr(value, "softGalleryLanguage_ReactInfo230", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ReactInfo230", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_PropsType:

    def __init__(self, nameProps: str, propsdatas: str, softGalleryLanguage_PropsType: "softGalleryLanguage_Props" = None):
        self.nameProps = nameProps
        self.propsdatas = propsdatas
        self.softGalleryLanguage_PropsType = softGalleryLanguage_PropsType
        
    @property
    def propsdatas(self) -> str:
        return self.__propsdatas

    @propsdatas.setter
    def propsdatas(self, propsdatas: str):
        self.__propsdatas = propsdatas

    @property
    def nameProps(self) -> str:
        return self.__nameProps

    @nameProps.setter
    def nameProps(self, nameProps: str):
        self.__nameProps = nameProps

    @property
    def softGalleryLanguage_PropsType(self):
        return self.__softGalleryLanguage_PropsType

    @softGalleryLanguage_PropsType.setter
    def softGalleryLanguage_PropsType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_PropsType__softGalleryLanguage_PropsType", None)
        self.__softGalleryLanguage_PropsType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_Props206"):
                opp_val = getattr(old_value, "softGalleryLanguage_Props206", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_Props206"):
                opp_val = getattr(value, "softGalleryLanguage_Props206", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_Props206", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_StateContent:

    def __init__(self, stateName: str, componentdatatyp: str, softGalleryLanguage_StateContent: "softGalleryLanguage_State" = None):
        self.stateName = stateName
        self.componentdatatyp = componentdatatyp
        self.softGalleryLanguage_StateContent = softGalleryLanguage_StateContent
        
    @property
    def stateName(self) -> str:
        return self.__stateName

    @stateName.setter
    def stateName(self, stateName: str):
        self.__stateName = stateName

    @property
    def componentdatatyp(self) -> str:
        return self.__componentdatatyp

    @componentdatatyp.setter
    def componentdatatyp(self, componentdatatyp: str):
        self.__componentdatatyp = componentdatatyp

    @property
    def softGalleryLanguage_StateContent(self):
        return self.__softGalleryLanguage_StateContent

    @softGalleryLanguage_StateContent.setter
    def softGalleryLanguage_StateContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_StateContent__softGalleryLanguage_StateContent", None)
        self.__softGalleryLanguage_StateContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_State204"):
                opp_val = getattr(old_value, "softGalleryLanguage_State204", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_State204"):
                opp_val = getattr(value, "softGalleryLanguage_State204", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_State204", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_CoreFunctionsDeclaration:

    def __init__(self, name: str, softGalleryLanguage_CoreFunctionsDeclaration: "softGalleryLanguage_ReactConstructor" = None):
        self.name = name
        self.softGalleryLanguage_CoreFunctionsDeclaration = softGalleryLanguage_CoreFunctionsDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_CoreFunctionsDeclaration(self):
        return self.__softGalleryLanguage_CoreFunctionsDeclaration

    @softGalleryLanguage_CoreFunctionsDeclaration.setter
    def softGalleryLanguage_CoreFunctionsDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_CoreFunctionsDeclaration__softGalleryLanguage_CoreFunctionsDeclaration", None)
        self.__softGalleryLanguage_CoreFunctionsDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ReactConstructor202"):
                opp_val = getattr(old_value, "softGalleryLanguage_ReactConstructor202", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ReactConstructor202"):
                opp_val = getattr(value, "softGalleryLanguage_ReactConstructor202", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ReactConstructor202", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_State:

    pass
class softGalleryLanguage_ReactServiceContent:

    def __init__(self, functName: str, softGalleryLanguage_ReactServiceContent: "softGalleryLanguage_ReactServicesType" = None, softGalleryLanguage_ReactServiceContent219: set["softGalleryLanguage_ReactServiceContRequest"] = None):
        self.functName = functName
        self.softGalleryLanguage_ReactServiceContent = softGalleryLanguage_ReactServiceContent
        self.softGalleryLanguage_ReactServiceContent219 = softGalleryLanguage_ReactServiceContent219 if softGalleryLanguage_ReactServiceContent219 is not None else set()
        
    @property
    def functName(self) -> str:
        return self.__functName

    @functName.setter
    def functName(self, functName: str):
        self.__functName = functName

    @property
    def softGalleryLanguage_ReactServiceContent219(self):
        return self.__softGalleryLanguage_ReactServiceContent219

    @softGalleryLanguage_ReactServiceContent219.setter
    def softGalleryLanguage_ReactServiceContent219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactServiceContent__softGalleryLanguage_ReactServiceContent219", None)
        self.__softGalleryLanguage_ReactServiceContent219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_ReactServiceContRequest"):
                    opp_val = getattr(item, "softGalleryLanguage_ReactServiceContRequest", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_ReactServiceContRequest", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_ReactServiceContRequest"):
                    opp_val = getattr(item, "softGalleryLanguage_ReactServiceContRequest", None)
                    
                    setattr(item, "softGalleryLanguage_ReactServiceContRequest", self)
                    

    @property
    def softGalleryLanguage_ReactServiceContent(self):
        return self.__softGalleryLanguage_ReactServiceContent

    @softGalleryLanguage_ReactServiceContent.setter
    def softGalleryLanguage_ReactServiceContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactServiceContent__softGalleryLanguage_ReactServiceContent", None)
        self.__softGalleryLanguage_ReactServiceContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ReactServicesType"):
                opp_val = getattr(old_value, "softGalleryLanguage_ReactServicesType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ReactServicesType"):
                opp_val = getattr(value, "softGalleryLanguage_ReactServicesType", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ReactServicesType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ReactServicesType:

    def __init__(self, name: str, softGalleryLanguage_ReactServicesType: set["softGalleryLanguage_ReactServiceContent"] = None, softGalleryLanguage_ReactServicesType226: "softGalleryLanguage_ReactsRelationServ" = None):
        self.name = name
        self.softGalleryLanguage_ReactServicesType = softGalleryLanguage_ReactServicesType if softGalleryLanguage_ReactServicesType is not None else set()
        self.softGalleryLanguage_ReactServicesType226 = softGalleryLanguage_ReactServicesType226
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_ReactServicesType(self):
        return self.__softGalleryLanguage_ReactServicesType

    @softGalleryLanguage_ReactServicesType.setter
    def softGalleryLanguage_ReactServicesType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactServicesType__softGalleryLanguage_ReactServicesType", None)
        self.__softGalleryLanguage_ReactServicesType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_ReactServiceContent"):
                    opp_val = getattr(item, "softGalleryLanguage_ReactServiceContent", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_ReactServiceContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_ReactServiceContent"):
                    opp_val = getattr(item, "softGalleryLanguage_ReactServiceContent", None)
                    
                    setattr(item, "softGalleryLanguage_ReactServiceContent", self)
                    

    @property
    def softGalleryLanguage_ReactServicesType226(self):
        return self.__softGalleryLanguage_ReactServicesType226

    @softGalleryLanguage_ReactServicesType226.setter
    def softGalleryLanguage_ReactServicesType226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactServicesType__softGalleryLanguage_ReactServicesType226", None)
        self.__softGalleryLanguage_ReactServicesType226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ReactsRelationServ225"):
                opp_val = getattr(old_value, "softGalleryLanguage_ReactsRelationServ225", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ReactsRelationServ225"):
                opp_val = getattr(value, "softGalleryLanguage_ReactsRelationServ225", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ReactsRelationServ225", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ReactServicesRelation:

    pass
class softGalleryLanguage_ReactActionsContent:

    pass
class softGalleryLanguage_StylePropertiesContent:

    def __init__(self, propName: str, softGalleryLanguage_StylePropertiesContent: "softGalleryLanguage_StyleProperties" = None):
        self.propName = propName
        self.softGalleryLanguage_StylePropertiesContent = softGalleryLanguage_StylePropertiesContent
        
    @property
    def propName(self) -> str:
        return self.__propName

    @propName.setter
    def propName(self, propName: str):
        self.__propName = propName

    @property
    def softGalleryLanguage_StylePropertiesContent(self):
        return self.__softGalleryLanguage_StylePropertiesContent

    @softGalleryLanguage_StylePropertiesContent.setter
    def softGalleryLanguage_StylePropertiesContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_StylePropertiesContent__softGalleryLanguage_StylePropertiesContent", None)
        self.__softGalleryLanguage_StylePropertiesContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_StyleProperties212"):
                opp_val = getattr(old_value, "softGalleryLanguage_StyleProperties212", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_StyleProperties212"):
                opp_val = getattr(value, "softGalleryLanguage_StyleProperties212", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_StyleProperties212", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_StyleProperties:

    pass
class softGalleryLanguage_ComponentsStylesContent:

    def __init__(self, nameStyle: str, softGalleryLanguage_ComponentsStylesContent: "softGalleryLanguage_ComponentsStyles" = None, softGalleryLanguage_ComponentsStylesContent210: set["softGalleryLanguage_StyleProperties"] = None):
        self.nameStyle = nameStyle
        self.softGalleryLanguage_ComponentsStylesContent = softGalleryLanguage_ComponentsStylesContent
        self.softGalleryLanguage_ComponentsStylesContent210 = softGalleryLanguage_ComponentsStylesContent210 if softGalleryLanguage_ComponentsStylesContent210 is not None else set()
        
    @property
    def nameStyle(self) -> str:
        return self.__nameStyle

    @nameStyle.setter
    def nameStyle(self, nameStyle: str):
        self.__nameStyle = nameStyle

    @property
    def softGalleryLanguage_ComponentsStylesContent210(self):
        return self.__softGalleryLanguage_ComponentsStylesContent210

    @softGalleryLanguage_ComponentsStylesContent210.setter
    def softGalleryLanguage_ComponentsStylesContent210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ComponentsStylesContent__softGalleryLanguage_ComponentsStylesContent210", None)
        self.__softGalleryLanguage_ComponentsStylesContent210 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_StyleProperties"):
                    opp_val = getattr(item, "softGalleryLanguage_StyleProperties", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_StyleProperties", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_StyleProperties"):
                    opp_val = getattr(item, "softGalleryLanguage_StyleProperties", None)
                    
                    setattr(item, "softGalleryLanguage_StyleProperties", self)
                    

    @property
    def softGalleryLanguage_ComponentsStylesContent(self):
        return self.__softGalleryLanguage_ComponentsStylesContent

    @softGalleryLanguage_ComponentsStylesContent.setter
    def softGalleryLanguage_ComponentsStylesContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ComponentsStylesContent__softGalleryLanguage_ComponentsStylesContent", None)
        self.__softGalleryLanguage_ComponentsStylesContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ComponentsStyles208"):
                opp_val = getattr(old_value, "softGalleryLanguage_ComponentsStyles208", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ComponentsStyles208"):
                opp_val = getattr(value, "softGalleryLanguage_ComponentsStyles208", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ComponentsStyles208", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_SubcomponentCont:

    def __init__(self, nameSubComp: str, softGalleryLanguage_SubcomponentCont185: set["softGalleryLanguage_ComponentClass"] = None, softGalleryLanguage_SubcomponentCont: "softGalleryLanguage_UIContent" = None):
        self.nameSubComp = nameSubComp
        self.softGalleryLanguage_SubcomponentCont185 = softGalleryLanguage_SubcomponentCont185 if softGalleryLanguage_SubcomponentCont185 is not None else set()
        self.softGalleryLanguage_SubcomponentCont = softGalleryLanguage_SubcomponentCont
        
    @property
    def nameSubComp(self) -> str:
        return self.__nameSubComp

    @nameSubComp.setter
    def nameSubComp(self, nameSubComp: str):
        self.__nameSubComp = nameSubComp

    @property
    def softGalleryLanguage_SubcomponentCont185(self):
        return self.__softGalleryLanguage_SubcomponentCont185

    @softGalleryLanguage_SubcomponentCont185.setter
    def softGalleryLanguage_SubcomponentCont185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_SubcomponentCont__softGalleryLanguage_SubcomponentCont185", None)
        self.__softGalleryLanguage_SubcomponentCont185 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_ComponentClass186"):
                    opp_val = getattr(item, "softGalleryLanguage_ComponentClass186", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_ComponentClass186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_ComponentClass186"):
                    opp_val = getattr(item, "softGalleryLanguage_ComponentClass186", None)
                    
                    setattr(item, "softGalleryLanguage_ComponentClass186", self)
                    

    @property
    def softGalleryLanguage_SubcomponentCont(self):
        return self.__softGalleryLanguage_SubcomponentCont

    @softGalleryLanguage_SubcomponentCont.setter
    def softGalleryLanguage_SubcomponentCont(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_SubcomponentCont__softGalleryLanguage_SubcomponentCont", None)
        self.__softGalleryLanguage_SubcomponentCont = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_UIContent180"):
                opp_val = getattr(old_value, "softGalleryLanguage_UIContent180", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_UIContent180"):
                opp_val = getattr(value, "softGalleryLanguage_UIContent180", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_UIContent180", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ViewComponentCont:

    def __init__(self, nameView: str, softGalleryLanguage_ViewComponentCont: "softGalleryLanguage_UIContent" = None, softGalleryLanguage_ViewComponentCont182: set["softGalleryLanguage_ComponentClass"] = None):
        self.nameView = nameView
        self.softGalleryLanguage_ViewComponentCont = softGalleryLanguage_ViewComponentCont
        self.softGalleryLanguage_ViewComponentCont182 = softGalleryLanguage_ViewComponentCont182 if softGalleryLanguage_ViewComponentCont182 is not None else set()
        
    @property
    def nameView(self) -> str:
        return self.__nameView

    @nameView.setter
    def nameView(self, nameView: str):
        self.__nameView = nameView

    @property
    def softGalleryLanguage_ViewComponentCont182(self):
        return self.__softGalleryLanguage_ViewComponentCont182

    @softGalleryLanguage_ViewComponentCont182.setter
    def softGalleryLanguage_ViewComponentCont182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ViewComponentCont__softGalleryLanguage_ViewComponentCont182", None)
        self.__softGalleryLanguage_ViewComponentCont182 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_ComponentClass183"):
                    opp_val = getattr(item, "softGalleryLanguage_ComponentClass183", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_ComponentClass183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_ComponentClass183"):
                    opp_val = getattr(item, "softGalleryLanguage_ComponentClass183", None)
                    
                    setattr(item, "softGalleryLanguage_ComponentClass183", self)
                    

    @property
    def softGalleryLanguage_ViewComponentCont(self):
        return self.__softGalleryLanguage_ViewComponentCont

    @softGalleryLanguage_ViewComponentCont.setter
    def softGalleryLanguage_ViewComponentCont(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ViewComponentCont__softGalleryLanguage_ViewComponentCont", None)
        self.__softGalleryLanguage_ViewComponentCont = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_UIContent178"):
                opp_val = getattr(old_value, "softGalleryLanguage_UIContent178", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_UIContent178"):
                opp_val = getattr(value, "softGalleryLanguage_UIContent178", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_UIContent178", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_UIContent:

    pass
class softGalleryLanguage_ComponentClass:

    pass
class softGalleryLanguage_LogicStructure:

    def __init__(self, appComName: str, indexCompName: str, softGalleryLanguage_LogicStructure: "softGalleryLanguage_LogicContent" = None, softGalleryLanguage_LogicStructure174: set["softGalleryLanguage_ComponentClass"] = None):
        self.appComName = appComName
        self.indexCompName = indexCompName
        self.softGalleryLanguage_LogicStructure = softGalleryLanguage_LogicStructure
        self.softGalleryLanguage_LogicStructure174 = softGalleryLanguage_LogicStructure174 if softGalleryLanguage_LogicStructure174 is not None else set()
        
    @property
    def indexCompName(self) -> str:
        return self.__indexCompName

    @indexCompName.setter
    def indexCompName(self, indexCompName: str):
        self.__indexCompName = indexCompName

    @property
    def appComName(self) -> str:
        return self.__appComName

    @appComName.setter
    def appComName(self, appComName: str):
        self.__appComName = appComName

    @property
    def softGalleryLanguage_LogicStructure174(self):
        return self.__softGalleryLanguage_LogicStructure174

    @softGalleryLanguage_LogicStructure174.setter
    def softGalleryLanguage_LogicStructure174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_LogicStructure__softGalleryLanguage_LogicStructure174", None)
        self.__softGalleryLanguage_LogicStructure174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_ComponentClass"):
                    opp_val = getattr(item, "softGalleryLanguage_ComponentClass", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_ComponentClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_ComponentClass"):
                    opp_val = getattr(item, "softGalleryLanguage_ComponentClass", None)
                    
                    setattr(item, "softGalleryLanguage_ComponentClass", self)
                    

    @property
    def softGalleryLanguage_LogicStructure(self):
        return self.__softGalleryLanguage_LogicStructure

    @softGalleryLanguage_LogicStructure.setter
    def softGalleryLanguage_LogicStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_LogicStructure__softGalleryLanguage_LogicStructure", None)
        self.__softGalleryLanguage_LogicStructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_LogicContent172"):
                opp_val = getattr(old_value, "softGalleryLanguage_LogicContent172", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_LogicContent172"):
                opp_val = getattr(value, "softGalleryLanguage_LogicContent172", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_LogicContent172", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ReactCoreFunctions:

    def __init__(self, name: str, softGalleryLanguage_ReactCoreFunctions: "softGalleryLanguage_ReactFunctions" = None):
        self.name = name
        self.softGalleryLanguage_ReactCoreFunctions = softGalleryLanguage_ReactCoreFunctions
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_ReactCoreFunctions(self):
        return self.__softGalleryLanguage_ReactCoreFunctions

    @softGalleryLanguage_ReactCoreFunctions.setter
    def softGalleryLanguage_ReactCoreFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactCoreFunctions__softGalleryLanguage_ReactCoreFunctions", None)
        self.__softGalleryLanguage_ReactCoreFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ReactFunctions198"):
                opp_val = getattr(old_value, "softGalleryLanguage_ReactFunctions198", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ReactFunctions198"):
                opp_val = getattr(value, "softGalleryLanguage_ReactFunctions198", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ReactFunctions198", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ReactConstructor:

    pass
class softGalleryLanguage_ReactImportContent:

    def __init__(self, impName: str, softGalleryLanguage_ReactImportContent: "softGalleryLanguage_ReactImports" = None):
        self.impName = impName
        self.softGalleryLanguage_ReactImportContent = softGalleryLanguage_ReactImportContent
        
    @property
    def impName(self) -> str:
        return self.__impName

    @impName.setter
    def impName(self, impName: str):
        self.__impName = impName

    @property
    def softGalleryLanguage_ReactImportContent(self):
        return self.__softGalleryLanguage_ReactImportContent

    @softGalleryLanguage_ReactImportContent.setter
    def softGalleryLanguage_ReactImportContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactImportContent__softGalleryLanguage_ReactImportContent", None)
        self.__softGalleryLanguage_ReactImportContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ReactImports194"):
                opp_val = getattr(old_value, "softGalleryLanguage_ReactImports194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ReactImports194"):
                opp_val = getattr(value, "softGalleryLanguage_ReactImports194", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ReactImports194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_Props:

    pass
class softGalleryLanguage_ReactFunctions:

    def __init__(self, lifecycleclass: str, renderclass: str, softGalleryLanguage_ReactFunctions: "softGalleryLanguage_ComponentClass" = None, softGalleryLanguage_ReactFunctions196: set["softGalleryLanguage_ReactConstructor"] = None, softGalleryLanguage_ReactFunctions198: set["softGalleryLanguage_ReactCoreFunctions"] = None):
        self.lifecycleclass = lifecycleclass
        self.renderclass = renderclass
        self.softGalleryLanguage_ReactFunctions = softGalleryLanguage_ReactFunctions
        self.softGalleryLanguage_ReactFunctions196 = softGalleryLanguage_ReactFunctions196 if softGalleryLanguage_ReactFunctions196 is not None else set()
        self.softGalleryLanguage_ReactFunctions198 = softGalleryLanguage_ReactFunctions198 if softGalleryLanguage_ReactFunctions198 is not None else set()
        
    @property
    def renderclass(self) -> str:
        return self.__renderclass

    @renderclass.setter
    def renderclass(self, renderclass: str):
        self.__renderclass = renderclass

    @property
    def lifecycleclass(self) -> str:
        return self.__lifecycleclass

    @lifecycleclass.setter
    def lifecycleclass(self, lifecycleclass: str):
        self.__lifecycleclass = lifecycleclass

    @property
    def softGalleryLanguage_ReactFunctions(self):
        return self.__softGalleryLanguage_ReactFunctions

    @softGalleryLanguage_ReactFunctions.setter
    def softGalleryLanguage_ReactFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactFunctions__softGalleryLanguage_ReactFunctions", None)
        self.__softGalleryLanguage_ReactFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ComponentClass190"):
                opp_val = getattr(old_value, "softGalleryLanguage_ComponentClass190", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ComponentClass190"):
                opp_val = getattr(value, "softGalleryLanguage_ComponentClass190", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ComponentClass190", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softGalleryLanguage_ReactFunctions198(self):
        return self.__softGalleryLanguage_ReactFunctions198

    @softGalleryLanguage_ReactFunctions198.setter
    def softGalleryLanguage_ReactFunctions198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactFunctions__softGalleryLanguage_ReactFunctions198", None)
        self.__softGalleryLanguage_ReactFunctions198 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_ReactCoreFunctions"):
                    opp_val = getattr(item, "softGalleryLanguage_ReactCoreFunctions", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_ReactCoreFunctions", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_ReactCoreFunctions"):
                    opp_val = getattr(item, "softGalleryLanguage_ReactCoreFunctions", None)
                    
                    setattr(item, "softGalleryLanguage_ReactCoreFunctions", self)
                    

    @property
    def softGalleryLanguage_ReactFunctions196(self):
        return self.__softGalleryLanguage_ReactFunctions196

    @softGalleryLanguage_ReactFunctions196.setter
    def softGalleryLanguage_ReactFunctions196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactFunctions__softGalleryLanguage_ReactFunctions196", None)
        self.__softGalleryLanguage_ReactFunctions196 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_ReactConstructor"):
                    opp_val = getattr(item, "softGalleryLanguage_ReactConstructor", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_ReactConstructor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_ReactConstructor"):
                    opp_val = getattr(item, "softGalleryLanguage_ReactConstructor", None)
                    
                    setattr(item, "softGalleryLanguage_ReactConstructor", self)
                    

class softGalleryLanguage_ReactImports:

    pass
class softGalleryLanguage_PackageName:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_SingleDependencies:

    pass
class softGalleryLanguage_ReactDependenciesSubRules:

    pass
class softGalleryLanguage_ReactDependenciesRules:

    def __init__(self, name: str, softGalleryLanguage_ReactDependenciesRules: "softGalleryLanguage_ReactDependencies" = None, softGalleryLanguage_ReactDependenciesRules155: set["softGalleryLanguage_ReactDependenciesSubRules"] = None):
        self.name = name
        self.softGalleryLanguage_ReactDependenciesRules = softGalleryLanguage_ReactDependenciesRules
        self.softGalleryLanguage_ReactDependenciesRules155 = softGalleryLanguage_ReactDependenciesRules155 if softGalleryLanguage_ReactDependenciesRules155 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_ReactDependenciesRules155(self):
        return self.__softGalleryLanguage_ReactDependenciesRules155

    @softGalleryLanguage_ReactDependenciesRules155.setter
    def softGalleryLanguage_ReactDependenciesRules155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactDependenciesRules__softGalleryLanguage_ReactDependenciesRules155", None)
        self.__softGalleryLanguage_ReactDependenciesRules155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_ReactDependenciesSubRules"):
                    opp_val = getattr(item, "softGalleryLanguage_ReactDependenciesSubRules", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_ReactDependenciesSubRules", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_ReactDependenciesSubRules"):
                    opp_val = getattr(item, "softGalleryLanguage_ReactDependenciesSubRules", None)
                    
                    setattr(item, "softGalleryLanguage_ReactDependenciesSubRules", self)
                    

    @property
    def softGalleryLanguage_ReactDependenciesRules(self):
        return self.__softGalleryLanguage_ReactDependenciesRules

    @softGalleryLanguage_ReactDependenciesRules.setter
    def softGalleryLanguage_ReactDependenciesRules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactDependenciesRules__softGalleryLanguage_ReactDependenciesRules", None)
        self.__softGalleryLanguage_ReactDependenciesRules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ReactDependencies153"):
                opp_val = getattr(old_value, "softGalleryLanguage_ReactDependencies153", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ReactDependencies153"):
                opp_val = getattr(value, "softGalleryLanguage_ReactDependencies153", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ReactDependencies153", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ReactConfigurations:

    def __init__(self, name: str, softGalleryLanguage_ReactConfigurations162: set["softGalleryLanguage_DOMConfigurations"] = None, softGalleryLanguage_ReactConfigurations: "softGalleryLanguage_ReactConfiguration" = None):
        self.name = name
        self.softGalleryLanguage_ReactConfigurations162 = softGalleryLanguage_ReactConfigurations162 if softGalleryLanguage_ReactConfigurations162 is not None else set()
        self.softGalleryLanguage_ReactConfigurations = softGalleryLanguage_ReactConfigurations
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_ReactConfigurations162(self):
        return self.__softGalleryLanguage_ReactConfigurations162

    @softGalleryLanguage_ReactConfigurations162.setter
    def softGalleryLanguage_ReactConfigurations162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactConfigurations__softGalleryLanguage_ReactConfigurations162", None)
        self.__softGalleryLanguage_ReactConfigurations162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_DOMConfigurations"):
                    opp_val = getattr(item, "softGalleryLanguage_DOMConfigurations", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_DOMConfigurations", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_DOMConfigurations"):
                    opp_val = getattr(item, "softGalleryLanguage_DOMConfigurations", None)
                    
                    setattr(item, "softGalleryLanguage_DOMConfigurations", self)
                    

    @property
    def softGalleryLanguage_ReactConfigurations(self):
        return self.__softGalleryLanguage_ReactConfigurations

    @softGalleryLanguage_ReactConfigurations.setter
    def softGalleryLanguage_ReactConfigurations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ReactConfigurations__softGalleryLanguage_ReactConfigurations", None)
        self.__softGalleryLanguage_ReactConfigurations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ReactConfiguration151"):
                opp_val = getattr(old_value, "softGalleryLanguage_ReactConfiguration151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ReactConfiguration151"):
                opp_val = getattr(value, "softGalleryLanguage_ReactConfiguration151", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ReactConfiguration151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ReactDependencies:

    pass
class softGalleryLanguage_ReactInfo:

    pass
class softGalleryLanguage_ReactLibraries:

    pass
class softGalleryLanguage_LogicContent:

    def __init__(self, name: str, softGalleryLanguage_LogicContent: "softGalleryLanguage_ComponentsLogic" = None, softGalleryLanguage_LogicContent172: set["softGalleryLanguage_LogicStructure"] = None):
        self.name = name
        self.softGalleryLanguage_LogicContent = softGalleryLanguage_LogicContent
        self.softGalleryLanguage_LogicContent172 = softGalleryLanguage_LogicContent172 if softGalleryLanguage_LogicContent172 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_LogicContent(self):
        return self.__softGalleryLanguage_LogicContent

    @softGalleryLanguage_LogicContent.setter
    def softGalleryLanguage_LogicContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_LogicContent__softGalleryLanguage_LogicContent", None)
        self.__softGalleryLanguage_LogicContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ComponentsLogic170"):
                opp_val = getattr(old_value, "softGalleryLanguage_ComponentsLogic170", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ComponentsLogic170"):
                opp_val = getattr(value, "softGalleryLanguage_ComponentsLogic170", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ComponentsLogic170", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softGalleryLanguage_LogicContent172(self):
        return self.__softGalleryLanguage_LogicContent172

    @softGalleryLanguage_LogicContent172.setter
    def softGalleryLanguage_LogicContent172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_LogicContent__softGalleryLanguage_LogicContent172", None)
        self.__softGalleryLanguage_LogicContent172 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_LogicStructure"):
                    opp_val = getattr(item, "softGalleryLanguage_LogicStructure", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_LogicStructure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_LogicStructure"):
                    opp_val = getattr(item, "softGalleryLanguage_LogicStructure", None)
                    
                    setattr(item, "softGalleryLanguage_LogicStructure", self)
                    

class softGalleryLanguage_ComponentsStyles:

    pass
class softGalleryLanguage_ComponentsUI:

    def __init__(self, name: str, softGalleryLanguage_ComponentsUI: "softGalleryLanguage_ReactComponents" = None, softGalleryLanguage_ComponentsUI176: set["softGalleryLanguage_UIContent"] = None):
        self.name = name
        self.softGalleryLanguage_ComponentsUI = softGalleryLanguage_ComponentsUI
        self.softGalleryLanguage_ComponentsUI176 = softGalleryLanguage_ComponentsUI176 if softGalleryLanguage_ComponentsUI176 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_ComponentsUI176(self):
        return self.__softGalleryLanguage_ComponentsUI176

    @softGalleryLanguage_ComponentsUI176.setter
    def softGalleryLanguage_ComponentsUI176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ComponentsUI__softGalleryLanguage_ComponentsUI176", None)
        self.__softGalleryLanguage_ComponentsUI176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_UIContent"):
                    opp_val = getattr(item, "softGalleryLanguage_UIContent", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_UIContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_UIContent"):
                    opp_val = getattr(item, "softGalleryLanguage_UIContent", None)
                    
                    setattr(item, "softGalleryLanguage_UIContent", self)
                    

    @property
    def softGalleryLanguage_ComponentsUI(self):
        return self.__softGalleryLanguage_ComponentsUI

    @softGalleryLanguage_ComponentsUI.setter
    def softGalleryLanguage_ComponentsUI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ComponentsUI__softGalleryLanguage_ComponentsUI", None)
        self.__softGalleryLanguage_ComponentsUI = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ReactComponents166"):
                opp_val = getattr(old_value, "softGalleryLanguage_ReactComponents166", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ReactComponents166"):
                opp_val = getattr(value, "softGalleryLanguage_ReactComponents166", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ReactComponents166", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ComponentsLogic:

    def __init__(self, name: str, softGalleryLanguage_ComponentsLogic: "softGalleryLanguage_ReactComponents" = None, softGalleryLanguage_ComponentsLogic170: set["softGalleryLanguage_LogicContent"] = None):
        self.name = name
        self.softGalleryLanguage_ComponentsLogic = softGalleryLanguage_ComponentsLogic
        self.softGalleryLanguage_ComponentsLogic170 = softGalleryLanguage_ComponentsLogic170 if softGalleryLanguage_ComponentsLogic170 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_ComponentsLogic(self):
        return self.__softGalleryLanguage_ComponentsLogic

    @softGalleryLanguage_ComponentsLogic.setter
    def softGalleryLanguage_ComponentsLogic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ComponentsLogic__softGalleryLanguage_ComponentsLogic", None)
        self.__softGalleryLanguage_ComponentsLogic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ReactComponents164"):
                opp_val = getattr(old_value, "softGalleryLanguage_ReactComponents164", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ReactComponents164"):
                opp_val = getattr(value, "softGalleryLanguage_ReactComponents164", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ReactComponents164", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softGalleryLanguage_ComponentsLogic170(self):
        return self.__softGalleryLanguage_ComponentsLogic170

    @softGalleryLanguage_ComponentsLogic170.setter
    def softGalleryLanguage_ComponentsLogic170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ComponentsLogic__softGalleryLanguage_ComponentsLogic170", None)
        self.__softGalleryLanguage_ComponentsLogic170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_LogicContent"):
                    opp_val = getattr(item, "softGalleryLanguage_LogicContent", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_LogicContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_LogicContent"):
                    opp_val = getattr(item, "softGalleryLanguage_LogicContent", None)
                    
                    setattr(item, "softGalleryLanguage_LogicContent", self)
                    

class softGalleryLanguage_DOMConfigurations:

    def __init__(self, elements: str, name: str, softGalleryLanguage_DOMConfigurations: "softGalleryLanguage_ReactConfigurations" = None):
        self.elements = elements
        self.name = name
        self.softGalleryLanguage_DOMConfigurations = softGalleryLanguage_DOMConfigurations
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def elements(self) -> str:
        return self.__elements

    @elements.setter
    def elements(self, elements: str):
        self.__elements = elements

    @property
    def softGalleryLanguage_DOMConfigurations(self):
        return self.__softGalleryLanguage_DOMConfigurations

    @softGalleryLanguage_DOMConfigurations.setter
    def softGalleryLanguage_DOMConfigurations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_DOMConfigurations__softGalleryLanguage_DOMConfigurations", None)
        self.__softGalleryLanguage_DOMConfigurations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ReactConfigurations162"):
                opp_val = getattr(old_value, "softGalleryLanguage_ReactConfigurations162", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ReactConfigurations162"):
                opp_val = getattr(value, "softGalleryLanguage_ReactConfigurations162", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ReactConfigurations162", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_PackageVersion:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_StorageActionReturn:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_StorageActionAnnotation:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_StorageAction:

    def __init__(self, name: str, softGalleryLanguage_StorageAction: set["softGalleryLanguage_EObject"] = None):
        self.name = name
        self.softGalleryLanguage_StorageAction = softGalleryLanguage_StorageAction if softGalleryLanguage_StorageAction is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_StorageAction(self):
        return self.__softGalleryLanguage_StorageAction

    @softGalleryLanguage_StorageAction.setter
    def softGalleryLanguage_StorageAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_StorageAction__softGalleryLanguage_StorageAction", None)
        self.__softGalleryLanguage_StorageAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_EObject131"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject131", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_EObject131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_EObject131"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject131", None)
                    
                    setattr(item, "softGalleryLanguage_EObject131", self)
                    

class softGalleryLanguage_StorageMemberAnnotation:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_StorageMemberType:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_StorageMember:

    def __init__(self, name: str, softGalleryLanguage_StorageMember: set["softGalleryLanguage_EObject"] = None):
        self.name = name
        self.softGalleryLanguage_StorageMember = softGalleryLanguage_StorageMember if softGalleryLanguage_StorageMember is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_StorageMember(self):
        return self.__softGalleryLanguage_StorageMember

    @softGalleryLanguage_StorageMember.setter
    def softGalleryLanguage_StorageMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_StorageMember__softGalleryLanguage_StorageMember", None)
        self.__softGalleryLanguage_StorageMember = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_EObject129"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject129", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_EObject129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_EObject129"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject129", None)
                    
                    setattr(item, "softGalleryLanguage_EObject129", self)
                    

class softGalleryLanguage_StorageClient:

    def __init__(self, name: str, softGalleryLanguage_StorageClient: set["softGalleryLanguage_EObject"] = None):
        self.name = name
        self.softGalleryLanguage_StorageClient = softGalleryLanguage_StorageClient if softGalleryLanguage_StorageClient is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_StorageClient(self):
        return self.__softGalleryLanguage_StorageClient

    @softGalleryLanguage_StorageClient.setter
    def softGalleryLanguage_StorageClient(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_StorageClient__softGalleryLanguage_StorageClient", None)
        self.__softGalleryLanguage_StorageClient = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_EObject127"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject127", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_EObject127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_EObject127"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject127", None)
                    
                    setattr(item, "softGalleryLanguage_EObject127", self)
                    

class softGalleryLanguage_SpringEntityAnnotationTypes:

    def __init__(self, name: str, softGalleryLanguage_SpringEntityAnnotationTypes: "softGalleryLanguage_SpringEntity" = None):
        self.name = name
        self.softGalleryLanguage_SpringEntityAnnotationTypes = softGalleryLanguage_SpringEntityAnnotationTypes
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_SpringEntityAnnotationTypes(self):
        return self.__softGalleryLanguage_SpringEntityAnnotationTypes

    @softGalleryLanguage_SpringEntityAnnotationTypes.setter
    def softGalleryLanguage_SpringEntityAnnotationTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_SpringEntityAnnotationTypes__softGalleryLanguage_SpringEntityAnnotationTypes", None)
        self.__softGalleryLanguage_SpringEntityAnnotationTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_SpringEntity"):
                opp_val = getattr(old_value, "softGalleryLanguage_SpringEntity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_SpringEntity"):
                opp_val = getattr(value, "softGalleryLanguage_SpringEntity", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_SpringEntity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_SpringEntity:

    pass
class softGalleryLanguage_ReactActions:

    pass
class softGalleryLanguage_ReactComponents:

    pass
class softGalleryLanguage_ReactConfiguration:

    pass
class softGalleryLanguage_ReactSubModules:

    pass
class softGalleryLanguage_ReactModules:

    pass
class softGalleryLanguage_StorageActionMemberName:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_StorageActionMemberType:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_StorageActionMember:

    pass
class softGalleryLanguage_RequestMappingProduces:

    def __init__(self, name: str, softGalleryLanguage_RequestMappingProduces: "softGalleryLanguage_RequestMapping" = None):
        self.name = name
        self.softGalleryLanguage_RequestMappingProduces = softGalleryLanguage_RequestMappingProduces
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_RequestMappingProduces(self):
        return self.__softGalleryLanguage_RequestMappingProduces

    @softGalleryLanguage_RequestMappingProduces.setter
    def softGalleryLanguage_RequestMappingProduces(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_RequestMappingProduces__softGalleryLanguage_RequestMappingProduces", None)
        self.__softGalleryLanguage_RequestMappingProduces = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_RequestMapping120"):
                opp_val = getattr(old_value, "softGalleryLanguage_RequestMapping120", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_RequestMapping120"):
                opp_val = getattr(value, "softGalleryLanguage_RequestMapping120", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_RequestMapping120", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_RequestMappingMethod:

    def __init__(self, name: str, softGalleryLanguage_RequestMappingMethod: "softGalleryLanguage_RequestMapping" = None):
        self.name = name
        self.softGalleryLanguage_RequestMappingMethod = softGalleryLanguage_RequestMappingMethod
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_RequestMappingMethod(self):
        return self.__softGalleryLanguage_RequestMappingMethod

    @softGalleryLanguage_RequestMappingMethod.setter
    def softGalleryLanguage_RequestMappingMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_RequestMappingMethod__softGalleryLanguage_RequestMappingMethod", None)
        self.__softGalleryLanguage_RequestMappingMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_RequestMapping118"):
                opp_val = getattr(old_value, "softGalleryLanguage_RequestMapping118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_RequestMapping118"):
                opp_val = getattr(value, "softGalleryLanguage_RequestMapping118", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_RequestMapping118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_RequestMappingValue:

    def __init__(self, name: str, softGalleryLanguage_RequestMappingValue: "softGalleryLanguage_RequestMapping" = None):
        self.name = name
        self.softGalleryLanguage_RequestMappingValue = softGalleryLanguage_RequestMappingValue
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_RequestMappingValue(self):
        return self.__softGalleryLanguage_RequestMappingValue

    @softGalleryLanguage_RequestMappingValue.setter
    def softGalleryLanguage_RequestMappingValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_RequestMappingValue__softGalleryLanguage_RequestMappingValue", None)
        self.__softGalleryLanguage_RequestMappingValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_RequestMapping"):
                opp_val = getattr(old_value, "softGalleryLanguage_RequestMapping", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_RequestMapping"):
                opp_val = getattr(value, "softGalleryLanguage_RequestMapping", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_RequestMapping", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MappingType:

    pass
class softGalleryLanguage_PostMapping(MappingType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_RequestMapping(MappingType):

    pass
class softGalleryLanguage_ResponseParameter:

    pass
class softGalleryLanguage_MappingType:

    pass
class softGalleryLanguage_ResponseEntity:

    def __init__(self, name: str, softGalleryLanguage_ResponseEntity: set["softGalleryLanguage_MappingType"] = None, softGalleryLanguage_ResponseEntity115: set["softGalleryLanguage_ResponseParameter"] = None):
        self.name = name
        self.softGalleryLanguage_ResponseEntity = softGalleryLanguage_ResponseEntity if softGalleryLanguage_ResponseEntity is not None else set()
        self.softGalleryLanguage_ResponseEntity115 = softGalleryLanguage_ResponseEntity115 if softGalleryLanguage_ResponseEntity115 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_ResponseEntity(self):
        return self.__softGalleryLanguage_ResponseEntity

    @softGalleryLanguage_ResponseEntity.setter
    def softGalleryLanguage_ResponseEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ResponseEntity__softGalleryLanguage_ResponseEntity", None)
        self.__softGalleryLanguage_ResponseEntity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_MappingType"):
                    opp_val = getattr(item, "softGalleryLanguage_MappingType", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_MappingType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_MappingType"):
                    opp_val = getattr(item, "softGalleryLanguage_MappingType", None)
                    
                    setattr(item, "softGalleryLanguage_MappingType", self)
                    

    @property
    def softGalleryLanguage_ResponseEntity115(self):
        return self.__softGalleryLanguage_ResponseEntity115

    @softGalleryLanguage_ResponseEntity115.setter
    def softGalleryLanguage_ResponseEntity115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ResponseEntity__softGalleryLanguage_ResponseEntity115", None)
        self.__softGalleryLanguage_ResponseEntity115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_ResponseParameter"):
                    opp_val = getattr(item, "softGalleryLanguage_ResponseParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_ResponseParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_ResponseParameter"):
                    opp_val = getattr(item, "softGalleryLanguage_ResponseParameter", None)
                    
                    setattr(item, "softGalleryLanguage_ResponseParameter", self)
                    

class softGalleryLanguage_Autowired:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_ExceptionProcess:

    def __init__(self, name: str, softGalleryLanguage_ExceptionProcess: "softGalleryLanguage_ExceptionHandler" = None):
        self.name = name
        self.softGalleryLanguage_ExceptionProcess = softGalleryLanguage_ExceptionProcess
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_ExceptionProcess(self):
        return self.__softGalleryLanguage_ExceptionProcess

    @softGalleryLanguage_ExceptionProcess.setter
    def softGalleryLanguage_ExceptionProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ExceptionProcess__softGalleryLanguage_ExceptionProcess", None)
        self.__softGalleryLanguage_ExceptionProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ExceptionHandler"):
                opp_val = getattr(old_value, "softGalleryLanguage_ExceptionHandler", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ExceptionHandler"):
                opp_val = getattr(value, "softGalleryLanguage_ExceptionHandler", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ExceptionHandler", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ExceptionHandler:

    def __init__(self, name: str, softGalleryLanguage_ExceptionHandler: set["softGalleryLanguage_ExceptionProcess"] = None):
        self.name = name
        self.softGalleryLanguage_ExceptionHandler = softGalleryLanguage_ExceptionHandler if softGalleryLanguage_ExceptionHandler is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_ExceptionHandler(self):
        return self.__softGalleryLanguage_ExceptionHandler

    @softGalleryLanguage_ExceptionHandler.setter
    def softGalleryLanguage_ExceptionHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ExceptionHandler__softGalleryLanguage_ExceptionHandler", None)
        self.__softGalleryLanguage_ExceptionHandler = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_ExceptionProcess"):
                    opp_val = getattr(item, "softGalleryLanguage_ExceptionProcess", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_ExceptionProcess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_ExceptionProcess"):
                    opp_val = getattr(item, "softGalleryLanguage_ExceptionProcess", None)
                    
                    setattr(item, "softGalleryLanguage_ExceptionProcess", self)
                    

class softGalleryLanguage_ResponseParameterName:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_ResponseParameterType:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_ResponseParameterAnnotation:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_DeleteMapping(MappingType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_PutMapping(MappingType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_GetMapping(MappingType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_OrderSpring:

    def __init__(self, name: str, softGalleryLanguage_OrderSpring: "softGalleryLanguage_SpringComponent" = None):
        self.name = name
        self.softGalleryLanguage_OrderSpring = softGalleryLanguage_OrderSpring
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_OrderSpring(self):
        return self.__softGalleryLanguage_OrderSpring

    @softGalleryLanguage_OrderSpring.setter
    def softGalleryLanguage_OrderSpring(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_OrderSpring__softGalleryLanguage_OrderSpring", None)
        self.__softGalleryLanguage_OrderSpring = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_SpringComponent"):
                opp_val = getattr(old_value, "softGalleryLanguage_SpringComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_SpringComponent"):
                opp_val = getattr(value, "softGalleryLanguage_SpringComponent", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_SpringComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_SpringComponent:

    pass
class softGalleryLanguage_EnableWebSecurity:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_EnableResourceServer:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_EnableAuthorizationServer:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_EnableGlobalMethodSecurity:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_Configuration:

    pass
class softGalleryLanguage_SpringBootApplication:

    pass
class softGalleryLanguage_AmazonWebServices:

    def __init__(self, name: str, softGalleryLanguage_AmazonWebServices: "softGalleryLanguage_Technologies" = None, softGalleryLanguage_AmazonWebServices252: set["softGalleryLanguage_EObject"] = None):
        self.name = name
        self.softGalleryLanguage_AmazonWebServices = softGalleryLanguage_AmazonWebServices
        self.softGalleryLanguage_AmazonWebServices252 = softGalleryLanguage_AmazonWebServices252 if softGalleryLanguage_AmazonWebServices252 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_AmazonWebServices(self):
        return self.__softGalleryLanguage_AmazonWebServices

    @softGalleryLanguage_AmazonWebServices.setter
    def softGalleryLanguage_AmazonWebServices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_AmazonWebServices__softGalleryLanguage_AmazonWebServices", None)
        self.__softGalleryLanguage_AmazonWebServices = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_Technologies98"):
                opp_val = getattr(old_value, "softGalleryLanguage_Technologies98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_Technologies98"):
                opp_val = getattr(value, "softGalleryLanguage_Technologies98", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_Technologies98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softGalleryLanguage_AmazonWebServices252(self):
        return self.__softGalleryLanguage_AmazonWebServices252

    @softGalleryLanguage_AmazonWebServices252.setter
    def softGalleryLanguage_AmazonWebServices252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_AmazonWebServices__softGalleryLanguage_AmazonWebServices252", None)
        self.__softGalleryLanguage_AmazonWebServices252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_EObject253"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject253", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_EObject253", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_EObject253"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject253", None)
                    
                    setattr(item, "softGalleryLanguage_EObject253", self)
                    

class softGalleryLanguage_PostgreSQL:

    def __init__(self, name: str, softGalleryLanguage_PostgreSQL: "softGalleryLanguage_Technologies" = None, softGalleryLanguage_PostgreSQL232: set["softGalleryLanguage_Cluster"] = None):
        self.name = name
        self.softGalleryLanguage_PostgreSQL = softGalleryLanguage_PostgreSQL
        self.softGalleryLanguage_PostgreSQL232 = softGalleryLanguage_PostgreSQL232 if softGalleryLanguage_PostgreSQL232 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_PostgreSQL(self):
        return self.__softGalleryLanguage_PostgreSQL

    @softGalleryLanguage_PostgreSQL.setter
    def softGalleryLanguage_PostgreSQL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_PostgreSQL__softGalleryLanguage_PostgreSQL", None)
        self.__softGalleryLanguage_PostgreSQL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_Technologies96"):
                opp_val = getattr(old_value, "softGalleryLanguage_Technologies96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_Technologies96"):
                opp_val = getattr(value, "softGalleryLanguage_Technologies96", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_Technologies96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softGalleryLanguage_PostgreSQL232(self):
        return self.__softGalleryLanguage_PostgreSQL232

    @softGalleryLanguage_PostgreSQL232.setter
    def softGalleryLanguage_PostgreSQL232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_PostgreSQL__softGalleryLanguage_PostgreSQL232", None)
        self.__softGalleryLanguage_PostgreSQL232 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_Cluster"):
                    opp_val = getattr(item, "softGalleryLanguage_Cluster", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_Cluster", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_Cluster"):
                    opp_val = getattr(item, "softGalleryLanguage_Cluster", None)
                    
                    setattr(item, "softGalleryLanguage_Cluster", self)
                    

class softGalleryLanguage_SearchCriteria:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_Predicate:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_Specification:

    pass
class softGalleryLanguage_RestController:

    def __init__(self, name: str, softGalleryLanguage_RestController: set["softGalleryLanguage_EObject"] = None):
        self.name = name
        self.softGalleryLanguage_RestController = softGalleryLanguage_RestController if softGalleryLanguage_RestController is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_RestController(self):
        return self.__softGalleryLanguage_RestController

    @softGalleryLanguage_RestController.setter
    def softGalleryLanguage_RestController(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_RestController__softGalleryLanguage_RestController", None)
        self.__softGalleryLanguage_RestController = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_EObject110"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject110", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_EObject110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_EObject110"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject110", None)
                    
                    setattr(item, "softGalleryLanguage_EObject110", self)
                    

class softGalleryLanguage_SpringRepositoryAnnotation:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_SpringRepositories:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_SpringRepository:

    pass
class softGalleryLanguage_NTierConnectionContent:

    def __init__(self, nTierName: str, ntierconnection: str, softGalleryLanguage_NTierConnectionContent82: set["softGalleryLanguage_NTierSource"] = None, softGalleryLanguage_NTierConnectionContent84: set["softGalleryLanguage_NTierTarget"] = None, softGalleryLanguage_NTierConnectionContent: "softGalleryLanguage_NTiersConnections" = None):
        self.nTierName = nTierName
        self.ntierconnection = ntierconnection
        self.softGalleryLanguage_NTierConnectionContent82 = softGalleryLanguage_NTierConnectionContent82 if softGalleryLanguage_NTierConnectionContent82 is not None else set()
        self.softGalleryLanguage_NTierConnectionContent84 = softGalleryLanguage_NTierConnectionContent84 if softGalleryLanguage_NTierConnectionContent84 is not None else set()
        self.softGalleryLanguage_NTierConnectionContent = softGalleryLanguage_NTierConnectionContent
        
    @property
    def nTierName(self) -> str:
        return self.__nTierName

    @nTierName.setter
    def nTierName(self, nTierName: str):
        self.__nTierName = nTierName

    @property
    def ntierconnection(self) -> str:
        return self.__ntierconnection

    @ntierconnection.setter
    def ntierconnection(self, ntierconnection: str):
        self.__ntierconnection = ntierconnection

    @property
    def softGalleryLanguage_NTierConnectionContent82(self):
        return self.__softGalleryLanguage_NTierConnectionContent82

    @softGalleryLanguage_NTierConnectionContent82.setter
    def softGalleryLanguage_NTierConnectionContent82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_NTierConnectionContent__softGalleryLanguage_NTierConnectionContent82", None)
        self.__softGalleryLanguage_NTierConnectionContent82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_NTierSource"):
                    opp_val = getattr(item, "softGalleryLanguage_NTierSource", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_NTierSource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_NTierSource"):
                    opp_val = getattr(item, "softGalleryLanguage_NTierSource", None)
                    
                    setattr(item, "softGalleryLanguage_NTierSource", self)
                    

    @property
    def softGalleryLanguage_NTierConnectionContent(self):
        return self.__softGalleryLanguage_NTierConnectionContent

    @softGalleryLanguage_NTierConnectionContent.setter
    def softGalleryLanguage_NTierConnectionContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_NTierConnectionContent__softGalleryLanguage_NTierConnectionContent", None)
        self.__softGalleryLanguage_NTierConnectionContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_NTiersConnections"):
                opp_val = getattr(old_value, "softGalleryLanguage_NTiersConnections", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_NTiersConnections"):
                opp_val = getattr(value, "softGalleryLanguage_NTiersConnections", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_NTiersConnections", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softGalleryLanguage_NTierConnectionContent84(self):
        return self.__softGalleryLanguage_NTierConnectionContent84

    @softGalleryLanguage_NTierConnectionContent84.setter
    def softGalleryLanguage_NTierConnectionContent84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_NTierConnectionContent__softGalleryLanguage_NTierConnectionContent84", None)
        self.__softGalleryLanguage_NTierConnectionContent84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_NTierTarget"):
                    opp_val = getattr(item, "softGalleryLanguage_NTierTarget", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_NTierTarget", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_NTierTarget"):
                    opp_val = getattr(item, "softGalleryLanguage_NTierTarget", None)
                    
                    setattr(item, "softGalleryLanguage_NTierTarget", self)
                    

class softGalleryLanguage_NTiersConnections:

    pass
class softGalleryLanguage_PersistenceDataComponent:

    def __init__(self, name: str, softGalleryLanguage_PersistenceDataComponent: "softGalleryLanguage_ArchitectureComponents" = None):
        self.name = name
        self.softGalleryLanguage_PersistenceDataComponent = softGalleryLanguage_PersistenceDataComponent
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_PersistenceDataComponent(self):
        return self.__softGalleryLanguage_PersistenceDataComponent

    @softGalleryLanguage_PersistenceDataComponent.setter
    def softGalleryLanguage_PersistenceDataComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_PersistenceDataComponent__softGalleryLanguage_PersistenceDataComponent", None)
        self.__softGalleryLanguage_PersistenceDataComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ArchitectureComponents79"):
                opp_val = getattr(old_value, "softGalleryLanguage_ArchitectureComponents79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ArchitectureComponents79"):
                opp_val = getattr(value, "softGalleryLanguage_ArchitectureComponents79", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ArchitectureComponents79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_BackEnd:

    def __init__(self, name: str, softGalleryLanguage_BackEnd: "softGalleryLanguage_ArchitectureComponents" = None):
        self.name = name
        self.softGalleryLanguage_BackEnd = softGalleryLanguage_BackEnd
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_BackEnd(self):
        return self.__softGalleryLanguage_BackEnd

    @softGalleryLanguage_BackEnd.setter
    def softGalleryLanguage_BackEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_BackEnd__softGalleryLanguage_BackEnd", None)
        self.__softGalleryLanguage_BackEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ArchitectureComponents77"):
                opp_val = getattr(old_value, "softGalleryLanguage_ArchitectureComponents77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ArchitectureComponents77"):
                opp_val = getattr(value, "softGalleryLanguage_ArchitectureComponents77", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ArchitectureComponents77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_FrontEnd:

    def __init__(self, name: str, softGalleryLanguage_FrontEnd: "softGalleryLanguage_ArchitectureComponents" = None):
        self.name = name
        self.softGalleryLanguage_FrontEnd = softGalleryLanguage_FrontEnd
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_FrontEnd(self):
        return self.__softGalleryLanguage_FrontEnd

    @softGalleryLanguage_FrontEnd.setter
    def softGalleryLanguage_FrontEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_FrontEnd__softGalleryLanguage_FrontEnd", None)
        self.__softGalleryLanguage_FrontEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ArchitectureComponents"):
                opp_val = getattr(old_value, "softGalleryLanguage_ArchitectureComponents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ArchitectureComponents"):
                opp_val = getattr(value, "softGalleryLanguage_ArchitectureComponents", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ArchitectureComponents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ArchitectureComponents:

    pass
class softGalleryLanguage_LayerTarget:

    def __init__(self, layerelations: str, softGalleryLanguage_LayerTarget: "softGalleryLanguage_LayerRelations" = None):
        self.layerelations = layerelations
        self.softGalleryLanguage_LayerTarget = softGalleryLanguage_LayerTarget
        
    @property
    def layerelations(self) -> str:
        return self.__layerelations

    @layerelations.setter
    def layerelations(self, layerelations: str):
        self.__layerelations = layerelations

    @property
    def softGalleryLanguage_LayerTarget(self):
        return self.__softGalleryLanguage_LayerTarget

    @softGalleryLanguage_LayerTarget.setter
    def softGalleryLanguage_LayerTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_LayerTarget__softGalleryLanguage_LayerTarget", None)
        self.__softGalleryLanguage_LayerTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_LayerRelations74"):
                opp_val = getattr(old_value, "softGalleryLanguage_LayerRelations74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_LayerRelations74"):
                opp_val = getattr(value, "softGalleryLanguage_LayerRelations74", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_LayerRelations74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_LayerSource:

    def __init__(self, layerelations: str, softGalleryLanguage_LayerSource: "softGalleryLanguage_LayerRelations" = None):
        self.layerelations = layerelations
        self.softGalleryLanguage_LayerSource = softGalleryLanguage_LayerSource
        
    @property
    def layerelations(self) -> str:
        return self.__layerelations

    @layerelations.setter
    def layerelations(self, layerelations: str):
        self.__layerelations = layerelations

    @property
    def softGalleryLanguage_LayerSource(self):
        return self.__softGalleryLanguage_LayerSource

    @softGalleryLanguage_LayerSource.setter
    def softGalleryLanguage_LayerSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_LayerSource__softGalleryLanguage_LayerSource", None)
        self.__softGalleryLanguage_LayerSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_LayerRelations"):
                opp_val = getattr(old_value, "softGalleryLanguage_LayerRelations", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_LayerRelations"):
                opp_val = getattr(value, "softGalleryLanguage_LayerRelations", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_LayerRelations", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_React:

    def __init__(self, name: str, softGalleryLanguage_React: "softGalleryLanguage_Technologies" = None, softGalleryLanguage_React135: set["softGalleryLanguage_ReactModules"] = None):
        self.name = name
        self.softGalleryLanguage_React = softGalleryLanguage_React
        self.softGalleryLanguage_React135 = softGalleryLanguage_React135 if softGalleryLanguage_React135 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_React(self):
        return self.__softGalleryLanguage_React

    @softGalleryLanguage_React.setter
    def softGalleryLanguage_React(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_React__softGalleryLanguage_React", None)
        self.__softGalleryLanguage_React = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_Technologies94"):
                opp_val = getattr(old_value, "softGalleryLanguage_Technologies94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_Technologies94"):
                opp_val = getattr(value, "softGalleryLanguage_Technologies94", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_Technologies94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softGalleryLanguage_React135(self):
        return self.__softGalleryLanguage_React135

    @softGalleryLanguage_React135.setter
    def softGalleryLanguage_React135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_React__softGalleryLanguage_React135", None)
        self.__softGalleryLanguage_React135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_ReactModules"):
                    opp_val = getattr(item, "softGalleryLanguage_ReactModules", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_ReactModules", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_ReactModules"):
                    opp_val = getattr(item, "softGalleryLanguage_ReactModules", None)
                    
                    setattr(item, "softGalleryLanguage_ReactModules", self)
                    

class softGalleryLanguage_Spring:

    def __init__(self, name: str, softGalleryLanguage_Spring: "softGalleryLanguage_Technologies" = None, softGalleryLanguage_Spring100: set["softGalleryLanguage_SpringBootApplication"] = None):
        self.name = name
        self.softGalleryLanguage_Spring = softGalleryLanguage_Spring
        self.softGalleryLanguage_Spring100 = softGalleryLanguage_Spring100 if softGalleryLanguage_Spring100 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_Spring100(self):
        return self.__softGalleryLanguage_Spring100

    @softGalleryLanguage_Spring100.setter
    def softGalleryLanguage_Spring100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Spring__softGalleryLanguage_Spring100", None)
        self.__softGalleryLanguage_Spring100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_SpringBootApplication"):
                    opp_val = getattr(item, "softGalleryLanguage_SpringBootApplication", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_SpringBootApplication", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_SpringBootApplication"):
                    opp_val = getattr(item, "softGalleryLanguage_SpringBootApplication", None)
                    
                    setattr(item, "softGalleryLanguage_SpringBootApplication", self)
                    

    @property
    def softGalleryLanguage_Spring(self):
        return self.__softGalleryLanguage_Spring

    @softGalleryLanguage_Spring.setter
    def softGalleryLanguage_Spring(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Spring__softGalleryLanguage_Spring", None)
        self.__softGalleryLanguage_Spring = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_Technologies92"):
                opp_val = getattr(old_value, "softGalleryLanguage_Technologies92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_Technologies92"):
                opp_val = getattr(value, "softGalleryLanguage_Technologies92", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_Technologies92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_Technologies:

    pass
class softGalleryLanguage_Technology:

    def __init__(self, name: str, softGalleryLanguage_Technology: set["softGalleryLanguage_Technologies"] = None):
        self.name = name
        self.softGalleryLanguage_Technology = softGalleryLanguage_Technology if softGalleryLanguage_Technology is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_Technology(self):
        return self.__softGalleryLanguage_Technology

    @softGalleryLanguage_Technology.setter
    def softGalleryLanguage_Technology(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Technology__softGalleryLanguage_Technology", None)
        self.__softGalleryLanguage_Technology = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_Technologies"):
                    opp_val = getattr(item, "softGalleryLanguage_Technologies", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_Technologies", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_Technologies"):
                    opp_val = getattr(item, "softGalleryLanguage_Technologies", None)
                    
                    setattr(item, "softGalleryLanguage_Technologies", self)
                    

class softGalleryLanguage_NTiersRelations:

    def __init__(self, name: str, softGalleryLanguage_NTiersRelations: "softGalleryLanguage_NTierSource" = None, softGalleryLanguage_NTiersRelations89: "softGalleryLanguage_NTierTarget" = None):
        self.name = name
        self.softGalleryLanguage_NTiersRelations = softGalleryLanguage_NTiersRelations
        self.softGalleryLanguage_NTiersRelations89 = softGalleryLanguage_NTiersRelations89
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_NTiersRelations(self):
        return self.__softGalleryLanguage_NTiersRelations

    @softGalleryLanguage_NTiersRelations.setter
    def softGalleryLanguage_NTiersRelations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_NTiersRelations__softGalleryLanguage_NTiersRelations", None)
        self.__softGalleryLanguage_NTiersRelations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_NTierSource86"):
                opp_val = getattr(old_value, "softGalleryLanguage_NTierSource86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_NTierSource86"):
                opp_val = getattr(value, "softGalleryLanguage_NTierSource86", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_NTierSource86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softGalleryLanguage_NTiersRelations89(self):
        return self.__softGalleryLanguage_NTiersRelations89

    @softGalleryLanguage_NTiersRelations89.setter
    def softGalleryLanguage_NTiersRelations89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_NTiersRelations__softGalleryLanguage_NTiersRelations89", None)
        self.__softGalleryLanguage_NTiersRelations89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_NTierTarget88"):
                opp_val = getattr(old_value, "softGalleryLanguage_NTierTarget88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_NTierTarget88"):
                opp_val = getattr(value, "softGalleryLanguage_NTierTarget88", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_NTierTarget88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_NTierTarget:

    pass
class softGalleryLanguage_NTierSource:

    pass
class softGalleryLanguage_DataPersistenceSegments:

    def __init__(self, postSName: str, amazonSName: str, softGalleryLanguage_DataPersistenceSegments: "softGalleryLanguage_DataPersistenceContent" = None):
        self.postSName = postSName
        self.amazonSName = amazonSName
        self.softGalleryLanguage_DataPersistenceSegments = softGalleryLanguage_DataPersistenceSegments
        
    @property
    def amazonSName(self) -> str:
        return self.__amazonSName

    @amazonSName.setter
    def amazonSName(self, amazonSName: str):
        self.__amazonSName = amazonSName

    @property
    def postSName(self) -> str:
        return self.__postSName

    @postSName.setter
    def postSName(self, postSName: str):
        self.__postSName = postSName

    @property
    def softGalleryLanguage_DataPersistenceSegments(self):
        return self.__softGalleryLanguage_DataPersistenceSegments

    @softGalleryLanguage_DataPersistenceSegments.setter
    def softGalleryLanguage_DataPersistenceSegments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_DataPersistenceSegments__softGalleryLanguage_DataPersistenceSegments", None)
        self.__softGalleryLanguage_DataPersistenceSegments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_DataPersistenceContent64"):
                opp_val = getattr(old_value, "softGalleryLanguage_DataPersistenceContent64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_DataPersistenceContent64"):
                opp_val = getattr(value, "softGalleryLanguage_DataPersistenceContent64", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_DataPersistenceContent64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_DataPersistenceContent:

    pass
class softGalleryLanguage_DataPersistenceLayer:

    pass
class softGalleryLanguage_CriteriaAttributeType:

    def __init__(self, name: str, softGalleryLanguage_CriteriaAttributeType: "softGalleryLanguage_SpecificationSegmentElement" = None):
        self.name = name
        self.softGalleryLanguage_CriteriaAttributeType = softGalleryLanguage_CriteriaAttributeType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_CriteriaAttributeType(self):
        return self.__softGalleryLanguage_CriteriaAttributeType

    @softGalleryLanguage_CriteriaAttributeType.setter
    def softGalleryLanguage_CriteriaAttributeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_CriteriaAttributeType__softGalleryLanguage_CriteriaAttributeType", None)
        self.__softGalleryLanguage_CriteriaAttributeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_SpecificationSegmentElement61"):
                opp_val = getattr(old_value, "softGalleryLanguage_SpecificationSegmentElement61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_SpecificationSegmentElement61"):
                opp_val = getattr(value, "softGalleryLanguage_SpecificationSegmentElement61", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_SpecificationSegmentElement61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_SpecificationSegmentElement:

    def __init__(self, name: str, softGalleryLanguage_SpecificationSegmentElement: "softGalleryLanguage_BusinessLogicSegments" = None, softGalleryLanguage_SpecificationSegmentElement61: set["softGalleryLanguage_CriteriaAttributeType"] = None):
        self.name = name
        self.softGalleryLanguage_SpecificationSegmentElement = softGalleryLanguage_SpecificationSegmentElement
        self.softGalleryLanguage_SpecificationSegmentElement61 = softGalleryLanguage_SpecificationSegmentElement61 if softGalleryLanguage_SpecificationSegmentElement61 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_SpecificationSegmentElement(self):
        return self.__softGalleryLanguage_SpecificationSegmentElement

    @softGalleryLanguage_SpecificationSegmentElement.setter
    def softGalleryLanguage_SpecificationSegmentElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_SpecificationSegmentElement__softGalleryLanguage_SpecificationSegmentElement", None)
        self.__softGalleryLanguage_SpecificationSegmentElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_BusinessLogicSegments59"):
                opp_val = getattr(old_value, "softGalleryLanguage_BusinessLogicSegments59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_BusinessLogicSegments59"):
                opp_val = getattr(value, "softGalleryLanguage_BusinessLogicSegments59", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_BusinessLogicSegments59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softGalleryLanguage_SpecificationSegmentElement61(self):
        return self.__softGalleryLanguage_SpecificationSegmentElement61

    @softGalleryLanguage_SpecificationSegmentElement61.setter
    def softGalleryLanguage_SpecificationSegmentElement61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_SpecificationSegmentElement__softGalleryLanguage_SpecificationSegmentElement61", None)
        self.__softGalleryLanguage_SpecificationSegmentElement61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_CriteriaAttributeType"):
                    opp_val = getattr(item, "softGalleryLanguage_CriteriaAttributeType", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_CriteriaAttributeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_CriteriaAttributeType"):
                    opp_val = getattr(item, "softGalleryLanguage_CriteriaAttributeType", None)
                    
                    setattr(item, "softGalleryLanguage_CriteriaAttributeType", self)
                    

class softGalleryLanguage_ControllerSegmentElement:

    def __init__(self, name: str, softGalleryLanguage_ControllerSegmentElement: "softGalleryLanguage_BusinessLogicSegments" = None):
        self.name = name
        self.softGalleryLanguage_ControllerSegmentElement = softGalleryLanguage_ControllerSegmentElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_ControllerSegmentElement(self):
        return self.__softGalleryLanguage_ControllerSegmentElement

    @softGalleryLanguage_ControllerSegmentElement.setter
    def softGalleryLanguage_ControllerSegmentElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ControllerSegmentElement__softGalleryLanguage_ControllerSegmentElement", None)
        self.__softGalleryLanguage_ControllerSegmentElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_BusinessLogicSegments57"):
                opp_val = getattr(old_value, "softGalleryLanguage_BusinessLogicSegments57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_BusinessLogicSegments57"):
                opp_val = getattr(value, "softGalleryLanguage_BusinessLogicSegments57", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_BusinessLogicSegments57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_BusinessLogicSegments:

    def __init__(self, name: str, softGalleryLanguage_BusinessLogicSegments: "softGalleryLanguage_BusinessLogicContent" = None, softGalleryLanguage_BusinessLogicSegments57: set["softGalleryLanguage_ControllerSegmentElement"] = None, softGalleryLanguage_BusinessLogicSegments59: set["softGalleryLanguage_SpecificationSegmentElement"] = None):
        self.name = name
        self.softGalleryLanguage_BusinessLogicSegments = softGalleryLanguage_BusinessLogicSegments
        self.softGalleryLanguage_BusinessLogicSegments57 = softGalleryLanguage_BusinessLogicSegments57 if softGalleryLanguage_BusinessLogicSegments57 is not None else set()
        self.softGalleryLanguage_BusinessLogicSegments59 = softGalleryLanguage_BusinessLogicSegments59 if softGalleryLanguage_BusinessLogicSegments59 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_BusinessLogicSegments59(self):
        return self.__softGalleryLanguage_BusinessLogicSegments59

    @softGalleryLanguage_BusinessLogicSegments59.setter
    def softGalleryLanguage_BusinessLogicSegments59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_BusinessLogicSegments__softGalleryLanguage_BusinessLogicSegments59", None)
        self.__softGalleryLanguage_BusinessLogicSegments59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_SpecificationSegmentElement"):
                    opp_val = getattr(item, "softGalleryLanguage_SpecificationSegmentElement", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_SpecificationSegmentElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_SpecificationSegmentElement"):
                    opp_val = getattr(item, "softGalleryLanguage_SpecificationSegmentElement", None)
                    
                    setattr(item, "softGalleryLanguage_SpecificationSegmentElement", self)
                    

    @property
    def softGalleryLanguage_BusinessLogicSegments(self):
        return self.__softGalleryLanguage_BusinessLogicSegments

    @softGalleryLanguage_BusinessLogicSegments.setter
    def softGalleryLanguage_BusinessLogicSegments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_BusinessLogicSegments__softGalleryLanguage_BusinessLogicSegments", None)
        self.__softGalleryLanguage_BusinessLogicSegments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_BusinessLogicContent"):
                opp_val = getattr(old_value, "softGalleryLanguage_BusinessLogicContent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_BusinessLogicContent"):
                opp_val = getattr(value, "softGalleryLanguage_BusinessLogicContent", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_BusinessLogicContent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softGalleryLanguage_BusinessLogicSegments57(self):
        return self.__softGalleryLanguage_BusinessLogicSegments57

    @softGalleryLanguage_BusinessLogicSegments57.setter
    def softGalleryLanguage_BusinessLogicSegments57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_BusinessLogicSegments__softGalleryLanguage_BusinessLogicSegments57", None)
        self.__softGalleryLanguage_BusinessLogicSegments57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_ControllerSegmentElement"):
                    opp_val = getattr(item, "softGalleryLanguage_ControllerSegmentElement", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_ControllerSegmentElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_ControllerSegmentElement"):
                    opp_val = getattr(item, "softGalleryLanguage_ControllerSegmentElement", None)
                    
                    setattr(item, "softGalleryLanguage_ControllerSegmentElement", self)
                    

class softGalleryLanguage_BusinessLogicContent:

    pass
class softGalleryLanguage_LayerRelations:

    def __init__(self, layerelations: str, name: str, softGalleryLanguage_LayerRelations: set["softGalleryLanguage_LayerSource"] = None, softGalleryLanguage_LayerRelations74: set["softGalleryLanguage_LayerTarget"] = None):
        self.layerelations = layerelations
        self.name = name
        self.softGalleryLanguage_LayerRelations = softGalleryLanguage_LayerRelations if softGalleryLanguage_LayerRelations is not None else set()
        self.softGalleryLanguage_LayerRelations74 = softGalleryLanguage_LayerRelations74 if softGalleryLanguage_LayerRelations74 is not None else set()
        
    @property
    def layerelations(self) -> str:
        return self.__layerelations

    @layerelations.setter
    def layerelations(self, layerelations: str):
        self.__layerelations = layerelations

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_LayerRelations74(self):
        return self.__softGalleryLanguage_LayerRelations74

    @softGalleryLanguage_LayerRelations74.setter
    def softGalleryLanguage_LayerRelations74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_LayerRelations__softGalleryLanguage_LayerRelations74", None)
        self.__softGalleryLanguage_LayerRelations74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_LayerTarget"):
                    opp_val = getattr(item, "softGalleryLanguage_LayerTarget", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_LayerTarget", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_LayerTarget"):
                    opp_val = getattr(item, "softGalleryLanguage_LayerTarget", None)
                    
                    setattr(item, "softGalleryLanguage_LayerTarget", self)
                    

    @property
    def softGalleryLanguage_LayerRelations(self):
        return self.__softGalleryLanguage_LayerRelations

    @softGalleryLanguage_LayerRelations.setter
    def softGalleryLanguage_LayerRelations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_LayerRelations__softGalleryLanguage_LayerRelations", None)
        self.__softGalleryLanguage_LayerRelations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_LayerSource"):
                    opp_val = getattr(item, "softGalleryLanguage_LayerSource", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_LayerSource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_LayerSource"):
                    opp_val = getattr(item, "softGalleryLanguage_LayerSource", None)
                    
                    setattr(item, "softGalleryLanguage_LayerSource", self)
                    

class softGalleryLanguage_SingleFile:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class softGalleryLanguage_MultipleFile:

    def __init__(self, name: str, softGalleryLanguage_MultipleFile: "softGalleryLanguage_Directories" = None):
        self.name = name
        self.softGalleryLanguage_MultipleFile = softGalleryLanguage_MultipleFile
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_MultipleFile(self):
        return self.__softGalleryLanguage_MultipleFile

    @softGalleryLanguage_MultipleFile.setter
    def softGalleryLanguage_MultipleFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_MultipleFile__softGalleryLanguage_MultipleFile", None)
        self.__softGalleryLanguage_MultipleFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_Directories"):
                opp_val = getattr(old_value, "softGalleryLanguage_Directories", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_Directories"):
                opp_val = getattr(value, "softGalleryLanguage_Directories", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_Directories", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_Directories:

    pass
class softGalleryLanguage_DirectoryContent:

    def __init__(self, name: str, softGalleryLanguage_DirectoryContent: "softGalleryLanguage_SegmentStructureContent" = None, softGalleryLanguage_DirectoryContent69: set["softGalleryLanguage_EObject"] = None):
        self.name = name
        self.softGalleryLanguage_DirectoryContent = softGalleryLanguage_DirectoryContent
        self.softGalleryLanguage_DirectoryContent69 = softGalleryLanguage_DirectoryContent69 if softGalleryLanguage_DirectoryContent69 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_DirectoryContent69(self):
        return self.__softGalleryLanguage_DirectoryContent69

    @softGalleryLanguage_DirectoryContent69.setter
    def softGalleryLanguage_DirectoryContent69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_DirectoryContent__softGalleryLanguage_DirectoryContent69", None)
        self.__softGalleryLanguage_DirectoryContent69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_EObject70"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject70", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_EObject70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_EObject70"):
                    opp_val = getattr(item, "softGalleryLanguage_EObject70", None)
                    
                    setattr(item, "softGalleryLanguage_EObject70", self)
                    

    @property
    def softGalleryLanguage_DirectoryContent(self):
        return self.__softGalleryLanguage_DirectoryContent

    @softGalleryLanguage_DirectoryContent.setter
    def softGalleryLanguage_DirectoryContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_DirectoryContent__softGalleryLanguage_DirectoryContent", None)
        self.__softGalleryLanguage_DirectoryContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_SegmentStructureContent67"):
                opp_val = getattr(old_value, "softGalleryLanguage_SegmentStructureContent67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_SegmentStructureContent67"):
                opp_val = getattr(value, "softGalleryLanguage_SegmentStructureContent67", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_SegmentStructureContent67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_SegmentStructureContent:

    def __init__(self, name: str, softGalleryLanguage_SegmentStructureContent: "softGalleryLanguage_SegmentStructure" = None, softGalleryLanguage_SegmentStructureContent67: set["softGalleryLanguage_DirectoryContent"] = None):
        self.name = name
        self.softGalleryLanguage_SegmentStructureContent = softGalleryLanguage_SegmentStructureContent
        self.softGalleryLanguage_SegmentStructureContent67 = softGalleryLanguage_SegmentStructureContent67 if softGalleryLanguage_SegmentStructureContent67 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_SegmentStructureContent(self):
        return self.__softGalleryLanguage_SegmentStructureContent

    @softGalleryLanguage_SegmentStructureContent.setter
    def softGalleryLanguage_SegmentStructureContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_SegmentStructureContent__softGalleryLanguage_SegmentStructureContent", None)
        self.__softGalleryLanguage_SegmentStructureContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_SegmentStructure"):
                opp_val = getattr(old_value, "softGalleryLanguage_SegmentStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_SegmentStructure"):
                opp_val = getattr(value, "softGalleryLanguage_SegmentStructure", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_SegmentStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def softGalleryLanguage_SegmentStructureContent67(self):
        return self.__softGalleryLanguage_SegmentStructureContent67

    @softGalleryLanguage_SegmentStructureContent67.setter
    def softGalleryLanguage_SegmentStructureContent67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_SegmentStructureContent__softGalleryLanguage_SegmentStructureContent67", None)
        self.__softGalleryLanguage_SegmentStructureContent67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_DirectoryContent"):
                    opp_val = getattr(item, "softGalleryLanguage_DirectoryContent", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_DirectoryContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_DirectoryContent"):
                    opp_val = getattr(item, "softGalleryLanguage_DirectoryContent", None)
                    
                    setattr(item, "softGalleryLanguage_DirectoryContent", self)
                    

class softGalleryLanguage_SegmentStructure:

    pass
class softGalleryLanguage_UserException:

    def __init__(self, name: str, softGalleryLanguage_UserException: "softGalleryLanguage_ExceptionsType" = None):
        self.name = name
        self.softGalleryLanguage_UserException = softGalleryLanguage_UserException
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_UserException(self):
        return self.__softGalleryLanguage_UserException

    @softGalleryLanguage_UserException.setter
    def softGalleryLanguage_UserException(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_UserException__softGalleryLanguage_UserException", None)
        self.__softGalleryLanguage_UserException = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ExceptionsType43"):
                opp_val = getattr(old_value, "softGalleryLanguage_ExceptionsType43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ExceptionsType43"):
                opp_val = getattr(value, "softGalleryLanguage_ExceptionsType43", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ExceptionsType43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_AlbumException:

    def __init__(self, name: str, softGalleryLanguage_AlbumException: "softGalleryLanguage_ExceptionsType" = None):
        self.name = name
        self.softGalleryLanguage_AlbumException = softGalleryLanguage_AlbumException
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_AlbumException(self):
        return self.__softGalleryLanguage_AlbumException

    @softGalleryLanguage_AlbumException.setter
    def softGalleryLanguage_AlbumException(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_AlbumException__softGalleryLanguage_AlbumException", None)
        self.__softGalleryLanguage_AlbumException = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ExceptionsType41"):
                opp_val = getattr(old_value, "softGalleryLanguage_ExceptionsType41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ExceptionsType41"):
                opp_val = getattr(value, "softGalleryLanguage_ExceptionsType41", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ExceptionsType41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_PhotoException:

    def __init__(self, name: str, softGalleryLanguage_PhotoException: "softGalleryLanguage_ExceptionsType" = None):
        self.name = name
        self.softGalleryLanguage_PhotoException = softGalleryLanguage_PhotoException
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_PhotoException(self):
        return self.__softGalleryLanguage_PhotoException

    @softGalleryLanguage_PhotoException.setter
    def softGalleryLanguage_PhotoException(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_PhotoException__softGalleryLanguage_PhotoException", None)
        self.__softGalleryLanguage_PhotoException = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ExceptionsType39"):
                opp_val = getattr(old_value, "softGalleryLanguage_ExceptionsType39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ExceptionsType39"):
                opp_val = getattr(value, "softGalleryLanguage_ExceptionsType39", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ExceptionsType39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_BusinessLogicLayer:

    pass
class softGalleryLanguage_PresentationSegments:

    def __init__(self, presentationSName: str, presentationCName: str, presentationAName: str, softGalleryLanguage_PresentationSegments: "softGalleryLanguage_PresentationContent" = None):
        self.presentationSName = presentationSName
        self.presentationCName = presentationCName
        self.presentationAName = presentationAName
        self.softGalleryLanguage_PresentationSegments = softGalleryLanguage_PresentationSegments
        
    @property
    def presentationSName(self) -> str:
        return self.__presentationSName

    @presentationSName.setter
    def presentationSName(self, presentationSName: str):
        self.__presentationSName = presentationSName

    @property
    def presentationAName(self) -> str:
        return self.__presentationAName

    @presentationAName.setter
    def presentationAName(self, presentationAName: str):
        self.__presentationAName = presentationAName

    @property
    def presentationCName(self) -> str:
        return self.__presentationCName

    @presentationCName.setter
    def presentationCName(self, presentationCName: str):
        self.__presentationCName = presentationCName

    @property
    def softGalleryLanguage_PresentationSegments(self):
        return self.__softGalleryLanguage_PresentationSegments

    @softGalleryLanguage_PresentationSegments.setter
    def softGalleryLanguage_PresentationSegments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_PresentationSegments__softGalleryLanguage_PresentationSegments", None)
        self.__softGalleryLanguage_PresentationSegments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_PresentationContent"):
                opp_val = getattr(old_value, "softGalleryLanguage_PresentationContent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_PresentationContent"):
                opp_val = getattr(value, "softGalleryLanguage_PresentationContent", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_PresentationContent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_PresentationContent:

    pass
class softGalleryLanguage_PresentationLayer:

    pass
class softGalleryLanguage_Layer:

    pass
class softGalleryLanguage_NTiers:

    pass
class softGalleryLanguage_Architecture:

    pass
class softGalleryLanguage_AlbumManagementFunctions:

    def __init__(self, createdAlbName: str, selectAlbName: str, softGalleryLanguage_AlbumManagementFunctions: "softGalleryLanguage_AlbumManagement" = None):
        self.createdAlbName = createdAlbName
        self.selectAlbName = selectAlbName
        self.softGalleryLanguage_AlbumManagementFunctions = softGalleryLanguage_AlbumManagementFunctions
        
    @property
    def createdAlbName(self) -> str:
        return self.__createdAlbName

    @createdAlbName.setter
    def createdAlbName(self, createdAlbName: str):
        self.__createdAlbName = createdAlbName

    @property
    def selectAlbName(self) -> str:
        return self.__selectAlbName

    @selectAlbName.setter
    def selectAlbName(self, selectAlbName: str):
        self.__selectAlbName = selectAlbName

    @property
    def softGalleryLanguage_AlbumManagementFunctions(self):
        return self.__softGalleryLanguage_AlbumManagementFunctions

    @softGalleryLanguage_AlbumManagementFunctions.setter
    def softGalleryLanguage_AlbumManagementFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_AlbumManagementFunctions__softGalleryLanguage_AlbumManagementFunctions", None)
        self.__softGalleryLanguage_AlbumManagementFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_AlbumManagement31"):
                opp_val = getattr(old_value, "softGalleryLanguage_AlbumManagement31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_AlbumManagement31"):
                opp_val = getattr(value, "softGalleryLanguage_AlbumManagement31", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_AlbumManagement31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_AppAccessFunctions:

    def __init__(self, loginName: str, registerName: str, softGalleryLanguage_AppAccessFunctions: "softGalleryLanguage_AppAccess" = None):
        self.loginName = loginName
        self.registerName = registerName
        self.softGalleryLanguage_AppAccessFunctions = softGalleryLanguage_AppAccessFunctions
        
    @property
    def registerName(self) -> str:
        return self.__registerName

    @registerName.setter
    def registerName(self, registerName: str):
        self.__registerName = registerName

    @property
    def loginName(self) -> str:
        return self.__loginName

    @loginName.setter
    def loginName(self, loginName: str):
        self.__loginName = loginName

    @property
    def softGalleryLanguage_AppAccessFunctions(self):
        return self.__softGalleryLanguage_AppAccessFunctions

    @softGalleryLanguage_AppAccessFunctions.setter
    def softGalleryLanguage_AppAccessFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_AppAccessFunctions__softGalleryLanguage_AppAccessFunctions", None)
        self.__softGalleryLanguage_AppAccessFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_AppAccess29"):
                opp_val = getattr(old_value, "softGalleryLanguage_AppAccess29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_AppAccess29"):
                opp_val = getattr(value, "softGalleryLanguage_AppAccess29", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_AppAccess29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ExceptionsType:

    pass
class softGalleryLanguage_LandingFunctions:

    def __init__(self, nameCarouselName: str, passPhotoName: str, softGalleryLanguage_LandingFunctions: "softGalleryLanguage_LandingActions" = None):
        self.nameCarouselName = nameCarouselName
        self.passPhotoName = passPhotoName
        self.softGalleryLanguage_LandingFunctions = softGalleryLanguage_LandingFunctions
        
    @property
    def nameCarouselName(self) -> str:
        return self.__nameCarouselName

    @nameCarouselName.setter
    def nameCarouselName(self, nameCarouselName: str):
        self.__nameCarouselName = nameCarouselName

    @property
    def passPhotoName(self) -> str:
        return self.__passPhotoName

    @passPhotoName.setter
    def passPhotoName(self, passPhotoName: str):
        self.__passPhotoName = passPhotoName

    @property
    def softGalleryLanguage_LandingFunctions(self):
        return self.__softGalleryLanguage_LandingFunctions

    @softGalleryLanguage_LandingFunctions.setter
    def softGalleryLanguage_LandingFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_LandingFunctions__softGalleryLanguage_LandingFunctions", None)
        self.__softGalleryLanguage_LandingFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_LandingActions35"):
                opp_val = getattr(old_value, "softGalleryLanguage_LandingActions35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_LandingActions35"):
                opp_val = getattr(value, "softGalleryLanguage_LandingActions35", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_LandingActions35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_PhotoActionsFunctions:

    def __init__(self, nameGenerico: str, namePhoto: str, nameLoad: str, softGalleryLanguage_PhotoActionsFunctions: "softGalleryLanguage_PhotoActions" = None):
        self.nameGenerico = nameGenerico
        self.namePhoto = namePhoto
        self.nameLoad = nameLoad
        self.softGalleryLanguage_PhotoActionsFunctions = softGalleryLanguage_PhotoActionsFunctions
        
    @property
    def nameLoad(self) -> str:
        return self.__nameLoad

    @nameLoad.setter
    def nameLoad(self, nameLoad: str):
        self.__nameLoad = nameLoad

    @property
    def nameGenerico(self) -> str:
        return self.__nameGenerico

    @nameGenerico.setter
    def nameGenerico(self, nameGenerico: str):
        self.__nameGenerico = nameGenerico

    @property
    def namePhoto(self) -> str:
        return self.__namePhoto

    @namePhoto.setter
    def namePhoto(self, namePhoto: str):
        self.__namePhoto = namePhoto

    @property
    def softGalleryLanguage_PhotoActionsFunctions(self):
        return self.__softGalleryLanguage_PhotoActionsFunctions

    @softGalleryLanguage_PhotoActionsFunctions.setter
    def softGalleryLanguage_PhotoActionsFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_PhotoActionsFunctions__softGalleryLanguage_PhotoActionsFunctions", None)
        self.__softGalleryLanguage_PhotoActionsFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_PhotoActions33"):
                opp_val = getattr(old_value, "softGalleryLanguage_PhotoActions33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_PhotoActions33"):
                opp_val = getattr(value, "softGalleryLanguage_PhotoActions33", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_PhotoActions33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_AppAccess:

    pass
class softGalleryLanguage_ProfileManagement:

    pass
class softGalleryLanguage_Functionalities:

    pass
class softGalleryLanguage_AtributeUserDomain:

    def __init__(self, name: str, softGalleryLanguage_AtributeUserDomain: "softGalleryLanguage_Entities" = None):
        self.name = name
        self.softGalleryLanguage_AtributeUserDomain = softGalleryLanguage_AtributeUserDomain
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_AtributeUserDomain(self):
        return self.__softGalleryLanguage_AtributeUserDomain

    @softGalleryLanguage_AtributeUserDomain.setter
    def softGalleryLanguage_AtributeUserDomain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_AtributeUserDomain__softGalleryLanguage_AtributeUserDomain", None)
        self.__softGalleryLanguage_AtributeUserDomain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_Entities13"):
                opp_val = getattr(old_value, "softGalleryLanguage_Entities13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_Entities13"):
                opp_val = getattr(value, "softGalleryLanguage_Entities13", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_Entities13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ProfileManagementFunctions:

    def __init__(self, viewprofileName: str, editProfileName: str, softGalleryLanguage_ProfileManagementFunctions: "softGalleryLanguage_ProfileManagement" = None):
        self.viewprofileName = viewprofileName
        self.editProfileName = editProfileName
        self.softGalleryLanguage_ProfileManagementFunctions = softGalleryLanguage_ProfileManagementFunctions
        
    @property
    def editProfileName(self) -> str:
        return self.__editProfileName

    @editProfileName.setter
    def editProfileName(self, editProfileName: str):
        self.__editProfileName = editProfileName

    @property
    def viewprofileName(self) -> str:
        return self.__viewprofileName

    @viewprofileName.setter
    def viewprofileName(self, viewprofileName: str):
        self.__viewprofileName = viewprofileName

    @property
    def softGalleryLanguage_ProfileManagementFunctions(self):
        return self.__softGalleryLanguage_ProfileManagementFunctions

    @softGalleryLanguage_ProfileManagementFunctions.setter
    def softGalleryLanguage_ProfileManagementFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_ProfileManagementFunctions__softGalleryLanguage_ProfileManagementFunctions", None)
        self.__softGalleryLanguage_ProfileManagementFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_ProfileManagement27"):
                opp_val = getattr(old_value, "softGalleryLanguage_ProfileManagement27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_ProfileManagement27"):
                opp_val = getattr(value, "softGalleryLanguage_ProfileManagement27", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_ProfileManagement27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_LandingActions:

    pass
class softGalleryLanguage_PhotoActions:

    pass
class softGalleryLanguage_AlbumManagement:

    pass
class softGalleryLanguage_Entity:

    pass
class softGalleryLanguage_Domain:

    def __init__(self, name: str, softGalleryLanguage_Domain3: set["softGalleryLanguage_Functionality"] = None, softGalleryLanguage_Domain5: set["softGalleryLanguage_ExceptionsDomain"] = None, softGalleryLanguage_Domain: set["softGalleryLanguage_Entity"] = None):
        self.name = name
        self.softGalleryLanguage_Domain3 = softGalleryLanguage_Domain3 if softGalleryLanguage_Domain3 is not None else set()
        self.softGalleryLanguage_Domain5 = softGalleryLanguage_Domain5 if softGalleryLanguage_Domain5 is not None else set()
        self.softGalleryLanguage_Domain = softGalleryLanguage_Domain if softGalleryLanguage_Domain is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_Domain5(self):
        return self.__softGalleryLanguage_Domain5

    @softGalleryLanguage_Domain5.setter
    def softGalleryLanguage_Domain5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Domain__softGalleryLanguage_Domain5", None)
        self.__softGalleryLanguage_Domain5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_ExceptionsDomain"):
                    opp_val = getattr(item, "softGalleryLanguage_ExceptionsDomain", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_ExceptionsDomain", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_ExceptionsDomain"):
                    opp_val = getattr(item, "softGalleryLanguage_ExceptionsDomain", None)
                    
                    setattr(item, "softGalleryLanguage_ExceptionsDomain", self)
                    

    @property
    def softGalleryLanguage_Domain(self):
        return self.__softGalleryLanguage_Domain

    @softGalleryLanguage_Domain.setter
    def softGalleryLanguage_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Domain__softGalleryLanguage_Domain", None)
        self.__softGalleryLanguage_Domain = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_Entity"):
                    opp_val = getattr(item, "softGalleryLanguage_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_Entity"):
                    opp_val = getattr(item, "softGalleryLanguage_Entity", None)
                    
                    setattr(item, "softGalleryLanguage_Entity", self)
                    

    @property
    def softGalleryLanguage_Domain3(self):
        return self.__softGalleryLanguage_Domain3

    @softGalleryLanguage_Domain3.setter
    def softGalleryLanguage_Domain3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Domain__softGalleryLanguage_Domain3", None)
        self.__softGalleryLanguage_Domain3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_Functionality"):
                    opp_val = getattr(item, "softGalleryLanguage_Functionality", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_Functionality", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_Functionality"):
                    opp_val = getattr(item, "softGalleryLanguage_Functionality", None)
                    
                    setattr(item, "softGalleryLanguage_Functionality", self)
                    

class softGalleryLanguage_EObject:

    pass
class softGalleryLanguage_Model:

    pass
class softGalleryLanguage_AtributeAlbum:

    def __init__(self, name: str, softGalleryLanguage_AtributeAlbum: "softGalleryLanguage_Entities" = None):
        self.name = name
        self.softGalleryLanguage_AtributeAlbum = softGalleryLanguage_AtributeAlbum
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_AtributeAlbum(self):
        return self.__softGalleryLanguage_AtributeAlbum

    @softGalleryLanguage_AtributeAlbum.setter
    def softGalleryLanguage_AtributeAlbum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_AtributeAlbum__softGalleryLanguage_AtributeAlbum", None)
        self.__softGalleryLanguage_AtributeAlbum = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_Entities11"):
                opp_val = getattr(old_value, "softGalleryLanguage_Entities11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_Entities11"):
                opp_val = getattr(value, "softGalleryLanguage_Entities11", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_Entities11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_AtributePhoto:

    def __init__(self, name: str, softGalleryLanguage_AtributePhoto: "softGalleryLanguage_Entities" = None):
        self.name = name
        self.softGalleryLanguage_AtributePhoto = softGalleryLanguage_AtributePhoto
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_AtributePhoto(self):
        return self.__softGalleryLanguage_AtributePhoto

    @softGalleryLanguage_AtributePhoto.setter
    def softGalleryLanguage_AtributePhoto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_AtributePhoto__softGalleryLanguage_AtributePhoto", None)
        self.__softGalleryLanguage_AtributePhoto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_Entities9"):
                opp_val = getattr(old_value, "softGalleryLanguage_Entities9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_Entities9"):
                opp_val = getattr(value, "softGalleryLanguage_Entities9", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_Entities9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_Entities:

    def __init__(self, name: str, softGalleryLanguage_Entities: "softGalleryLanguage_Entity" = None, softGalleryLanguage_Entities9: set["softGalleryLanguage_AtributePhoto"] = None, softGalleryLanguage_Entities11: set["softGalleryLanguage_AtributeAlbum"] = None, softGalleryLanguage_Entities13: set["softGalleryLanguage_AtributeUserDomain"] = None):
        self.name = name
        self.softGalleryLanguage_Entities = softGalleryLanguage_Entities
        self.softGalleryLanguage_Entities9 = softGalleryLanguage_Entities9 if softGalleryLanguage_Entities9 is not None else set()
        self.softGalleryLanguage_Entities11 = softGalleryLanguage_Entities11 if softGalleryLanguage_Entities11 is not None else set()
        self.softGalleryLanguage_Entities13 = softGalleryLanguage_Entities13 if softGalleryLanguage_Entities13 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def softGalleryLanguage_Entities9(self):
        return self.__softGalleryLanguage_Entities9

    @softGalleryLanguage_Entities9.setter
    def softGalleryLanguage_Entities9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Entities__softGalleryLanguage_Entities9", None)
        self.__softGalleryLanguage_Entities9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_AtributePhoto"):
                    opp_val = getattr(item, "softGalleryLanguage_AtributePhoto", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_AtributePhoto", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_AtributePhoto"):
                    opp_val = getattr(item, "softGalleryLanguage_AtributePhoto", None)
                    
                    setattr(item, "softGalleryLanguage_AtributePhoto", self)
                    

    @property
    def softGalleryLanguage_Entities13(self):
        return self.__softGalleryLanguage_Entities13

    @softGalleryLanguage_Entities13.setter
    def softGalleryLanguage_Entities13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Entities__softGalleryLanguage_Entities13", None)
        self.__softGalleryLanguage_Entities13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_AtributeUserDomain"):
                    opp_val = getattr(item, "softGalleryLanguage_AtributeUserDomain", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_AtributeUserDomain", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_AtributeUserDomain"):
                    opp_val = getattr(item, "softGalleryLanguage_AtributeUserDomain", None)
                    
                    setattr(item, "softGalleryLanguage_AtributeUserDomain", self)
                    

    @property
    def softGalleryLanguage_Entities11(self):
        return self.__softGalleryLanguage_Entities11

    @softGalleryLanguage_Entities11.setter
    def softGalleryLanguage_Entities11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Entities__softGalleryLanguage_Entities11", None)
        self.__softGalleryLanguage_Entities11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "softGalleryLanguage_AtributeAlbum"):
                    opp_val = getattr(item, "softGalleryLanguage_AtributeAlbum", None)
                    
                    if opp_val == self:
                        setattr(item, "softGalleryLanguage_AtributeAlbum", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "softGalleryLanguage_AtributeAlbum"):
                    opp_val = getattr(item, "softGalleryLanguage_AtributeAlbum", None)
                    
                    setattr(item, "softGalleryLanguage_AtributeAlbum", self)
                    

    @property
    def softGalleryLanguage_Entities(self):
        return self.__softGalleryLanguage_Entities

    @softGalleryLanguage_Entities.setter
    def softGalleryLanguage_Entities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_softGalleryLanguage_Entities__softGalleryLanguage_Entities", None)
        self.__softGalleryLanguage_Entities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "softGalleryLanguage_Entity7"):
                opp_val = getattr(old_value, "softGalleryLanguage_Entity7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "softGalleryLanguage_Entity7"):
                opp_val = getattr(value, "softGalleryLanguage_Entity7", None)
                if opp_val is None:
                    setattr(value, "softGalleryLanguage_Entity7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class softGalleryLanguage_ExceptionsDomain:

    pass
class softGalleryLanguage_Functionality:

    pass