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
myDsl_Classs = Class(name="myDsl::Classs")
myDsl_Instance = Class(name="myDsl::Instance")
myDsl_Method = Class(name="myDsl::Method")
Instance = Class(name="Instance")
myDsl_Parameter = Class(name="myDsl::Parameter")
myDsl_MathExp = Class(name="myDsl::MathExp")
myDsl_Expression = Class(name="myDsl::Expression")
myDsl_Plus = Class(name="myDsl::Plus")
Expression = Class(name="Expression")
myDsl_Minus = Class(name="myDsl::Minus")
myDsl_Var = Class(name="myDsl::Var")
myDsl_Let = Class(name="myDsl::Let")
myDsl_Num = Class(name="myDsl::Num")
myDsl_Mult = Class(name="myDsl::Mult")
myDsl_Div = Class(name="myDsl::Div")

# myDsl_Classs class attributes and methods

# myDsl_Instance class attributes and methods

# myDsl_Method class attributes and methods
myDsl_Method_name: Property = Property(name="name", type=StringType)
myDsl_Method.attributes={myDsl_Method_name}

# Instance class attributes and methods

# myDsl_Parameter class attributes and methods
myDsl_Parameter_name: Property = Property(name="name", type=StringType)
myDsl_Parameter.attributes={myDsl_Parameter_name}

# myDsl_MathExp class attributes and methods
myDsl_MathExp_text: Property = Property(name="text", type=StringType)
myDsl_MathExp.attributes={myDsl_MathExp_text}

# myDsl_Expression class attributes and methods

# myDsl_Plus class attributes and methods

# Expression class attributes and methods

# myDsl_Minus class attributes and methods

# myDsl_Var class attributes and methods
myDsl_Var_id: Property = Property(name="id", type=StringType)
myDsl_Var.attributes={myDsl_Var_id}

# myDsl_Let class attributes and methods
myDsl_Let_id: Property = Property(name="id", type=StringType)
myDsl_Let.attributes={myDsl_Let_id}

# myDsl_Num class attributes and methods
myDsl_Num_value: Property = Property(name="value", type=IntegerType)
myDsl_Num.attributes={myDsl_Num_value}

# myDsl_Mult class attributes and methods

# myDsl_Div class attributes and methods

# Relationships
instances0: BinaryAssociation = BinaryAssociation(
    name="instances0",
    ends={
        Property(name="myDsl_Instance", type=myDsl_Classs, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Classs", type=myDsl_Instance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params1: BinaryAssociation = BinaryAssociation(
    name="params1",
    ends={
        Property(name="myDsl_Parameter", type=myDsl_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Method", type=myDsl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp2: BinaryAssociation = BinaryAssociation(
    name="exp2",
    ends={
        Property(name="myDsl_Expression", type=myDsl_MathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MathExp", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left3: BinaryAssociation = BinaryAssociation(
    name="left3",
    ends={
        Property(name="myDsl_Expression4", type=myDsl_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Plus", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right5: BinaryAssociation = BinaryAssociation(
    name="right5",
    ends={
        Property(name="myDsl_Expression7", type=myDsl_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Plus6", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left8: BinaryAssociation = BinaryAssociation(
    name="left8",
    ends={
        Property(name="myDsl_Expression9", type=myDsl_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Minus", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right20: BinaryAssociation = BinaryAssociation(
    name="right20",
    ends={
        Property(name="myDsl_Expression22", type=myDsl_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Div21", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
binding23: BinaryAssociation = BinaryAssociation(
    name="binding23",
    ends={
        Property(name="myDsl_Expression24", type=myDsl_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Let", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body25: BinaryAssociation = BinaryAssociation(
    name="body25",
    ends={
        Property(name="myDsl_Expression27", type=myDsl_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Let26", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right10: BinaryAssociation = BinaryAssociation(
    name="right10",
    ends={
        Property(name="myDsl_Expression12", type=myDsl_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Minus11", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left13: BinaryAssociation = BinaryAssociation(
    name="left13",
    ends={
        Property(name="myDsl_Expression14", type=myDsl_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Mult", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right15: BinaryAssociation = BinaryAssociation(
    name="right15",
    ends={
        Property(name="myDsl_Expression17", type=myDsl_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Mult16", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left18: BinaryAssociation = BinaryAssociation(
    name="left18",
    ends={
        Property(name="myDsl_Expression19", type=myDsl_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Div", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_myDsl_Method_Instance = Generalization(general=Instance, specific=myDsl_Method)
gen_myDsl_MathExp_Instance = Generalization(general=Instance, specific=myDsl_MathExp)
gen_myDsl_Plus_Expression = Generalization(general=Expression, specific=myDsl_Plus)
gen_myDsl_Minus_Expression = Generalization(general=Expression, specific=myDsl_Minus)
gen_myDsl_Var_Expression = Generalization(general=Expression, specific=myDsl_Var)
gen_myDsl_Let_Expression = Generalization(general=Expression, specific=myDsl_Let)
gen_myDsl_Num_Expression = Generalization(general=Expression, specific=myDsl_Num)
gen_myDsl_Mult_Expression = Generalization(general=Expression, specific=myDsl_Mult)
gen_myDsl_Div_Expression = Generalization(general=Expression, specific=myDsl_Div)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Classs, myDsl_Instance, myDsl_Method, Instance, myDsl_Parameter, myDsl_MathExp, myDsl_Expression, myDsl_Plus, Expression, myDsl_Minus, myDsl_Var, myDsl_Let, myDsl_Num, myDsl_Mult, myDsl_Div},
    associations={instances0, params1, exp2, left3, right5, left8, right20, binding23, body25, right10, left13, right15, left18},
    generalizations={gen_myDsl_Method_Instance, gen_myDsl_MathExp_Instance, gen_myDsl_Plus_Expression, gen_myDsl_Minus_Expression, gen_myDsl_Var_Expression, gen_myDsl_Let_Expression, gen_myDsl_Num_Expression, gen_myDsl_Mult_Expression, gen_myDsl_Div_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)