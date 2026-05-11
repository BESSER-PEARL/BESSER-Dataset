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
ComparisonOperator: Enumeration = Enumeration(
    name="ComparisonOperator",
    literals={
            EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="geq"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="leq"),
			EnumerationLiteral(name="lt")
    }
)

SelectionOperator: Enumeration = Enumeration(
    name="SelectionOperator",
    literals={
            EnumerationLiteral(name="deselect"),
			EnumerationLiteral(name="select")
    }
)

# Classes
featureModel_FeatureModel = Class(name="featureModel_FeatureModel")
featureModel_FMConstraint = Class(name="featureModel_FMConstraint", is_abstract=True)
featureModel_Feature = Class(name="featureModel_Feature")
VariabilityElement = Class(name="VariabilityElement")
featureModel_Attribute = Class(name="featureModel_Attribute")
featureModel_Exclusive = Class(name="featureModel_Exclusive")
Alternative = Class(name="Alternative")
featureModel_Value = Class(name="featureModel_Value")
featureModel_BooleanConstraint = Class(name="featureModel_BooleanConstraint", is_abstract=True)
FMConstraint = Class(name="FMConstraint")
featureModel_Implies = Class(name="featureModel_Implies")
BooleanConstraint = Class(name="BooleanConstraint")
featureModel_Excludes = Class(name="featureModel_Excludes")
featureModel_AdaptationRule = Class(name="featureModel_AdaptationRule")
featureModel_Condition = Class(name="featureModel_Condition")
featureModel_Action = Class(name="featureModel_Action")
featureModel_Alternative = Class(name="featureModel_Alternative")
Feature = Class(name="Feature")
featureModel_IntValue = Class(name="featureModel_IntValue")
featureModel_VariabilityElement = Class(name="featureModel_VariabilityElement", is_abstract=True)

# featureModel_FeatureModel class attributes and methods

# featureModel_FMConstraint class attributes and methods

# featureModel_Feature class attributes and methods
featureModel_Feature_name: Property = Property(name="name", type=StringType)
featureModel_Feature_selected: Property = Property(name="selected", type=BooleanType)
featureModel_Feature_unselected: Property = Property(name="unselected", type=BooleanType)
featureModel_Feature_mandatory: Property = Property(name="mandatory", type=BooleanType)
featureModel_Feature.attributes={featureModel_Feature_unselected, featureModel_Feature_name, featureModel_Feature_selected, featureModel_Feature_mandatory}

# VariabilityElement class attributes and methods

# featureModel_Attribute class attributes and methods
featureModel_Attribute_name: Property = Property(name="name", type=StringType)
featureModel_Attribute_runtime: Property = Property(name="runtime", type=BooleanType)
featureModel_Attribute.attributes={featureModel_Attribute_name, featureModel_Attribute_runtime}

# featureModel_Exclusive class attributes and methods

# Alternative class attributes and methods

# featureModel_Value class attributes and methods

# featureModel_BooleanConstraint class attributes and methods

# FMConstraint class attributes and methods

# featureModel_Implies class attributes and methods

# BooleanConstraint class attributes and methods

# featureModel_Excludes class attributes and methods

# featureModel_AdaptationRule class attributes and methods

# featureModel_Condition class attributes and methods
featureModel_Condition_type: Property = Property(name="type", type=StringType)
featureModel_Condition.attributes={featureModel_Condition_type}

# featureModel_Action class attributes and methods
featureModel_Action_type: Property = Property(name="type", type=StringType)
featureModel_Action.attributes={featureModel_Action_type}

# featureModel_Alternative class attributes and methods

# Feature class attributes and methods

# featureModel_IntValue class attributes and methods

# featureModel_VariabilityElement class attributes and methods

# Relationships
constraints0: BinaryAssociation = BinaryAssociation(
    name="constraints0",
    ends={
        Property(name="featureModel_FMConstraint", type=featureModel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_FeatureModel", type=featureModel_FMConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootFeature1: BinaryAssociation = BinaryAssociation(
    name="rootFeature1",
    ends={
        Property(name="featureModel_Feature", type=featureModel_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_FeatureModel2", type=featureModel_Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="featureModel_Attribute", type=featureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Feature4", type=featureModel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subFeatures6: BinaryAssociation = BinaryAssociation(
    name="subFeatures6",
    ends={
        Property(name="featureModel_Feature7", type=featureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Feature5", type=featureModel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variants8: BinaryAssociation = BinaryAssociation(
    name="variants8",
    ends={
        Property(name="featureModel_Feature9", type=featureModel_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Alternative", type=featureModel_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value10: BinaryAssociation = BinaryAssociation(
    name="value10",
    ends={
        Property(name="featureModel_Value", type=featureModel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Attribute11", type=featureModel_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from_12: BinaryAssociation = BinaryAssociation(
    name="from_12",
    ends={
        Property(name="featureModel_Feature13", type=featureModel_BooleanConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_BooleanConstraint", type=featureModel_Feature, multiplicity=Multiplicity(1, 1))
    }
)
to14: BinaryAssociation = BinaryAssociation(
    name="to14",
    ends={
        Property(name="featureModel_Feature16", type=featureModel_BooleanConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_BooleanConstraint15", type=featureModel_Feature, multiplicity=Multiplicity(1, 1))
    }
)
condition17: BinaryAssociation = BinaryAssociation(
    name="condition17",
    ends={
        Property(name="featureModel_Condition", type=featureModel_AdaptationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_AdaptationRule", type=featureModel_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action18: BinaryAssociation = BinaryAssociation(
    name="action18",
    ends={
        Property(name="featureModel_Action", type=featureModel_AdaptationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_AdaptationRule19", type=featureModel_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value23: BinaryAssociation = BinaryAssociation(
    name="value23",
    ends={
        Property(name="featureModel_IntValue", type=featureModel_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Condition24", type=featureModel_IntValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature25: BinaryAssociation = BinaryAssociation(
    name="feature25",
    ends={
        Property(name="featureModel_Feature27", type=featureModel_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Condition26", type=featureModel_Feature, multiplicity=Multiplicity(1, 1))
    }
)
feature28: BinaryAssociation = BinaryAssociation(
    name="feature28",
    ends={
        Property(name="featureModel_Feature30", type=featureModel_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Action29", type=featureModel_Feature, multiplicity=Multiplicity(1, 1))
    }
)
attribute20: BinaryAssociation = BinaryAssociation(
    name="attribute20",
    ends={
        Property(name="featureModel_Attribute22", type=featureModel_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Condition21", type=featureModel_Attribute, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_featureModel_Feature_VariabilityElement = Generalization(general=VariabilityElement, specific=featureModel_Feature)
gen_featureModel_Exclusive_Alternative = Generalization(general=Alternative, specific=featureModel_Exclusive)
gen_featureModel_Attribute_VariabilityElement = Generalization(general=VariabilityElement, specific=featureModel_Attribute)
gen_featureModel_BooleanConstraint_FMConstraint = Generalization(general=FMConstraint, specific=featureModel_BooleanConstraint)
gen_featureModel_Implies_BooleanConstraint = Generalization(general=BooleanConstraint, specific=featureModel_Implies)
gen_featureModel_Excludes_BooleanConstraint = Generalization(general=BooleanConstraint, specific=featureModel_Excludes)
gen_featureModel_AdaptationRule_FMConstraint = Generalization(general=FMConstraint, specific=featureModel_AdaptationRule)
gen_featureModel_Alternative_Feature = Generalization(general=Feature, specific=featureModel_Alternative)

# Domain Model
domain_model = DomainModel(
    name="featureModel",
    types={featureModel_FeatureModel, featureModel_FMConstraint, featureModel_Feature, VariabilityElement, featureModel_Attribute, featureModel_Exclusive, Alternative, featureModel_Value, featureModel_BooleanConstraint, FMConstraint, featureModel_Implies, BooleanConstraint, featureModel_Excludes, featureModel_AdaptationRule, featureModel_Condition, featureModel_Action, featureModel_Alternative, Feature, featureModel_IntValue, featureModel_VariabilityElement, ComparisonOperator, SelectionOperator},
    associations={constraints0, rootFeature1, attributes3, subFeatures6, variants8, value10, from_12, to14, condition17, action18, value23, feature25, feature28, attribute20},
    generalizations={gen_featureModel_Feature_VariabilityElement, gen_featureModel_Exclusive_Alternative, gen_featureModel_Attribute_VariabilityElement, gen_featureModel_BooleanConstraint_FMConstraint, gen_featureModel_Implies_BooleanConstraint, gen_featureModel_Excludes_BooleanConstraint, gen_featureModel_AdaptationRule_FMConstraint, gen_featureModel_Alternative_Feature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)