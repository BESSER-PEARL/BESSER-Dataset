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
DecisionType: Enumeration = Enumeration(
    name="DecisionType",
    literals={
            EnumerationLiteral(name="manual"),
			EnumerationLiteral(name="propagated"),
			EnumerationLiteral(name="autocompleted")
    }
)

# Classes
sxfm_Feature = Class(name="sxfm_Feature", is_abstract=True)
sxfm_Group = Class(name="sxfm_Group")
sxfm_FeatureModel = Class(name="sxfm_FeatureModel")
sxfm_ConstraintsSet = Class(name="sxfm_ConstraintsSet")
sxfm_FeatureTree = Class(name="sxfm_FeatureTree")
sxfm_MetadataSet = Class(name="sxfm_MetadataSet")
sxfm_FeatureModelConfiguaration = Class(name="sxfm_FeatureModelConfiguaration")
sxfm_Root = Class(name="sxfm_Root")
sxfm_CardinalizedElement = Class(name="sxfm_CardinalizedElement", is_abstract=True)
CardinalizedElement = Class(name="CardinalizedElement")
sxfm_GroupedFeature = Class(name="sxfm_GroupedFeature")
sxfm_Constraint = Class(name="sxfm_Constraint")
sxfm_Or = Class(name="sxfm_Or")
sxfm_Mandatory = Class(name="sxfm_Mandatory")
ContainerElement = Class(name="ContainerElement")
ContainableElement = Class(name="ContainableElement")
Feature = Class(name="Feature")
ConstraintableElement = Class(name="ConstraintableElement")
CommonFeature = Class(name="CommonFeature")
sxfm_Optional = Class(name="sxfm_Optional")
VariableFeature = Class(name="VariableFeature")
sxfm_FeatureChoice = Class(name="sxfm_FeatureChoice")
sxfm_VariableFeature = Class(name="sxfm_VariableFeature", is_abstract=True)
sxfm_CommonFeature = Class(name="sxfm_CommonFeature", is_abstract=True)
sxfm_ContainerElement = Class(name="sxfm_ContainerElement", is_abstract=True)
sxfm_ContainableElement = Class(name="sxfm_ContainableElement", is_abstract=True)
sxfm_ConstraintableElement = Class(name="sxfm_ConstraintableElement", is_abstract=True)
sxfm_Not = Class(name="sxfm_Not")
Literal = Class(name="Literal")
sxfm_Atom = Class(name="sxfm_Atom")
sxfm_Literal = Class(name="sxfm_Literal", is_abstract=True)
sxfm_Data = Class(name="sxfm_Data")

# sxfm_Feature class attributes and methods
sxfm_Feature_name: Property = Property(name="name", type=StringType)
sxfm_Feature_id: Property = Property(name="id", type=StringType)
sxfm_Feature_treeLevel: Property = Property(name="treeLevel", type=IntegerType)
sxfm_Feature_description: Property = Property(name="description", type=StringType)
sxfm_Feature.attributes={sxfm_Feature_description, sxfm_Feature_id, sxfm_Feature_treeLevel, sxfm_Feature_name}

# sxfm_Group class attributes and methods
sxfm_Group_id: Property = Property(name="id", type=StringType)
sxfm_Group.attributes={sxfm_Group_id}

# sxfm_FeatureModel class attributes and methods
sxfm_FeatureModel_name: Property = Property(name="name", type=StringType)
sxfm_FeatureModel.attributes={sxfm_FeatureModel_name}

# sxfm_ConstraintsSet class attributes and methods

# sxfm_FeatureTree class attributes and methods

# sxfm_MetadataSet class attributes and methods

# sxfm_FeatureModelConfiguaration class attributes and methods

# sxfm_Root class attributes and methods

# sxfm_CardinalizedElement class attributes and methods
sxfm_CardinalizedElement_minCardinality: Property = Property(name="minCardinality", type=IntegerType)
sxfm_CardinalizedElement_maxCardinality: Property = Property(name="maxCardinality", type=IntegerType)
sxfm_CardinalizedElement.attributes={sxfm_CardinalizedElement_maxCardinality, sxfm_CardinalizedElement_minCardinality}

# CardinalizedElement class attributes and methods

# sxfm_GroupedFeature class attributes and methods

# sxfm_Constraint class attributes and methods
sxfm_Constraint_id: Property = Property(name="id", type=IntegerType)
sxfm_Constraint.attributes={sxfm_Constraint_id}

# sxfm_Or class attributes and methods

# sxfm_Mandatory class attributes and methods

# ContainerElement class attributes and methods

# ContainableElement class attributes and methods

# Feature class attributes and methods

# ConstraintableElement class attributes and methods

# CommonFeature class attributes and methods

# sxfm_Optional class attributes and methods

# VariableFeature class attributes and methods

# sxfm_FeatureChoice class attributes and methods
sxfm_FeatureChoice_selected: Property = Property(name="selected", type=BooleanType)
sxfm_FeatureChoice_decisionType: Property = Property(name="decisionType", type=StringType)
sxfm_FeatureChoice_decisionStep: Property = Property(name="decisionStep", type=IntegerType)
sxfm_FeatureChoice.attributes={sxfm_FeatureChoice_selected, sxfm_FeatureChoice_decisionType, sxfm_FeatureChoice_decisionStep}

# sxfm_VariableFeature class attributes and methods

# sxfm_CommonFeature class attributes and methods

# sxfm_ContainerElement class attributes and methods

# sxfm_ContainableElement class attributes and methods

# sxfm_ConstraintableElement class attributes and methods

# sxfm_Not class attributes and methods

# Literal class attributes and methods

# sxfm_Atom class attributes and methods

# sxfm_Literal class attributes and methods

# sxfm_Data class attributes and methods
sxfm_Data_value: Property = Property(name="value", type=StringType)
sxfm_Data_name: Property = Property(name="name", type=StringType)
sxfm_Data.attributes={sxfm_Data_name, sxfm_Data_value}

# Relationships
groups0: BinaryAssociation = BinaryAssociation(
    name="groups0",
    ends={
        Property(name="sxfm_Group", type=sxfm_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_Feature", type=sxfm_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraintsSet4: BinaryAssociation = BinaryAssociation(
    name="constraintsSet4",
    ends={
        Property(name="sxfm_ConstraintsSet", type=sxfm_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_FeatureModel", type=sxfm_ConstraintsSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featureTree5: BinaryAssociation = BinaryAssociation(
    name="featureTree5",
    ends={
        Property(name="sxfm_FeatureTree", type=sxfm_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_FeatureModel6", type=sxfm_FeatureTree, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featureModelInfo7: BinaryAssociation = BinaryAssociation(
    name="featureModelInfo7",
    ends={
        Property(name="sxfm_MetadataSet", type=sxfm_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_FeatureModel8", type=sxfm_MetadataSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
configuration9: BinaryAssociation = BinaryAssociation(
    name="configuration9",
    ends={
        Property(name="sxfm_FeatureModelConfiguaration", type=sxfm_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_FeatureModel10", type=sxfm_FeatureModelConfiguaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root11: BinaryAssociation = BinaryAssociation(
    name="root11",
    ends={
        Property(name="sxfm_Root", type=sxfm_FeatureTree, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_FeatureTree12", type=sxfm_Root, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraints13: BinaryAssociation = BinaryAssociation(
    name="constraints13",
    ends={
        Property(name="sxfm_Constraint15", type=sxfm_ConstraintsSet, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_ConstraintsSet14", type=sxfm_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupedFeatures1: BinaryAssociation = BinaryAssociation(
    name="groupedFeatures1",
    ends={
        Property(name="sxfm_GroupedFeature", type=sxfm_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_Group2", type=sxfm_GroupedFeature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
or_3: BinaryAssociation = BinaryAssociation(
    name="or_3",
    ends={
        Property(name="sxfm_Or", type=sxfm_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_Constraint", type=sxfm_Or, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
data22: BinaryAssociation = BinaryAssociation(
    name="data22",
    ends={
        Property(name="sxfm_Data", type=sxfm_MetadataSet, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_MetadataSet23", type=sxfm_Data, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureChoice24: BinaryAssociation = BinaryAssociation(
    name="featureChoice24",
    ends={
        Property(name="sxfm_FeatureChoice", type=sxfm_FeatureModelConfiguaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_FeatureModelConfiguaration25", type=sxfm_FeatureChoice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature26: BinaryAssociation = BinaryAssociation(
    name="feature26",
    ends={
        Property(name="sxfm_Feature28", type=sxfm_FeatureChoice, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_FeatureChoice27", type=sxfm_Feature, multiplicity=Multiplicity(1, 1))
    }
)
childrenFeatures16: BinaryAssociation = BinaryAssociation(
    name="childrenFeatures16",
    ends={
        Property(name="sxfm_ContainableElement", type=sxfm_ContainerElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_ContainerElement", type=sxfm_ContainableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature17: BinaryAssociation = BinaryAssociation(
    name="feature17",
    ends={
        Property(name="sxfm_Atom", type=sxfm_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_Not", type=sxfm_Atom, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
clause18: BinaryAssociation = BinaryAssociation(
    name="clause18",
    ends={
        Property(name="sxfm_Literal", type=sxfm_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_Or19", type=sxfm_Literal, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
feature20: BinaryAssociation = BinaryAssociation(
    name="feature20",
    ends={
        Property(name="sxfm_ConstraintableElement", type=sxfm_Atom, multiplicity=Multiplicity(1, 1)),
        Property(name="sxfm_Atom21", type=sxfm_ConstraintableElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_sxfm_GroupedFeature_Feature = Generalization(general=Feature, specific=sxfm_GroupedFeature)
gen_sxfm_GroupedFeature_ConstraintableElement = Generalization(general=ConstraintableElement, specific=sxfm_GroupedFeature)
gen_sxfm_GroupedFeature_ContainerElement = Generalization(general=ContainerElement, specific=sxfm_GroupedFeature)
gen_sxfm_GroupedFeature_VariableFeature = Generalization(general=VariableFeature, specific=sxfm_GroupedFeature)
gen_sxfm_Root_ContainerElement = Generalization(general=ContainerElement, specific=sxfm_Root)
gen_sxfm_Root_Feature = Generalization(general=Feature, specific=sxfm_Root)
gen_sxfm_Group_CardinalizedElement = Generalization(general=CardinalizedElement, specific=sxfm_Group)
gen_sxfm_Mandatory_ContainerElement = Generalization(general=ContainerElement, specific=sxfm_Mandatory)
gen_sxfm_Mandatory_ContainableElement = Generalization(general=ContainableElement, specific=sxfm_Mandatory)
gen_sxfm_Mandatory_Feature = Generalization(general=Feature, specific=sxfm_Mandatory)
gen_sxfm_Mandatory_ConstraintableElement = Generalization(general=ConstraintableElement, specific=sxfm_Mandatory)
gen_sxfm_Mandatory_CommonFeature = Generalization(general=CommonFeature, specific=sxfm_Mandatory)
gen_sxfm_Optional_Feature = Generalization(general=Feature, specific=sxfm_Optional)
gen_sxfm_Optional_ContainerElement = Generalization(general=ContainerElement, specific=sxfm_Optional)
gen_sxfm_Optional_ContainableElement = Generalization(general=ContainableElement, specific=sxfm_Optional)
gen_sxfm_Optional_ConstraintableElement = Generalization(general=ConstraintableElement, specific=sxfm_Optional)
gen_sxfm_Optional_VariableFeature = Generalization(general=VariableFeature, specific=sxfm_Optional)
gen_sxfm_Root_CommonFeature = Generalization(general=CommonFeature, specific=sxfm_Root)
gen_sxfm_Not_Literal = Generalization(general=Literal, specific=sxfm_Not)
gen_sxfm_Atom_Literal = Generalization(general=Literal, specific=sxfm_Atom)

# Domain Model
domain_model = DomainModel(
    name="sxfm",
    types={sxfm_Feature, sxfm_Group, sxfm_FeatureModel, sxfm_ConstraintsSet, sxfm_FeatureTree, sxfm_MetadataSet, sxfm_FeatureModelConfiguaration, sxfm_Root, sxfm_CardinalizedElement, CardinalizedElement, sxfm_GroupedFeature, sxfm_Constraint, sxfm_Or, sxfm_Mandatory, ContainerElement, ContainableElement, Feature, ConstraintableElement, CommonFeature, sxfm_Optional, VariableFeature, sxfm_FeatureChoice, sxfm_VariableFeature, sxfm_CommonFeature, sxfm_ContainerElement, sxfm_ContainableElement, sxfm_ConstraintableElement, sxfm_Not, Literal, sxfm_Atom, sxfm_Literal, sxfm_Data, DecisionType},
    associations={groups0, constraintsSet4, featureTree5, featureModelInfo7, configuration9, root11, constraints13, groupedFeatures1, or_3, data22, featureChoice24, feature26, childrenFeatures16, feature17, clause18, feature20},
    generalizations={gen_sxfm_GroupedFeature_Feature, gen_sxfm_GroupedFeature_ConstraintableElement, gen_sxfm_GroupedFeature_ContainerElement, gen_sxfm_GroupedFeature_VariableFeature, gen_sxfm_Root_ContainerElement, gen_sxfm_Root_Feature, gen_sxfm_Group_CardinalizedElement, gen_sxfm_Mandatory_ContainerElement, gen_sxfm_Mandatory_ContainableElement, gen_sxfm_Mandatory_Feature, gen_sxfm_Mandatory_ConstraintableElement, gen_sxfm_Mandatory_CommonFeature, gen_sxfm_Optional_Feature, gen_sxfm_Optional_ContainerElement, gen_sxfm_Optional_ContainableElement, gen_sxfm_Optional_ConstraintableElement, gen_sxfm_Optional_VariableFeature, gen_sxfm_Root_CommonFeature, gen_sxfm_Not_Literal, gen_sxfm_Atom_Literal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)