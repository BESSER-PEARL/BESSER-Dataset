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
fl_Exp = Class(name="fl::Exp", is_abstract=True)
fl_LiteralExp = Class(name="fl::LiteralExp")
Exp = Class(name="Exp")
fl_Program = Class(name="fl::Program")
fl_Function = Class(name="fl::Function")
fl_Argument = Class(name="fl::Argument")
fl_ArgumentExp = Class(name="fl::ArgumentExp")
fl_IfThenElseExp = Class(name="fl::IfThenElseExp")
fl_ApplyExp = Class(name="fl::ApplyExp")
fl_BinaryExp = Class(name="fl::BinaryExp", is_abstract=True)
fl_PlusExp = Class(name="fl::PlusExp")
BinaryExp = Class(name="BinaryExp")
fl_MinusExp = Class(name="fl::MinusExp")
fl_EqualExp = Class(name="fl::EqualExp")

# fl_Exp class attributes and methods

# fl_LiteralExp class attributes and methods
fl_LiteralExp_value: Property = Property(name="value", type=IntegerType)
fl_LiteralExp.attributes={fl_LiteralExp_value}

# Exp class attributes and methods

# fl_Program class attributes and methods

# fl_Function class attributes and methods
fl_Function_name: Property = Property(name="name", type=StringType)
fl_Function.attributes={fl_Function_name}

# fl_Argument class attributes and methods
fl_Argument_name: Property = Property(name="name", type=StringType)
fl_Argument.attributes={fl_Argument_name}

# fl_ArgumentExp class attributes and methods

# fl_IfThenElseExp class attributes and methods

# fl_ApplyExp class attributes and methods

# fl_BinaryExp class attributes and methods

# fl_PlusExp class attributes and methods

# BinaryExp class attributes and methods

# fl_MinusExp class attributes and methods

# fl_EqualExp class attributes and methods

# Relationships
definition3: BinaryAssociation = BinaryAssociation(
    name="definition3",
    ends={
        Property(name="fl_Exp", type=fl_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_Function4", type=fl_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function0: BinaryAssociation = BinaryAssociation(
    name="function0",
    ends={
        Property(name="fl_Function", type=fl_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_Program", type=fl_Function, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
argument1: BinaryAssociation = BinaryAssociation(
    name="argument1",
    ends={
        Property(name="fl_Argument", type=fl_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_Function2", type=fl_Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument5: BinaryAssociation = BinaryAssociation(
    name="argument5",
    ends={
        Property(name="fl_Argument6", type=fl_ArgumentExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_ArgumentExp", type=fl_Argument, multiplicity=Multiplicity(1, 1))
    }
)
if7: BinaryAssociation = BinaryAssociation(
    name="if7",
    ends={
        Property(name="fl_Exp8", type=fl_IfThenElseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_IfThenElseExp", type=fl_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then9: BinaryAssociation = BinaryAssociation(
    name="then9",
    ends={
        Property(name="fl_Exp11", type=fl_IfThenElseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_IfThenElseExp10", type=fl_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else12: BinaryAssociation = BinaryAssociation(
    name="else12",
    ends={
        Property(name="fl_Exp14", type=fl_IfThenElseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_IfThenElseExp13", type=fl_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function15: BinaryAssociation = BinaryAssociation(
    name="function15",
    ends={
        Property(name="fl_Function16", type=fl_ApplyExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_ApplyExp", type=fl_Function, multiplicity=Multiplicity(1, 1))
    }
)
argument17: BinaryAssociation = BinaryAssociation(
    name="argument17",
    ends={
        Property(name="fl_Exp19", type=fl_ApplyExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_ApplyExp18", type=fl_Exp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left20: BinaryAssociation = BinaryAssociation(
    name="left20",
    ends={
        Property(name="fl_Exp21", type=fl_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_BinaryExp", type=fl_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right22: BinaryAssociation = BinaryAssociation(
    name="right22",
    ends={
        Property(name="fl_Exp24", type=fl_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_BinaryExp23", type=fl_Exp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_fl_LiteralExp_Exp = Generalization(general=Exp, specific=fl_LiteralExp)
gen_fl_ArgumentExp_Exp = Generalization(general=Exp, specific=fl_ArgumentExp)
gen_fl_IfThenElseExp_Exp = Generalization(general=Exp, specific=fl_IfThenElseExp)
gen_fl_ApplyExp_Exp = Generalization(general=Exp, specific=fl_ApplyExp)
gen_fl_BinaryExp_Exp = Generalization(general=Exp, specific=fl_BinaryExp)
gen_fl_PlusExp_BinaryExp = Generalization(general=BinaryExp, specific=fl_PlusExp)
gen_fl_MinusExp_BinaryExp = Generalization(general=BinaryExp, specific=fl_MinusExp)
gen_fl_EqualExp_BinaryExp = Generalization(general=BinaryExp, specific=fl_EqualExp)

# Domain Model
domain_model = DomainModel(
    name="fl",
    types={fl_Exp, fl_LiteralExp, Exp, fl_Program, fl_Function, fl_Argument, fl_ArgumentExp, fl_IfThenElseExp, fl_ApplyExp, fl_BinaryExp, fl_PlusExp, BinaryExp, fl_MinusExp, fl_EqualExp},
    associations={definition3, function0, argument1, argument5, if7, then9, else12, function15, argument17, left20, right22},
    generalizations={gen_fl_LiteralExp_Exp, gen_fl_ArgumentExp_Exp, gen_fl_IfThenElseExp_Exp, gen_fl_ApplyExp_Exp, gen_fl_BinaryExp_Exp, gen_fl_PlusExp_BinaryExp, gen_fl_MinusExp_BinaryExp, gen_fl_EqualExp_BinaryExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)