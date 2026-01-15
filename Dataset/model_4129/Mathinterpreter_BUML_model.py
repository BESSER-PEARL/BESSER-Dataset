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
mathinterpreter_External = Class(name="mathinterpreter::External")
Primary = Class(name="Primary")
mathinterpreter_Primary = Class(name="mathinterpreter::Primary")
mathinterpreter_EObject = Class(name="mathinterpreter::EObject")
mathinterpreter_Model = Class(name="mathinterpreter::Model")
mathinterpreter_MathExpression = Class(name="mathinterpreter::MathExpression")
mathinterpreter_PMExpression = Class(name="mathinterpreter::PMExpression")
mathinterpreter_Function = Class(name="mathinterpreter::Function")
MathExpression = Class(name="MathExpression")
mathinterpreter_DefineExpr = Class(name="mathinterpreter::DefineExpr")
DefParenthesis = Class(name="DefParenthesis")
mathinterpreter_Variable = Class(name="mathinterpreter::Variable")
mathinterpreter_MDExpression = Class(name="mathinterpreter::MDExpression")
PMExpression = Class(name="PMExpression")
mathinterpreter_PowExpression = Class(name="mathinterpreter::PowExpression")
MDExpression = Class(name="MDExpression")
mathinterpreter_Power = Class(name="mathinterpreter::Power")
mathinterpreter_PlusMinus = Class(name="mathinterpreter::PlusMinus")
mathinterpreter_MultiplyDivide = Class(name="mathinterpreter::MultiplyDivide")
PowExpression = Class(name="PowExpression")
mathinterpreter_VariableName = Class(name="mathinterpreter::VariableName")
mathinterpreter_Number = Class(name="mathinterpreter::Number")
mathinterpreter_Positive = Class(name="mathinterpreter::Positive")
Number = Class(name="Number")
mathinterpreter_Negative = Class(name="mathinterpreter::Negative")
mathinterpreter_PMParenthesis = Class(name="mathinterpreter::PMParenthesis")
mathinterpreter_DefParenthesis = Class(name="mathinterpreter::DefParenthesis")
mathinterpreter_Pow = Class(name="mathinterpreter::Pow")
Power = Class(name="Power")
mathinterpreter_Plus = Class(name="mathinterpreter::Plus")
PlusMinus = Class(name="PlusMinus")
mathinterpreter_Minus = Class(name="mathinterpreter::Minus")
mathinterpreter_Multiply = Class(name="mathinterpreter::Multiply")
MultiplyDivide = Class(name="MultiplyDivide")
mathinterpreter_Divide = Class(name="mathinterpreter::Divide")

# mathinterpreter_External class attributes and methods
mathinterpreter_External_name: Property = Property(name="name", type=StringType)
mathinterpreter_External.attributes={mathinterpreter_External_name}

# Primary class attributes and methods

# mathinterpreter_Primary class attributes and methods

# mathinterpreter_EObject class attributes and methods

# mathinterpreter_Model class attributes and methods

# mathinterpreter_MathExpression class attributes and methods
mathinterpreter_MathExpression_description: Property = Property(name="description", type=StringType)
mathinterpreter_MathExpression.attributes={mathinterpreter_MathExpression_description}

# mathinterpreter_PMExpression class attributes and methods

# mathinterpreter_Function class attributes and methods

# MathExpression class attributes and methods

# mathinterpreter_DefineExpr class attributes and methods

# DefParenthesis class attributes and methods

# mathinterpreter_Variable class attributes and methods
mathinterpreter_Variable_name: Property = Property(name="name", type=StringType)
mathinterpreter_Variable.attributes={mathinterpreter_Variable_name}

# mathinterpreter_MDExpression class attributes and methods

# PMExpression class attributes and methods

# mathinterpreter_PowExpression class attributes and methods

# MDExpression class attributes and methods

# mathinterpreter_Power class attributes and methods

# mathinterpreter_PlusMinus class attributes and methods

# mathinterpreter_MultiplyDivide class attributes and methods

# PowExpression class attributes and methods

# mathinterpreter_VariableName class attributes and methods
mathinterpreter_VariableName_name: Property = Property(name="name", type=StringType)
mathinterpreter_VariableName.attributes={mathinterpreter_VariableName_name}

# mathinterpreter_Number class attributes and methods
mathinterpreter_Number_value: Property = Property(name="value", type=IntegerType)
mathinterpreter_Number.attributes={mathinterpreter_Number_value}

# mathinterpreter_Positive class attributes and methods

# Number class attributes and methods

# mathinterpreter_Negative class attributes and methods

# mathinterpreter_PMParenthesis class attributes and methods

# mathinterpreter_DefParenthesis class attributes and methods

# mathinterpreter_Pow class attributes and methods

# Power class attributes and methods

# mathinterpreter_Plus class attributes and methods

# PlusMinus class attributes and methods

# mathinterpreter_Minus class attributes and methods

# mathinterpreter_Multiply class attributes and methods

# MultiplyDivide class attributes and methods

# mathinterpreter_Divide class attributes and methods

# Relationships
expression4: BinaryAssociation = BinaryAssociation(
    name="expression4",
    ends={
        Property(name="mathinterpreter_PMExpression6", type=mathinterpreter_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="mathinterpreter_Variable5", type=mathinterpreter_PMExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments7: BinaryAssociation = BinaryAssociation(
    name="arguments7",
    ends={
        Property(name="mathinterpreter_Primary", type=mathinterpreter_External, multiplicity=Multiplicity(1, 1)),
        Property(name="mathinterpreter_External", type=mathinterpreter_Primary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left9: BinaryAssociation = BinaryAssociation(
    name="left9",
    ends={
        Property(name="mathinterpreter_PMExpression10", type=mathinterpreter_PMExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mathinterpreter_PMExpression8", type=mathinterpreter_PMExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mathexpression0: BinaryAssociation = BinaryAssociation(
    name="mathexpression0",
    ends={
        Property(name="mathinterpreter_MathExpression", type=mathinterpreter_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="mathinterpreter_Model", type=mathinterpreter_MathExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression1: BinaryAssociation = BinaryAssociation(
    name="expression1",
    ends={
        Property(name="mathinterpreter_PMExpression", type=mathinterpreter_MathExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mathinterpreter_MathExpression2", type=mathinterpreter_PMExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables3: BinaryAssociation = BinaryAssociation(
    name="variables3",
    ends={
        Property(name="mathinterpreter_Variable", type=mathinterpreter_DefineExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="mathinterpreter_DefineExpr", type=mathinterpreter_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operator11: BinaryAssociation = BinaryAssociation(
    name="operator11",
    ends={
        Property(name="mathinterpreter_EObject", type=mathinterpreter_PMExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mathinterpreter_PMExpression12", type=mathinterpreter_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right13: BinaryAssociation = BinaryAssociation(
    name="right13",
    ends={
        Property(name="mathinterpreter_MDExpression", type=mathinterpreter_PMExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mathinterpreter_PMExpression14", type=mathinterpreter_MDExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression15: BinaryAssociation = BinaryAssociation(
    name="expression15",
    ends={
        Property(name="mathinterpreter_PMExpression16", type=mathinterpreter_PMParenthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="mathinterpreter_PMParenthesis", type=mathinterpreter_PMExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_mathinterpreter_External_Primary = Generalization(general=Primary, specific=mathinterpreter_External)
gen_mathinterpreter_Function_MathExpression = Generalization(general=MathExpression, specific=mathinterpreter_Function)
gen_mathinterpreter_DefineExpr_MathExpression = Generalization(general=MathExpression, specific=mathinterpreter_DefineExpr)
gen_mathinterpreter_DefineExpr_DefParenthesis = Generalization(general=DefParenthesis, specific=mathinterpreter_DefineExpr)
gen_mathinterpreter_MDExpression_PMExpression = Generalization(general=PMExpression, specific=mathinterpreter_MDExpression)
gen_mathinterpreter_PowExpression_MDExpression = Generalization(general=MDExpression, specific=mathinterpreter_PowExpression)
gen_mathinterpreter_Primary_PowExpression = Generalization(general=PowExpression, specific=mathinterpreter_Primary)
gen_mathinterpreter_VariableName_Primary = Generalization(general=Primary, specific=mathinterpreter_VariableName)
gen_mathinterpreter_Number_Primary = Generalization(general=Primary, specific=mathinterpreter_Number)
gen_mathinterpreter_Positive_Number = Generalization(general=Number, specific=mathinterpreter_Positive)
gen_mathinterpreter_Negative_Number = Generalization(general=Number, specific=mathinterpreter_Negative)
gen_mathinterpreter_PMParenthesis_Primary = Generalization(general=Primary, specific=mathinterpreter_PMParenthesis)
gen_mathinterpreter_DefParenthesis_Primary = Generalization(general=Primary, specific=mathinterpreter_DefParenthesis)
gen_mathinterpreter_Pow_Power = Generalization(general=Power, specific=mathinterpreter_Pow)
gen_mathinterpreter_Plus_PlusMinus = Generalization(general=PlusMinus, specific=mathinterpreter_Plus)
gen_mathinterpreter_Minus_PlusMinus = Generalization(general=PlusMinus, specific=mathinterpreter_Minus)
gen_mathinterpreter_Multiply_MultiplyDivide = Generalization(general=MultiplyDivide, specific=mathinterpreter_Multiply)
gen_mathinterpreter_Divide_MultiplyDivide = Generalization(general=MultiplyDivide, specific=mathinterpreter_Divide)

# Domain Model
domain_model = DomainModel(
    name="mathinterpreter",
    types={mathinterpreter_External, Primary, mathinterpreter_Primary, mathinterpreter_EObject, mathinterpreter_Model, mathinterpreter_MathExpression, mathinterpreter_PMExpression, mathinterpreter_Function, MathExpression, mathinterpreter_DefineExpr, DefParenthesis, mathinterpreter_Variable, mathinterpreter_MDExpression, PMExpression, mathinterpreter_PowExpression, MDExpression, mathinterpreter_Power, mathinterpreter_PlusMinus, mathinterpreter_MultiplyDivide, PowExpression, mathinterpreter_VariableName, mathinterpreter_Number, mathinterpreter_Positive, Number, mathinterpreter_Negative, mathinterpreter_PMParenthesis, mathinterpreter_DefParenthesis, mathinterpreter_Pow, Power, mathinterpreter_Plus, PlusMinus, mathinterpreter_Minus, mathinterpreter_Multiply, MultiplyDivide, mathinterpreter_Divide},
    associations={expression4, arguments7, left9, mathexpression0, expression1, variables3, operator11, right13, expression15},
    generalizations={gen_mathinterpreter_External_Primary, gen_mathinterpreter_Function_MathExpression, gen_mathinterpreter_DefineExpr_MathExpression, gen_mathinterpreter_DefineExpr_DefParenthesis, gen_mathinterpreter_MDExpression_PMExpression, gen_mathinterpreter_PowExpression_MDExpression, gen_mathinterpreter_Primary_PowExpression, gen_mathinterpreter_VariableName_Primary, gen_mathinterpreter_Number_Primary, gen_mathinterpreter_Positive_Number, gen_mathinterpreter_Negative_Number, gen_mathinterpreter_PMParenthesis_Primary, gen_mathinterpreter_DefParenthesis_Primary, gen_mathinterpreter_Pow_Power, gen_mathinterpreter_Plus_PlusMinus, gen_mathinterpreter_Minus_PlusMinus, gen_mathinterpreter_Multiply_MultiplyDivide, gen_mathinterpreter_Divide_MultiplyDivide},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)