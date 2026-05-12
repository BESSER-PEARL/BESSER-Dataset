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
d3ql_Query = Class(name="d3ql_Query")
d3ql_FromStatement = Class(name="d3ql_FromStatement")
d3ql_SelectStatement = Class(name="d3ql_SelectStatement")
d3ql_AggregateRoot = Class(name="d3ql_AggregateRoot")
d3ql_Named = Class(name="d3ql_Named")
Named = Class(name="Named")
d3ql_Alias = Class(name="d3ql_Alias")
d3ql_SelectExpression = Class(name="d3ql_SelectExpression")
d3ql_EObject = Class(name="d3ql_EObject")
d3ql_PathExpression = Class(name="d3ql_PathExpression")
d3ql_PathElement = Class(name="d3ql_PathElement")
d3ql_FunctionCall = Class(name="d3ql_FunctionCall")
d3ql_FunctionArgument = Class(name="d3ql_FunctionArgument")
d3ql_Literal = Class(name="d3ql_Literal")
d3ql_IntegerLiteral = Class(name="d3ql_IntegerLiteral")
Literal = Class(name="Literal")
d3ql_StringLiteral = Class(name="d3ql_StringLiteral")
d3ql_BooleanLiteral = Class(name="d3ql_BooleanLiteral")

# d3ql_Query class attributes and methods

# d3ql_FromStatement class attributes and methods

# d3ql_SelectStatement class attributes and methods

# d3ql_AggregateRoot class attributes and methods

# d3ql_Named class attributes and methods
d3ql_Named_name: Property = Property(name="name", type=StringType)
d3ql_Named.attributes={d3ql_Named_name}

# Named class attributes and methods

# d3ql_Alias class attributes and methods

# d3ql_SelectExpression class attributes and methods

# d3ql_EObject class attributes and methods

# d3ql_PathExpression class attributes and methods

# d3ql_PathElement class attributes and methods
d3ql_PathElement_name: Property = Property(name="name", type=StringType)
d3ql_PathElement.attributes={d3ql_PathElement_name}

# d3ql_FunctionCall class attributes and methods
d3ql_FunctionCall_function: Property = Property(name="function", type=StringType)
d3ql_FunctionCall.attributes={d3ql_FunctionCall_function}

# d3ql_FunctionArgument class attributes and methods

# d3ql_Literal class attributes and methods

# d3ql_IntegerLiteral class attributes and methods
d3ql_IntegerLiteral_value: Property = Property(name="value", type=IntegerType)
d3ql_IntegerLiteral.attributes={d3ql_IntegerLiteral_value}

# Literal class attributes and methods

# d3ql_StringLiteral class attributes and methods
d3ql_StringLiteral_value: Property = Property(name="value", type=StringType)
d3ql_StringLiteral.attributes={d3ql_StringLiteral_value}

# d3ql_BooleanLiteral class attributes and methods
d3ql_BooleanLiteral_value: Property = Property(name="value", type=StringType)
d3ql_BooleanLiteral.attributes={d3ql_BooleanLiteral_value}

# Relationships
fromStatement0: BinaryAssociation = BinaryAssociation(
    name="fromStatement0",
    ends={
        Property(name="d3ql_FromStatement", type=d3ql_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="d3ql_Query", type=d3ql_FromStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectStatement1: BinaryAssociation = BinaryAssociation(
    name="selectStatement1",
    ends={
        Property(name="d3ql_SelectStatement", type=d3ql_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="d3ql_Query2", type=d3ql_SelectStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggregates3: BinaryAssociation = BinaryAssociation(
    name="aggregates3",
    ends={
        Property(name="d3ql_AggregateRoot", type=d3ql_FromStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="d3ql_FromStatement4", type=d3ql_AggregateRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alias5: BinaryAssociation = BinaryAssociation(
    name="alias5",
    ends={
        Property(name="d3ql_Alias", type=d3ql_AggregateRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="d3ql_AggregateRoot6", type=d3ql_Alias, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions7: BinaryAssociation = BinaryAssociation(
    name="expressions7",
    ends={
        Property(name="d3ql_SelectExpression", type=d3ql_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="d3ql_SelectStatement8", type=d3ql_SelectExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression9: BinaryAssociation = BinaryAssociation(
    name="expression9",
    ends={
        Property(name="d3ql_EObject", type=d3ql_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="d3ql_SelectExpression10", type=d3ql_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alias11: BinaryAssociation = BinaryAssociation(
    name="alias11",
    ends={
        Property(name="d3ql_Alias13", type=d3ql_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="d3ql_SelectExpression12", type=d3ql_Alias, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
head14: BinaryAssociation = BinaryAssociation(
    name="head14",
    ends={
        Property(name="d3ql_Named", type=d3ql_PathExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="d3ql_PathExpression", type=d3ql_Named, multiplicity=Multiplicity(0, 1))
    }
)
tail15: BinaryAssociation = BinaryAssociation(
    name="tail15",
    ends={
        Property(name="d3ql_PathElement", type=d3ql_PathExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="d3ql_PathExpression16", type=d3ql_PathElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments17: BinaryAssociation = BinaryAssociation(
    name="arguments17",
    ends={
        Property(name="d3ql_FunctionArgument", type=d3ql_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="d3ql_FunctionCall", type=d3ql_FunctionArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value18: BinaryAssociation = BinaryAssociation(
    name="value18",
    ends={
        Property(name="d3ql_EObject20", type=d3ql_FunctionArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="d3ql_FunctionArgument19", type=d3ql_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_d3ql_AggregateRoot_Named = Generalization(general=Named, specific=d3ql_AggregateRoot)
gen_d3ql_Alias_Named = Generalization(general=Named, specific=d3ql_Alias)
gen_d3ql_IntegerLiteral_Literal = Generalization(general=Literal, specific=d3ql_IntegerLiteral)
gen_d3ql_StringLiteral_Literal = Generalization(general=Literal, specific=d3ql_StringLiteral)
gen_d3ql_BooleanLiteral_Literal = Generalization(general=Literal, specific=d3ql_BooleanLiteral)

# Domain Model
domain_model = DomainModel(
    name="d3ql",
    types={d3ql_Query, d3ql_FromStatement, d3ql_SelectStatement, d3ql_AggregateRoot, d3ql_Named, Named, d3ql_Alias, d3ql_SelectExpression, d3ql_EObject, d3ql_PathExpression, d3ql_PathElement, d3ql_FunctionCall, d3ql_FunctionArgument, d3ql_Literal, d3ql_IntegerLiteral, Literal, d3ql_StringLiteral, d3ql_BooleanLiteral},
    associations={fromStatement0, selectStatement1, aggregates3, alias5, expressions7, expression9, alias11, head14, tail15, arguments17, value18},
    generalizations={gen_d3ql_AggregateRoot_Named, gen_d3ql_Alias_Named, gen_d3ql_IntegerLiteral_Literal, gen_d3ql_StringLiteral_Literal, gen_d3ql_BooleanLiteral_Literal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)