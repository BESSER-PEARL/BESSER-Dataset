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
EEnumOp: Enumeration = Enumeration(
    name="EEnumOp",
    literals={
            EnumerationLiteral(name="oneway"),
			EnumerationLiteral(name="notification"),
			EnumerationLiteral(name="requestresponse"),
			EnumerationLiteral(name="solicitresponse")
    }
)

EEnumMes: Enumeration = Enumeration(
    name="EEnumMes",
    literals={
            EnumerationLiteral(name="input"),
			EnumerationLiteral(name="output"),
			EnumerationLiteral(name="fault")
    }
)

EEnumSubset: Enumeration = Enumeration(
    name="EEnumSubset",
    literals={
            EnumerationLiteral(name="req"),
			EnumerationLiteral(name="pro"),
			EnumerationLiteral(name="off"),
			EnumerationLiteral(name="exp")
    }
)

EEnumValueType: Enumeration = Enumeration(
    name="EEnumValueType",
    literals={
            EnumerationLiteral(name="string"),
			EnumerationLiteral(name="date"),
			EnumerationLiteral(name="document"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="double")
    }
)

EEnumDimensionType: Enumeration = Enumeration(
    name="EEnumDimensionType",
    literals={
            EnumerationLiteral(name="monotonic"),
			EnumerationLiteral(name="antitonic")
    }
)

EEnumIntention: Enumeration = Enumeration(
    name="EEnumIntention",
    literals={
            EnumerationLiteral(name="offering"),
			EnumerationLiteral(name="expectation")
    }
)

EEnumlogicalType: Enumeration = Enumeration(
    name="EEnumlogicalType",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

# Classes
ASD_ServiceDescription = Class(name="ASD::ServiceDescription")
NamedElement = Class(name="NamedElement")
ASD_Operation = Class(name="ASD::Operation")
ASD_InfoType = Class(name="ASD::InfoType")
ASD_Message = Class(name="ASD::Message")
ASD_Profile = Class(name="ASD::Profile")
ASD_AssertionSet = Class(name="ASD::AssertionSet")
ASD_Assertion = Class(name="ASD::Assertion")
ASD_NamedElement = Class(name="ASD::NamedElement", is_abstract=True)
ASD_Annotation = Class(name="ASD::Annotation")
ASD_InfoTypeImported = Class(name="ASD::InfoTypeImported")
InfoType = Class(name="InfoType")

# ASD_ServiceDescription class attributes and methods

# NamedElement class attributes and methods

# ASD_Operation class attributes and methods
ASD_Operation_messagePattern: Property = Property(name="messagePattern", type=StringType)
ASD_Operation.attributes={ASD_Operation_messagePattern}

# ASD_InfoType class attributes and methods
ASD_InfoType_valueType: Property = Property(name="valueType", type=StringType)
ASD_InfoType_valueRange: Property = Property(name="valueRange", type=StringType)
ASD_InfoType_subset: Property = Property(name="subset", type=StringType)
ASD_InfoType.attributes={ASD_InfoType_subset, ASD_InfoType_valueType, ASD_InfoType_valueRange}

# ASD_Message class attributes and methods
ASD_Message_role: Property = Property(name="role", type=StringType)
ASD_Message_subset: Property = Property(name="subset", type=StringType)
ASD_Message.attributes={ASD_Message_subset, ASD_Message_role}

# ASD_Profile class attributes and methods

# ASD_AssertionSet class attributes and methods
ASD_AssertionSet_lType: Property = Property(name="lType", type=StringType)
ASD_AssertionSet.attributes={ASD_AssertionSet_lType}

# ASD_Assertion class attributes and methods
ASD_Assertion_dimensionType: Property = Property(name="dimensionType", type=StringType)
ASD_Assertion_role: Property = Property(name="role", type=StringType)
ASD_Assertion_minVal: Property = Property(name="minVal", type=FloatType)
ASD_Assertion_maxVal: Property = Property(name="maxVal", type=FloatType)
ASD_Assertion_lType: Property = Property(name="lType", type=StringType)
ASD_Assertion_subset: Property = Property(name="subset", type=StringType)
ASD_Assertion_dimension: Property = Property(name="dimension", type=StringType)
ASD_Assertion.attributes={ASD_Assertion_dimension, ASD_Assertion_role, ASD_Assertion_minVal, ASD_Assertion_lType, ASD_Assertion_subset, ASD_Assertion_dimensionType, ASD_Assertion_maxVal}

# ASD_NamedElement class attributes and methods
ASD_NamedElement_name: Property = Property(name="name", type=StringType)
ASD_NamedElement.attributes={ASD_NamedElement_name}

# ASD_Annotation class attributes and methods
ASD_Annotation_value: Property = Property(name="value", type=StringType)
ASD_Annotation_key: Property = Property(name="key", type=StringType)
ASD_Annotation.attributes={ASD_Annotation_key, ASD_Annotation_value}

# ASD_InfoTypeImported class attributes and methods
ASD_InfoTypeImported_url: Property = Property(name="url", type=StringType)
ASD_InfoTypeImported.attributes={ASD_InfoTypeImported_url}

# InfoType class attributes and methods

# Relationships
operations0: BinaryAssociation = BinaryAssociation(
    name="operations0",
    ends={
        Property(name="Operation", type=ASD_ServiceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service", type=ASD_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents5: BinaryAssociation = BinaryAssociation(
    name="contents5",
    ends={
        Property(name="Message", type=ASD_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=ASD_Message, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
service6: BinaryAssociation = BinaryAssociation(
    name="service6",
    ends={
        Property(name="ServiceDescription", type=ASD_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operations", type=ASD_ServiceDescription, multiplicity=Multiplicity(0, 1))
    }
)
infoType7: BinaryAssociation = BinaryAssociation(
    name="infoType7",
    ends={
        Property(name="InfoType8", type=ASD_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="message", type=ASD_InfoType, multiplicity=Multiplicity(1, 9999))
    }
)
operation9: BinaryAssociation = BinaryAssociation(
    name="operation9",
    ends={
        Property(name="Operation10", type=ASD_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=ASD_Operation, multiplicity=Multiplicity(0, 1))
    }
)
infotypes1: BinaryAssociation = BinaryAssociation(
    name="infotypes1",
    ends={
        Property(name="InfoType", type=ASD_ServiceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service2", type=ASD_InfoType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
profiles3: BinaryAssociation = BinaryAssociation(
    name="profiles3",
    ends={
        Property(name="Profile", type=ASD_ServiceDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="service4", type=ASD_Profile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message16: BinaryAssociation = BinaryAssociation(
    name="message16",
    ends={
        Property(name="Message17", type=ASD_InfoType, multiplicity=Multiplicity(1, 1)),
        Property(name="infoType", type=ASD_Message, multiplicity=Multiplicity(0, 9999))
    }
)
service18: BinaryAssociation = BinaryAssociation(
    name="service18",
    ends={
        Property(name="ServiceDescription19", type=ASD_InfoType, multiplicity=Multiplicity(1, 1)),
        Property(name="infotypes", type=ASD_ServiceDescription, multiplicity=Multiplicity(0, 1))
    }
)
infoType12: BinaryAssociation = BinaryAssociation(
    name="infoType12",
    ends={
        Property(name="ASD_InfoType", type=ASD_InfoType, multiplicity=Multiplicity(1, 1)),
        Property(name="ASD_InfoType11", type=ASD_InfoType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref14: BinaryAssociation = BinaryAssociation(
    name="ref14",
    ends={
        Property(name="ASD_InfoType15", type=ASD_InfoType, multiplicity=Multiplicity(1, 1)),
        Property(name="ASD_InfoType13", type=ASD_InfoType, multiplicity=Multiplicity(0, 1))
    }
)
refers20: BinaryAssociation = BinaryAssociation(
    name="refers20",
    ends={
        Property(name="ASD_Operation", type=ASD_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="ASD_Profile", type=ASD_Operation, multiplicity=Multiplicity(1, 9999))
    }
)
sets21: BinaryAssociation = BinaryAssociation(
    name="sets21",
    ends={
        Property(name="AssertionSet", type=ASD_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="profile", type=ASD_AssertionSet, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
service22: BinaryAssociation = BinaryAssociation(
    name="service22",
    ends={
        Property(name="ServiceDescription23", type=ASD_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="profiles", type=ASD_ServiceDescription, multiplicity=Multiplicity(0, 1))
    }
)
profile24: BinaryAssociation = BinaryAssociation(
    name="profile24",
    ends={
        Property(name="Profile25", type=ASD_AssertionSet, multiplicity=Multiplicity(1, 1)),
        Property(name="sets", type=ASD_Profile, multiplicity=Multiplicity(0, 1))
    }
)
assertions26: BinaryAssociation = BinaryAssociation(
    name="assertions26",
    ends={
        Property(name="Assertion", type=ASD_AssertionSet, multiplicity=Multiplicity(1, 1)),
        Property(name="set", type=ASD_Assertion, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
set27: BinaryAssociation = BinaryAssociation(
    name="set27",
    ends={
        Property(name="AssertionSet28", type=ASD_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="assertions", type=ASD_AssertionSet, multiplicity=Multiplicity(0, 1))
    }
)
annotations29: BinaryAssociation = BinaryAssociation(
    name="annotations29",
    ends={
        Property(name="Annotation", type=ASD_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=ASD_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner30: BinaryAssociation = BinaryAssociation(
    name="owner30",
    ends={
        Property(name="NamedElement", type=ASD_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="annotations", type=ASD_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ASD_ServiceDescription_NamedElement = Generalization(general=NamedElement, specific=ASD_ServiceDescription)
gen_ASD_Operation_NamedElement = Generalization(general=NamedElement, specific=ASD_Operation)
gen_ASD_Message_NamedElement = Generalization(general=NamedElement, specific=ASD_Message)
gen_ASD_InfoType_NamedElement = Generalization(general=NamedElement, specific=ASD_InfoType)
gen_ASD_Profile_NamedElement = Generalization(general=NamedElement, specific=ASD_Profile)
gen_ASD_AssertionSet_NamedElement = Generalization(general=NamedElement, specific=ASD_AssertionSet)
gen_ASD_Assertion_NamedElement = Generalization(general=NamedElement, specific=ASD_Assertion)
gen_ASD_InfoTypeImported_InfoType = Generalization(general=InfoType, specific=ASD_InfoTypeImported)

# Domain Model
domain_model = DomainModel(
    name="ASD",
    types={ASD_ServiceDescription, NamedElement, ASD_Operation, ASD_InfoType, ASD_Message, ASD_Profile, ASD_AssertionSet, ASD_Assertion, ASD_NamedElement, ASD_Annotation, ASD_InfoTypeImported, InfoType, EEnumOp, EEnumMes, EEnumSubset, EEnumValueType, EEnumDimensionType, EEnumIntention, EEnumlogicalType},
    associations={operations0, contents5, service6, infoType7, operation9, infotypes1, profiles3, message16, service18, infoType12, ref14, refers20, sets21, service22, profile24, assertions26, set27, annotations29, owner30},
    generalizations={gen_ASD_ServiceDescription_NamedElement, gen_ASD_Operation_NamedElement, gen_ASD_Message_NamedElement, gen_ASD_InfoType_NamedElement, gen_ASD_Profile_NamedElement, gen_ASD_AssertionSet_NamedElement, gen_ASD_Assertion_NamedElement, gen_ASD_InfoTypeImported_InfoType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)