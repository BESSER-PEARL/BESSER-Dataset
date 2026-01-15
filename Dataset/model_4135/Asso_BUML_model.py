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
asso_Model = Class(name="asso::Model")
asso_Variable = Class(name="asso::Variable")
asso_EvalExpression = Class(name="asso::EvalExpression")
asso_Expression = Class(name="asso::Expression")
asso_FloatConstant = Class(name="asso::FloatConstant")
Expression = Class(name="Expression")
asso_NegFloatConstant = Class(name="asso::NegFloatConstant")
asso_Minus = Class(name="asso::Minus")
asso_Mult = Class(name="asso::Mult")
asso_Div = Class(name="asso::Div")
asso_VariableRef = Class(name="asso::VariableRef")
asso_Plus = Class(name="asso::Plus")

# asso_Model class attributes and methods

# asso_Variable class attributes and methods
asso_Variable_name: Property = Property(name="name", type=StringType)
asso_Variable.attributes={asso_Variable_name}

# asso_EvalExpression class attributes and methods

# asso_Expression class attributes and methods

# asso_FloatConstant class attributes and methods
asso_FloatConstant_value: Property = Property(name="value", type=FloatType)
asso_FloatConstant.attributes={asso_FloatConstant_value}

# Expression class attributes and methods

# asso_NegFloatConstant class attributes and methods
asso_NegFloatConstant_value: Property = Property(name="value", type=FloatType)
asso_NegFloatConstant.attributes={asso_NegFloatConstant_value}

# asso_Minus class attributes and methods

# asso_Mult class attributes and methods

# asso_Div class attributes and methods

# asso_VariableRef class attributes and methods

# asso_Plus class attributes and methods

# Relationships
variables0: BinaryAssociation = BinaryAssociation(
    name="variables0",
    ends={
        Property(name="asso_Variable", type=asso_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="asso_Model", type=asso_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
evaluations1: BinaryAssociation = BinaryAssociation(
    name="evaluations1",
    ends={
        Property(name="asso_EvalExpression", type=asso_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="asso_Model2", type=asso_EvalExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subVar4: BinaryAssociation = BinaryAssociation(
    name="subVar4",
    ends={
        Property(name="asso_Variable5", type=asso_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="asso_Variable3", type=asso_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression6: BinaryAssociation = BinaryAssociation(
    name="expression6",
    ends={
        Property(name="asso_Expression", type=asso_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="asso_Variable7", type=asso_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression8: BinaryAssociation = BinaryAssociation(
    name="expression8",
    ends={
        Property(name="asso_Expression10", type=asso_EvalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="asso_EvalExpression9", type=asso_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left18: BinaryAssociation = BinaryAssociation(
    name="left18",
    ends={
        Property(name="asso_Expression19", type=asso_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="asso_Minus", type=asso_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right20: BinaryAssociation = BinaryAssociation(
    name="right20",
    ends={
        Property(name="asso_Expression22", type=asso_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="asso_Minus21", type=asso_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left23: BinaryAssociation = BinaryAssociation(
    name="left23",
    ends={
        Property(name="asso_Expression24", type=asso_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="asso_Mult", type=asso_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right25: BinaryAssociation = BinaryAssociation(
    name="right25",
    ends={
        Property(name="asso_Expression27", type=asso_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="asso_Mult26", type=asso_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left28: BinaryAssociation = BinaryAssociation(
    name="left28",
    ends={
        Property(name="asso_Expression29", type=asso_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="asso_Div", type=asso_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right30: BinaryAssociation = BinaryAssociation(
    name="right30",
    ends={
        Property(name="asso_Expression32", type=asso_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="asso_Div31", type=asso_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value11: BinaryAssociation = BinaryAssociation(
    name="value11",
    ends={
        Property(name="asso_Variable12", type=asso_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="asso_VariableRef", type=asso_Variable, multiplicity=Multiplicity(0, 1))
    }
)
left13: BinaryAssociation = BinaryAssociation(
    name="left13",
    ends={
        Property(name="asso_Expression14", type=asso_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="asso_Plus", type=asso_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right15: BinaryAssociation = BinaryAssociation(
    name="right15",
    ends={
        Property(name="asso_Expression17", type=asso_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="asso_Plus16", type=asso_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_asso_FloatConstant_Expression = Generalization(general=Expression, specific=asso_FloatConstant)
gen_asso_Minus_Expression = Generalization(general=Expression, specific=asso_Minus)
gen_asso_Mult_Expression = Generalization(general=Expression, specific=asso_Mult)
gen_asso_Div_Expression = Generalization(general=Expression, specific=asso_Div)
gen_asso_NegFloatConstant_Expression = Generalization(general=Expression, specific=asso_NegFloatConstant)
gen_asso_VariableRef_Expression = Generalization(general=Expression, specific=asso_VariableRef)
gen_asso_Plus_Expression = Generalization(general=Expression, specific=asso_Plus)

# Domain Model
domain_model = DomainModel(
    name="asso",
    types={asso_Model, asso_Variable, asso_EvalExpression, asso_Expression, asso_FloatConstant, Expression, asso_NegFloatConstant, asso_Minus, asso_Mult, asso_Div, asso_VariableRef, asso_Plus},
    associations={variables0, evaluations1, subVar4, expression6, expression8, left18, right20, left23, right25, left28, right30, value11, left13, right15},
    generalizations={gen_asso_FloatConstant_Expression, gen_asso_Minus_Expression, gen_asso_Mult_Expression, gen_asso_Div_Expression, gen_asso_NegFloatConstant_Expression, gen_asso_VariableRef_Expression, gen_asso_Plus_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)