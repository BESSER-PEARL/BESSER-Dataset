from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class IReferenceDescription:

    pass
class builderState_ReferenceDescription(IReferenceDescription):

    def __init__(self, externalFormOfEReference: str):
        self.externalFormOfEReference = externalFormOfEReference
        
        pass
    @property
    def externalFormOfEReference(self):
        return self.__externalFormOfEReference

    @externalFormOfEReference.setter
    def externalFormOfEReference(self, externalFormOfEReference: str):
        self.__externalFormOfEReference = externalFormOfEReference


class builderState_UserDataEntry:

    def __init__(self, key: str, value: str, builderState_UserDataEntry: "builderState_EObjectDescription" = None):
        self.key = key
        self.value = value
        self.builderState_UserDataEntry = builderState_UserDataEntry
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def builderState_UserDataEntry(self):
        return self.__builderState_UserDataEntry

    @builderState_UserDataEntry.setter
    def builderState_UserDataEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builderState_UserDataEntry__builderState_UserDataEntry", None)
        self.__builderState_UserDataEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builderState_EObjectDescription"):
                opp_val = getattr(old_value, "builderState_EObjectDescription", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builderState_EObjectDescription"):
                opp_val = getattr(value, "builderState_EObjectDescription", None)
                if opp_val is None:
                    setattr(value, "builderState_EObjectDescription", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class builderState_EClass:

    pass
class builderState_ResourceDescription:

    def __init__(self, URI: str, importedNames: str, builderState_ResourceDescription: set["builderState_IEObjectDescription"] = None, builderState_ResourceDescription2: set["builderState_IReferenceDescription"] = None):
        self.URI = URI
        self.importedNames = importedNames
        self.builderState_ResourceDescription = builderState_ResourceDescription if builderState_ResourceDescription is not None else set()
        self.builderState_ResourceDescription2 = builderState_ResourceDescription2 if builderState_ResourceDescription2 is not None else set()
        
        pass
    @property
    def importedNames(self):
        return self.__importedNames

    @importedNames.setter
    def importedNames(self, importedNames: str):
        self.__importedNames = importedNames


    @property
    def URI(self):
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI


    @property
    def builderState_ResourceDescription2(self):
        return self.__builderState_ResourceDescription2

    @builderState_ResourceDescription2.setter
    def builderState_ResourceDescription2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builderState_ResourceDescription__builderState_ResourceDescription2", None)
        self.__builderState_ResourceDescription2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "builderState_IReferenceDescription"):
                    opp_val = getattr(item, "builderState_IReferenceDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "builderState_IReferenceDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "builderState_IReferenceDescription"):
                    opp_val = getattr(item, "builderState_IReferenceDescription", None)
                    
                    setattr(item, "builderState_IReferenceDescription", self)
                    

    @property
    def builderState_ResourceDescription(self):
        return self.__builderState_ResourceDescription

    @builderState_ResourceDescription.setter
    def builderState_ResourceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builderState_ResourceDescription__builderState_ResourceDescription", None)
        self.__builderState_ResourceDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "builderState_IEObjectDescription"):
                    opp_val = getattr(item, "builderState_IEObjectDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "builderState_IEObjectDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "builderState_IEObjectDescription"):
                    opp_val = getattr(item, "builderState_IEObjectDescription", None)
                    
                    setattr(item, "builderState_IEObjectDescription", self)
                    

    def getExportedObjectsByType(self, builderState_type) :
        # TODO: Implement getExportedObjectsByType method
        pass

    def getExportedObjects(self, builderState_name, builderState_ignoreCase, builderState_type) :
        # TODO: Implement getExportedObjects method
        pass

    def isEmpty(self) :
        # TODO: Implement isEmpty method
        pass

    def getExportedObjectsByObject(self, builderState_object) :
        # TODO: Implement getExportedObjectsByObject method
        pass

class IEObjectDescription:

    pass
class builderState_EObjectDescription(IEObjectDescription):

    def __init__(self, fragment: str, builderState_EObjectDescription: set["builderState_UserDataEntry"] = None):
        self.fragment = fragment
        self.builderState_EObjectDescription = builderState_EObjectDescription if builderState_EObjectDescription is not None else set()
        
        pass
    @property
    def fragment(self):
        return self.__fragment

    @fragment.setter
    def fragment(self, fragment: str):
        self.__fragment = fragment


    @property
    def builderState_EObjectDescription(self):
        return self.__builderState_EObjectDescription

    @builderState_EObjectDescription.setter
    def builderState_EObjectDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builderState_EObjectDescription__builderState_EObjectDescription", None)
        self.__builderState_EObjectDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "builderState_UserDataEntry"):
                    opp_val = getattr(item, "builderState_UserDataEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "builderState_UserDataEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "builderState_UserDataEntry"):
                    opp_val = getattr(item, "builderState_UserDataEntry", None)
                    
                    setattr(item, "builderState_UserDataEntry", self)
                    

class builderState_IReferenceDescription(ABC):

    def __init__(self, sourceEObjectUri: str, targetEObjectUri: str, indexInList: int, containerEObjectURI: str, builderState_IReferenceDescription: "builderState_ResourceDescription" = None):
        self.sourceEObjectUri = sourceEObjectUri
        self.targetEObjectUri = targetEObjectUri
        self.indexInList = indexInList
        self.containerEObjectURI = containerEObjectURI
        self.builderState_IReferenceDescription = builderState_IReferenceDescription
        
        pass
    @property
    def indexInList(self):
        return self.__indexInList

    @indexInList.setter
    def indexInList(self, indexInList: int):
        self.__indexInList = indexInList


    @property
    def sourceEObjectUri(self):
        return self.__sourceEObjectUri

    @sourceEObjectUri.setter
    def sourceEObjectUri(self, sourceEObjectUri: str):
        self.__sourceEObjectUri = sourceEObjectUri


    @property
    def targetEObjectUri(self):
        return self.__targetEObjectUri

    @targetEObjectUri.setter
    def targetEObjectUri(self, targetEObjectUri: str):
        self.__targetEObjectUri = targetEObjectUri


    @property
    def containerEObjectURI(self):
        return self.__containerEObjectURI

    @containerEObjectURI.setter
    def containerEObjectURI(self, containerEObjectURI: str):
        self.__containerEObjectURI = containerEObjectURI


    @property
    def builderState_IReferenceDescription(self):
        return self.__builderState_IReferenceDescription

    @builderState_IReferenceDescription.setter
    def builderState_IReferenceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builderState_IReferenceDescription__builderState_IReferenceDescription", None)
        self.__builderState_IReferenceDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builderState_ResourceDescription2"):
                opp_val = getattr(old_value, "builderState_ResourceDescription2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builderState_ResourceDescription2"):
                opp_val = getattr(value, "builderState_ResourceDescription2", None)
                if opp_val is None:
                    setattr(value, "builderState_ResourceDescription2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class builderState_IEObjectDescription(ABC):

    def __init__(self, name: str, builderState_IEObjectDescription: "builderState_ResourceDescription" = None, builderState_IEObjectDescription5: "builderState_EClass" = None):
        self.name = name
        self.builderState_IEObjectDescription = builderState_IEObjectDescription
        self.builderState_IEObjectDescription5 = builderState_IEObjectDescription5
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def builderState_IEObjectDescription5(self):
        return self.__builderState_IEObjectDescription5

    @builderState_IEObjectDescription5.setter
    def builderState_IEObjectDescription5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builderState_IEObjectDescription__builderState_IEObjectDescription5", None)
        self.__builderState_IEObjectDescription5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builderState_EClass"):
                opp_val = getattr(old_value, "builderState_EClass", None)
                if opp_val == self:
                    setattr(old_value, "builderState_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builderState_EClass"):
                opp_val = getattr(value, "builderState_EClass", None)
                setattr(value, "builderState_EClass", self)

    @property
    def builderState_IEObjectDescription(self):
        return self.__builderState_IEObjectDescription

    @builderState_IEObjectDescription.setter
    def builderState_IEObjectDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_builderState_IEObjectDescription__builderState_IEObjectDescription", None)
        self.__builderState_IEObjectDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "builderState_ResourceDescription"):
                opp_val = getattr(old_value, "builderState_ResourceDescription", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "builderState_ResourceDescription"):
                opp_val = getattr(value, "builderState_ResourceDescription", None)
                if opp_val is None:
                    setattr(value, "builderState_ResourceDescription", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getEObjectURI(self) :
        # TODO: Implement getEObjectURI method
        pass

    def getUserData(self, builderState_name) :
        # TODO: Implement getUserData method
        pass

    def getQualifiedName(self) :
        # TODO: Implement getQualifiedName method
        pass

    def getUserDataKeys(self) :
        # TODO: Implement getUserDataKeys method
        pass

    def getEObjectOrProxy(self) :
        # TODO: Implement getEObjectOrProxy method
        pass
