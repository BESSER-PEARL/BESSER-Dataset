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
CodeTagType: Enumeration = Enumeration(
    name="CodeTagType",
    literals={
            EnumerationLiteral(name="CLASSPUBLICMETHODSSECTIONDECLARE"),
			EnumerationLiteral(name="CLASSPUBLICMETHODSSECTIONIMPL"),
			EnumerationLiteral(name="CLASSPRIVATEMETHODSSECTIONDECLARE"),
			EnumerationLiteral(name="CLASSPRIVATEMETHODSSECTIONIMPL"),
			EnumerationLiteral(name="FILEHEADERH"),
			EnumerationLiteral(name="FILEHEADERCPP"),
			EnumerationLiteral(name="FILEFOOTERH"),
			EnumerationLiteral(name="FILEFOOTERCPP"),
			EnumerationLiteral(name="FILEINCLUDESH"),
			EnumerationLiteral(name="FILEINCLUDESCPP"),
			EnumerationLiteral(name="CONSTRUCTORINITLIST"),
			EnumerationLiteral(name="CLASSGENERATEDOPERATIONIMPL"),
			EnumerationLiteral(name="CLASSGENERATEDATTRIBUTEGET"),
			EnumerationLiteral(name="CLASSGENERATEDATTRIBUTESET"),
			EnumerationLiteral(name="CLASSPRIVATEMEMBERSSECTIONDECLARE")
    }
)

# Classes
codetaginfo_CodeTag = Class(name="codetaginfo::CodeTag")
codetaginfo_CodeTagContext = Class(name="codetaginfo::CodeTagContext")
codetaginfo_CodeTagInfo = Class(name="codetaginfo::CodeTagInfo")
codetaginfo_DocumentRoot = Class(name="codetaginfo::DocumentRoot")
codetaginfo_EStringToStringMapEntry = Class(name="codetaginfo::EStringToStringMapEntry")

# codetaginfo_CodeTag class attributes and methods
codetaginfo_CodeTag_name: Property = Property(name="name", type=StringType)
codetaginfo_CodeTag_uuid: Property = Property(name="uuid", type=StringType)
codetaginfo_CodeTag_type: Property = Property(name="type", type=StringType)
codetaginfo_CodeTag_tag_begin: Property = Property(name="tag_begin", type=StringType)
codetaginfo_CodeTag_group: Property = Property(name="group", type=StringType)
codetaginfo_CodeTag_contents: Property = Property(name="contents", type=StringType)
codetaginfo_CodeTag_tag_end: Property = Property(name="tag_end", type=StringType)
codetaginfo_CodeTag.attributes={codetaginfo_CodeTag_tag_end, codetaginfo_CodeTag_contents, codetaginfo_CodeTag_type, codetaginfo_CodeTag_uuid, codetaginfo_CodeTag_group, codetaginfo_CodeTag_tag_begin, codetaginfo_CodeTag_name}

# codetaginfo_CodeTagContext class attributes and methods
codetaginfo_CodeTagContext_group: Property = Property(name="group", type=StringType)
codetaginfo_CodeTagContext_component_name: Property = Property(name="component_name", type=StringType)
codetaginfo_CodeTagContext_class_name: Property = Property(name="class_name", type=StringType)
codetaginfo_CodeTagContext_operation_name: Property = Property(name="operation_name", type=StringType)
codetaginfo_CodeTagContext.attributes={codetaginfo_CodeTagContext_component_name, codetaginfo_CodeTagContext_group, codetaginfo_CodeTagContext_operation_name, codetaginfo_CodeTagContext_class_name}

# codetaginfo_CodeTagInfo class attributes and methods
codetaginfo_CodeTagInfo_group: Property = Property(name="group", type=StringType)
codetaginfo_CodeTagInfo_filename: Property = Property(name="filename", type=StringType)
codetaginfo_CodeTagInfo.attributes={codetaginfo_CodeTagInfo_group, codetaginfo_CodeTagInfo_filename}

# codetaginfo_DocumentRoot class attributes and methods
codetaginfo_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
codetaginfo_DocumentRoot.attributes={codetaginfo_DocumentRoot_mixed}

# codetaginfo_EStringToStringMapEntry class attributes and methods

# Relationships
contextinfo0: BinaryAssociation = BinaryAssociation(
    name="contextinfo0",
    ends={
        Property(name="codetaginfo_CodeTagContext", type=codetaginfo_CodeTag, multiplicity=Multiplicity(1, 1)),
        Property(name="codetaginfo_CodeTag", type=codetaginfo_CodeTagContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
codetag1: BinaryAssociation = BinaryAssociation(
    name="codetag1",
    ends={
        Property(name="codetaginfo_CodeTag2", type=codetaginfo_CodeTagInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="codetaginfo_CodeTagInfo", type=codetaginfo_CodeTag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap3: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap3",
    ends={
        Property(name="codetaginfo_EStringToStringMapEntry", type=codetaginfo_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="codetaginfo_DocumentRoot", type=codetaginfo_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation4: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation4",
    ends={
        Property(name="codetaginfo_EStringToStringMapEntry6", type=codetaginfo_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="codetaginfo_DocumentRoot5", type=codetaginfo_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
codeTagInfo7: BinaryAssociation = BinaryAssociation(
    name="codeTagInfo7",
    ends={
        Property(name="codetaginfo_CodeTagInfo9", type=codetaginfo_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="codetaginfo_DocumentRoot8", type=codetaginfo_CodeTagInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="codetaginfo",
    types={codetaginfo_CodeTag, codetaginfo_CodeTagContext, codetaginfo_CodeTagInfo, codetaginfo_DocumentRoot, codetaginfo_EStringToStringMapEntry, CodeTagType},
    associations={contextinfo0, codetag1, xMLNSPrefixMap3, xSISchemaLocation4, codeTagInfo7},
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