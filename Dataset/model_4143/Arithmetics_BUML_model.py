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
arithmetics_Import = Class(name="arithmetics::Import")
arithmetics_Statement = Class(name="arithmetics::Statement")
arithmetics_Definition = Class(name="arithmetics::Definition")
Statement = Class(name="Statement")
AbstractDefinition = Class(name="AbstractDefinition")
arithmetics_DeclaredParameter = Class(name="arithmetics::DeclaredParameter")
arithmetics_Expression = Class(name="arithmetics::Expression")
arithmetics_AbstractDefinition = Class(name="arithmetics::AbstractDefinition")
arithmetics_Evaluation = Class(name="arithmetics::Evaluation")
arithmetics_Plus = Class(name="arithmetics::Plus")
arithmetics_Module = Class(name="arithmetics::Module")
arithmetics_NumberLiteral = Class(name="arithmetics::NumberLiteral")
arithmetics_FunctionCall = Class(name="arithmetics::FunctionCall")
Expression = Class(name="Expression")
arithmetics_Minus = Class(name="arithmetics::Minus")
arithmetics_Multi = Class(name="arithmetics::Multi")
arithmetics_Div = Class(name="arithmetics::Div")

# arithmetics_Import class attributes and methods
arithmetics_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
arithmetics_Import.attributes={arithmetics_Import_importedNamespace}

# arithmetics_Statement class attributes and methods

# arithmetics_Definition class attributes and methods

# Statement class attributes and methods

# AbstractDefinition class attributes and methods

# arithmetics_DeclaredParameter class attributes and methods

# arithmetics_Expression class attributes and methods

# arithmetics_AbstractDefinition class attributes and methods
arithmetics_AbstractDefinition_name: Property = Property(name="name", type=StringType)
arithmetics_AbstractDefinition.attributes={arithmetics_AbstractDefinition_name}

# arithmetics_Evaluation class attributes and methods

# arithmetics_Plus class attributes and methods

# arithmetics_Module class attributes and methods
arithmetics_Module_name: Property = Property(name="name", type=StringType)
arithmetics_Module.attributes={arithmetics_Module_name}

# arithmetics_NumberLiteral class attributes and methods
arithmetics_NumberLiteral_value: Property = Property(name="value", type=StringType)
arithmetics_NumberLiteral.attributes={arithmetics_NumberLiteral_value}

# arithmetics_FunctionCall class attributes and methods

# Expression class attributes and methods

# arithmetics_Minus class attributes and methods

# arithmetics_Multi class attributes and methods

# arithmetics_Div class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="arithmetics_Import", type=arithmetics_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Module", type=arithmetics_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements1: BinaryAssociation = BinaryAssociation(
    name="statements1",
    ends={
        Property(name="arithmetics_Statement", type=arithmetics_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Module2", type=arithmetics_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args3: BinaryAssociation = BinaryAssociation(
    name="args3",
    ends={
        Property(name="arithmetics_DeclaredParameter", type=arithmetics_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Definition", type=arithmetics_DeclaredParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr4: BinaryAssociation = BinaryAssociation(
    name="expr4",
    ends={
        Property(name="arithmetics_Expression", type=arithmetics_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Definition5", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression6: BinaryAssociation = BinaryAssociation(
    name="expression6",
    ends={
        Property(name="arithmetics_Expression7", type=arithmetics_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Evaluation", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right25: BinaryAssociation = BinaryAssociation(
    name="right25",
    ends={
        Property(name="arithmetics_Expression27", type=arithmetics_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Div26", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
func28: BinaryAssociation = BinaryAssociation(
    name="func28",
    ends={
        Property(name="arithmetics_AbstractDefinition", type=arithmetics_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_FunctionCall", type=arithmetics_AbstractDefinition, multiplicity=Multiplicity(0, 1))
    }
)
args29: BinaryAssociation = BinaryAssociation(
    name="args29",
    ends={
        Property(name="arithmetics_Expression31", type=arithmetics_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_FunctionCall30", type=arithmetics_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left8: BinaryAssociation = BinaryAssociation(
    name="left8",
    ends={
        Property(name="arithmetics_Expression9", type=arithmetics_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Plus", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right10: BinaryAssociation = BinaryAssociation(
    name="right10",
    ends={
        Property(name="arithmetics_Expression12", type=arithmetics_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Plus11", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left13: BinaryAssociation = BinaryAssociation(
    name="left13",
    ends={
        Property(name="arithmetics_Expression14", type=arithmetics_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Minus", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right15: BinaryAssociation = BinaryAssociation(
    name="right15",
    ends={
        Property(name="arithmetics_Expression17", type=arithmetics_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Minus16", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left18: BinaryAssociation = BinaryAssociation(
    name="left18",
    ends={
        Property(name="arithmetics_Expression19", type=arithmetics_Multi, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Multi", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right20: BinaryAssociation = BinaryAssociation(
    name="right20",
    ends={
        Property(name="arithmetics_Expression22", type=arithmetics_Multi, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Multi21", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left23: BinaryAssociation = BinaryAssociation(
    name="left23",
    ends={
        Property(name="arithmetics_Expression24", type=arithmetics_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetics_Div", type=arithmetics_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_arithmetics_Definition_Statement = Generalization(general=Statement, specific=arithmetics_Definition)
gen_arithmetics_Definition_AbstractDefinition = Generalization(general=AbstractDefinition, specific=arithmetics_Definition)
gen_arithmetics_DeclaredParameter_AbstractDefinition = Generalization(general=AbstractDefinition, specific=arithmetics_DeclaredParameter)
gen_arithmetics_Evaluation_Statement = Generalization(general=Statement, specific=arithmetics_Evaluation)
gen_arithmetics_NumberLiteral_Expression = Generalization(general=Expression, specific=arithmetics_NumberLiteral)
gen_arithmetics_FunctionCall_Expression = Generalization(general=Expression, specific=arithmetics_FunctionCall)
gen_arithmetics_Plus_Expression = Generalization(general=Expression, specific=arithmetics_Plus)
gen_arithmetics_Minus_Expression = Generalization(general=Expression, specific=arithmetics_Minus)
gen_arithmetics_Multi_Expression = Generalization(general=Expression, specific=arithmetics_Multi)
gen_arithmetics_Div_Expression = Generalization(general=Expression, specific=arithmetics_Div)

# Domain Model
domain_model = DomainModel(
    name="arithmetics",
    types={arithmetics_Import, arithmetics_Statement, arithmetics_Definition, Statement, AbstractDefinition, arithmetics_DeclaredParameter, arithmetics_Expression, arithmetics_AbstractDefinition, arithmetics_Evaluation, arithmetics_Plus, arithmetics_Module, arithmetics_NumberLiteral, arithmetics_FunctionCall, Expression, arithmetics_Minus, arithmetics_Multi, arithmetics_Div},
    associations={imports0, statements1, args3, expr4, expression6, right25, func28, args29, left8, right10, left13, right15, left18, right20, left23},
    generalizations={gen_arithmetics_Definition_Statement, gen_arithmetics_Definition_AbstractDefinition, gen_arithmetics_DeclaredParameter_AbstractDefinition, gen_arithmetics_Evaluation_Statement, gen_arithmetics_NumberLiteral_Expression, gen_arithmetics_FunctionCall_Expression, gen_arithmetics_Plus_Expression, gen_arithmetics_Minus_Expression, gen_arithmetics_Multi_Expression, gen_arithmetics_Div_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)