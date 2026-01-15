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

# Enumerations
Ops: Enumeration = Enumeration(
    name="Ops",
    literals={
            EnumerationLiteral(name="Equal"),
			EnumerationLiteral(name="Plus"),
			EnumerationLiteral(name="Minus")
    }
)

# Classes
fl_Argument = Class(name="fl::Argument")
fl_Binary = Class(name="fl::Binary")
fl_Apply = Class(name="fl::Apply")
Expr = Class(name="Expr")
fl_Expr = Class(name="fl::Expr", is_abstract=True)
fl_ProgramType = Class(name="fl::ProgramType")
fl_Function = Class(name="fl::Function")
fl_DocumentRoot = Class(name="fl::DocumentRoot")
fl_EStringToStringMapEntry = Class(name="fl::EStringToStringMapEntry")
fl_IfThenElse = Class(name="fl::IfThenElse")
fl_Literal = Class(name="fl::Literal")

# fl_Argument class attributes and methods
fl_Argument_name: Property = Property(name="name", type=StringType)
fl_Argument.attributes={fl_Argument_name}

# fl_Binary class attributes and methods
fl_Binary_ops: Property = Property(name="ops", type=StringType)
fl_Binary.attributes={fl_Binary_ops}

# fl_Apply class attributes and methods
fl_Apply_name: Property = Property(name="name", type=StringType)
fl_Apply.attributes={fl_Apply_name}

# Expr class attributes and methods

# fl_Expr class attributes and methods

# fl_ProgramType class attributes and methods

# fl_Function class attributes and methods
fl_Function_name: Property = Property(name="name", type=StringType)
fl_Function_arg: Property = Property(name="arg", type=StringType)
fl_Function.attributes={fl_Function_arg, fl_Function_name}

# fl_DocumentRoot class attributes and methods
fl_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
fl_DocumentRoot.attributes={fl_DocumentRoot_mixed}

# fl_EStringToStringMapEntry class attributes and methods

# fl_IfThenElse class attributes and methods

# fl_Literal class attributes and methods
fl_Literal_info: Property = Property(name="info", type=StringType)
fl_Literal.attributes={fl_Literal_info}

# Relationships
arg0: BinaryAssociation = BinaryAssociation(
    name="arg0",
    ends={
        Property(name="fl_Expr", type=fl_Apply, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_Apply", type=fl_Expr, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
program13: BinaryAssociation = BinaryAssociation(
    name="program13",
    ends={
        Property(name="fl_ProgramType", type=fl_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_DocumentRoot14", type=fl_ProgramType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="fl_Expr2", type=fl_Binary, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_Binary", type=fl_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right3: BinaryAssociation = BinaryAssociation(
    name="right3",
    ends={
        Property(name="fl_Expr5", type=fl_Binary, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_Binary4", type=fl_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
xMLNSPrefixMap6: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap6",
    ends={
        Property(name="fl_EStringToStringMapEntry", type=fl_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_DocumentRoot", type=fl_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation7: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation7",
    ends={
        Property(name="fl_EStringToStringMapEntry9", type=fl_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_DocumentRoot8", type=fl_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragment10: BinaryAssociation = BinaryAssociation(
    name="fragment10",
    ends={
        Property(name="fl_Expr12", type=fl_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_DocumentRoot11", type=fl_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function25: BinaryAssociation = BinaryAssociation(
    name="function25",
    ends={
        Property(name="fl_Function27", type=fl_ProgramType, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_ProgramType26", type=fl_Function, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rhs15: BinaryAssociation = BinaryAssociation(
    name="rhs15",
    ends={
        Property(name="fl_Expr16", type=fl_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_Function", type=fl_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifExpr17: BinaryAssociation = BinaryAssociation(
    name="ifExpr17",
    ends={
        Property(name="fl_Expr18", type=fl_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_IfThenElse", type=fl_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpr19: BinaryAssociation = BinaryAssociation(
    name="thenExpr19",
    ends={
        Property(name="fl_Expr21", type=fl_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_IfThenElse20", type=fl_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpr22: BinaryAssociation = BinaryAssociation(
    name="elseExpr22",
    ends={
        Property(name="fl_Expr24", type=fl_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="fl_IfThenElse23", type=fl_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_fl_Argument_Expr = Generalization(general=Expr, specific=fl_Argument)
gen_fl_Binary_Expr = Generalization(general=Expr, specific=fl_Binary)
gen_fl_Apply_Expr = Generalization(general=Expr, specific=fl_Apply)
gen_fl_IfThenElse_Expr = Generalization(general=Expr, specific=fl_IfThenElse)
gen_fl_Literal_Expr = Generalization(general=Expr, specific=fl_Literal)

# Domain Model
domain_model = DomainModel(
    name="fl",
    types={fl_Argument, fl_Binary, fl_Apply, Expr, fl_Expr, fl_ProgramType, fl_Function, fl_DocumentRoot, fl_EStringToStringMapEntry, fl_IfThenElse, fl_Literal, Ops},
    associations={arg0, program13, left1, right3, xMLNSPrefixMap6, xSISchemaLocation7, fragment10, function25, rhs15, ifExpr17, thenExpr19, elseExpr22},
    generalizations={gen_fl_Argument_Expr, gen_fl_Binary_Expr, gen_fl_Apply_Expr, gen_fl_IfThenElse_Expr, gen_fl_Literal_Expr},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)