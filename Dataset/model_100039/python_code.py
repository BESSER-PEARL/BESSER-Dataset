from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TypeType(Enum):
    xml = "xml"
    text = "text"


############################################
# Definition of Classes
############################################

class qsar_PreprocessingType:

    pass
class qsar_PreprocessingStepType:

    def __init__(self, id: str, name: str, namespace: str, order: str, vendor: str, qsar_PreprocessingStepType: "qsar_PreprocessingType" = None):
        self.id = id
        self.name = name
        self.namespace = namespace
        self.order = order
        self.vendor = vendor
        self.qsar_PreprocessingStepType = qsar_PreprocessingStepType
        
        pass
    @property
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def vendor(self):
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order


    @property
    def qsar_PreprocessingStepType(self):
        return self.__qsar_PreprocessingStepType

    @qsar_PreprocessingStepType.setter
    def qsar_PreprocessingStepType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_PreprocessingStepType__qsar_PreprocessingStepType", None)
        self.__qsar_PreprocessingStepType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qsar_PreprocessingType"):
                opp_val = getattr(old_value, "qsar_PreprocessingType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qsar_PreprocessingType"):
                opp_val = getattr(value, "qsar_PreprocessingType", None)
                if opp_val is None:
                    setattr(value, "qsar_PreprocessingType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class qsar_ResponseunitType:

    def __init__(self, description: str, id: str, name: str, shortname: str, uRL: str, qsar_ResponseunitType: "qsar_QsarType" = None):
        self.description = description
        self.id = id
        self.name = name
        self.shortname = shortname
        self.uRL = uRL
        self.qsar_ResponseunitType = qsar_ResponseunitType
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def uRL(self):
        return self.__uRL

    @uRL.setter
    def uRL(self, uRL: str):
        self.__uRL = uRL


    @property
    def shortname(self):
        return self.__shortname

    @shortname.setter
    def shortname(self, shortname: str):
        self.__shortname = shortname


    @property
    def qsar_ResponseunitType(self):
        return self.__qsar_ResponseunitType

    @qsar_ResponseunitType.setter
    def qsar_ResponseunitType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_ResponseunitType__qsar_ResponseunitType", None)
        self.__qsar_ResponseunitType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qsar_QsarType27"):
                opp_val = getattr(old_value, "qsar_QsarType27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qsar_QsarType27"):
                opp_val = getattr(value, "qsar_QsarType27", None)
                if opp_val is None:
                    setattr(value, "qsar_QsarType27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class qsar_BibTeXMLEntriesClass:

    pass
class qsar_EStringToStringMapEntry:

    pass
class qsar_DocumentRoot:

    def __init__(self, mixed: str, qsar_DocumentRoot8: set["qsar_EStringToStringMapEntry"] = None, qsar_DocumentRoot11: set["qsar_QsarType"] = None, qsar_DocumentRoot: set["qsar_EStringToStringMapEntry"] = None):
        self.mixed = mixed
        self.qsar_DocumentRoot8 = qsar_DocumentRoot8 if qsar_DocumentRoot8 is not None else set()
        self.qsar_DocumentRoot11 = qsar_DocumentRoot11 if qsar_DocumentRoot11 is not None else set()
        self.qsar_DocumentRoot = qsar_DocumentRoot if qsar_DocumentRoot is not None else set()
        
        pass
    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def qsar_DocumentRoot(self):
        return self.__qsar_DocumentRoot

    @qsar_DocumentRoot.setter
    def qsar_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_DocumentRoot__qsar_DocumentRoot", None)
        self.__qsar_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qsar_EStringToStringMapEntry"):
                    opp_val = getattr(item, "qsar_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "qsar_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qsar_EStringToStringMapEntry"):
                    opp_val = getattr(item, "qsar_EStringToStringMapEntry", None)
                    
                    setattr(item, "qsar_EStringToStringMapEntry", self)
                    

    @property
    def qsar_DocumentRoot8(self):
        return self.__qsar_DocumentRoot8

    @qsar_DocumentRoot8.setter
    def qsar_DocumentRoot8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_DocumentRoot__qsar_DocumentRoot8", None)
        self.__qsar_DocumentRoot8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qsar_EStringToStringMapEntry9"):
                    opp_val = getattr(item, "qsar_EStringToStringMapEntry9", None)
                    
                    if opp_val == self:
                        setattr(item, "qsar_EStringToStringMapEntry9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qsar_EStringToStringMapEntry9"):
                    opp_val = getattr(item, "qsar_EStringToStringMapEntry9", None)
                    
                    setattr(item, "qsar_EStringToStringMapEntry9", self)
                    

    @property
    def qsar_DocumentRoot11(self):
        return self.__qsar_DocumentRoot11

    @qsar_DocumentRoot11.setter
    def qsar_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_DocumentRoot__qsar_DocumentRoot11", None)
        self.__qsar_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qsar_QsarType"):
                    opp_val = getattr(item, "qsar_QsarType", None)
                    
                    if opp_val == self:
                        setattr(item, "qsar_QsarType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qsar_QsarType"):
                    opp_val = getattr(item, "qsar_QsarType", None)
                    
                    setattr(item, "qsar_QsarType", self)
                    

class qsar_ParameterType:

    def __init__(self, key: str, value: str, qsar_ParameterType: "qsar_DescriptorType" = None):
        self.key = key
        self.value = value
        self.qsar_ParameterType = qsar_ParameterType
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def qsar_ParameterType(self):
        return self.__qsar_ParameterType

    @qsar_ParameterType.setter
    def qsar_ParameterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_ParameterType__qsar_ParameterType", None)
        self.__qsar_ParameterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qsar_DescriptorType5"):
                opp_val = getattr(old_value, "qsar_DescriptorType5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qsar_DescriptorType5"):
                opp_val = getattr(value, "qsar_DescriptorType5", None)
                if opp_val is None:
                    setattr(value, "qsar_DescriptorType5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class qsar_MetadataType:

    def __init__(self, authors: str, datasetname: str, description: str, license: str, responseLabel: str, responsePlacement: str, uRL: str, qsar_MetadataType: set["qsar_BibTeXMLEntriesClass"] = None, qsar_MetadataType30: "qsar_QsarType" = None):
        self.authors = authors
        self.datasetname = datasetname
        self.description = description
        self.license = license
        self.responseLabel = responseLabel
        self.responsePlacement = responsePlacement
        self.uRL = uRL
        self.qsar_MetadataType = qsar_MetadataType if qsar_MetadataType is not None else set()
        self.qsar_MetadataType30 = qsar_MetadataType30
        
        pass
    @property
    def responseLabel(self):
        return self.__responseLabel

    @responseLabel.setter
    def responseLabel(self, responseLabel: str):
        self.__responseLabel = responseLabel


    @property
    def datasetname(self):
        return self.__datasetname

    @datasetname.setter
    def datasetname(self, datasetname: str):
        self.__datasetname = datasetname


    @property
    def uRL(self):
        return self.__uRL

    @uRL.setter
    def uRL(self, uRL: str):
        self.__uRL = uRL


    @property
    def license(self):
        return self.__license

    @license.setter
    def license(self, license: str):
        self.__license = license


    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, authors: str):
        self.__authors = authors


    @property
    def responsePlacement(self):
        return self.__responsePlacement

    @responsePlacement.setter
    def responsePlacement(self, responsePlacement: str):
        self.__responsePlacement = responsePlacement


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def qsar_MetadataType(self):
        return self.__qsar_MetadataType

    @qsar_MetadataType.setter
    def qsar_MetadataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_MetadataType__qsar_MetadataType", None)
        self.__qsar_MetadataType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qsar_BibTeXMLEntriesClass"):
                    opp_val = getattr(item, "qsar_BibTeXMLEntriesClass", None)
                    
                    if opp_val == self:
                        setattr(item, "qsar_BibTeXMLEntriesClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qsar_BibTeXMLEntriesClass"):
                    opp_val = getattr(item, "qsar_BibTeXMLEntriesClass", None)
                    
                    setattr(item, "qsar_BibTeXMLEntriesClass", self)
                    

    @property
    def qsar_MetadataType30(self):
        return self.__qsar_MetadataType30

    @qsar_MetadataType30.setter
    def qsar_MetadataType30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_MetadataType__qsar_MetadataType30", None)
        self.__qsar_MetadataType30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qsar_QsarType29"):
                opp_val = getattr(old_value, "qsar_QsarType29", None)
                if opp_val == self:
                    setattr(old_value, "qsar_QsarType29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qsar_QsarType29"):
                opp_val = getattr(value, "qsar_QsarType29", None)
                setattr(value, "qsar_QsarType29", self)

class qsar_QsarType:

    pass
class qsar_DescriptorvalueType:

    def __init__(self, index: str, label: str, value: str, qsar_DescriptorvalueType: "qsar_DescriptorresultType" = None):
        self.index = index
        self.label = label
        self.value = value
        self.qsar_DescriptorvalueType = qsar_DescriptorvalueType
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def qsar_DescriptorvalueType(self):
        return self.__qsar_DescriptorvalueType

    @qsar_DescriptorvalueType.setter
    def qsar_DescriptorvalueType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_DescriptorvalueType__qsar_DescriptorvalueType", None)
        self.__qsar_DescriptorvalueType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qsar_DescriptorresultType3"):
                opp_val = getattr(old_value, "qsar_DescriptorresultType3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qsar_DescriptorresultType3"):
                opp_val = getattr(value, "qsar_DescriptorresultType3", None)
                if opp_val is None:
                    setattr(value, "qsar_DescriptorresultType3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class qsar_DescriptorresultType:

    def __init__(self, errorString: str, structureid: str, descriptorid: str, qsar_DescriptorresultType: "qsar_DescriptorresultlistsType" = None, qsar_DescriptorresultType3: set["qsar_DescriptorvalueType"] = None):
        self.errorString = errorString
        self.structureid = structureid
        self.descriptorid = descriptorid
        self.qsar_DescriptorresultType = qsar_DescriptorresultType
        self.qsar_DescriptorresultType3 = qsar_DescriptorresultType3 if qsar_DescriptorresultType3 is not None else set()
        
        pass
    @property
    def structureid(self):
        return self.__structureid

    @structureid.setter
    def structureid(self, structureid: str):
        self.__structureid = structureid


    @property
    def errorString(self):
        return self.__errorString

    @errorString.setter
    def errorString(self, errorString: str):
        self.__errorString = errorString


    @property
    def descriptorid(self):
        return self.__descriptorid

    @descriptorid.setter
    def descriptorid(self, descriptorid: str):
        self.__descriptorid = descriptorid


    @property
    def qsar_DescriptorresultType(self):
        return self.__qsar_DescriptorresultType

    @qsar_DescriptorresultType.setter
    def qsar_DescriptorresultType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_DescriptorresultType__qsar_DescriptorresultType", None)
        self.__qsar_DescriptorresultType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qsar_DescriptorresultlistsType"):
                opp_val = getattr(old_value, "qsar_DescriptorresultlistsType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qsar_DescriptorresultlistsType"):
                opp_val = getattr(value, "qsar_DescriptorresultlistsType", None)
                if opp_val is None:
                    setattr(value, "qsar_DescriptorresultlistsType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qsar_DescriptorresultType3(self):
        return self.__qsar_DescriptorresultType3

    @qsar_DescriptorresultType3.setter
    def qsar_DescriptorresultType3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_DescriptorresultType__qsar_DescriptorresultType3", None)
        self.__qsar_DescriptorresultType3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qsar_DescriptorvalueType"):
                    opp_val = getattr(item, "qsar_DescriptorvalueType", None)
                    
                    if opp_val == self:
                        setattr(item, "qsar_DescriptorvalueType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qsar_DescriptorvalueType"):
                    opp_val = getattr(item, "qsar_DescriptorvalueType", None)
                    
                    setattr(item, "qsar_DescriptorvalueType", self)
                    

class qsar_DescriptorresultlistsType:

    pass
class qsar_DescriptorproviderType:

    def __init__(self, id: str, name: str, uRL: str, vendor: str, version: str, qsar_DescriptorproviderType: "qsar_QsarType" = None):
        self.id = id
        self.name = name
        self.uRL = uRL
        self.vendor = vendor
        self.version = version
        self.qsar_DescriptorproviderType = qsar_DescriptorproviderType
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def vendor(self):
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor


    @property
    def uRL(self):
        return self.__uRL

    @uRL.setter
    def uRL(self, uRL: str):
        self.__uRL = uRL


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def qsar_DescriptorproviderType(self):
        return self.__qsar_DescriptorproviderType

    @qsar_DescriptorproviderType.setter
    def qsar_DescriptorproviderType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_DescriptorproviderType__qsar_DescriptorproviderType", None)
        self.__qsar_DescriptorproviderType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qsar_QsarType20"):
                opp_val = getattr(old_value, "qsar_QsarType20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qsar_QsarType20"):
                opp_val = getattr(value, "qsar_QsarType20", None)
                if opp_val is None:
                    setattr(value, "qsar_QsarType20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class qsar_DescriptorType:

    def __init__(self, id: str, ontologyid: str, provider: str, qsar_DescriptorType: "qsar_DescriptorlistType" = None, qsar_DescriptorType5: set["qsar_ParameterType"] = None):
        self.id = id
        self.ontologyid = ontologyid
        self.provider = provider
        self.qsar_DescriptorType = qsar_DescriptorType
        self.qsar_DescriptorType5 = qsar_DescriptorType5 if qsar_DescriptorType5 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def ontologyid(self):
        return self.__ontologyid

    @ontologyid.setter
    def ontologyid(self, ontologyid: str):
        self.__ontologyid = ontologyid


    @property
    def provider(self):
        return self.__provider

    @provider.setter
    def provider(self, provider: str):
        self.__provider = provider


    @property
    def qsar_DescriptorType5(self):
        return self.__qsar_DescriptorType5

    @qsar_DescriptorType5.setter
    def qsar_DescriptorType5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_DescriptorType__qsar_DescriptorType5", None)
        self.__qsar_DescriptorType5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qsar_ParameterType"):
                    opp_val = getattr(item, "qsar_ParameterType", None)
                    
                    if opp_val == self:
                        setattr(item, "qsar_ParameterType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qsar_ParameterType"):
                    opp_val = getattr(item, "qsar_ParameterType", None)
                    
                    setattr(item, "qsar_ParameterType", self)
                    

    @property
    def qsar_DescriptorType(self):
        return self.__qsar_DescriptorType

    @qsar_DescriptorType.setter
    def qsar_DescriptorType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_DescriptorType__qsar_DescriptorType", None)
        self.__qsar_DescriptorType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qsar_DescriptorlistType"):
                opp_val = getattr(old_value, "qsar_DescriptorlistType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qsar_DescriptorlistType"):
                opp_val = getattr(value, "qsar_DescriptorlistType", None)
                if opp_val is None:
                    setattr(value, "qsar_DescriptorlistType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class qsar_DescriptorlistType:

    pass
class qsar_ResponseType:

    def __init__(self, value: str, structureID: str, unit: str, qsar_ResponseType: "qsar_ResponsesListType" = None):
        self.value = value
        self.structureID = structureID
        self.unit = unit
        self.qsar_ResponseType = qsar_ResponseType
        
        pass
    @property
    def structureID(self):
        return self.__structureID

    @structureID.setter
    def structureID(self, structureID: str):
        self.__structureID = structureID


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def qsar_ResponseType(self):
        return self.__qsar_ResponseType

    @qsar_ResponseType.setter
    def qsar_ResponseType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_ResponseType__qsar_ResponseType", None)
        self.__qsar_ResponseType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qsar_ResponsesListType36"):
                opp_val = getattr(old_value, "qsar_ResponsesListType36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qsar_ResponsesListType36"):
                opp_val = getattr(value, "qsar_ResponsesListType36", None)
                if opp_val is None:
                    setattr(value, "qsar_ResponsesListType36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class qsar_StructureType:

    def __init__(self, problem: str, has2d: str, has3d: str, id: str, inchi: str, resourceid: str, resourceindex: str, qsar_StructureType: "qsar_ResourceType" = None):
        self.problem = problem
        self.has2d = has2d
        self.has3d = has3d
        self.id = id
        self.inchi = inchi
        self.resourceid = resourceid
        self.resourceindex = resourceindex
        self.qsar_StructureType = qsar_StructureType
        
        pass
    @property
    def resourceid(self):
        return self.__resourceid

    @resourceid.setter
    def resourceid(self, resourceid: str):
        self.__resourceid = resourceid


    @property
    def has2d(self):
        return self.__has2d

    @has2d.setter
    def has2d(self, has2d: str):
        self.__has2d = has2d


    @property
    def resourceindex(self):
        return self.__resourceindex

    @resourceindex.setter
    def resourceindex(self, resourceindex: str):
        self.__resourceindex = resourceindex


    @property
    def has3d(self):
        return self.__has3d

    @has3d.setter
    def has3d(self, has3d: str):
        self.__has3d = has3d


    @property
    def inchi(self):
        return self.__inchi

    @inchi.setter
    def inchi(self, inchi: str):
        self.__inchi = inchi


    @property
    def problem(self):
        return self.__problem

    @problem.setter
    def problem(self, problem: str):
        self.__problem = problem


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def qsar_StructureType(self):
        return self.__qsar_StructureType

    @qsar_StructureType.setter
    def qsar_StructureType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_StructureType__qsar_StructureType", None)
        self.__qsar_StructureType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qsar_ResourceType"):
                opp_val = getattr(old_value, "qsar_ResourceType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qsar_ResourceType"):
                opp_val = getattr(value, "qsar_ResourceType", None)
                if opp_val is None:
                    setattr(value, "qsar_ResourceType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class qsar_ResourceType:

    def __init__(self, noMols: str, type: str, uRL: str, checksum: str, containsErrors: str, excluded: str, file: str, id: str, name: str, no2d: str, no3d: str, qsar_ResourceType: set["qsar_StructureType"] = None, qsar_ResourceType39: "qsar_StructurelistType" = None):
        self.noMols = noMols
        self.type = type
        self.uRL = uRL
        self.checksum = checksum
        self.containsErrors = containsErrors
        self.excluded = excluded
        self.file = file
        self.id = id
        self.name = name
        self.no2d = no2d
        self.no3d = no3d
        self.qsar_ResourceType = qsar_ResourceType if qsar_ResourceType is not None else set()
        self.qsar_ResourceType39 = qsar_ResourceType39
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def uRL(self):
        return self.__uRL

    @uRL.setter
    def uRL(self, uRL: str):
        self.__uRL = uRL


    @property
    def checksum(self):
        return self.__checksum

    @checksum.setter
    def checksum(self, checksum: str):
        self.__checksum = checksum


    @property
    def excluded(self):
        return self.__excluded

    @excluded.setter
    def excluded(self, excluded: str):
        self.__excluded = excluded


    @property
    def no2d(self):
        return self.__no2d

    @no2d.setter
    def no2d(self, no2d: str):
        self.__no2d = no2d


    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def no3d(self):
        return self.__no3d

    @no3d.setter
    def no3d(self, no3d: str):
        self.__no3d = no3d


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def containsErrors(self):
        return self.__containsErrors

    @containsErrors.setter
    def containsErrors(self, containsErrors: str):
        self.__containsErrors = containsErrors


    @property
    def noMols(self):
        return self.__noMols

    @noMols.setter
    def noMols(self, noMols: str):
        self.__noMols = noMols


    @property
    def qsar_ResourceType39(self):
        return self.__qsar_ResourceType39

    @qsar_ResourceType39.setter
    def qsar_ResourceType39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_ResourceType__qsar_ResourceType39", None)
        self.__qsar_ResourceType39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qsar_StructurelistType38"):
                opp_val = getattr(old_value, "qsar_StructurelistType38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qsar_StructurelistType38"):
                opp_val = getattr(value, "qsar_StructurelistType38", None)
                if opp_val is None:
                    setattr(value, "qsar_StructurelistType38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qsar_ResourceType(self):
        return self.__qsar_ResourceType

    @qsar_ResourceType.setter
    def qsar_ResourceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qsar_ResourceType__qsar_ResourceType", None)
        self.__qsar_ResourceType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qsar_StructureType"):
                    opp_val = getattr(item, "qsar_StructureType", None)
                    
                    if opp_val == self:
                        setattr(item, "qsar_StructureType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qsar_StructureType"):
                    opp_val = getattr(item, "qsar_StructureType", None)
                    
                    setattr(item, "qsar_StructureType", self)
                    

class qsar_ResponsesListType:

    pass
class qsar_StructurelistType:

    pass