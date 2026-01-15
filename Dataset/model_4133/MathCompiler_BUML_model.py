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
mathCompiler_Expressions = Class(name="mathCompiler::Expressions")
mathCompiler_MathExp = Class(name="mathCompiler::MathExp")
mathCompiler_Mult = Class(name="mathCompiler::Mult")
mathCompiler_Div = Class(name="mathCompiler::Div")
mathCompiler_External = Class(name="mathCompiler::External")
mathCompiler_Var = Class(name="mathCompiler::Var")
mathCompiler_Let = Class(name="mathCompiler::Let")
mathCompiler_Num = Class(name="mathCompiler::Num")
mathCompiler_Expression = Class(name="mathCompiler::Expression")
mathCompiler_Plus = Class(name="mathCompiler::Plus")
Expression = Class(name="Expression")
mathCompiler_Minus = Class(name="mathCompiler::Minus")

# mathCompiler_Expressions class attributes and methods

# mathCompiler_MathExp class attributes and methods
mathCompiler_MathExp_line: Property = Property(name="line", type=StringType)
mathCompiler_MathExp.attributes={mathCompiler_MathExp_line}

# mathCompiler_Mult class attributes and methods

# mathCompiler_Div class attributes and methods

# mathCompiler_External class attributes and methods
mathCompiler_External_base: Property = Property(name="base", type=IntegerType)
mathCompiler_External_exponent: Property = Property(name="exponent", type=IntegerType)
mathCompiler_External.attributes={mathCompiler_External_exponent, mathCompiler_External_base}

# mathCompiler_Var class attributes and methods
mathCompiler_Var_id: Property = Property(name="id", type=StringType)
mathCompiler_Var.attributes={mathCompiler_Var_id}

# mathCompiler_Let class attributes and methods
mathCompiler_Let_id: Property = Property(name="id", type=StringType)
mathCompiler_Let.attributes={mathCompiler_Let_id}

# mathCompiler_Num class attributes and methods
mathCompiler_Num_value: Property = Property(name="value", type=IntegerType)
mathCompiler_Num.attributes={mathCompiler_Num_value}

# mathCompiler_Expression class attributes and methods

# mathCompiler_Plus class attributes and methods

# Expression class attributes and methods

# mathCompiler_Minus class attributes and methods

# Relationships
expressions0: BinaryAssociation = BinaryAssociation(
    name="expressions0",
    ends={
        Property(name="mathCompiler_MathExp", type=mathCompiler_Expressions, multiplicity=Multiplicity(1, 1)),
        Property(name="mathCompiler_Expressions", type=mathCompiler_MathExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right10: BinaryAssociation = BinaryAssociation(
    name="right10",
    ends={
        Property(name="mathCompiler_Expression12", type=mathCompiler_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="mathCompiler_Minus11", type=mathCompiler_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left13: BinaryAssociation = BinaryAssociation(
    name="left13",
    ends={
        Property(name="mathCompiler_Expression14", type=mathCompiler_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="mathCompiler_Mult", type=mathCompiler_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right15: BinaryAssociation = BinaryAssociation(
    name="right15",
    ends={
        Property(name="mathCompiler_Expression17", type=mathCompiler_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="mathCompiler_Mult16", type=mathCompiler_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left18: BinaryAssociation = BinaryAssociation(
    name="left18",
    ends={
        Property(name="mathCompiler_Expression19", type=mathCompiler_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="mathCompiler_Div", type=mathCompiler_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right20: BinaryAssociation = BinaryAssociation(
    name="right20",
    ends={
        Property(name="mathCompiler_Expression22", type=mathCompiler_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="mathCompiler_Div21", type=mathCompiler_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
binding23: BinaryAssociation = BinaryAssociation(
    name="binding23",
    ends={
        Property(name="mathCompiler_Expression24", type=mathCompiler_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="mathCompiler_Let", type=mathCompiler_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body25: BinaryAssociation = BinaryAssociation(
    name="body25",
    ends={
        Property(name="mathCompiler_Expression27", type=mathCompiler_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="mathCompiler_Let26", type=mathCompiler_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp1: BinaryAssociation = BinaryAssociation(
    name="exp1",
    ends={
        Property(name="mathCompiler_Expression", type=mathCompiler_MathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="mathCompiler_MathExp2", type=mathCompiler_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left3: BinaryAssociation = BinaryAssociation(
    name="left3",
    ends={
        Property(name="mathCompiler_Expression4", type=mathCompiler_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="mathCompiler_Plus", type=mathCompiler_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right5: BinaryAssociation = BinaryAssociation(
    name="right5",
    ends={
        Property(name="mathCompiler_Expression7", type=mathCompiler_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="mathCompiler_Plus6", type=mathCompiler_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left8: BinaryAssociation = BinaryAssociation(
    name="left8",
    ends={
        Property(name="mathCompiler_Expression9", type=mathCompiler_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="mathCompiler_Minus", type=mathCompiler_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_mathCompiler_Mult_Expression = Generalization(general=Expression, specific=mathCompiler_Mult)
gen_mathCompiler_Div_Expression = Generalization(general=Expression, specific=mathCompiler_Div)
gen_mathCompiler_External_Expression = Generalization(general=Expression, specific=mathCompiler_External)
gen_mathCompiler_Var_Expression = Generalization(general=Expression, specific=mathCompiler_Var)
gen_mathCompiler_Let_Expression = Generalization(general=Expression, specific=mathCompiler_Let)
gen_mathCompiler_Plus_Expression = Generalization(general=Expression, specific=mathCompiler_Plus)
gen_mathCompiler_Minus_Expression = Generalization(general=Expression, specific=mathCompiler_Minus)
gen_mathCompiler_Num_Expression = Generalization(general=Expression, specific=mathCompiler_Num)

# Domain Model
domain_model = DomainModel(
    name="mathCompiler",
    types={mathCompiler_Expressions, mathCompiler_MathExp, mathCompiler_Mult, mathCompiler_Div, mathCompiler_External, mathCompiler_Var, mathCompiler_Let, mathCompiler_Num, mathCompiler_Expression, mathCompiler_Plus, Expression, mathCompiler_Minus},
    associations={expressions0, right10, left13, right15, left18, right20, binding23, body25, exp1, left3, right5, left8},
    generalizations={gen_mathCompiler_Mult_Expression, gen_mathCompiler_Div_Expression, gen_mathCompiler_External_Expression, gen_mathCompiler_Var_Expression, gen_mathCompiler_Let_Expression, gen_mathCompiler_Plus_Expression, gen_mathCompiler_Minus_Expression, gen_mathCompiler_Num_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)