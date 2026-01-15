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
myMath_MathExp = Class(name="myMath::MathExp")
myMath_Expression = Class(name="myMath::Expression")
myMath_Add = Class(name="myMath::Add")
Expression = Class(name="Expression")
myMath_Sub = Class(name="myMath::Sub")
myMath_Mult = Class(name="myMath::Mult")
myMath_Div = Class(name="myMath::Div")
myMath_Num = Class(name="myMath::Num")

# myMath_MathExp class attributes and methods

# myMath_Expression class attributes and methods

# myMath_Add class attributes and methods

# Expression class attributes and methods

# myMath_Sub class attributes and methods

# myMath_Mult class attributes and methods

# myMath_Div class attributes and methods

# myMath_Num class attributes and methods
myMath_Num_value: Property = Property(name="value", type=IntegerType)
myMath_Num.attributes={myMath_Num_value}

# Relationships
exp0: BinaryAssociation = BinaryAssociation(
    name="exp0",
    ends={
        Property(name="myMath_Expression", type=myMath_MathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="myMath_MathExp", type=myMath_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="myMath_Expression2", type=myMath_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="myMath_Add", type=myMath_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right3: BinaryAssociation = BinaryAssociation(
    name="right3",
    ends={
        Property(name="myMath_Expression5", type=myMath_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="myMath_Add4", type=myMath_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left6: BinaryAssociation = BinaryAssociation(
    name="left6",
    ends={
        Property(name="myMath_Expression7", type=myMath_Sub, multiplicity=Multiplicity(1, 1)),
        Property(name="myMath_Sub", type=myMath_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right8: BinaryAssociation = BinaryAssociation(
    name="right8",
    ends={
        Property(name="myMath_Expression10", type=myMath_Sub, multiplicity=Multiplicity(1, 1)),
        Property(name="myMath_Sub9", type=myMath_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left11: BinaryAssociation = BinaryAssociation(
    name="left11",
    ends={
        Property(name="myMath_Expression12", type=myMath_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="myMath_Mult", type=myMath_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right13: BinaryAssociation = BinaryAssociation(
    name="right13",
    ends={
        Property(name="myMath_Expression15", type=myMath_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="myMath_Mult14", type=myMath_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left16: BinaryAssociation = BinaryAssociation(
    name="left16",
    ends={
        Property(name="myMath_Expression17", type=myMath_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="myMath_Div", type=myMath_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right18: BinaryAssociation = BinaryAssociation(
    name="right18",
    ends={
        Property(name="myMath_Expression20", type=myMath_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="myMath_Div19", type=myMath_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_myMath_Add_Expression = Generalization(general=Expression, specific=myMath_Add)
gen_myMath_Sub_Expression = Generalization(general=Expression, specific=myMath_Sub)
gen_myMath_Mult_Expression = Generalization(general=Expression, specific=myMath_Mult)
gen_myMath_Div_Expression = Generalization(general=Expression, specific=myMath_Div)
gen_myMath_Num_Expression = Generalization(general=Expression, specific=myMath_Num)

# Domain Model
domain_model = DomainModel(
    name="myMath",
    types={myMath_MathExp, myMath_Expression, myMath_Add, Expression, myMath_Sub, myMath_Mult, myMath_Div, myMath_Num},
    associations={exp0, left1, right3, left6, right8, left11, right13, left16, right18},
    generalizations={gen_myMath_Add_Expression, gen_myMath_Sub_Expression, gen_myMath_Mult_Expression, gen_myMath_Div_Expression, gen_myMath_Num_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)