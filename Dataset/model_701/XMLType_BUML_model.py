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

# Classes
type_AnyType = Class(name="type::AnyType")
type_ProcessingInstruction = Class(name="type::ProcessingInstruction")
type_SimpleAnyType = Class(name="type::SimpleAnyType")
AnyType = Class(name="AnyType")
type_EDataType = Class(name="type::EDataType")
type_XMLTypeDocumentRoot = Class(name="type::XMLTypeDocumentRoot")
type_EStringToStringMapEntry = Class(name="type::EStringToStringMapEntry")

# type_AnyType class attributes and methods
type_AnyType_any: Property = Property(name="any", type=StringType)
type_AnyType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
type_AnyType_mixed: Property = Property(name="mixed", type=StringType)
type_AnyType.attributes={type_AnyType_anyAttribute, type_AnyType_any, type_AnyType_mixed}

# type_ProcessingInstruction class attributes and methods
type_ProcessingInstruction_data: Property = Property(name="data", type=StringType)
type_ProcessingInstruction_target: Property = Property(name="target", type=StringType)
type_ProcessingInstruction.attributes={type_ProcessingInstruction_target, type_ProcessingInstruction_data}

# type_SimpleAnyType class attributes and methods
type_SimpleAnyType_rawValue: Property = Property(name="rawValue", type=StringType)
type_SimpleAnyType_value: Property = Property(name="value", type=StringType)
type_SimpleAnyType.attributes={type_SimpleAnyType_value, type_SimpleAnyType_rawValue}

# AnyType class attributes and methods

# type_EDataType class attributes and methods

# type_XMLTypeDocumentRoot class attributes and methods
type_XMLTypeDocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
type_XMLTypeDocumentRoot_cDATA: Property = Property(name="cDATA", type=StringType)
type_XMLTypeDocumentRoot_text: Property = Property(name="text", type=StringType)
type_XMLTypeDocumentRoot_comment: Property = Property(name="comment", type=StringType)
type_XMLTypeDocumentRoot.attributes={type_XMLTypeDocumentRoot_cDATA, type_XMLTypeDocumentRoot_comment, type_XMLTypeDocumentRoot_text, type_XMLTypeDocumentRoot_mixed}

# type_EStringToStringMapEntry class attributes and methods

# Relationships
instanceType0: BinaryAssociation = BinaryAssociation(
    name="instanceType0",
    ends={
        Property(name="type_EDataType", type=type_SimpleAnyType, multiplicity=Multiplicity(1, 1)),
        Property(name="type_SimpleAnyType", type=type_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
xMLNSPrefixMap1: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap1",
    ends={
        Property(name="type_EStringToStringMapEntry", type=type_XMLTypeDocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="type_XMLTypeDocumentRoot", type=type_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation2: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation2",
    ends={
        Property(name="type_EStringToStringMapEntry4", type=type_XMLTypeDocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="type_XMLTypeDocumentRoot3", type=type_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processingInstruction5: BinaryAssociation = BinaryAssociation(
    name="processingInstruction5",
    ends={
        Property(name="type_ProcessingInstruction", type=type_XMLTypeDocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="type_XMLTypeDocumentRoot6", type=type_ProcessingInstruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_type_SimpleAnyType_AnyType = Generalization(general=AnyType, specific=type_SimpleAnyType)

# Domain Model
domain_model = DomainModel(
    name="type",
    types={type_AnyType, type_ProcessingInstruction, type_SimpleAnyType, AnyType, type_EDataType, type_XMLTypeDocumentRoot, type_EStringToStringMapEntry},
    associations={instanceType0, xMLNSPrefixMap1, xSISchemaLocation2, processingInstruction5},
    generalizations={gen_type_SimpleAnyType_AnyType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)