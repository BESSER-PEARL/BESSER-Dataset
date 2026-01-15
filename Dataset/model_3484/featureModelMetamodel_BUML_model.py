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
            EnumerationLiteral(name="or"),
			EnumerationLiteral(name="optional"),
			EnumerationLiteral(name="mandatory"),
			EnumerationLiteral(name="alternative")
    }
)

SelectionState: Enumeration = Enumeration(
    name="SelectionState",
    literals={
            EnumerationLiteral(name="selected"),
			EnumerationLiteral(name="unselected")
    }
)

# Classes
featureModelMetamodel_Feature = Class(name="featureModelMetamodel::Feature")
featureModelMetamodel_GroupMultiplicity = Class(name="featureModelMetamodel::GroupMultiplicity")
featureModelMetamodel_VariableFeature = Class(name="featureModelMetamodel::VariableFeature")
Feature = Class(name="Feature")
featureModelMetamodel_ClonableFeature = Class(name="featureModelMetamodel::ClonableFeature")
featureModelMetamodel_Multiplicity = Class(name="featureModelMetamodel::Multiplicity")
featureModelMetamodel_Attribute = Class(name="featureModelMetamodel::Attribute")
featureModelMetamodel_AbstractFeature = Class(name="featureModelMetamodel::AbstractFeature")
featureModelMetamodel_Constraint = Class(name="featureModelMetamodel::Constraint")
featureModelMetamodel_FeatureModel = Class(name="featureModelMetamodel::FeatureModel")
Multiplicity = Class(name="Multiplicity")
featureModelMetamodel_Selection = Class(name="featureModelMetamodel::Selection")
featureModelMetamodel_ClonableSelection = Class(name="featureModelMetamodel::ClonableSelection")
Selection = Class(name="Selection")
featureModelMetamodel_ConfigurationModel = Class(name="featureModelMetamodel::ConfigurationModel")

# featureModelMetamodel_Feature class attributes and methods
featureModelMetamodel_Feature_variabilityType: Property = Property(name="variabilityType", type=StringType)
featureModelMetamodel_Feature_name: Property = Property(name="name", type=StringType)
featureModelMetamodel_Feature_id: Property = Property(name="id", type=StringType)
featureModelMetamodel_Feature.attributes={featureModelMetamodel_Feature_variabilityType, featureModelMetamodel_Feature_name, featureModelMetamodel_Feature_id}

# featureModelMetamodel_GroupMultiplicity class attributes and methods

# featureModelMetamodel_VariableFeature class attributes and methods

# Feature class attributes and methods

# featureModelMetamodel_ClonableFeature class attributes and methods

# featureModelMetamodel_Multiplicity class attributes and methods
featureModelMetamodel_Multiplicity_lower: Property = Property(name="lower", type=StringType)
featureModelMetamodel_Multiplicity_upper: Property = Property(name="upper", type=StringType)
featureModelMetamodel_Multiplicity.attributes={featureModelMetamodel_Multiplicity_upper, featureModelMetamodel_Multiplicity_lower}

# featureModelMetamodel_Attribute class attributes and methods

# featureModelMetamodel_AbstractFeature class attributes and methods

# featureModelMetamodel_Constraint class attributes and methods
featureModelMetamodel_Constraint_id: Property = Property(name="id", type=StringType)
featureModelMetamodel_Constraint_language: Property = Property(name="language", type=StringType)
featureModelMetamodel_Constraint_code: Property = Property(name="code", type=StringType)
featureModelMetamodel_Constraint.attributes={featureModelMetamodel_Constraint_code, featureModelMetamodel_Constraint_language, featureModelMetamodel_Constraint_id}

# featureModelMetamodel_FeatureModel class attributes and methods

# Multiplicity class attributes and methods

# featureModelMetamodel_Selection class attributes and methods
featureModelMetamodel_Selection_state: Property = Property(name="state", type=StringType)
featureModelMetamodel_Selection_name: Property = Property(name="name", type=StringType)
featureModelMetamodel_Selection.attributes={featureModelMetamodel_Selection_name, featureModelMetamodel_Selection_state}

# featureModelMetamodel_ClonableSelection class attributes and methods
featureModelMetamodel_ClonableSelection_instance: Property = Property(name="instance", type=StringType)
featureModelMetamodel_ClonableSelection.attributes={featureModelMetamodel_ClonableSelection_instance}

# Selection class attributes and methods

# featureModelMetamodel_ConfigurationModel class attributes and methods

# Relationships
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="featureModelMetamodel_Feature", type=featureModelMetamodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModelMetamodel_Feature0", type=featureModelMetamodel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupMultiplicity2: BinaryAssociation = BinaryAssociation(
    name="groupMultiplicity2",
    ends={
        Property(name="featureModelMetamodel_GroupMultiplicity", type=featureModelMetamodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModelMetamodel_Feature3", type=featureModelMetamodel_GroupMultiplicity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent7: BinaryAssociation = BinaryAssociation(
    name="parent7",
    ends={
        Property(name="featureModelMetamodel_Feature8", type=featureModelMetamodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModelMetamodel_Feature6", type=featureModelMetamodel_Feature, multiplicity=Multiplicity(0, 1))
    }
)
instanceMultiplicity9: BinaryAssociation = BinaryAssociation(
    name="instanceMultiplicity9",
    ends={
        Property(name="featureModelMetamodel_Multiplicity", type=featureModelMetamodel_ClonableFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModelMetamodel_ClonableFeature", type=featureModelMetamodel_Multiplicity, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes4: BinaryAssociation = BinaryAssociation(
    name="attributes4",
    ends={
        Property(name="featureModelMetamodel_Attribute", type=featureModelMetamodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModelMetamodel_Feature5", type=featureModelMetamodel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root10: BinaryAssociation = BinaryAssociation(
    name="root10",
    ends={
        Property(name="featureModelMetamodel_Feature11", type=featureModelMetamodel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModelMetamodel_FeatureModel", type=featureModelMetamodel_Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
features17: BinaryAssociation = BinaryAssociation(
    name="features17",
    ends={
        Property(name="featureModelMetamodel_Feature19", type=featureModelMetamodel_GroupMultiplicity, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModelMetamodel_GroupMultiplicity18", type=featureModelMetamodel_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
feature20: BinaryAssociation = BinaryAssociation(
    name="feature20",
    ends={
        Property(name="featureModelMetamodel_Feature21", type=featureModelMetamodel_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModelMetamodel_Selection", type=featureModelMetamodel_Feature, multiplicity=Multiplicity(1, 1))
    }
)
constraints12: BinaryAssociation = BinaryAssociation(
    name="constraints12",
    ends={
        Property(name="featureModelMetamodel_Constraint", type=featureModelMetamodel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModelMetamodel_FeatureModel13", type=featureModelMetamodel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features14: BinaryAssociation = BinaryAssociation(
    name="features14",
    ends={
        Property(name="featureModelMetamodel_Feature16", type=featureModelMetamodel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModelMetamodel_FeatureModel15", type=featureModelMetamodel_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
selections22: BinaryAssociation = BinaryAssociation(
    name="selections22",
    ends={
        Property(name="featureModelMetamodel_ConfigurationModel", type=featureModelMetamodel_Selection, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="featureModelMetamodel_Selection23", type=featureModelMetamodel_ConfigurationModel, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_featureModelMetamodel_VariableFeature_Feature = Generalization(general=Feature, specific=featureModelMetamodel_VariableFeature)
gen_featureModelMetamodel_ClonableFeature_Feature = Generalization(general=Feature, specific=featureModelMetamodel_ClonableFeature)
gen_featureModelMetamodel_AbstractFeature_Feature = Generalization(general=Feature, specific=featureModelMetamodel_AbstractFeature)
gen_featureModelMetamodel_GroupMultiplicity_Multiplicity = Generalization(general=Multiplicity, specific=featureModelMetamodel_GroupMultiplicity)
gen_featureModelMetamodel_ClonableSelection_Selection = Generalization(general=Selection, specific=featureModelMetamodel_ClonableSelection)

# Domain Model
domain_model = DomainModel(
    name="featureModelMetamodel",
    types={featureModelMetamodel_Feature, featureModelMetamodel_GroupMultiplicity, featureModelMetamodel_VariableFeature, Feature, featureModelMetamodel_ClonableFeature, featureModelMetamodel_Multiplicity, featureModelMetamodel_Attribute, featureModelMetamodel_AbstractFeature, featureModelMetamodel_Constraint, featureModelMetamodel_FeatureModel, Multiplicity, featureModelMetamodel_Selection, featureModelMetamodel_ClonableSelection, Selection, featureModelMetamodel_ConfigurationModel, VariabilityType, SelectionState},
    associations={children1, groupMultiplicity2, parent7, instanceMultiplicity9, attributes4, root10, features17, feature20, constraints12, features14, selections22},
    generalizations={gen_featureModelMetamodel_VariableFeature_Feature, gen_featureModelMetamodel_ClonableFeature_Feature, gen_featureModelMetamodel_AbstractFeature_Feature, gen_featureModelMetamodel_GroupMultiplicity_Multiplicity, gen_featureModelMetamodel_ClonableSelection_Selection},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)