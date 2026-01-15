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
fc_FeatureModel = Class(name="fc::FeatureModel")
fc_FeatureConfiguration = Class(name="fc::FeatureConfiguration")
fc_Selection = Class(name="fc::Selection")
fc_AttributeValue = Class(name="fc::AttributeValue", is_abstract=True)
fc_Feature = Class(name="fc::Feature")
fc_DoubleValue = Class(name="fc::DoubleValue")
fc_StringValue = Class(name="fc::StringValue")
fc_Attribute = Class(name="fc::Attribute")
fc_BooleanValue = Class(name="fc::BooleanValue")
AttributeValue = Class(name="AttributeValue")
fc_IntegerValue = Class(name="fc::IntegerValue")

# fc_FeatureModel class attributes and methods

# fc_FeatureConfiguration class attributes and methods
fc_FeatureConfiguration_comment: Property = Property(name="comment", type=StringType)
fc_FeatureConfiguration_name: Property = Property(name="name", type=StringType)
fc_FeatureConfiguration_version: Property = Property(name="version", type=StringType)
fc_FeatureConfiguration_description: Property = Property(name="description", type=StringType)
fc_FeatureConfiguration_m_getSelectionsById: Method = Method(name="getSelectionsById", parameters={Parameter(name='id')})
fc_FeatureConfiguration.attributes={fc_FeatureConfiguration_comment, fc_FeatureConfiguration_version, fc_FeatureConfiguration_description, fc_FeatureConfiguration_name}
fc_FeatureConfiguration.methods={fc_FeatureConfiguration_m_getSelectionsById}

# fc_Selection class attributes and methods
fc_Selection_description: Property = Property(name="description", type=StringType)
fc_Selection_comment: Property = Property(name="comment", type=StringType)
fc_Selection_id: Property = Property(name="id", type=StringType)
fc_Selection_name: Property = Property(name="name", type=StringType)
fc_Selection_root: Property = Property(name="root", type=BooleanType)
fc_Selection_present: Property = Property(name="present", type=BooleanType)
fc_Selection_enabled: Property = Property(name="enabled", type=BooleanType)
fc_Selection.attributes={fc_Selection_description, fc_Selection_comment, fc_Selection_id, fc_Selection_name, fc_Selection_present, fc_Selection_enabled, fc_Selection_root}

# fc_AttributeValue class attributes and methods
fc_AttributeValue_comment: Property = Property(name="comment", type=StringType)
fc_AttributeValue_id: Property = Property(name="id", type=StringType)
fc_AttributeValue_name: Property = Property(name="name", type=StringType)
fc_AttributeValue_description: Property = Property(name="description", type=StringType)
fc_AttributeValue.attributes={fc_AttributeValue_name, fc_AttributeValue_comment, fc_AttributeValue_description, fc_AttributeValue_id}

# fc_Feature class attributes and methods

# fc_DoubleValue class attributes and methods
fc_DoubleValue_value: Property = Property(name="value", type=FloatType)
fc_DoubleValue.attributes={fc_DoubleValue_value}

# fc_StringValue class attributes and methods
fc_StringValue_value: Property = Property(name="value", type=StringType)
fc_StringValue.attributes={fc_StringValue_value}

# fc_Attribute class attributes and methods

# fc_BooleanValue class attributes and methods
fc_BooleanValue_value: Property = Property(name="value", type=BooleanType)
fc_BooleanValue.attributes={fc_BooleanValue_value}

# AttributeValue class attributes and methods

# fc_IntegerValue class attributes and methods
fc_IntegerValue_value: Property = Property(name="value", type=IntegerType)
fc_IntegerValue.attributes={fc_IntegerValue_value}

# Relationships
featureModel0: BinaryAssociation = BinaryAssociation(
    name="featureModel0",
    ends={
        Property(name="fc_FeatureModel", type=fc_FeatureConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="fc_FeatureConfiguration", type=fc_FeatureModel, multiplicity=Multiplicity(0, 1))
    }
)
featureModelCopy1: BinaryAssociation = BinaryAssociation(
    name="featureModelCopy1",
    ends={
        Property(name="fc_FeatureModel3", type=fc_FeatureConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="fc_FeatureConfiguration2", type=fc_FeatureModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
root4: BinaryAssociation = BinaryAssociation(
    name="root4",
    ends={
        Property(name="fc_Selection", type=fc_FeatureConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="fc_FeatureConfiguration5", type=fc_Selection, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selections10: BinaryAssociation = BinaryAssociation(
    name="selections10",
    ends={
        Property(name="Selection11", type=fc_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=fc_Selection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent7: BinaryAssociation = BinaryAssociation(
    name="parent7",
    ends={
        Property(name="Selection", type=fc_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="selections", type=fc_Selection, multiplicity=Multiplicity(0, 1))
    }
)
values8: BinaryAssociation = BinaryAssociation(
    name="values8",
    ends={
        Property(name="AttributeValue", type=fc_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="selection", type=fc_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureConfiguration12: BinaryAssociation = BinaryAssociation(
    name="featureConfiguration12",
    ends={
        Property(name="fc_FeatureConfiguration14", type=fc_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="fc_Selection13", type=fc_FeatureConfiguration, multiplicity=Multiplicity(1, 1))
    }
)
feature15: BinaryAssociation = BinaryAssociation(
    name="feature15",
    ends={
        Property(name="fc_Feature", type=fc_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="fc_Selection16", type=fc_Feature, multiplicity=Multiplicity(1, 1))
    }
)
selection17: BinaryAssociation = BinaryAssociation(
    name="selection17",
    ends={
        Property(name="Selection18", type=fc_AttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="values", type=fc_Selection, multiplicity=Multiplicity(1, 1))
    }
)
attribute19: BinaryAssociation = BinaryAssociation(
    name="attribute19",
    ends={
        Property(name="fc_Attribute", type=fc_AttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fc_AttributeValue", type=fc_Attribute, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fc_DoubleValue_AttributeValue = Generalization(general=AttributeValue, specific=fc_DoubleValue)
gen_fc_StringValue_AttributeValue = Generalization(general=AttributeValue, specific=fc_StringValue)
gen_fc_BooleanValue_AttributeValue = Generalization(general=AttributeValue, specific=fc_BooleanValue)
gen_fc_IntegerValue_AttributeValue = Generalization(general=AttributeValue, specific=fc_IntegerValue)

# Domain Model
domain_model = DomainModel(
    name="fc",
    types={fc_FeatureModel, fc_FeatureConfiguration, fc_Selection, fc_AttributeValue, fc_Feature, fc_DoubleValue, fc_StringValue, fc_Attribute, fc_BooleanValue, AttributeValue, fc_IntegerValue},
    associations={featureModel0, featureModelCopy1, root4, selections10, parent7, values8, featureConfiguration12, feature15, selection17, attribute19},
    generalizations={gen_fc_DoubleValue_AttributeValue, gen_fc_StringValue_AttributeValue, gen_fc_BooleanValue_AttributeValue, gen_fc_IntegerValue_AttributeValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)