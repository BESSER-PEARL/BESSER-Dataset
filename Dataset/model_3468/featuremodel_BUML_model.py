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
VariabilityType: Enumeration = Enumeration(
    name="VariabilityType",
    literals={
            EnumerationLiteral(name="mandatory"),
			EnumerationLiteral(name="optional"),
			EnumerationLiteral(name="alternative"),
			EnumerationLiteral(name="or")
    }
)

# Classes
featuremodel_Rule = Class(name="featuremodel::Rule")
featuremodel_FeatureModel = Class(name="featuremodel::FeatureModel")
featuremodel_Description = Class(name="featuremodel::Description")
featuremodel_Attribute = Class(name="featuremodel::Attribute")
featuremodel_Feature = Class(name="featuremodel::Feature")
featuremodel_Constraint = Class(name="featuremodel::Constraint")
Rule = Class(name="Rule")
featuremodel_Group = Class(name="featuremodel::Group")
featuremodel_AttributeValue = Class(name="featuremodel::AttributeValue", is_abstract=True)
featuremodel_AttributeType = Class(name="featuremodel::AttributeType", is_abstract=True)
featuremodel_AttributeTypeInt = Class(name="featuremodel::AttributeTypeInt")
AttributeType = Class(name="AttributeType")
featuremodel_AttributeTypeString = Class(name="featuremodel::AttributeTypeString")
featuremodel_AttributeTypeBoolean = Class(name="featuremodel::AttributeTypeBoolean")
featuremodel_AttributeTypeEObject = Class(name="featuremodel::AttributeTypeEObject")
featuremodel_AttributeValueInt = Class(name="featuremodel::AttributeValueInt")
AttributeValue = Class(name="AttributeValue")
featuremodel_AttributeValueString = Class(name="featuremodel::AttributeValueString")
featuremodel_AttributeValueBoolean = Class(name="featuremodel::AttributeValueBoolean")
featuremodel_AttributeValueEObject = Class(name="featuremodel::AttributeValueEObject")
featuremodel_EObject = Class(name="featuremodel::EObject")

# featuremodel_Rule class attributes and methods
featuremodel_Rule_language: Property = Property(name="language", type=StringType)
featuremodel_Rule_code: Property = Property(name="code", type=StringType)
featuremodel_Rule.attributes={featuremodel_Rule_code, featuremodel_Rule_language}

# featuremodel_FeatureModel class attributes and methods
featuremodel_FeatureModel_id: Property = Property(name="id", type=StringType)
featuremodel_FeatureModel_version: Property = Property(name="version", type=StringType)
featuremodel_FeatureModel.attributes={featuremodel_FeatureModel_version, featuremodel_FeatureModel_id}

# featuremodel_Description class attributes and methods
featuremodel_Description_id: Property = Property(name="id", type=StringType)
featuremodel_Description_text: Property = Property(name="text", type=StringType)
featuremodel_Description.attributes={featuremodel_Description_text, featuremodel_Description_id}

# featuremodel_Attribute class attributes and methods
featuremodel_Attribute_id: Property = Property(name="id", type=StringType)
featuremodel_Attribute_name: Property = Property(name="name", type=StringType)
featuremodel_Attribute_setable: Property = Property(name="setable", type=BooleanType)
featuremodel_Attribute.attributes={featuremodel_Attribute_name, featuremodel_Attribute_id, featuremodel_Attribute_setable}

# featuremodel_Feature class attributes and methods
featuremodel_Feature_id: Property = Property(name="id", type=StringType)
featuremodel_Feature_name: Property = Property(name="name", type=StringType)
featuremodel_Feature_type: Property = Property(name="type", type=StringType)
featuremodel_Feature_m_getParent: Method = Method(name="getParent", parameters={}, type=StringType)
featuremodel_Feature_m_getParentGroup: Method = Method(name="getParentGroup", parameters={}, type=StringType)
featuremodel_Feature_m_getModel: Method = Method(name="getModel", parameters={}, type=StringType)
featuremodel_Feature_m_getVariabilityType: Method = Method(name="getVariabilityType", parameters={}, type=StringType)
featuremodel_Feature.attributes={featuremodel_Feature_id, featuremodel_Feature_type, featuremodel_Feature_name}
featuremodel_Feature.methods={featuremodel_Feature_m_getModel, featuremodel_Feature_m_getParentGroup, featuremodel_Feature_m_getVariabilityType, featuremodel_Feature_m_getParent}

# featuremodel_Constraint class attributes and methods
featuremodel_Constraint_id: Property = Property(name="id", type=StringType)
featuremodel_Constraint_m_getModel: Method = Method(name="getModel", parameters={}, type=StringType)
featuremodel_Constraint.attributes={featuremodel_Constraint_id}
featuremodel_Constraint.methods={featuremodel_Constraint_m_getModel}

# Rule class attributes and methods

# featuremodel_Group class attributes and methods
featuremodel_Group_id: Property = Property(name="id", type=StringType)
featuremodel_Group_lower: Property = Property(name="lower", type=IntegerType)
featuremodel_Group_upper: Property = Property(name="upper", type=IntegerType)
featuremodel_Group.attributes={featuremodel_Group_id, featuremodel_Group_lower, featuremodel_Group_upper}

# featuremodel_AttributeValue class attributes and methods

# featuremodel_AttributeType class attributes and methods

# featuremodel_AttributeTypeInt class attributes and methods

# AttributeType class attributes and methods

# featuremodel_AttributeTypeString class attributes and methods

# featuremodel_AttributeTypeBoolean class attributes and methods

# featuremodel_AttributeTypeEObject class attributes and methods

# featuremodel_AttributeValueInt class attributes and methods
featuremodel_AttributeValueInt_value: Property = Property(name="value", type=IntegerType)
featuremodel_AttributeValueInt.attributes={featuremodel_AttributeValueInt_value}

# AttributeValue class attributes and methods

# featuremodel_AttributeValueString class attributes and methods
featuremodel_AttributeValueString_value: Property = Property(name="value", type=StringType)
featuremodel_AttributeValueString.attributes={featuremodel_AttributeValueString_value}

# featuremodel_AttributeValueBoolean class attributes and methods
featuremodel_AttributeValueBoolean_value: Property = Property(name="value", type=BooleanType)
featuremodel_AttributeValueBoolean.attributes={featuremodel_AttributeValueBoolean_value}

# featuremodel_AttributeValueEObject class attributes and methods

# featuremodel_EObject class attributes and methods

# Relationships
description0: BinaryAssociation = BinaryAssociation(
    name="description0",
    ends={
        Property(name="featuremodel_Description", type=featuremodel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodel_FeatureModel", type=featuremodel_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="featuremodel_Attribute", type=featuremodel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodel_FeatureModel2", type=featuremodel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root3: BinaryAssociation = BinaryAssociation(
    name="root3",
    ends={
        Property(name="featuremodel_Feature", type=featuremodel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodel_FeatureModel4", type=featuremodel_Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraints5: BinaryAssociation = BinaryAssociation(
    name="constraints5",
    ends={
        Property(name="featuremodel_Constraint", type=featuremodel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodel_FeatureModel6", type=featuremodel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description7: BinaryAssociation = BinaryAssociation(
    name="description7",
    ends={
        Property(name="featuremodel_Description9", type=featuremodel_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodel_Constraint8", type=featuremodel_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
features10: BinaryAssociation = BinaryAssociation(
    name="features10",
    ends={
        Property(name="featuremodel_Feature11", type=featuremodel_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodel_Group", type=featuremodel_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
description12: BinaryAssociation = BinaryAssociation(
    name="description12",
    ends={
        Property(name="featuremodel_Description14", type=featuremodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodel_Feature13", type=featuremodel_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes15: BinaryAssociation = BinaryAssociation(
    name="attributes15",
    ends={
        Property(name="featuremodel_Attribute17", type=featuremodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodel_Feature16", type=featuremodel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children18: BinaryAssociation = BinaryAssociation(
    name="children18",
    ends={
        Property(name="featuremodel_Group20", type=featuremodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodel_Feature19", type=featuremodel_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description21: BinaryAssociation = BinaryAssociation(
    name="description21",
    ends={
        Property(name="featuremodel_Description23", type=featuremodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodel_Attribute22", type=featuremodel_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue24: BinaryAssociation = BinaryAssociation(
    name="defaultValue24",
    ends={
        Property(name="featuremodel_AttributeValue", type=featuremodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodel_Attribute25", type=featuremodel_AttributeValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="featuremodel_AttributeType", type=featuremodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodel_Attribute27", type=featuremodel_AttributeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value28: BinaryAssociation = BinaryAssociation(
    name="value28",
    ends={
        Property(name="featuremodel_EObject", type=featuremodel_AttributeValueEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="featuremodel_AttributeValueEObject", type=featuremodel_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_featuremodel_Constraint_Rule = Generalization(general=Rule, specific=featuremodel_Constraint)
gen_featuremodel_AttributeTypeInt_AttributeType = Generalization(general=AttributeType, specific=featuremodel_AttributeTypeInt)
gen_featuremodel_AttributeTypeString_AttributeType = Generalization(general=AttributeType, specific=featuremodel_AttributeTypeString)
gen_featuremodel_AttributeTypeBoolean_AttributeType = Generalization(general=AttributeType, specific=featuremodel_AttributeTypeBoolean)
gen_featuremodel_AttributeTypeEObject_AttributeType = Generalization(general=AttributeType, specific=featuremodel_AttributeTypeEObject)
gen_featuremodel_AttributeValueInt_AttributeValue = Generalization(general=AttributeValue, specific=featuremodel_AttributeValueInt)
gen_featuremodel_AttributeValueString_AttributeValue = Generalization(general=AttributeValue, specific=featuremodel_AttributeValueString)
gen_featuremodel_AttributeValueBoolean_AttributeValue = Generalization(general=AttributeValue, specific=featuremodel_AttributeValueBoolean)
gen_featuremodel_AttributeValueEObject_AttributeValue = Generalization(general=AttributeValue, specific=featuremodel_AttributeValueEObject)

# Domain Model
domain_model = DomainModel(
    name="featuremodel",
    types={featuremodel_Rule, featuremodel_FeatureModel, featuremodel_Description, featuremodel_Attribute, featuremodel_Feature, featuremodel_Constraint, Rule, featuremodel_Group, featuremodel_AttributeValue, featuremodel_AttributeType, featuremodel_AttributeTypeInt, AttributeType, featuremodel_AttributeTypeString, featuremodel_AttributeTypeBoolean, featuremodel_AttributeTypeEObject, featuremodel_AttributeValueInt, AttributeValue, featuremodel_AttributeValueString, featuremodel_AttributeValueBoolean, featuremodel_AttributeValueEObject, featuremodel_EObject, VariabilityType},
    associations={description0, attributes1, root3, constraints5, description7, features10, description12, attributes15, children18, description21, defaultValue24, type26, value28},
    generalizations={gen_featuremodel_Constraint_Rule, gen_featuremodel_AttributeTypeInt_AttributeType, gen_featuremodel_AttributeTypeString_AttributeType, gen_featuremodel_AttributeTypeBoolean_AttributeType, gen_featuremodel_AttributeTypeEObject_AttributeType, gen_featuremodel_AttributeValueInt_AttributeValue, gen_featuremodel_AttributeValueString_AttributeValue, gen_featuremodel_AttributeValueBoolean_AttributeValue, gen_featuremodel_AttributeValueEObject_AttributeValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)