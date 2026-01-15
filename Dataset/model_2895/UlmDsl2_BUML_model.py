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
ulmDsl2_Model = Class(name="ulmDsl2::Model")
ulmDsl2_Context = Class(name="ulmDsl2::Context")
ulmDsl2_Attribute = Class(name="ulmDsl2::Attribute")
ulmDsl2_Lookup = Class(name="ulmDsl2::Lookup")
ulmDsl2_Entity = Class(name="ulmDsl2::Entity")
ulmDsl2_AttributeStringType = Class(name="ulmDsl2::AttributeStringType")
ulmDsl2_AttributeDecimalType = Class(name="ulmDsl2::AttributeDecimalType")
ulmDsl2_Feature = Class(name="ulmDsl2::Feature")
ulmDsl2_FeatureType = Class(name="ulmDsl2::FeatureType")
ulmDsl2_EObject = Class(name="ulmDsl2::EObject")
ulmDsl2_AttributeType = Class(name="ulmDsl2::AttributeType")
ulmDsl2_AttributeFeatureType = Class(name="ulmDsl2::AttributeFeatureType")
ulmDsl2_EntityFeatureType = Class(name="ulmDsl2::EntityFeatureType")
ulmDsl2_LookupInt = Class(name="ulmDsl2::LookupInt")
ulmDsl2_LookupIntValue = Class(name="ulmDsl2::LookupIntValue")
ulmDsl2_LookupString = Class(name="ulmDsl2::LookupString")
ulmDsl2_LookupStringValue = Class(name="ulmDsl2::LookupStringValue")

# ulmDsl2_Model class attributes and methods
ulmDsl2_Model_name: Property = Property(name="name", type=StringType)
ulmDsl2_Model.attributes={ulmDsl2_Model_name}

# ulmDsl2_Context class attributes and methods
ulmDsl2_Context_name: Property = Property(name="name", type=StringType)
ulmDsl2_Context_version: Property = Property(name="version", type=StringType)
ulmDsl2_Context.attributes={ulmDsl2_Context_version, ulmDsl2_Context_name}

# ulmDsl2_Attribute class attributes and methods
ulmDsl2_Attribute_name: Property = Property(name="name", type=StringType)
ulmDsl2_Attribute_desc: Property = Property(name="desc", type=StringType)
ulmDsl2_Attribute.attributes={ulmDsl2_Attribute_desc, ulmDsl2_Attribute_name}

# ulmDsl2_Lookup class attributes and methods
ulmDsl2_Lookup_name: Property = Property(name="name", type=StringType)
ulmDsl2_Lookup.attributes={ulmDsl2_Lookup_name}

# ulmDsl2_Entity class attributes and methods
ulmDsl2_Entity_type: Property = Property(name="type", type=StringType)
ulmDsl2_Entity_name: Property = Property(name="name", type=StringType)
ulmDsl2_Entity_desc: Property = Property(name="desc", type=StringType)
ulmDsl2_Entity.attributes={ulmDsl2_Entity_desc, ulmDsl2_Entity_type, ulmDsl2_Entity_name}

# ulmDsl2_AttributeStringType class attributes and methods
ulmDsl2_AttributeStringType_name: Property = Property(name="name", type=StringType)
ulmDsl2_AttributeStringType_array: Property = Property(name="array", type=BooleanType)
ulmDsl2_AttributeStringType_length: Property = Property(name="length", type=IntegerType)
ulmDsl2_AttributeStringType.attributes={ulmDsl2_AttributeStringType_array, ulmDsl2_AttributeStringType_name, ulmDsl2_AttributeStringType_length}

# ulmDsl2_AttributeDecimalType class attributes and methods
ulmDsl2_AttributeDecimalType_name: Property = Property(name="name", type=StringType)
ulmDsl2_AttributeDecimalType_array: Property = Property(name="array", type=BooleanType)
ulmDsl2_AttributeDecimalType_scale: Property = Property(name="scale", type=IntegerType)
ulmDsl2_AttributeDecimalType_precision: Property = Property(name="precision", type=IntegerType)
ulmDsl2_AttributeDecimalType.attributes={ulmDsl2_AttributeDecimalType_name, ulmDsl2_AttributeDecimalType_scale, ulmDsl2_AttributeDecimalType_precision, ulmDsl2_AttributeDecimalType_array}

# ulmDsl2_Feature class attributes and methods
ulmDsl2_Feature_mandatory: Property = Property(name="mandatory", type=BooleanType)
ulmDsl2_Feature_identifier: Property = Property(name="identifier", type=BooleanType)
ulmDsl2_Feature_name: Property = Property(name="name", type=StringType)
ulmDsl2_Feature.attributes={ulmDsl2_Feature_identifier, ulmDsl2_Feature_mandatory, ulmDsl2_Feature_name}

# ulmDsl2_FeatureType class attributes and methods

# ulmDsl2_EObject class attributes and methods

# ulmDsl2_AttributeType class attributes and methods
ulmDsl2_AttributeType_name: Property = Property(name="name", type=StringType)
ulmDsl2_AttributeType.attributes={ulmDsl2_AttributeType_name}

# ulmDsl2_AttributeFeatureType class attributes and methods

# ulmDsl2_EntityFeatureType class attributes and methods
ulmDsl2_EntityFeatureType_array: Property = Property(name="array", type=BooleanType)
ulmDsl2_EntityFeatureType_length: Property = Property(name="length", type=IntegerType)
ulmDsl2_EntityFeatureType.attributes={ulmDsl2_EntityFeatureType_length, ulmDsl2_EntityFeatureType_array}

# ulmDsl2_LookupInt class attributes and methods
ulmDsl2_LookupInt_description: Property = Property(name="description", type=StringType)
ulmDsl2_LookupInt.attributes={ulmDsl2_LookupInt_description}

# ulmDsl2_LookupIntValue class attributes and methods
ulmDsl2_LookupIntValue_value: Property = Property(name="value", type=IntegerType)
ulmDsl2_LookupIntValue_description: Property = Property(name="description", type=StringType)
ulmDsl2_LookupIntValue.attributes={ulmDsl2_LookupIntValue_value, ulmDsl2_LookupIntValue_description}

# ulmDsl2_LookupString class attributes and methods
ulmDsl2_LookupString_description: Property = Property(name="description", type=StringType)
ulmDsl2_LookupString.attributes={ulmDsl2_LookupString_description}

# ulmDsl2_LookupStringValue class attributes and methods
ulmDsl2_LookupStringValue_value: Property = Property(name="value", type=StringType)
ulmDsl2_LookupStringValue_description: Property = Property(name="description", type=StringType)
ulmDsl2_LookupStringValue.attributes={ulmDsl2_LookupStringValue_value, ulmDsl2_LookupStringValue_description}

# Relationships
contexts0: BinaryAssociation = BinaryAssociation(
    name="contexts0",
    ends={
        Property(name="ulmDsl2_Context", type=ulmDsl2_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_Model", type=ulmDsl2_Context, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="ulmDsl2_Attribute", type=ulmDsl2_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_Context2", type=ulmDsl2_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lookups3: BinaryAssociation = BinaryAssociation(
    name="lookups3",
    ends={
        Property(name="ulmDsl2_Lookup", type=ulmDsl2_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_Context4", type=ulmDsl2_Lookup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities5: BinaryAssociation = BinaryAssociation(
    name="entities5",
    ends={
        Property(name="ulmDsl2_Entity", type=ulmDsl2_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_Context6", type=ulmDsl2_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType10: BinaryAssociation = BinaryAssociation(
    name="superType10",
    ends={
        Property(name="ulmDsl2_Entity11", type=ulmDsl2_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_Entity9", type=ulmDsl2_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features12: BinaryAssociation = BinaryAssociation(
    name="features12",
    ends={
        Property(name="ulmDsl2_Feature", type=ulmDsl2_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_Entity13", type=ulmDsl2_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="ulmDsl2_EObject", type=ulmDsl2_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_Attribute8", type=ulmDsl2_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="ulmDsl2_EObject18", type=ulmDsl2_FeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_FeatureType17", type=ulmDsl2_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute19: BinaryAssociation = BinaryAssociation(
    name="attribute19",
    ends={
        Property(name="ulmDsl2_Attribute20", type=ulmDsl2_AttributeFeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_AttributeFeatureType", type=ulmDsl2_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
lookup21: BinaryAssociation = BinaryAssociation(
    name="lookup21",
    ends={
        Property(name="ulmDsl2_Lookup23", type=ulmDsl2_AttributeFeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_AttributeFeatureType22", type=ulmDsl2_Lookup, multiplicity=Multiplicity(0, 1))
    }
)
entity24: BinaryAssociation = BinaryAssociation(
    name="entity24",
    ends={
        Property(name="ulmDsl2_Entity25", type=ulmDsl2_EntityFeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_EntityFeatureType", type=ulmDsl2_Entity, multiplicity=Multiplicity(0, 1))
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="ulmDsl2_EObject28", type=ulmDsl2_Lookup, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_Lookup27", type=ulmDsl2_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values29: BinaryAssociation = BinaryAssociation(
    name="values29",
    ends={
        Property(name="ulmDsl2_LookupIntValue", type=ulmDsl2_LookupInt, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_LookupInt", type=ulmDsl2_LookupIntValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="ulmDsl2_FeatureType", type=ulmDsl2_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_Feature15", type=ulmDsl2_FeatureType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values30: BinaryAssociation = BinaryAssociation(
    name="values30",
    ends={
        Property(name="ulmDsl2_LookupStringValue", type=ulmDsl2_LookupString, multiplicity=Multiplicity(1, 1)),
        Property(name="ulmDsl2_LookupString", type=ulmDsl2_LookupStringValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ulmDsl2",
    types={ulmDsl2_Model, ulmDsl2_Context, ulmDsl2_Attribute, ulmDsl2_Lookup, ulmDsl2_Entity, ulmDsl2_AttributeStringType, ulmDsl2_AttributeDecimalType, ulmDsl2_Feature, ulmDsl2_FeatureType, ulmDsl2_EObject, ulmDsl2_AttributeType, ulmDsl2_AttributeFeatureType, ulmDsl2_EntityFeatureType, ulmDsl2_LookupInt, ulmDsl2_LookupIntValue, ulmDsl2_LookupString, ulmDsl2_LookupStringValue},
    associations={contexts0, attributes1, lookups3, entities5, superType10, features12, type7, type16, attribute19, lookup21, entity24, type26, values29, type14, values30},
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