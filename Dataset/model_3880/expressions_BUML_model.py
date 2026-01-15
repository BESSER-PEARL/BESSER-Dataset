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
expressions_Function = Class(name="expressions::Function")
expressions_Parameter = Class(name="expressions::Parameter")
expressions_Expression = Class(name="expressions::Expression", is_abstract=True)
expressions_Number = Class(name="expressions::Number")
Expression = Class(name="Expression")
expressions_ParameterAccess = Class(name="expressions::ParameterAccess")
expressions_Plus = Class(name="expressions::Plus")
BinaryOperator = Class(name="BinaryOperator")
expressions_Minus = Class(name="expressions::Minus")
expressions_Mul = Class(name="expressions::Mul")
expressions_Div = Class(name="expressions::Div")
expressions_Neg = Class(name="expressions::Neg")
UnaryOperator = Class(name="UnaryOperator")
expressions_FunctionCall = Class(name="expressions::FunctionCall")
expressions_Model = Class(name="expressions::Model")
expressions_BinaryOperator = Class(name="expressions::BinaryOperator", is_abstract=True)
expressions_UnaryOperator = Class(name="expressions::UnaryOperator", is_abstract=True)

# expressions_Function class attributes and methods
expressions_Function_name: Property = Property(name="name", type=StringType)
expressions_Function.attributes={expressions_Function_name}

# expressions_Parameter class attributes and methods
expressions_Parameter_name: Property = Property(name="name", type=StringType)
expressions_Parameter.attributes={expressions_Parameter_name}

# expressions_Expression class attributes and methods

# expressions_Number class attributes and methods
expressions_Number_value: Property = Property(name="value", type=IntegerType)
expressions_Number.attributes={expressions_Number_value}

# Expression class attributes and methods

# expressions_ParameterAccess class attributes and methods

# expressions_Plus class attributes and methods

# BinaryOperator class attributes and methods

# expressions_Minus class attributes and methods

# expressions_Mul class attributes and methods

# expressions_Div class attributes and methods

# expressions_Neg class attributes and methods

# UnaryOperator class attributes and methods

# expressions_FunctionCall class attributes and methods

# expressions_Model class attributes and methods

# expressions_BinaryOperator class attributes and methods

# expressions_UnaryOperator class attributes and methods

# Relationships
parameters0: BinaryAssociation = BinaryAssociation(
    name="parameters0",
    ends={
        Property(name="expressions_Parameter", type=expressions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Function", type=expressions_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body1: BinaryAssociation = BinaryAssociation(
    name="body1",
    ends={
        Property(name="expressions_Expression", type=expressions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Function2", type=expressions_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op10: BinaryAssociation = BinaryAssociation(
    name="op10",
    ends={
        Property(name="expressions_Expression11", type=expressions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_UnaryOperator", type=expressions_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function12: BinaryAssociation = BinaryAssociation(
    name="function12",
    ends={
        Property(name="expressions_Function13", type=expressions_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_FunctionCall", type=expressions_Function, multiplicity=Multiplicity(1, 1))
    }
)
arguments14: BinaryAssociation = BinaryAssociation(
    name="arguments14",
    ends={
        Property(name="expressions_Expression16", type=expressions_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_FunctionCall15", type=expressions_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions17: BinaryAssociation = BinaryAssociation(
    name="functions17",
    ends={
        Property(name="expressions_Function18", type=expressions_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Model", type=expressions_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter3: BinaryAssociation = BinaryAssociation(
    name="parameter3",
    ends={
        Property(name="expressions_Parameter4", type=expressions_ParameterAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ParameterAccess", type=expressions_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
op15: BinaryAssociation = BinaryAssociation(
    name="op15",
    ends={
        Property(name="expressions_Expression6", type=expressions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_BinaryOperator", type=expressions_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op27: BinaryAssociation = BinaryAssociation(
    name="op27",
    ends={
        Property(name="expressions_Expression9", type=expressions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_BinaryOperator8", type=expressions_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_expressions_Number_Expression = Generalization(general=Expression, specific=expressions_Number)
gen_expressions_ParameterAccess_Expression = Generalization(general=Expression, specific=expressions_ParameterAccess)
gen_expressions_UnaryOperator_Expression = Generalization(general=Expression, specific=expressions_UnaryOperator)
gen_expressions_Plus_BinaryOperator = Generalization(general=BinaryOperator, specific=expressions_Plus)
gen_expressions_Minus_BinaryOperator = Generalization(general=BinaryOperator, specific=expressions_Minus)
gen_expressions_Mul_BinaryOperator = Generalization(general=BinaryOperator, specific=expressions_Mul)
gen_expressions_Div_BinaryOperator = Generalization(general=BinaryOperator, specific=expressions_Div)
gen_expressions_Neg_UnaryOperator = Generalization(general=UnaryOperator, specific=expressions_Neg)
gen_expressions_FunctionCall_Expression = Generalization(general=Expression, specific=expressions_FunctionCall)
gen_expressions_BinaryOperator_Expression = Generalization(general=Expression, specific=expressions_BinaryOperator)

# Domain Model
domain_model = DomainModel(
    name="expressions",
    types={expressions_Function, expressions_Parameter, expressions_Expression, expressions_Number, Expression, expressions_ParameterAccess, expressions_Plus, BinaryOperator, expressions_Minus, expressions_Mul, expressions_Div, expressions_Neg, UnaryOperator, expressions_FunctionCall, expressions_Model, expressions_BinaryOperator, expressions_UnaryOperator},
    associations={parameters0, body1, op10, function12, arguments14, functions17, parameter3, op15, op27},
    generalizations={gen_expressions_Number_Expression, gen_expressions_ParameterAccess_Expression, gen_expressions_UnaryOperator_Expression, gen_expressions_Plus_BinaryOperator, gen_expressions_Minus_BinaryOperator, gen_expressions_Mul_BinaryOperator, gen_expressions_Div_BinaryOperator, gen_expressions_Neg_UnaryOperator, gen_expressions_FunctionCall_Expression, gen_expressions_BinaryOperator_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)