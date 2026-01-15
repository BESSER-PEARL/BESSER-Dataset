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
rankPL_Model = Class(name="rankPL::Model")
rankPL_AbstractDefinition = Class(name="rankPL::AbstractDefinition")
rankPL_Definition = Class(name="rankPL::Definition")
AbstractDefinition = Class(name="AbstractDefinition")
rankPL_Expression = Class(name="rankPL::Expression")
rankPL_DeclaredParameter = Class(name="rankPL::DeclaredParameter")
rankPL_Plus = Class(name="rankPL::Plus")
Expression = Class(name="Expression")
rankPL_Minus = Class(name="rankPL::Minus")
rankPL_Multi = Class(name="rankPL::Multi")
rankPL_Div = Class(name="rankPL::Div")
rankPL_NumberLiteral = Class(name="rankPL::NumberLiteral")
rankPL_FunctionCall = Class(name="rankPL::FunctionCall")

# rankPL_Model class attributes and methods

# rankPL_AbstractDefinition class attributes and methods
rankPL_AbstractDefinition_name: Property = Property(name="name", type=StringType)
rankPL_AbstractDefinition.attributes={rankPL_AbstractDefinition_name}

# rankPL_Definition class attributes and methods

# AbstractDefinition class attributes and methods

# rankPL_Expression class attributes and methods

# rankPL_DeclaredParameter class attributes and methods

# rankPL_Plus class attributes and methods

# Expression class attributes and methods

# rankPL_Minus class attributes and methods

# rankPL_Multi class attributes and methods

# rankPL_Div class attributes and methods

# rankPL_NumberLiteral class attributes and methods
rankPL_NumberLiteral_value: Property = Property(name="value", type=StringType)
rankPL_NumberLiteral.attributes={rankPL_NumberLiteral_value}

# rankPL_FunctionCall class attributes and methods

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="rankPL_AbstractDefinition", type=rankPL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="rankPL_Model", type=rankPL_AbstractDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr1: BinaryAssociation = BinaryAssociation(
    name="expr1",
    ends={
        Property(name="rankPL_Expression", type=rankPL_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="rankPL_Definition", type=rankPL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left2: BinaryAssociation = BinaryAssociation(
    name="left2",
    ends={
        Property(name="rankPL_Expression3", type=rankPL_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="rankPL_Plus", type=rankPL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right4: BinaryAssociation = BinaryAssociation(
    name="right4",
    ends={
        Property(name="rankPL_Expression6", type=rankPL_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="rankPL_Plus5", type=rankPL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left7: BinaryAssociation = BinaryAssociation(
    name="left7",
    ends={
        Property(name="rankPL_Expression8", type=rankPL_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="rankPL_Minus", type=rankPL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right9: BinaryAssociation = BinaryAssociation(
    name="right9",
    ends={
        Property(name="rankPL_Expression11", type=rankPL_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="rankPL_Minus10", type=rankPL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left12: BinaryAssociation = BinaryAssociation(
    name="left12",
    ends={
        Property(name="rankPL_Expression13", type=rankPL_Multi, multiplicity=Multiplicity(1, 1)),
        Property(name="rankPL_Multi", type=rankPL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
func22: BinaryAssociation = BinaryAssociation(
    name="func22",
    ends={
        Property(name="rankPL_FunctionCall", type=rankPL_AbstractDefinition, multiplicity=Multiplicity(0, 1)),
        Property(name="rankPL_AbstractDefinition23", type=rankPL_FunctionCall, multiplicity=Multiplicity(1, 1))
    }
)
args24: BinaryAssociation = BinaryAssociation(
    name="args24",
    ends={
        Property(name="rankPL_Expression26", type=rankPL_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="rankPL_FunctionCall25", type=rankPL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right14: BinaryAssociation = BinaryAssociation(
    name="right14",
    ends={
        Property(name="rankPL_Expression16", type=rankPL_Multi, multiplicity=Multiplicity(1, 1)),
        Property(name="rankPL_Multi15", type=rankPL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left17: BinaryAssociation = BinaryAssociation(
    name="left17",
    ends={
        Property(name="rankPL_Expression18", type=rankPL_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="rankPL_Div", type=rankPL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right19: BinaryAssociation = BinaryAssociation(
    name="right19",
    ends={
        Property(name="rankPL_Expression21", type=rankPL_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="rankPL_Div20", type=rankPL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_rankPL_Definition_AbstractDefinition = Generalization(general=AbstractDefinition, specific=rankPL_Definition)
gen_rankPL_DeclaredParameter_AbstractDefinition = Generalization(general=AbstractDefinition, specific=rankPL_DeclaredParameter)
gen_rankPL_Plus_Expression = Generalization(general=Expression, specific=rankPL_Plus)
gen_rankPL_Minus_Expression = Generalization(general=Expression, specific=rankPL_Minus)
gen_rankPL_Multi_Expression = Generalization(general=Expression, specific=rankPL_Multi)
gen_rankPL_Div_Expression = Generalization(general=Expression, specific=rankPL_Div)
gen_rankPL_NumberLiteral_Expression = Generalization(general=Expression, specific=rankPL_NumberLiteral)
gen_rankPL_FunctionCall_Expression = Generalization(general=Expression, specific=rankPL_FunctionCall)

# Domain Model
domain_model = DomainModel(
    name="rankPL",
    types={rankPL_Model, rankPL_AbstractDefinition, rankPL_Definition, AbstractDefinition, rankPL_Expression, rankPL_DeclaredParameter, rankPL_Plus, Expression, rankPL_Minus, rankPL_Multi, rankPL_Div, rankPL_NumberLiteral, rankPL_FunctionCall},
    associations={greetings0, expr1, left2, right4, left7, right9, left12, func22, args24, right14, left17, right19},
    generalizations={gen_rankPL_Definition_AbstractDefinition, gen_rankPL_DeclaredParameter_AbstractDefinition, gen_rankPL_Plus_Expression, gen_rankPL_Minus_Expression, gen_rankPL_Multi_Expression, gen_rankPL_Div_Expression, gen_rankPL_NumberLiteral_Expression, gen_rankPL_FunctionCall_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)