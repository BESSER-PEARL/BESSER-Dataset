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
SimpleType: Enumeration = Enumeration(
    name="SimpleType",
    literals={
            EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="nulltype")
    }
)

BinaryOperator: Enumeration = Enumeration(
    name="BinaryOperator",
    literals={
            EnumerationLiteral(name="Equals"),
			EnumerationLiteral(name="Higher"),
			EnumerationLiteral(name="Lower"),
			EnumerationLiteral(name="And"),
			EnumerationLiteral(name="Add"),
			EnumerationLiteral(name="Subtract"),
			EnumerationLiteral(name="Divide"),
			EnumerationLiteral(name="Multiply"),
			EnumerationLiteral(name="Or")
    }
)

UnaryOperator: Enumeration = Enumeration(
    name="UnaryOperator",
    literals={
            EnumerationLiteral(name="Not"),
			EnumerationLiteral(name="Minus")
    }
)

SolitaryType: Enumeration = Enumeration(
    name="SolitaryType",
    literals={
            EnumerationLiteral(name="Mandatory"),
			EnumerationLiteral(name="Optional")
    }
)

# Classes
featureModel_SolitaryFeature = Class(name="featureModel_SolitaryFeature")
Feature = Class(name="Feature")
featureModel_Feature = Class(name="featureModel_Feature", is_abstract=True)
featureModel_GroupedFeature = Class(name="featureModel_GroupedFeature")
featureModel_Model = Class(name="featureModel_Model")
featureModel_BinaryOperation = Class(name="featureModel_BinaryOperation")
Expression = Class(name="Expression")
featureModel_UnaryOperation = Class(name="featureModel_UnaryOperation")
featureModel_Group = Class(name="featureModel_Group")
featureModel_Expression = Class(name="featureModel_Expression", is_abstract=True)
featureModel_Constant = Class(name="featureModel_Constant", is_abstract=True)
featureModel_NULL = Class(name="featureModel_NULL")
Constant = Class(name="Constant")
featureModel_Number = Class(name="featureModel_Number")
featureModel_Identifier = Class(name="featureModel_Identifier")

# featureModel_SolitaryFeature class attributes and methods
featureModel_SolitaryFeature_required: Property = Property(name="required", type=StringType)
featureModel_SolitaryFeature.attributes={featureModel_SolitaryFeature_required}

# Feature class attributes and methods

# featureModel_Feature class attributes and methods
featureModel_Feature_name: Property = Property(name="name", type=StringType)
featureModel_Feature_type: Property = Property(name="type", type=StringType)
featureModel_Feature.attributes={featureModel_Feature_type, featureModel_Feature_name}

# featureModel_GroupedFeature class attributes and methods

# featureModel_Model class attributes and methods

# featureModel_BinaryOperation class attributes and methods
featureModel_BinaryOperation_operator: Property = Property(name="operator", type=StringType)
featureModel_BinaryOperation.attributes={featureModel_BinaryOperation_operator}

# Expression class attributes and methods

# featureModel_UnaryOperation class attributes and methods
featureModel_UnaryOperation_operator: Property = Property(name="operator", type=StringType)
featureModel_UnaryOperation.attributes={featureModel_UnaryOperation_operator}

# featureModel_Group class attributes and methods
featureModel_Group_inclusive: Property = Property(name="inclusive", type=BooleanType)
featureModel_Group.attributes={featureModel_Group_inclusive}

# featureModel_Expression class attributes and methods

# featureModel_Constant class attributes and methods

# featureModel_NULL class attributes and methods

# Constant class attributes and methods

# featureModel_Number class attributes and methods
featureModel_Number_value: Property = Property(name="value", type=IntegerType)
featureModel_Number.attributes={featureModel_Number_value}

# featureModel_Identifier class attributes and methods
featureModel_Identifier_name: Property = Property(name="name", type=StringType)
featureModel_Identifier.attributes={featureModel_Identifier_name}

# Relationships
RootFeature5: BinaryAssociation = BinaryAssociation(
    name="RootFeature5",
    ends={
        Property(name="featureModel_Feature6", type=featureModel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Model", type=featureModel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupedFeatures7: BinaryAssociation = BinaryAssociation(
    name="groupedFeatures7",
    ends={
        Property(name="featureModel_GroupedFeature", type=featureModel_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Group8", type=featureModel_GroupedFeature, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
rexp9: BinaryAssociation = BinaryAssociation(
    name="rexp9",
    ends={
        Property(name="featureModel_Expression10", type=featureModel_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_BinaryOperation", type=featureModel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lexp11: BinaryAssociation = BinaryAssociation(
    name="lexp11",
    ends={
        Property(name="featureModel_Expression13", type=featureModel_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_BinaryOperation12", type=featureModel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exp14: BinaryAssociation = BinaryAssociation(
    name="exp14",
    ends={
        Property(name="featureModel_Expression15", type=featureModel_UnaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_UnaryOperation", type=featureModel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
groups0: BinaryAssociation = BinaryAssociation(
    name="groups0",
    ends={
        Property(name="featureModel_Group", type=featureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Feature", type=featureModel_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features1: BinaryAssociation = BinaryAssociation(
    name="features1",
    ends={
        Property(name="featureModel_SolitaryFeature", type=featureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Feature2", type=featureModel_SolitaryFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints3: BinaryAssociation = BinaryAssociation(
    name="constraints3",
    ends={
        Property(name="featureModel_Expression", type=featureModel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Feature4", type=featureModel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref16: BinaryAssociation = BinaryAssociation(
    name="ref16",
    ends={
        Property(name="featureModel_Feature17", type=featureModel_Identifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel_Identifier", type=featureModel_Feature, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_featureModel_SolitaryFeature_Feature = Generalization(general=Feature, specific=featureModel_SolitaryFeature)
gen_featureModel_GroupedFeature_Feature = Generalization(general=Feature, specific=featureModel_GroupedFeature)
gen_featureModel_BinaryOperation_Expression = Generalization(general=Expression, specific=featureModel_BinaryOperation)
gen_featureModel_UnaryOperation_Expression = Generalization(general=Expression, specific=featureModel_UnaryOperation)
gen_featureModel_Constant_Expression = Generalization(general=Expression, specific=featureModel_Constant)
gen_featureModel_NULL_Constant = Generalization(general=Constant, specific=featureModel_NULL)
gen_featureModel_Number_Constant = Generalization(general=Constant, specific=featureModel_Number)
gen_featureModel_Identifier_Expression = Generalization(general=Expression, specific=featureModel_Identifier)

# Domain Model
domain_model = DomainModel(
    name="featureModel",
    types={featureModel_SolitaryFeature, Feature, featureModel_Feature, featureModel_GroupedFeature, featureModel_Model, featureModel_BinaryOperation, Expression, featureModel_UnaryOperation, featureModel_Group, featureModel_Expression, featureModel_Constant, featureModel_NULL, Constant, featureModel_Number, featureModel_Identifier, SimpleType, BinaryOperator, UnaryOperator, SolitaryType},
    associations={RootFeature5, groupedFeatures7, rexp9, lexp11, exp14, groups0, features1, constraints3, ref16},
    generalizations={gen_featureModel_SolitaryFeature_Feature, gen_featureModel_GroupedFeature_Feature, gen_featureModel_BinaryOperation_Expression, gen_featureModel_UnaryOperation_Expression, gen_featureModel_Constant_Expression, gen_featureModel_NULL_Constant, gen_featureModel_Number_Constant, gen_featureModel_Identifier_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)