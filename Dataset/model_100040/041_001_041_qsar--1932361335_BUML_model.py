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
TypeType: Enumeration = Enumeration(
    name="TypeType",
    literals={
            EnumerationLiteral(name="xml"),
			EnumerationLiteral(name="text")
    }
)

# Classes
qsar_DescriptorlistType = Class(name="qsar_DescriptorlistType")
qsar_DescriptorType = Class(name="qsar_DescriptorType")
qsar_DescriptorproviderType = Class(name="qsar_DescriptorproviderType")
qsar_DescriptorresultlistsType = Class(name="qsar_DescriptorresultlistsType")
qsar_DescriptorresultType = Class(name="qsar_DescriptorresultType")
qsar_DescriptorvalueType = Class(name="qsar_DescriptorvalueType")
qsar_ParameterType = Class(name="qsar_ParameterType")
qsar_DocumentRoot = Class(name="qsar_DocumentRoot")
qsar_EStringToStringMapEntry = Class(name="qsar_EStringToStringMapEntry")
qsar_QsarType = Class(name="qsar_QsarType")
qsar_MetadataType = Class(name="qsar_MetadataType")
qsar_BibTeXMLEntriesClass = Class(name="qsar_BibTeXMLEntriesClass")
qsar_PreprocessingStepType = Class(name="qsar_PreprocessingStepType")
qsar_PreprocessingType = Class(name="qsar_PreprocessingType")
qsar_StructurelistType = Class(name="qsar_StructurelistType")
qsar_ResponsesListType = Class(name="qsar_ResponsesListType")
qsar_ResponseunitType = Class(name="qsar_ResponseunitType")
qsar_ResourceType = Class(name="qsar_ResourceType")
qsar_StructureType = Class(name="qsar_StructureType")
qsar_ResponseType = Class(name="qsar_ResponseType")

# qsar_DescriptorlistType class attributes and methods

# qsar_DescriptorType class attributes and methods
qsar_DescriptorType_id: Property = Property(name="id", type=StringType)
qsar_DescriptorType_ontologyid: Property = Property(name="ontologyid", type=StringType)
qsar_DescriptorType_provider: Property = Property(name="provider", type=StringType)
qsar_DescriptorType.attributes={qsar_DescriptorType_provider, qsar_DescriptorType_ontologyid, qsar_DescriptorType_id}

# qsar_DescriptorproviderType class attributes and methods
qsar_DescriptorproviderType_name: Property = Property(name="name", type=StringType)
qsar_DescriptorproviderType_uRL: Property = Property(name="uRL", type=StringType)
qsar_DescriptorproviderType_id: Property = Property(name="id", type=StringType)
qsar_DescriptorproviderType_vendor: Property = Property(name="vendor", type=StringType)
qsar_DescriptorproviderType_version: Property = Property(name="version", type=StringType)
qsar_DescriptorproviderType.attributes={qsar_DescriptorproviderType_uRL, qsar_DescriptorproviderType_version, qsar_DescriptorproviderType_id, qsar_DescriptorproviderType_vendor, qsar_DescriptorproviderType_name}

# qsar_DescriptorresultlistsType class attributes and methods

# qsar_DescriptorresultType class attributes and methods
qsar_DescriptorresultType_descriptorid: Property = Property(name="descriptorid", type=StringType)
qsar_DescriptorresultType_structureid: Property = Property(name="structureid", type=StringType)
qsar_DescriptorresultType.attributes={qsar_DescriptorresultType_descriptorid, qsar_DescriptorresultType_structureid}

# qsar_DescriptorvalueType class attributes and methods
qsar_DescriptorvalueType_index: Property = Property(name="index", type=StringType)
qsar_DescriptorvalueType_label: Property = Property(name="label", type=StringType)
qsar_DescriptorvalueType_value: Property = Property(name="value", type=StringType)
qsar_DescriptorvalueType.attributes={qsar_DescriptorvalueType_index, qsar_DescriptorvalueType_label, qsar_DescriptorvalueType_value}

# qsar_ParameterType class attributes and methods
qsar_ParameterType_key: Property = Property(name="key", type=StringType)
qsar_ParameterType_value: Property = Property(name="value", type=StringType)
qsar_ParameterType.attributes={qsar_ParameterType_value, qsar_ParameterType_key}

# qsar_DocumentRoot class attributes and methods
qsar_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
qsar_DocumentRoot.attributes={qsar_DocumentRoot_mixed}

# qsar_EStringToStringMapEntry class attributes and methods

# qsar_QsarType class attributes and methods

# qsar_MetadataType class attributes and methods
qsar_MetadataType_license: Property = Property(name="license", type=StringType)
qsar_MetadataType_uRL: Property = Property(name="uRL", type=StringType)
qsar_MetadataType_authors: Property = Property(name="authors", type=StringType)
qsar_MetadataType_datasetname: Property = Property(name="datasetname", type=StringType)
qsar_MetadataType_description: Property = Property(name="description", type=StringType)
qsar_MetadataType.attributes={qsar_MetadataType_description, qsar_MetadataType_uRL, qsar_MetadataType_datasetname, qsar_MetadataType_license, qsar_MetadataType_authors}

# qsar_BibTeXMLEntriesClass class attributes and methods

# qsar_PreprocessingStepType class attributes and methods
qsar_PreprocessingStepType_id: Property = Property(name="id", type=StringType)
qsar_PreprocessingStepType_name: Property = Property(name="name", type=StringType)
qsar_PreprocessingStepType_namespace: Property = Property(name="namespace", type=StringType)
qsar_PreprocessingStepType_order: Property = Property(name="order", type=StringType)
qsar_PreprocessingStepType_vendor: Property = Property(name="vendor", type=StringType)
qsar_PreprocessingStepType.attributes={qsar_PreprocessingStepType_order, qsar_PreprocessingStepType_vendor, qsar_PreprocessingStepType_name, qsar_PreprocessingStepType_id, qsar_PreprocessingStepType_namespace}

# qsar_PreprocessingType class attributes and methods

# qsar_StructurelistType class attributes and methods

# qsar_ResponsesListType class attributes and methods

# qsar_ResponseunitType class attributes and methods
qsar_ResponseunitType_description: Property = Property(name="description", type=StringType)
qsar_ResponseunitType_id: Property = Property(name="id", type=StringType)
qsar_ResponseunitType_name: Property = Property(name="name", type=StringType)
qsar_ResponseunitType_shortname: Property = Property(name="shortname", type=StringType)
qsar_ResponseunitType_uRL: Property = Property(name="uRL", type=StringType)
qsar_ResponseunitType.attributes={qsar_ResponseunitType_id, qsar_ResponseunitType_shortname, qsar_ResponseunitType_description, qsar_ResponseunitType_uRL, qsar_ResponseunitType_name}

# qsar_ResourceType class attributes and methods
qsar_ResourceType_checksum: Property = Property(name="checksum", type=StringType)
qsar_ResourceType_excluded: Property = Property(name="excluded", type=StringType)
qsar_ResourceType_file: Property = Property(name="file", type=StringType)
qsar_ResourceType_id: Property = Property(name="id", type=StringType)
qsar_ResourceType_name: Property = Property(name="name", type=StringType)
qsar_ResourceType_no2d: Property = Property(name="no2d", type=StringType)
qsar_ResourceType_no3d: Property = Property(name="no3d", type=StringType)
qsar_ResourceType_noMols: Property = Property(name="noMols", type=StringType)
qsar_ResourceType_type: Property = Property(name="type", type=StringType)
qsar_ResourceType_uRL: Property = Property(name="uRL", type=StringType)
qsar_ResourceType.attributes={qsar_ResourceType_name, qsar_ResourceType_file, qsar_ResourceType_type, qsar_ResourceType_id, qsar_ResourceType_no2d, qsar_ResourceType_uRL, qsar_ResourceType_no3d, qsar_ResourceType_noMols, qsar_ResourceType_excluded, qsar_ResourceType_checksum}

# qsar_StructureType class attributes and methods
qsar_StructureType_resourceindex: Property = Property(name="resourceindex", type=StringType)
qsar_StructureType_id: Property = Property(name="id", type=StringType)
qsar_StructureType_inchi: Property = Property(name="inchi", type=StringType)
qsar_StructureType_resourceid: Property = Property(name="resourceid", type=StringType)
qsar_StructureType.attributes={qsar_StructureType_resourceid, qsar_StructureType_inchi, qsar_StructureType_resourceindex, qsar_StructureType_id}

# qsar_ResponseType class attributes and methods
qsar_ResponseType_value: Property = Property(name="value", type=StringType)
qsar_ResponseType_arrayValues: Property = Property(name="arrayValues", type=StringType)
qsar_ResponseType_structureID: Property = Property(name="structureID", type=StringType)
qsar_ResponseType_unit: Property = Property(name="unit", type=StringType)
qsar_ResponseType.attributes={qsar_ResponseType_value, qsar_ResponseType_unit, qsar_ResponseType_arrayValues, qsar_ResponseType_structureID}

# Relationships
descriptors0: BinaryAssociation = BinaryAssociation(
    name="descriptors0",
    ends={
        Property(name="qsar_DescriptorType", type=qsar_DescriptorlistType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_DescriptorlistType", type=qsar_DescriptorType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptorresult1: BinaryAssociation = BinaryAssociation(
    name="descriptorresult1",
    ends={
        Property(name="qsar_DescriptorresultType", type=qsar_DescriptorresultlistsType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_DescriptorresultlistsType", type=qsar_DescriptorresultType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptorvalue2: BinaryAssociation = BinaryAssociation(
    name="descriptorvalue2",
    ends={
        Property(name="qsar_DescriptorvalueType", type=qsar_DescriptorresultType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_DescriptorresultType3", type=qsar_DescriptorvalueType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter4: BinaryAssociation = BinaryAssociation(
    name="parameter4",
    ends={
        Property(name="qsar_ParameterType", type=qsar_DescriptorType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_DescriptorType5", type=qsar_ParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap6: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap6",
    ends={
        Property(name="qsar_EStringToStringMapEntry", type=qsar_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_DocumentRoot", type=qsar_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation7: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation7",
    ends={
        Property(name="qsar_EStringToStringMapEntry9", type=qsar_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_DocumentRoot8", type=qsar_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qsar10: BinaryAssociation = BinaryAssociation(
    name="qsar10",
    ends={
        Property(name="qsar_QsarType", type=qsar_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_DocumentRoot11", type=qsar_QsarType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference12: BinaryAssociation = BinaryAssociation(
    name="reference12",
    ends={
        Property(name="qsar_BibTeXMLEntriesClass", type=qsar_MetadataType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_MetadataType", type=qsar_BibTeXMLEntriesClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptorproviders19: BinaryAssociation = BinaryAssociation(
    name="descriptorproviders19",
    ends={
        Property(name="qsar_DescriptorproviderType", type=qsar_QsarType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_QsarType20", type=qsar_DescriptorproviderType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preprocessing21: BinaryAssociation = BinaryAssociation(
    name="preprocessing21",
    ends={
        Property(name="qsar_PreprocessingType23", type=qsar_QsarType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_QsarType22", type=qsar_PreprocessingType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preprocessingStep13: BinaryAssociation = BinaryAssociation(
    name="preprocessingStep13",
    ends={
        Property(name="qsar_PreprocessingStepType", type=qsar_PreprocessingType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_PreprocessingType", type=qsar_PreprocessingStepType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structurelist14: BinaryAssociation = BinaryAssociation(
    name="structurelist14",
    ends={
        Property(name="qsar_StructurelistType", type=qsar_QsarType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_QsarType15", type=qsar_StructurelistType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
descriptorlist16: BinaryAssociation = BinaryAssociation(
    name="descriptorlist16",
    ends={
        Property(name="qsar_DescriptorlistType18", type=qsar_QsarType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_QsarType17", type=qsar_DescriptorlistType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
responselist24: BinaryAssociation = BinaryAssociation(
    name="responselist24",
    ends={
        Property(name="qsar_ResponsesListType", type=qsar_QsarType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_QsarType25", type=qsar_ResponsesListType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
responseunit26: BinaryAssociation = BinaryAssociation(
    name="responseunit26",
    ends={
        Property(name="qsar_ResponseunitType", type=qsar_QsarType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_QsarType27", type=qsar_ResponseunitType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metadata28: BinaryAssociation = BinaryAssociation(
    name="metadata28",
    ends={
        Property(name="qsar_MetadataType30", type=qsar_QsarType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_QsarType29", type=qsar_MetadataType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
descriptorresultlist31: BinaryAssociation = BinaryAssociation(
    name="descriptorresultlist31",
    ends={
        Property(name="qsar_DescriptorresultlistsType33", type=qsar_QsarType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_QsarType32", type=qsar_DescriptorresultlistsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structure34: BinaryAssociation = BinaryAssociation(
    name="structure34",
    ends={
        Property(name="qsar_StructureType", type=qsar_ResourceType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_ResourceType", type=qsar_StructureType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
response35: BinaryAssociation = BinaryAssociation(
    name="response35",
    ends={
        Property(name="qsar_ResponseType", type=qsar_ResponsesListType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_ResponsesListType36", type=qsar_ResponseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources37: BinaryAssociation = BinaryAssociation(
    name="resources37",
    ends={
        Property(name="qsar_ResourceType39", type=qsar_StructurelistType, multiplicity=Multiplicity(1, 1)),
        Property(name="qsar_StructurelistType38", type=qsar_ResourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="qsar",
    types={qsar_DescriptorlistType, qsar_DescriptorType, qsar_DescriptorproviderType, qsar_DescriptorresultlistsType, qsar_DescriptorresultType, qsar_DescriptorvalueType, qsar_ParameterType, qsar_DocumentRoot, qsar_EStringToStringMapEntry, qsar_QsarType, qsar_MetadataType, qsar_BibTeXMLEntriesClass, qsar_PreprocessingStepType, qsar_PreprocessingType, qsar_StructurelistType, qsar_ResponsesListType, qsar_ResponseunitType, qsar_ResourceType, qsar_StructureType, qsar_ResponseType, TypeType},
    associations={descriptors0, descriptorresult1, descriptorvalue2, parameter4, xMLNSPrefixMap6, xSISchemaLocation7, qsar10, reference12, descriptorproviders19, preprocessing21, preprocessingStep13, structurelist14, descriptorlist16, responselist24, responseunit26, metadata28, descriptorresultlist31, structure34, response35, resources37},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)