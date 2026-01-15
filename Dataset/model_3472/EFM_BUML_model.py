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

Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="select"),
			EnumerationLiteral(name="add"),
			EnumerationLiteral(name="remove"),
			EnumerationLiteral(name="multiply"),
			EnumerationLiteral(name="divide")
    }
)

LogicalOperator: Enumeration = Enumeration(
    name="LogicalOperator",
    literals={
            EnumerationLiteral(name="void"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or")
    }
)

# Classes
EFM_FeatCardinality = Class(name="EFM::FeatCardinality")
EFM_NodeFeature = Class(name="EFM::NodeFeature")
EFM_Exclusive = Class(name="EFM::Exclusive")
Alternative = Class(name="Alternative")
EFM_Alternative = Class(name="EFM::Alternative")
Feature = Class(name="Feature")
EFM_Cardinality = Class(name="EFM::Cardinality", is_abstract=True)
EFM_Value = Class(name="EFM::Value")
EFM_BooleanConstraint = Class(name="EFM::BooleanConstraint", is_abstract=True)
FMConstraint = Class(name="FMConstraint")
Cardinality = Class(name="Cardinality")
EFM_Implies = Class(name="EFM::Implies")
BooleanConstraint = Class(name="BooleanConstraint")
EFM_Excludes = Class(name="EFM::Excludes")
EFM_Requires = Class(name="EFM::Requires")
EFM_Operation = Class(name="EFM::Operation")
EFM_FeatureModel = Class(name="EFM::FeatureModel")
EFM_FMConstraint = Class(name="EFM::FMConstraint", is_abstract=True)
EFM_Feature = Class(name="EFM::Feature")
EFM_FMElement = Class(name="EFM::FMElement")
FMElement = Class(name="FMElement")
EFM_Attribute = Class(name="EFM::Attribute")
EFM_RangeOperation = Class(name="EFM::RangeOperation")
Operation = Class(name="Operation")
EFM_ValueOperation = Class(name="EFM::ValueOperation")
EFM_IntValue = Class(name="EFM::IntValue")
EFM_Functional = Class(name="EFM::Functional")
EFM_Comparison = Class(name="EFM::Comparison")
EFM_HostedBy = Class(name="EFM::HostedBy")
EFM_NotHostedBy = Class(name="EFM::NotHostedBy")
EFM_Colocated = Class(name="EFM::Colocated")
NodeFeatureElement = Class(name="NodeFeatureElement")
EFM_NodeFeatureElement = Class(name="EFM::NodeFeatureElement", is_abstract=True)
EFM_Separated = Class(name="EFM::Separated")
EFM_ResourceVerification = Class(name="EFM::ResourceVerification")

# EFM_FeatCardinality class attributes and methods

# EFM_NodeFeature class attributes and methods
EFM_NodeFeature_name: Property = Property(name="name", type=StringType)
EFM_NodeFeature.attributes={EFM_NodeFeature_name}

# EFM_Exclusive class attributes and methods

# Alternative class attributes and methods

# EFM_Alternative class attributes and methods

# Feature class attributes and methods

# EFM_Cardinality class attributes and methods
EFM_Cardinality_cardinalityMin: Property = Property(name="cardinalityMin", type=IntegerType)
EFM_Cardinality_cardinalityMax: Property = Property(name="cardinalityMax", type=IntegerType)
EFM_Cardinality_configValue: Property = Property(name="configValue", type=IntegerType)
EFM_Cardinality.attributes={EFM_Cardinality_cardinalityMin, EFM_Cardinality_cardinalityMax, EFM_Cardinality_configValue}

# EFM_Value class attributes and methods

# EFM_BooleanConstraint class attributes and methods

# FMConstraint class attributes and methods

# Cardinality class attributes and methods

# EFM_Implies class attributes and methods

# BooleanConstraint class attributes and methods

# EFM_Excludes class attributes and methods

# EFM_Requires class attributes and methods
EFM_Requires_operator: Property = Property(name="operator", type=StringType)
EFM_Requires.attributes={EFM_Requires_operator}

# EFM_Operation class attributes and methods

# EFM_FeatureModel class attributes and methods

# EFM_FMConstraint class attributes and methods

# EFM_Feature class attributes and methods
EFM_Feature_name: Property = Property(name="name", type=StringType)
EFM_Feature.attributes={EFM_Feature_name}

# EFM_FMElement class attributes and methods

# FMElement class attributes and methods

# EFM_Attribute class attributes and methods
EFM_Attribute_name: Property = Property(name="name", type=StringType)
EFM_Attribute.attributes={EFM_Attribute_name}

# EFM_RangeOperation class attributes and methods
EFM_RangeOperation_min: Property = Property(name="min", type=IntegerType)
EFM_RangeOperation_max: Property = Property(name="max", type=IntegerType)
EFM_RangeOperation.attributes={EFM_RangeOperation_min, EFM_RangeOperation_max}

# Operation class attributes and methods

# EFM_ValueOperation class attributes and methods

# EFM_IntValue class attributes and methods

# EFM_Functional class attributes and methods
EFM_Functional_type: Property = Property(name="type", type=StringType)
EFM_Functional_value: Property = Property(name="value", type=IntegerType)
EFM_Functional.attributes={EFM_Functional_type, EFM_Functional_value}

# EFM_Comparison class attributes and methods
EFM_Comparison_type: Property = Property(name="type", type=StringType)
EFM_Comparison.attributes={EFM_Comparison_type}

# EFM_HostedBy class attributes and methods

# EFM_NotHostedBy class attributes and methods

# EFM_Colocated class attributes and methods

# NodeFeatureElement class attributes and methods

# EFM_NodeFeatureElement class attributes and methods

# EFM_Separated class attributes and methods

# EFM_ResourceVerification class attributes and methods

# Relationships
featureCardinality8: BinaryAssociation = BinaryAssociation(
    name="featureCardinality8",
    ends={
        Property(name="EFM_FeatCardinality", type=EFM_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Feature9", type=EFM_FeatCardinality, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nodeFeature10: BinaryAssociation = BinaryAssociation(
    name="nodeFeature10",
    ends={
        Property(name="EFM_NodeFeature", type=EFM_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Feature11", type=EFM_NodeFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variants12: BinaryAssociation = BinaryAssociation(
    name="variants12",
    ends={
        Property(name="EFM_Feature13", type=EFM_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Alternative", type=EFM_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value14: BinaryAssociation = BinaryAssociation(
    name="value14",
    ends={
        Property(name="EFM_Value", type=EFM_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Attribute15", type=EFM_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from16: BinaryAssociation = BinaryAssociation(
    name="from16",
    ends={
        Property(name="EFM_Feature17", type=EFM_BooleanConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_BooleanConstraint", type=EFM_Feature, multiplicity=Multiplicity(1, 1))
    }
)
to18: BinaryAssociation = BinaryAssociation(
    name="to18",
    ends={
        Property(name="EFM_Feature20", type=EFM_BooleanConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_BooleanConstraint19", type=EFM_Feature, multiplicity=Multiplicity(1, 1))
    }
)
constraints0: BinaryAssociation = BinaryAssociation(
    name="constraints0",
    ends={
        Property(name="EFM_FMConstraint", type=EFM_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_FeatureModel", type=EFM_FMConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootFeature1: BinaryAssociation = BinaryAssociation(
    name="rootFeature1",
    ends={
        Property(name="EFM_Feature", type=EFM_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_FeatureModel2", type=EFM_Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="EFM_Attribute", type=EFM_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Feature4", type=EFM_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subFeatures6: BinaryAssociation = BinaryAssociation(
    name="subFeatures6",
    ends={
        Property(name="EFM_Feature7", type=EFM_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Feature5", type=EFM_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute37: BinaryAssociation = BinaryAssociation(
    name="attribute37",
    ends={
        Property(name="EFM_Attribute38", type=EFM_RangeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_RangeOperation", type=EFM_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
attribute39: BinaryAssociation = BinaryAssociation(
    name="attribute39",
    ends={
        Property(name="EFM_Attribute40", type=EFM_ValueOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_ValueOperation", type=EFM_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
value41: BinaryAssociation = BinaryAssociation(
    name="value41",
    ends={
        Property(name="EFM_IntValue", type=EFM_ValueOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_ValueOperation42", type=EFM_IntValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditions21: BinaryAssociation = BinaryAssociation(
    name="conditions21",
    ends={
        Property(name="EFM_Operation", type=EFM_Requires, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Requires", type=EFM_Operation, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
action22: BinaryAssociation = BinaryAssociation(
    name="action22",
    ends={
        Property(name="EFM_Operation24", type=EFM_Requires, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Requires23", type=EFM_Operation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from25: BinaryAssociation = BinaryAssociation(
    name="from25",
    ends={
        Property(name="EFM_Feature26", type=EFM_Functional, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Functional", type=EFM_Feature, multiplicity=Multiplicity(1, 1))
    }
)
to27: BinaryAssociation = BinaryAssociation(
    name="to27",
    ends={
        Property(name="EFM_Feature29", type=EFM_Functional, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Functional28", type=EFM_Feature, multiplicity=Multiplicity(1, 1))
    }
)
from30: BinaryAssociation = BinaryAssociation(
    name="from30",
    ends={
        Property(name="EFM_FMElement", type=EFM_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Comparison", type=EFM_FMElement, multiplicity=Multiplicity(1, 1))
    }
)
to31: BinaryAssociation = BinaryAssociation(
    name="to31",
    ends={
        Property(name="EFM_FMElement33", type=EFM_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Comparison32", type=EFM_FMElement, multiplicity=Multiplicity(1, 1))
    }
)
feature34: BinaryAssociation = BinaryAssociation(
    name="feature34",
    ends={
        Property(name="EFM_Feature36", type=EFM_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Operation35", type=EFM_Feature, multiplicity=Multiplicity(1, 1))
    }
)
NodeAttributes48: BinaryAssociation = BinaryAssociation(
    name="NodeAttributes48",
    ends={
        Property(name="EFM_Attribute50", type=EFM_NodeFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_NodeFeature49", type=EFM_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
NodeCardinalities51: BinaryAssociation = BinaryAssociation(
    name="NodeCardinalities51",
    ends={
        Property(name="EFM_FeatCardinality53", type=EFM_NodeFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_NodeFeature52", type=EFM_FeatCardinality, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
HostedBy54: BinaryAssociation = BinaryAssociation(
    name="HostedBy54",
    ends={
        Property(name="EFM_HostedBy", type=EFM_NodeFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_NodeFeature55", type=EFM_HostedBy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
NotHostedBy56: BinaryAssociation = BinaryAssociation(
    name="NotHostedBy56",
    ends={
        Property(name="EFM_NotHostedBy", type=EFM_NodeFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_NodeFeature57", type=EFM_NotHostedBy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from58: BinaryAssociation = BinaryAssociation(
    name="from58",
    ends={
        Property(name="EFM_Feature60", type=EFM_HostedBy, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_HostedBy59", type=EFM_Feature, multiplicity=Multiplicity(1, 9999))
    }
)
to61: BinaryAssociation = BinaryAssociation(
    name="to61",
    ends={
        Property(name="EFM_NodeFeature63", type=EFM_HostedBy, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_HostedBy62", type=EFM_NodeFeature, multiplicity=Multiplicity(1, 1))
    }
)
from43: BinaryAssociation = BinaryAssociation(
    name="from43",
    ends={
        Property(name="EFM_Feature44", type=EFM_Colocated, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Colocated", type=EFM_Feature, multiplicity=Multiplicity(1, 1))
    }
)
fromAgain45: BinaryAssociation = BinaryAssociation(
    name="fromAgain45",
    ends={
        Property(name="EFM_Feature47", type=EFM_Colocated, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Colocated46", type=EFM_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
fromAtt69: BinaryAssociation = BinaryAssociation(
    name="fromAtt69",
    ends={
        Property(name="EFM_Attribute70", type=EFM_ResourceVerification, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_ResourceVerification", type=EFM_Attribute, multiplicity=Multiplicity(1, 9999))
    }
)
extF71: BinaryAssociation = BinaryAssociation(
    name="extF71",
    ends={
        Property(name="EFM_Attribute73", type=EFM_ResourceVerification, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_ResourceVerification72", type=EFM_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
extF74: BinaryAssociation = BinaryAssociation(
    name="extF74",
    ends={
        Property(name="EFM_NodeFeature76", type=EFM_NotHostedBy, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_NotHostedBy75", type=EFM_NodeFeature, multiplicity=Multiplicity(1, 1))
    }
)
From77: BinaryAssociation = BinaryAssociation(
    name="From77",
    ends={
        Property(name="EFM_Feature79", type=EFM_NotHostedBy, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_NotHostedBy78", type=EFM_Feature, multiplicity=Multiplicity(1, 9999))
    }
)
from64: BinaryAssociation = BinaryAssociation(
    name="from64",
    ends={
        Property(name="EFM_Feature65", type=EFM_Separated, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Separated", type=EFM_Feature, multiplicity=Multiplicity(1, 1))
    }
)
to66: BinaryAssociation = BinaryAssociation(
    name="to66",
    ends={
        Property(name="EFM_Feature68", type=EFM_Separated, multiplicity=Multiplicity(1, 1)),
        Property(name="EFM_Separated67", type=EFM_Feature, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_EFM_Exclusive_Alternative = Generalization(general=Alternative, specific=EFM_Exclusive)
gen_EFM_Alternative_Feature = Generalization(general=Feature, specific=EFM_Alternative)
gen_EFM_Attribute_FMElement = Generalization(general=FMElement, specific=EFM_Attribute)
gen_EFM_BooleanConstraint_FMConstraint = Generalization(general=FMConstraint, specific=EFM_BooleanConstraint)
gen_EFM_FeatCardinality_Cardinality = Generalization(general=Cardinality, specific=EFM_FeatCardinality)
gen_EFM_Implies_BooleanConstraint = Generalization(general=BooleanConstraint, specific=EFM_Implies)
gen_EFM_Excludes_BooleanConstraint = Generalization(general=BooleanConstraint, specific=EFM_Excludes)
gen_EFM_Requires_FMConstraint = Generalization(general=FMConstraint, specific=EFM_Requires)
gen_EFM_Feature_FMElement = Generalization(general=FMElement, specific=EFM_Feature)
gen_EFM_RangeOperation_Operation = Generalization(general=Operation, specific=EFM_RangeOperation)
gen_EFM_ValueOperation_Operation = Generalization(general=Operation, specific=EFM_ValueOperation)
gen_EFM_Functional_FMConstraint = Generalization(general=FMConstraint, specific=EFM_Functional)
gen_EFM_Comparison_FMConstraint = Generalization(general=FMConstraint, specific=EFM_Comparison)
gen_EFM_HostedBy_FMConstraint = Generalization(general=FMConstraint, specific=EFM_HostedBy)
gen_EFM_Colocated_FMConstraint = Generalization(general=FMConstraint, specific=EFM_Colocated)
gen_EFM_NodeFeature_NodeFeatureElement = Generalization(general=NodeFeatureElement, specific=EFM_NodeFeature)
gen_EFM_NotHostedBy_FMConstraint = Generalization(general=FMConstraint, specific=EFM_NotHostedBy)
gen_EFM_Separated_FMConstraint = Generalization(general=FMConstraint, specific=EFM_Separated)
gen_EFM_ResourceVerification_FMConstraint = Generalization(general=FMConstraint, specific=EFM_ResourceVerification)

# Domain Model
domain_model = DomainModel(
    name="EFM",
    types={EFM_FeatCardinality, EFM_NodeFeature, EFM_Exclusive, Alternative, EFM_Alternative, Feature, EFM_Cardinality, EFM_Value, EFM_BooleanConstraint, FMConstraint, Cardinality, EFM_Implies, BooleanConstraint, EFM_Excludes, EFM_Requires, EFM_Operation, EFM_FeatureModel, EFM_FMConstraint, EFM_Feature, EFM_FMElement, FMElement, EFM_Attribute, EFM_RangeOperation, Operation, EFM_ValueOperation, EFM_IntValue, EFM_Functional, EFM_Comparison, EFM_HostedBy, EFM_NotHostedBy, EFM_Colocated, NodeFeatureElement, EFM_NodeFeatureElement, EFM_Separated, EFM_ResourceVerification, ComparisonOperator, Operator, LogicalOperator},
    associations={featureCardinality8, nodeFeature10, variants12, value14, from16, to18, constraints0, rootFeature1, attributes3, subFeatures6, attribute37, attribute39, value41, conditions21, action22, from25, to27, from30, to31, feature34, NodeAttributes48, NodeCardinalities51, HostedBy54, NotHostedBy56, from58, to61, from43, fromAgain45, fromAtt69, extF71, extF74, From77, from64, to66},
    generalizations={gen_EFM_Exclusive_Alternative, gen_EFM_Alternative_Feature, gen_EFM_Attribute_FMElement, gen_EFM_BooleanConstraint_FMConstraint, gen_EFM_FeatCardinality_Cardinality, gen_EFM_Implies_BooleanConstraint, gen_EFM_Excludes_BooleanConstraint, gen_EFM_Requires_FMConstraint, gen_EFM_Feature_FMElement, gen_EFM_RangeOperation_Operation, gen_EFM_ValueOperation_Operation, gen_EFM_Functional_FMConstraint, gen_EFM_Comparison_FMConstraint, gen_EFM_HostedBy_FMConstraint, gen_EFM_Colocated_FMConstraint, gen_EFM_NodeFeature_NodeFeatureElement, gen_EFM_NotHostedBy_FMConstraint, gen_EFM_Separated_FMConstraint, gen_EFM_ResourceVerification_FMConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)