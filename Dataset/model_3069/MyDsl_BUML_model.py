####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
RestStatusCode: Enumeration = Enumeration(
    name="RestStatusCode",
    literals={
            EnumerationLiteral(name="INFORMATIONAL"),
			EnumerationLiteral(name="SUCCESS"),
			EnumerationLiteral(name="REDIRECTION"),
			EnumerationLiteral(name="CLIENT_ERROR"),
			EnumerationLiteral(name="SERVER_ERROR"),
			EnumerationLiteral(name="NETWORK_ERROR")
    }
)

# Classes
myDsl_RestAPI = Class(name="myDsl::RestAPI")
myDsl_Resource = Class(name="myDsl::Resource")
myDsl_Service = Class(name="myDsl::Service")
myDsl_DataAccessObject = Class(name="myDsl::DataAccessObject")
myDsl_ExceptionMapper = Class(name="myDsl::ExceptionMapper")
myDsl_DomainModel = Class(name="myDsl::DomainModel")
myDsl_Type = Class(name="myDsl::Type")
myDsl_ModelMapper = Class(name="myDsl::ModelMapper")
myDsl_Transformation = Class(name="myDsl::Transformation")
myDsl_PrimitiveType = Class(name="myDsl::PrimitiveType")
Type = Class(name="Type")
myDsl_DataModel = Class(name="myDsl::DataModel")
myDsl_Feature = Class(name="myDsl::Feature")
myDsl_RestModel = Class(name="myDsl::RestModel")
myDsl_ValidationService = Class(name="myDsl::ValidationService")
myDsl_Block = Class(name="myDsl::Block")
myDsl_RestModelMethodConclusion = Class(name="myDsl::RestModelMethodConclusion")
myDsl_DataModelMethodConclusion = Class(name="myDsl::DataModelMethodConclusion")
myDsl_RestExceptionList = Class(name="myDsl::RestExceptionList")
myDsl_RestException = Class(name="myDsl::RestException")
myDsl_BaseException = Class(name="myDsl::BaseException")

# myDsl_RestAPI class attributes and methods

# myDsl_Resource class attributes and methods
myDsl_Resource_findby: Property = Property(name="findby", type=StringType)
myDsl_Resource_updateby: Property = Property(name="updateby", type=StringType)
myDsl_Resource_name: Property = Property(name="name", type=StringType)
myDsl_Resource_deleteby: Property = Property(name="deleteby", type=StringType)
myDsl_Resource.attributes={myDsl_Resource_deleteby, myDsl_Resource_name, myDsl_Resource_findby, myDsl_Resource_updateby}

# myDsl_Service class attributes and methods
myDsl_Service_name: Property = Property(name="name", type=StringType)
myDsl_Service_findby: Property = Property(name="findby", type=StringType)
myDsl_Service_updateby: Property = Property(name="updateby", type=StringType)
myDsl_Service_deleteby: Property = Property(name="deleteby", type=StringType)
myDsl_Service.attributes={myDsl_Service_deleteby, myDsl_Service_name, myDsl_Service_updateby, myDsl_Service_findby}

# myDsl_DataAccessObject class attributes and methods
myDsl_DataAccessObject_name: Property = Property(name="name", type=StringType)
myDsl_DataAccessObject_findby: Property = Property(name="findby", type=StringType)
myDsl_DataAccessObject_deleteby: Property = Property(name="deleteby", type=StringType)
myDsl_DataAccessObject_updateby: Property = Property(name="updateby", type=StringType)
myDsl_DataAccessObject.attributes={myDsl_DataAccessObject_name, myDsl_DataAccessObject_updateby, myDsl_DataAccessObject_findby, myDsl_DataAccessObject_deleteby}

# myDsl_ExceptionMapper class attributes and methods
myDsl_ExceptionMapper_name: Property = Property(name="name", type=StringType)
myDsl_ExceptionMapper.attributes={myDsl_ExceptionMapper_name}

# myDsl_DomainModel class attributes and methods

# myDsl_Type class attributes and methods
myDsl_Type_name: Property = Property(name="name", type=StringType)
myDsl_Type.attributes={myDsl_Type_name}

# myDsl_ModelMapper class attributes and methods

# myDsl_Transformation class attributes and methods

# myDsl_PrimitiveType class attributes and methods

# Type class attributes and methods

# myDsl_DataModel class attributes and methods
myDsl_DataModel_id: Property = Property(name="id", type=StringType)
myDsl_DataModel.attributes={myDsl_DataModel_id}

# myDsl_Feature class attributes and methods
myDsl_Feature_many: Property = Property(name="many", type=BooleanType)
myDsl_Feature_name: Property = Property(name="name", type=StringType)
myDsl_Feature.attributes={myDsl_Feature_name, myDsl_Feature_many}

# myDsl_RestModel class attributes and methods
myDsl_RestModel_id: Property = Property(name="id", type=StringType)
myDsl_RestModel_self: Property = Property(name="self", type=StringType)
myDsl_RestModel.attributes={myDsl_RestModel_self, myDsl_RestModel_id}

# myDsl_ValidationService class attributes and methods

# myDsl_Block class attributes and methods
myDsl_Block_code: Property = Property(name="code", type=StringType)
myDsl_Block.attributes={myDsl_Block_code}

# myDsl_RestModelMethodConclusion class attributes and methods

# myDsl_DataModelMethodConclusion class attributes and methods

# myDsl_RestExceptionList class attributes and methods

# myDsl_RestException class attributes and methods
myDsl_RestException_statusCode: Property = Property(name="statusCode", type=StringType)
myDsl_RestException_message: Property = Property(name="message", type=StringType)
myDsl_RestException.attributes={myDsl_RestException_message, myDsl_RestException_statusCode}

# myDsl_BaseException class attributes and methods
myDsl_BaseException_errorCode: Property = Property(name="errorCode", type=StringType)
myDsl_BaseException_message: Property = Property(name="message", type=StringType)
myDsl_BaseException.attributes={myDsl_BaseException_errorCode, myDsl_BaseException_message}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="myDsl_DomainModel", type=myDsl_Type, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="myDsl_Type", type=myDsl_DomainModel, multiplicity=Multiplicity(1, 1))
    }
)
apis1: BinaryAssociation = BinaryAssociation(
    name="apis1",
    ends={
        Property(name="myDsl_RestAPI", type=myDsl_DomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DomainModel2", type=myDsl_RestAPI, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resource3: BinaryAssociation = BinaryAssociation(
    name="resource3",
    ends={
        Property(name="myDsl_Resource", type=myDsl_RestAPI, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_RestAPI4", type=myDsl_Resource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
service5: BinaryAssociation = BinaryAssociation(
    name="service5",
    ends={
        Property(name="myDsl_Service", type=myDsl_RestAPI, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_RestAPI6", type=myDsl_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dao7: BinaryAssociation = BinaryAssociation(
    name="dao7",
    ends={
        Property(name="myDsl_DataAccessObject", type=myDsl_RestAPI, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_RestAPI8", type=myDsl_DataAccessObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptionMapper9: BinaryAssociation = BinaryAssociation(
    name="exceptionMapper9",
    ends={
        Property(name="myDsl_ExceptionMapper", type=myDsl_RestAPI, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_RestAPI10", type=myDsl_ExceptionMapper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType16: BinaryAssociation = BinaryAssociation(
    name="superType16",
    ends={
        Property(name="myDsl_RestModel", type=myDsl_RestModel, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_RestModel15", type=myDsl_RestModel, multiplicity=Multiplicity(0, 1))
    }
)
features17: BinaryAssociation = BinaryAssociation(
    name="features17",
    ends={
        Property(name="myDsl_Feature19", type=myDsl_RestModel, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_RestModel18", type=myDsl_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformation20: BinaryAssociation = BinaryAssociation(
    name="transformation20",
    ends={
        Property(name="myDsl_Transformation", type=myDsl_ModelMapper, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ModelMapper", type=myDsl_Transformation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataModel21: BinaryAssociation = BinaryAssociation(
    name="dataModel21",
    ends={
        Property(name="myDsl_DataModel23", type=myDsl_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Transformation22", type=myDsl_DataModel, multiplicity=Multiplicity(0, 1))
    }
)
restModel24: BinaryAssociation = BinaryAssociation(
    name="restModel24",
    ends={
        Property(name="myDsl_RestModel26", type=myDsl_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Transformation25", type=myDsl_RestModel, multiplicity=Multiplicity(0, 1))
    }
)
superType12: BinaryAssociation = BinaryAssociation(
    name="superType12",
    ends={
        Property(name="myDsl_DataModel", type=myDsl_DataModel, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataModel11", type=myDsl_DataModel, multiplicity=Multiplicity(0, 1))
    }
)
features13: BinaryAssociation = BinaryAssociation(
    name="features13",
    ends={
        Property(name="myDsl_Feature", type=myDsl_DataModel, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataModel14", type=myDsl_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createValService39: BinaryAssociation = BinaryAssociation(
    name="createValService39",
    ends={
        Property(name="myDsl_ValidationService", type=myDsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Resource40", type=myDsl_ValidationService, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
createMethod41: BinaryAssociation = BinaryAssociation(
    name="createMethod41",
    ends={
        Property(name="myDsl_Block", type=myDsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Resource42", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
createConclusion43: BinaryAssociation = BinaryAssociation(
    name="createConclusion43",
    ends={
        Property(name="myDsl_RestModelMethodConclusion", type=myDsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Resource44", type=myDsl_RestModelMethodConclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
findMethod45: BinaryAssociation = BinaryAssociation(
    name="findMethod45",
    ends={
        Property(name="myDsl_Block47", type=myDsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Resource46", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
findConclusion48: BinaryAssociation = BinaryAssociation(
    name="findConclusion48",
    ends={
        Property(name="myDsl_RestModelMethodConclusion50", type=myDsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Resource49", type=myDsl_RestModelMethodConclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateRestModel51: BinaryAssociation = BinaryAssociation(
    name="updateRestModel51",
    ends={
        Property(name="myDsl_RestModel53", type=myDsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Resource52", type=myDsl_RestModel, multiplicity=Multiplicity(0, 1))
    }
)
updateValService54: BinaryAssociation = BinaryAssociation(
    name="updateValService54",
    ends={
        Property(name="myDsl_ValidationService56", type=myDsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Resource55", type=myDsl_ValidationService, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="myDsl_Type29", type=myDsl_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Feature28", type=myDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
service30: BinaryAssociation = BinaryAssociation(
    name="service30",
    ends={
        Property(name="myDsl_Service32", type=myDsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Resource31", type=myDsl_Service, multiplicity=Multiplicity(0, 9999))
    }
)
exceptionMapper33: BinaryAssociation = BinaryAssociation(
    name="exceptionMapper33",
    ends={
        Property(name="myDsl_ExceptionMapper35", type=myDsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Resource34", type=myDsl_ExceptionMapper, multiplicity=Multiplicity(0, 1))
    }
)
createRestModel36: BinaryAssociation = BinaryAssociation(
    name="createRestModel36",
    ends={
        Property(name="myDsl_RestModel38", type=myDsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Resource37", type=myDsl_RestModel, multiplicity=Multiplicity(0, 1))
    }
)
dao68: BinaryAssociation = BinaryAssociation(
    name="dao68",
    ends={
        Property(name="myDsl_DataAccessObject70", type=myDsl_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Service69", type=myDsl_DataAccessObject, multiplicity=Multiplicity(0, 9999))
    }
)
createDataModel71: BinaryAssociation = BinaryAssociation(
    name="createDataModel71",
    ends={
        Property(name="myDsl_DataModel73", type=myDsl_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Service72", type=myDsl_DataModel, multiplicity=Multiplicity(0, 1))
    }
)
createMethod74: BinaryAssociation = BinaryAssociation(
    name="createMethod74",
    ends={
        Property(name="myDsl_Block76", type=myDsl_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Service75", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
createConclusion77: BinaryAssociation = BinaryAssociation(
    name="createConclusion77",
    ends={
        Property(name="myDsl_DataModelMethodConclusion", type=myDsl_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Service78", type=myDsl_DataModelMethodConclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
findMethod79: BinaryAssociation = BinaryAssociation(
    name="findMethod79",
    ends={
        Property(name="myDsl_Block81", type=myDsl_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Service80", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
findConclusion82: BinaryAssociation = BinaryAssociation(
    name="findConclusion82",
    ends={
        Property(name="myDsl_DataModelMethodConclusion84", type=myDsl_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Service83", type=myDsl_DataModelMethodConclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateMethod57: BinaryAssociation = BinaryAssociation(
    name="updateMethod57",
    ends={
        Property(name="myDsl_Block59", type=myDsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Resource58", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateConclusion60: BinaryAssociation = BinaryAssociation(
    name="updateConclusion60",
    ends={
        Property(name="myDsl_RestModelMethodConclusion62", type=myDsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Resource61", type=myDsl_RestModelMethodConclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deleteMethod63: BinaryAssociation = BinaryAssociation(
    name="deleteMethod63",
    ends={
        Property(name="myDsl_Block65", type=myDsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Resource64", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception466: BinaryAssociation = BinaryAssociation(
    name="exception466",
    ends={
        Property(name="myDsl_RestExceptionList", type=myDsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Resource67", type=myDsl_RestExceptionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception497: BinaryAssociation = BinaryAssociation(
    name="exception497",
    ends={
        Property(name="myDsl_Service98", type=myDsl_RestExceptionList, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="myDsl_RestExceptionList99", type=myDsl_Service, multiplicity=Multiplicity(1, 1))
    }
)
restModel100: BinaryAssociation = BinaryAssociation(
    name="restModel100",
    ends={
        Property(name="myDsl_RestModel102", type=myDsl_ValidationService, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ValidationService101", type=myDsl_RestModel, multiplicity=Multiplicity(0, 1))
    }
)
block103: BinaryAssociation = BinaryAssociation(
    name="block103",
    ends={
        Property(name="myDsl_Block105", type=myDsl_ValidationService, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ValidationService104", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
createDataModel106: BinaryAssociation = BinaryAssociation(
    name="createDataModel106",
    ends={
        Property(name="myDsl_DataModel108", type=myDsl_DataAccessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataAccessObject107", type=myDsl_DataModel, multiplicity=Multiplicity(0, 1))
    }
)
createMethod109: BinaryAssociation = BinaryAssociation(
    name="createMethod109",
    ends={
        Property(name="myDsl_Block111", type=myDsl_DataAccessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataAccessObject110", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
createConclusion112: BinaryAssociation = BinaryAssociation(
    name="createConclusion112",
    ends={
        Property(name="myDsl_DataModelMethodConclusion114", type=myDsl_DataAccessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataAccessObject113", type=myDsl_DataModelMethodConclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateDataModel85: BinaryAssociation = BinaryAssociation(
    name="updateDataModel85",
    ends={
        Property(name="myDsl_DataModel87", type=myDsl_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Service86", type=myDsl_DataModel, multiplicity=Multiplicity(0, 1))
    }
)
updateMethod88: BinaryAssociation = BinaryAssociation(
    name="updateMethod88",
    ends={
        Property(name="myDsl_Block90", type=myDsl_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Service89", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateConclusion91: BinaryAssociation = BinaryAssociation(
    name="updateConclusion91",
    ends={
        Property(name="myDsl_DataModelMethodConclusion93", type=myDsl_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Service92", type=myDsl_DataModelMethodConclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deleteMethod94: BinaryAssociation = BinaryAssociation(
    name="deleteMethod94",
    ends={
        Property(name="myDsl_Block96", type=myDsl_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Service95", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateConclusion127: BinaryAssociation = BinaryAssociation(
    name="updateConclusion127",
    ends={
        Property(name="myDsl_DataModelMethodConclusion129", type=myDsl_DataAccessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataAccessObject128", type=myDsl_DataModelMethodConclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deleteMethod130: BinaryAssociation = BinaryAssociation(
    name="deleteMethod130",
    ends={
        Property(name="myDsl_Block132", type=myDsl_DataAccessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataAccessObject131", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptions133: BinaryAssociation = BinaryAssociation(
    name="exceptions133",
    ends={
        Property(name="myDsl_RestExceptionList135", type=myDsl_DataAccessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataAccessObject134", type=myDsl_RestExceptionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
findMethod115: BinaryAssociation = BinaryAssociation(
    name="findMethod115",
    ends={
        Property(name="myDsl_Block117", type=myDsl_DataAccessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataAccessObject116", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
findConclusion118: BinaryAssociation = BinaryAssociation(
    name="findConclusion118",
    ends={
        Property(name="myDsl_DataModelMethodConclusion120", type=myDsl_DataAccessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataAccessObject119", type=myDsl_DataModelMethodConclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateDataModel121: BinaryAssociation = BinaryAssociation(
    name="updateDataModel121",
    ends={
        Property(name="myDsl_DataModel123", type=myDsl_DataAccessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataAccessObject122", type=myDsl_DataModel, multiplicity=Multiplicity(0, 1))
    }
)
updateMethod124: BinaryAssociation = BinaryAssociation(
    name="updateMethod124",
    ends={
        Property(name="myDsl_Block126", type=myDsl_DataAccessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataAccessObject125", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restException150: BinaryAssociation = BinaryAssociation(
    name="restException150",
    ends={
        Property(name="myDsl_RestException152", type=myDsl_ExceptionMapper, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExceptionMapper151", type=myDsl_RestException, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseException153: BinaryAssociation = BinaryAssociation(
    name="baseException153",
    ends={
        Property(name="myDsl_BaseException", type=myDsl_ExceptionMapper, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExceptionMapper154", type=myDsl_BaseException, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataModel136: BinaryAssociation = BinaryAssociation(
    name="dataModel136",
    ends={
        Property(name="myDsl_DataModel138", type=myDsl_DataModelMethodConclusion, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataModelMethodConclusion137", type=myDsl_DataModel, multiplicity=Multiplicity(0, 1))
    }
)
exceptions139: BinaryAssociation = BinaryAssociation(
    name="exceptions139",
    ends={
        Property(name="myDsl_RestExceptionList141", type=myDsl_DataModelMethodConclusion, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DataModelMethodConclusion140", type=myDsl_RestExceptionList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
restModel142: BinaryAssociation = BinaryAssociation(
    name="restModel142",
    ends={
        Property(name="myDsl_RestModel144", type=myDsl_RestModelMethodConclusion, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_RestModelMethodConclusion143", type=myDsl_RestModel, multiplicity=Multiplicity(0, 1))
    }
)
exception145: BinaryAssociation = BinaryAssociation(
    name="exception145",
    ends={
        Property(name="myDsl_RestExceptionList147", type=myDsl_RestModelMethodConclusion, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_RestModelMethodConclusion146", type=myDsl_RestExceptionList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exception148: BinaryAssociation = BinaryAssociation(
    name="exception148",
    ends={
        Property(name="myDsl_RestException", type=myDsl_RestExceptionList, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_RestExceptionList149", type=myDsl_RestException, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_myDsl_ModelMapper_Type = Generalization(general=Type, specific=myDsl_ModelMapper)
gen_myDsl_PrimitiveType_Type = Generalization(general=Type, specific=myDsl_PrimitiveType)
gen_myDsl_DataModel_Type = Generalization(general=Type, specific=myDsl_DataModel)
gen_myDsl_RestModel_Type = Generalization(general=Type, specific=myDsl_RestModel)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_RestAPI, myDsl_Resource, myDsl_Service, myDsl_DataAccessObject, myDsl_ExceptionMapper, myDsl_DomainModel, myDsl_Type, myDsl_ModelMapper, myDsl_Transformation, myDsl_PrimitiveType, Type, myDsl_DataModel, myDsl_Feature, myDsl_RestModel, myDsl_ValidationService, myDsl_Block, myDsl_RestModelMethodConclusion, myDsl_DataModelMethodConclusion, myDsl_RestExceptionList, myDsl_RestException, myDsl_BaseException, RestStatusCode},
    associations={elements0, apis1, resource3, service5, dao7, exceptionMapper9, superType16, features17, transformation20, dataModel21, restModel24, superType12, features13, createValService39, createMethod41, createConclusion43, findMethod45, findConclusion48, updateRestModel51, updateValService54, type27, service30, exceptionMapper33, createRestModel36, dao68, createDataModel71, createMethod74, createConclusion77, findMethod79, findConclusion82, updateMethod57, updateConclusion60, deleteMethod63, exception466, exception497, restModel100, block103, createDataModel106, createMethod109, createConclusion112, updateDataModel85, updateMethod88, updateConclusion91, deleteMethod94, updateConclusion127, deleteMethod130, exceptions133, findMethod115, findConclusion118, updateDataModel121, updateMethod124, restException150, baseException153, dataModel136, exceptions139, restModel142, exception145, exception148},
    generalizations={gen_myDsl_ModelMapper_Type, gen_myDsl_PrimitiveType_Type, gen_myDsl_DataModel_Type, gen_myDsl_RestModel_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)