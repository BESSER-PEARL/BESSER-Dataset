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
B_SET = Class(name="B::SET")
B_Operation = Class(name="B::Operation")
B_Predicate = Class(name="B::Predicate")
B_Variable = Class(name="B::Variable")
B_Action = Class(name="B::Action")
B_Expression = Class(name="B::Expression")
B_VariableList = Class(name="B::VariableList")
B_Machine = Class(name="B::Machine")
B_If = Class(name="B::If")
B_Skip = Class(name="B::Skip")
B_Begin = Class(name="B::Begin")
Expression = Class(name="Expression")
B_Any = Class(name="B::Any")

# B_SET class attributes and methods
B_SET_name: Property = Property(name="name", type=StringType)
B_SET.attributes={B_SET_name}

# B_Operation class attributes and methods
B_Operation_name: Property = Property(name="name", type=StringType)
B_Operation.attributes={B_Operation_name}

# B_Predicate class attributes and methods

# B_Variable class attributes and methods
B_Variable_name: Property = Property(name="name", type=StringType)
B_Variable.attributes={B_Variable_name}

# B_Action class attributes and methods

# B_Expression class attributes and methods
B_Expression_expression: Property = Property(name="expression", type=StringType)
B_Expression.attributes={B_Expression_expression}

# B_VariableList class attributes and methods
B_VariableList_size: Property = Property(name="size", type=StringType)
B_VariableList.attributes={B_VariableList_size}

# B_Machine class attributes and methods
B_Machine_name: Property = Property(name="name", type=StringType)
B_Machine.attributes={B_Machine_name}

# B_If class attributes and methods

# B_Skip class attributes and methods

# B_Begin class attributes and methods

# Expression class attributes and methods

# B_Any class attributes and methods

# Relationships
refines1: BinaryAssociation = BinaryAssociation(
    name="refines1",
    ends={
        Property(name="B_Machine", type=B_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Machine0", type=B_Machine, multiplicity=Multiplicity(0, 1))
    }
)
sets2: BinaryAssociation = BinaryAssociation(
    name="sets2",
    ends={
        Property(name="B_SET", type=B_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Machine3", type=B_SET, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations4: BinaryAssociation = BinaryAssociation(
    name="operations4",
    ends={
        Property(name="B_Operation", type=B_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Machine5", type=B_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invariants6: BinaryAssociation = BinaryAssociation(
    name="invariants6",
    ends={
        Property(name="B_Predicate", type=B_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Machine7", type=B_Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables8: BinaryAssociation = BinaryAssociation(
    name="variables8",
    ends={
        Property(name="B_Variable", type=B_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Machine9", type=B_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialisations10: BinaryAssociation = BinaryAssociation(
    name="initialisations10",
    ends={
        Property(name="B_Action", type=B_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Machine11", type=B_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements12: BinaryAssociation = BinaryAssociation(
    name="statements12",
    ends={
        Property(name="B_Expression", type=B_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Operation13", type=B_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inputs14: BinaryAssociation = BinaryAssociation(
    name="inputs14",
    ends={
        Property(name="B_VariableList", type=B_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Operation15", type=B_VariableList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
var_conditions36: BinaryAssociation = BinaryAssociation(
    name="var_conditions36",
    ends={
        Property(name="B_Predicate38", type=B_Any, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Any37", type=B_Predicate, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
statements39: BinaryAssociation = BinaryAssociation(
    name="statements39",
    ends={
        Property(name="B_Expression41", type=B_Any, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Any40", type=B_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
true_statements42: BinaryAssociation = BinaryAssociation(
    name="true_statements42",
    ends={
        Property(name="B_Expression43", type=B_If, multiplicity=Multiplicity(1, 1)),
        Property(name="B_If", type=B_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
false_statements44: BinaryAssociation = BinaryAssociation(
    name="false_statements44",
    ends={
        Property(name="B_Expression46", type=B_If, multiplicity=Multiplicity(1, 1)),
        Property(name="B_If45", type=B_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditions47: BinaryAssociation = BinaryAssociation(
    name="conditions47",
    ends={
        Property(name="B_Predicate49", type=B_If, multiplicity=Multiplicity(1, 1)),
        Property(name="B_If48", type=B_Predicate, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
statements50: BinaryAssociation = BinaryAssociation(
    name="statements50",
    ends={
        Property(name="B_Expression51", type=B_Begin, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Begin", type=B_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outputs16: BinaryAssociation = BinaryAssociation(
    name="outputs16",
    ends={
        Property(name="B_VariableList18", type=B_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Operation17", type=B_VariableList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
preconditions19: BinaryAssociation = BinaryAssociation(
    name="preconditions19",
    ends={
        Property(name="B_Predicate21", type=B_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Operation20", type=B_Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preceeds23: BinaryAssociation = BinaryAssociation(
    name="preceeds23",
    ends={
        Property(name="B_Variable24", type=B_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Variable22", type=B_Variable, multiplicity=Multiplicity(0, 1))
    }
)
type25: BinaryAssociation = BinaryAssociation(
    name="type25",
    ends={
        Property(name="B_Predicate27", type=B_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Variable26", type=B_Predicate, multiplicity=Multiplicity(0, 1))
    }
)
variables28: BinaryAssociation = BinaryAssociation(
    name="variables28",
    ends={
        Property(name="B_Variable30", type=B_VariableList, multiplicity=Multiplicity(1, 1)),
        Property(name="B_VariableList29", type=B_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
first31: BinaryAssociation = BinaryAssociation(
    name="first31",
    ends={
        Property(name="B_Variable33", type=B_VariableList, multiplicity=Multiplicity(1, 1)),
        Property(name="B_VariableList32", type=B_Variable, multiplicity=Multiplicity(1, 1))
    }
)
variables34: BinaryAssociation = BinaryAssociation(
    name="variables34",
    ends={
        Property(name="B_Variable35", type=B_Any, multiplicity=Multiplicity(1, 1)),
        Property(name="B_Any", type=B_Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_B_Action_Expression = Generalization(general=Expression, specific=B_Action)
gen_B_If_Expression = Generalization(general=Expression, specific=B_If)
gen_B_Skip_Expression = Generalization(general=Expression, specific=B_Skip)
gen_B_Begin_Expression = Generalization(general=Expression, specific=B_Begin)
gen_B_Predicate_Expression = Generalization(general=Expression, specific=B_Predicate)
gen_B_Any_Expression = Generalization(general=Expression, specific=B_Any)

# Domain Model
domain_model = DomainModel(
    name="B",
    types={B_SET, B_Operation, B_Predicate, B_Variable, B_Action, B_Expression, B_VariableList, B_Machine, B_If, B_Skip, B_Begin, Expression, B_Any},
    associations={refines1, sets2, operations4, invariants6, variables8, initialisations10, statements12, inputs14, var_conditions36, statements39, true_statements42, false_statements44, conditions47, statements50, outputs16, preconditions19, preceeds23, type25, variables28, first31, variables34},
    generalizations={gen_B_Action_Expression, gen_B_If_Expression, gen_B_Skip_Expression, gen_B_Begin_Expression, gen_B_Predicate_Expression, gen_B_Any_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)