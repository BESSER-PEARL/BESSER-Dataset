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
assignment2_ExpMinusPlus = Class(name="assignment2::ExpMinusPlus")
assignment2_ExpMultDiv = Class(name="assignment2::ExpMultDiv")
ExpMinusPlus = Class(name="ExpMinusPlus")
assignment2_EObject = Class(name="assignment2::EObject")
assignment2_ExpPM = Class(name="assignment2::ExpPM")
assignment2_ExpMD = Class(name="assignment2::ExpMD")
assignment2_Primary = Class(name="assignment2::Primary")
ExpMultDiv = Class(name="ExpMultDiv")
assignment2_Parenthesis = Class(name="assignment2::Parenthesis")
Primary = Class(name="Primary")
assignment2_Number = Class(name="assignment2::Number")
assignment2_Exp = Class(name="assignment2::Exp")
assignment2_Plus = Class(name="assignment2::Plus")
ExpPM = Class(name="ExpPM")
assignment2_Model = Class(name="assignment2::Model")
assignment2_MathExp = Class(name="assignment2::MathExp")
assignment2_Minus = Class(name="assignment2::Minus")
assignment2_Mult = Class(name="assignment2::Mult")
ExpMD = Class(name="ExpMD")
assignment2_Div = Class(name="assignment2::Div")

# assignment2_ExpMinusPlus class attributes and methods

# assignment2_ExpMultDiv class attributes and methods

# ExpMinusPlus class attributes and methods

# assignment2_EObject class attributes and methods

# assignment2_ExpPM class attributes and methods

# assignment2_ExpMD class attributes and methods

# assignment2_Primary class attributes and methods

# ExpMultDiv class attributes and methods

# assignment2_Parenthesis class attributes and methods

# Primary class attributes and methods

# assignment2_Number class attributes and methods
assignment2_Number_value: Property = Property(name="value", type=IntegerType)
assignment2_Number.attributes={assignment2_Number_value}

# assignment2_Exp class attributes and methods

# assignment2_Plus class attributes and methods

# ExpPM class attributes and methods

# assignment2_Model class attributes and methods

# assignment2_MathExp class attributes and methods

# assignment2_Minus class attributes and methods

# assignment2_Mult class attributes and methods

# ExpMD class attributes and methods

# assignment2_Div class attributes and methods

# Relationships
exp1: BinaryAssociation = BinaryAssociation(
    name="exp1",
    ends={
        Property(name="assignment2_ExpMinusPlus", type=assignment2_MathExp, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment2_MathExp2", type=assignment2_ExpMinusPlus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left4: BinaryAssociation = BinaryAssociation(
    name="left4",
    ends={
        Property(name="assignment2_ExpMinusPlus5", type=assignment2_ExpMinusPlus, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment2_ExpMinusPlus3", type=assignment2_ExpMinusPlus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator6: BinaryAssociation = BinaryAssociation(
    name="operator6",
    ends={
        Property(name="assignment2_EObject", type=assignment2_ExpMinusPlus, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment2_ExpMinusPlus7", type=assignment2_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right8: BinaryAssociation = BinaryAssociation(
    name="right8",
    ends={
        Property(name="assignment2_ExpMultDiv", type=assignment2_ExpMinusPlus, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment2_ExpMinusPlus9", type=assignment2_ExpMultDiv, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp10: BinaryAssociation = BinaryAssociation(
    name="exp10",
    ends={
        Property(name="assignment2_ExpMinusPlus11", type=assignment2_Parenthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment2_Parenthesis", type=assignment2_ExpMinusPlus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
math0: BinaryAssociation = BinaryAssociation(
    name="math0",
    ends={
        Property(name="assignment2_MathExp", type=assignment2_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment2_Model", type=assignment2_MathExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_assignment2_ExpMultDiv_ExpMinusPlus = Generalization(general=ExpMinusPlus, specific=assignment2_ExpMultDiv)
gen_assignment2_Primary_ExpMultDiv = Generalization(general=ExpMultDiv, specific=assignment2_Primary)
gen_assignment2_Parenthesis_Primary = Generalization(general=Primary, specific=assignment2_Parenthesis)
gen_assignment2_Number_Primary = Generalization(general=Primary, specific=assignment2_Number)
gen_assignment2_Exp_ExpMultDiv = Generalization(general=ExpMultDiv, specific=assignment2_Exp)
gen_assignment2_Plus_ExpPM = Generalization(general=ExpPM, specific=assignment2_Plus)
gen_assignment2_Minus_ExpPM = Generalization(general=ExpPM, specific=assignment2_Minus)
gen_assignment2_Mult_ExpMD = Generalization(general=ExpMD, specific=assignment2_Mult)
gen_assignment2_Div_ExpMD = Generalization(general=ExpMD, specific=assignment2_Div)

# Domain Model
domain_model = DomainModel(
    name="assignment2",
    types={assignment2_ExpMinusPlus, assignment2_ExpMultDiv, ExpMinusPlus, assignment2_EObject, assignment2_ExpPM, assignment2_ExpMD, assignment2_Primary, ExpMultDiv, assignment2_Parenthesis, Primary, assignment2_Number, assignment2_Exp, assignment2_Plus, ExpPM, assignment2_Model, assignment2_MathExp, assignment2_Minus, assignment2_Mult, ExpMD, assignment2_Div},
    associations={exp1, left4, operator6, right8, exp10, math0},
    generalizations={gen_assignment2_ExpMultDiv_ExpMinusPlus, gen_assignment2_Primary_ExpMultDiv, gen_assignment2_Parenthesis_Primary, gen_assignment2_Number_Primary, gen_assignment2_Exp_ExpMultDiv, gen_assignment2_Plus_ExpPM, gen_assignment2_Minus_ExpPM, gen_assignment2_Mult_ExpMD, gen_assignment2_Div_ExpMD},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)