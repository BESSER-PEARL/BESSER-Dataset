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
model_ExistsContextualExpression = Class(name="model::ExistsContextualExpression")
model_Equation = Class(name="model::Equation")
model_Implication = Class(name="model::Implication")
model_Disjunction = Class(name="model::Disjunction")
model_Conjunction = Class(name="model::Conjunction")
model_Expression = Class(name="model::Expression", is_abstract=True)
model_ForAllContextualExpression = Class(name="model::ForAllContextualExpression")
Expression = Class(name="Expression")
model_Negation = Class(name="model::Negation")
model_PrimaryExpression = Class(name="model::PrimaryExpression")

# model_ExistsContextualExpression class attributes and methods
model_ExistsContextualExpression_contextId: Property = Property(name="contextId", type=StringType)
model_ExistsContextualExpression.attributes={model_ExistsContextualExpression_contextId}

# model_Equation class attributes and methods

# model_Implication class attributes and methods

# model_Disjunction class attributes and methods

# model_Conjunction class attributes and methods

# model_Expression class attributes and methods

# model_ForAllContextualExpression class attributes and methods
model_ForAllContextualExpression_contextId: Property = Property(name="contextId", type=StringType)
model_ForAllContextualExpression.attributes={model_ForAllContextualExpression_contextId}

# Expression class attributes and methods

# model_Negation class attributes and methods

# model_PrimaryExpression class attributes and methods
model_PrimaryExpression_featureId: Property = Property(name="featureId", type=StringType)
model_PrimaryExpression.attributes={model_PrimaryExpression_featureId}

# Relationships
expression0: BinaryAssociation = BinaryAssociation(
    name="expression0",
    ends={
        Property(name="model_Expression", type=model_ForAllContextualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ForAllContextualExpression", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression1: BinaryAssociation = BinaryAssociation(
    name="expression1",
    ends={
        Property(name="model_Expression2", type=model_ExistsContextualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ExistsContextualExpression", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftPart3: BinaryAssociation = BinaryAssociation(
    name="leftPart3",
    ends={
        Property(name="model_Expression4", type=model_Equation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Equation", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightPart5: BinaryAssociation = BinaryAssociation(
    name="rightPart5",
    ends={
        Property(name="model_Expression7", type=model_Equation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Equation6", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftPart8: BinaryAssociation = BinaryAssociation(
    name="leftPart8",
    ends={
        Property(name="model_Expression9", type=model_Implication, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Implication", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightPart10: BinaryAssociation = BinaryAssociation(
    name="rightPart10",
    ends={
        Property(name="model_Expression12", type=model_Implication, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Implication11", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftPart13: BinaryAssociation = BinaryAssociation(
    name="leftPart13",
    ends={
        Property(name="model_Expression14", type=model_Disjunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Disjunction", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightPart15: BinaryAssociation = BinaryAssociation(
    name="rightPart15",
    ends={
        Property(name="model_Expression17", type=model_Disjunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Disjunction16", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftPart18: BinaryAssociation = BinaryAssociation(
    name="leftPart18",
    ends={
        Property(name="model_Expression19", type=model_Conjunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Conjunction", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightPart20: BinaryAssociation = BinaryAssociation(
    name="rightPart20",
    ends={
        Property(name="model_Expression22", type=model_Conjunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Conjunction21", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression23: BinaryAssociation = BinaryAssociation(
    name="expression23",
    ends={
        Property(name="model_Expression24", type=model_Negation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Negation", type=model_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_model_ExistsContextualExpression_Expression = Generalization(general=Expression, specific=model_ExistsContextualExpression)
gen_model_Equation_Expression = Generalization(general=Expression, specific=model_Equation)
gen_model_Implication_Expression = Generalization(general=Expression, specific=model_Implication)
gen_model_Disjunction_Expression = Generalization(general=Expression, specific=model_Disjunction)
gen_model_Conjunction_Expression = Generalization(general=Expression, specific=model_Conjunction)
gen_model_ForAllContextualExpression_Expression = Generalization(general=Expression, specific=model_ForAllContextualExpression)
gen_model_Negation_Expression = Generalization(general=Expression, specific=model_Negation)
gen_model_PrimaryExpression_Expression = Generalization(general=Expression, specific=model_PrimaryExpression)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_ExistsContextualExpression, model_Equation, model_Implication, model_Disjunction, model_Conjunction, model_Expression, model_ForAllContextualExpression, Expression, model_Negation, model_PrimaryExpression},
    associations={expression0, expression1, leftPart3, rightPart5, leftPart8, rightPart10, leftPart13, rightPart15, leftPart18, rightPart20, expression23},
    generalizations={gen_model_ExistsContextualExpression_Expression, gen_model_Equation_Expression, gen_model_Implication_Expression, gen_model_Disjunction_Expression, gen_model_Conjunction_Expression, gen_model_ForAllContextualExpression_Expression, gen_model_Negation_Expression, gen_model_PrimaryExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)