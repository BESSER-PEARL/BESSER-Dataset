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
mathInterpreter_Solution = Class(name="mathInterpreter::Solution")
mathInterpreter_Variable = Class(name="mathInterpreter::Variable")
mathInterpreter_Expression = Class(name="mathInterpreter::Expression")
mathInterpreter_PlusOrMinus = Class(name="mathInterpreter::PlusOrMinus")
mathInterpreter_EObject = Class(name="mathInterpreter::EObject")
mathInterpreter_MultiplyOrDivide = Class(name="mathInterpreter::MultiplyOrDivide")
mathInterpreter_Primary = Class(name="mathInterpreter::Primary")
mathInterpreter_VariableRef = Class(name="mathInterpreter::VariableRef")
mathInterpreter_Bracket = Class(name="mathInterpreter::Bracket")
mathInterpreter_Plus = Class(name="mathInterpreter::Plus")
PlusOrMinus = Class(name="PlusOrMinus")
mathInterpreter_Minus = Class(name="mathInterpreter::Minus")
mathInterpreter_Multiply = Class(name="mathInterpreter::Multiply")
MultiplyOrDivide = Class(name="MultiplyOrDivide")
mathInterpreter_Divide = Class(name="mathInterpreter::Divide")
mathInterpreter_Num = Class(name="mathInterpreter::Num")
Primary = Class(name="Primary")

# mathInterpreter_Solution class attributes and methods

# mathInterpreter_Variable class attributes and methods
mathInterpreter_Variable_name: Property = Property(name="name", type=StringType)
mathInterpreter_Variable.attributes={mathInterpreter_Variable_name}

# mathInterpreter_Expression class attributes and methods

# mathInterpreter_PlusOrMinus class attributes and methods
mathInterpreter_PlusOrMinus_operator: Property = Property(name="operator", type=StringType)
mathInterpreter_PlusOrMinus.attributes={mathInterpreter_PlusOrMinus_operator}

# mathInterpreter_EObject class attributes and methods

# mathInterpreter_MultiplyOrDivide class attributes and methods
mathInterpreter_MultiplyOrDivide_operator: Property = Property(name="operator", type=StringType)
mathInterpreter_MultiplyOrDivide.attributes={mathInterpreter_MultiplyOrDivide_operator}

# mathInterpreter_Primary class attributes and methods

# mathInterpreter_VariableRef class attributes and methods

# mathInterpreter_Bracket class attributes and methods

# mathInterpreter_Plus class attributes and methods

# PlusOrMinus class attributes and methods

# mathInterpreter_Minus class attributes and methods

# mathInterpreter_Multiply class attributes and methods

# MultiplyOrDivide class attributes and methods

# mathInterpreter_Divide class attributes and methods

# mathInterpreter_Num class attributes and methods
mathInterpreter_Num_value: Property = Property(name="value", type=IntegerType)
mathInterpreter_Num.attributes={mathInterpreter_Num_value}

# Primary class attributes and methods

# Relationships
variables0: BinaryAssociation = BinaryAssociation(
    name="variables0",
    ends={
        Property(name="mathInterpreter_Variable", type=mathInterpreter_Solution, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_Solution", type=mathInterpreter_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression1: BinaryAssociation = BinaryAssociation(
    name="expression1",
    ends={
        Property(name="mathInterpreter_Expression", type=mathInterpreter_Solution, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_Solution2", type=mathInterpreter_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value3: BinaryAssociation = BinaryAssociation(
    name="value3",
    ends={
        Property(name="mathInterpreter_Expression5", type=mathInterpreter_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_Variable4", type=mathInterpreter_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp6: BinaryAssociation = BinaryAssociation(
    name="exp6",
    ends={
        Property(name="mathInterpreter_PlusOrMinus", type=mathInterpreter_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_Expression7", type=mathInterpreter_PlusOrMinus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left8: BinaryAssociation = BinaryAssociation(
    name="left8",
    ends={
        Property(name="mathInterpreter_EObject", type=mathInterpreter_PlusOrMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_PlusOrMinus9", type=mathInterpreter_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right10: BinaryAssociation = BinaryAssociation(
    name="right10",
    ends={
        Property(name="mathInterpreter_MultiplyOrDivide", type=mathInterpreter_PlusOrMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_PlusOrMinus11", type=mathInterpreter_MultiplyOrDivide, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left12: BinaryAssociation = BinaryAssociation(
    name="left12",
    ends={
        Property(name="mathInterpreter_EObject14", type=mathInterpreter_MultiplyOrDivide, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_MultiplyOrDivide13", type=mathInterpreter_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right15: BinaryAssociation = BinaryAssociation(
    name="right15",
    ends={
        Property(name="mathInterpreter_Primary", type=mathInterpreter_MultiplyOrDivide, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_MultiplyOrDivide16", type=mathInterpreter_Primary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="mathInterpreter_Variable18", type=mathInterpreter_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_VariableRef", type=mathInterpreter_Variable, multiplicity=Multiplicity(0, 1))
    }
)
value19: BinaryAssociation = BinaryAssociation(
    name="value19",
    ends={
        Property(name="mathInterpreter_Expression20", type=mathInterpreter_Bracket, multiplicity=Multiplicity(1, 1)),
        Property(name="mathInterpreter_Bracket", type=mathInterpreter_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_mathInterpreter_VariableRef_Primary = Generalization(general=Primary, specific=mathInterpreter_VariableRef)
gen_mathInterpreter_Bracket_Primary = Generalization(general=Primary, specific=mathInterpreter_Bracket)
gen_mathInterpreter_Plus_PlusOrMinus = Generalization(general=PlusOrMinus, specific=mathInterpreter_Plus)
gen_mathInterpreter_Minus_PlusOrMinus = Generalization(general=PlusOrMinus, specific=mathInterpreter_Minus)
gen_mathInterpreter_Multiply_MultiplyOrDivide = Generalization(general=MultiplyOrDivide, specific=mathInterpreter_Multiply)
gen_mathInterpreter_Divide_MultiplyOrDivide = Generalization(general=MultiplyOrDivide, specific=mathInterpreter_Divide)
gen_mathInterpreter_Num_Primary = Generalization(general=Primary, specific=mathInterpreter_Num)

# Domain Model
domain_model = DomainModel(
    name="mathInterpreter",
    types={mathInterpreter_Solution, mathInterpreter_Variable, mathInterpreter_Expression, mathInterpreter_PlusOrMinus, mathInterpreter_EObject, mathInterpreter_MultiplyOrDivide, mathInterpreter_Primary, mathInterpreter_VariableRef, mathInterpreter_Bracket, mathInterpreter_Plus, PlusOrMinus, mathInterpreter_Minus, mathInterpreter_Multiply, MultiplyOrDivide, mathInterpreter_Divide, mathInterpreter_Num, Primary},
    associations={variables0, expression1, value3, exp6, left8, right10, left12, right15, value17, value19},
    generalizations={gen_mathInterpreter_VariableRef_Primary, gen_mathInterpreter_Bracket_Primary, gen_mathInterpreter_Plus_PlusOrMinus, gen_mathInterpreter_Minus_PlusOrMinus, gen_mathInterpreter_Multiply_MultiplyOrDivide, gen_mathInterpreter_Divide_MultiplyOrDivide, gen_mathInterpreter_Num_Primary},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)