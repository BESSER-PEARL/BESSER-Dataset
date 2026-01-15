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
type: Enumeration = Enumeration(
    name="type",
    literals={
            EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="STRING")
    }
)

# Classes
pascal_Pascal = Class(name="pascal::Pascal")
pascal_program = Class(name="pascal::program")
pascal_var_block = Class(name="pascal::var::block")
pascal_block = Class(name="pascal::block")
pascal_EObject = Class(name="pascal::EObject")
pascal_var_decl = Class(name="pascal::var::decl")
pascal_var_list = Class(name="pascal::var::list")
pascal_statement = Class(name="pascal::statement")
pascal_atrib = Class(name="pascal::atrib")
pascal_expression = Class(name="pascal::expression")
expression = Class(name="expression")
pascal_repetitive_arit_expression = Class(name="pascal::repetitive::arit::expression")
pascal_rel_expression = Class(name="pascal::rel::expression")
pascal_arit_expression = Class(name="pascal::arit::expression")

# pascal_Pascal class attributes and methods

# pascal_program class attributes and methods
pascal_program_name: Property = Property(name="name", type=StringType)
pascal_program.attributes={pascal_program_name}

# pascal_var_block class attributes and methods

# pascal_block class attributes and methods

# pascal_EObject class attributes and methods

# pascal_var_decl class attributes and methods
pascal_var_decl_var_id: Property = Property(name="var_id", type=StringType)
pascal_var_decl_var_type: Property = Property(name="var_type", type=StringType)
pascal_var_decl_value: Property = Property(name="value", type=StringType)
pascal_var_decl.attributes={pascal_var_decl_var_id, pascal_var_decl_var_type, pascal_var_decl_value}

# pascal_var_list class attributes and methods
pascal_var_list_var_id: Property = Property(name="var_id", type=StringType)
pascal_var_list_var_ids: Property = Property(name="var_ids", type=StringType)
pascal_var_list_var_type: Property = Property(name="var_type", type=StringType)
pascal_var_list.attributes={pascal_var_list_var_id, pascal_var_list_var_type, pascal_var_list_var_ids}

# pascal_statement class attributes and methods

# pascal_atrib class attributes and methods
pascal_atrib_var_id: Property = Property(name="var_id", type=StringType)
pascal_atrib.attributes={pascal_atrib_var_id}

# pascal_expression class attributes and methods

# expression class attributes and methods

# pascal_repetitive_arit_expression class attributes and methods
pascal_repetitive_arit_expression_op: Property = Property(name="op", type=StringType)
pascal_repetitive_arit_expression_value: Property = Property(name="value", type=StringType)
pascal_repetitive_arit_expression.attributes={pascal_repetitive_arit_expression_value, pascal_repetitive_arit_expression_op}

# pascal_rel_expression class attributes and methods
pascal_rel_expression_open: Property = Property(name="open", type=StringType)
pascal_rel_expression_first: Property = Property(name="first", type=StringType)
pascal_rel_expression_op: Property = Property(name="op", type=StringType)
pascal_rel_expression_second: Property = Property(name="second", type=StringType)
pascal_rel_expression_close: Property = Property(name="close", type=StringType)
pascal_rel_expression.attributes={pascal_rel_expression_op, pascal_rel_expression_open, pascal_rel_expression_first, pascal_rel_expression_close, pascal_rel_expression_second}

# pascal_arit_expression class attributes and methods
pascal_arit_expression_value: Property = Property(name="value", type=StringType)
pascal_arit_expression.attributes={pascal_arit_expression_value}

# Relationships
head0: BinaryAssociation = BinaryAssociation(
    name="head0",
    ends={
        Property(name="pascal_program", type=pascal_Pascal, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_Pascal", type=pascal_program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarations1: BinaryAssociation = BinaryAssociation(
    name="declarations1",
    ends={
        Property(name="pascal_var_block", type=pascal_Pascal, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_Pascal2", type=pascal_var_block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scope3: BinaryAssociation = BinaryAssociation(
    name="scope3",
    ends={
        Property(name="pascal_block", type=pascal_Pascal, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_Pascal4", type=pascal_block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var_statements5: BinaryAssociation = BinaryAssociation(
    name="var_statements5",
    ends={
        Property(name="pascal_EObject", type=pascal_var_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_var_block6", type=pascal_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements7: BinaryAssociation = BinaryAssociation(
    name="statements7",
    ends={
        Property(name="pascal_statement", type=pascal_block, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_block8", type=pascal_statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
atrib_block9: BinaryAssociation = BinaryAssociation(
    name="atrib_block9",
    ends={
        Property(name="pascal_atrib", type=pascal_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_statement10", type=pascal_atrib, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp11: BinaryAssociation = BinaryAssociation(
    name="exp11",
    ends={
        Property(name="pascal_expression", type=pascal_atrib, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_atrib12", type=pascal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp13: BinaryAssociation = BinaryAssociation(
    name="exp13",
    ends={
        Property(name="pascal_repetitive_arit_expression", type=pascal_arit_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_arit_expression", type=pascal_repetitive_arit_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp15: BinaryAssociation = BinaryAssociation(
    name="exp15",
    ends={
        Property(name="pascal_repetitive_arit_expression16", type=pascal_repetitive_arit_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="pascal_repetitive_arit_expression14", type=pascal_repetitive_arit_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_pascal_arit_expression_expression = Generalization(general=expression, specific=pascal_arit_expression)
gen_pascal_rel_expression_expression = Generalization(general=expression, specific=pascal_rel_expression)

# Domain Model
domain_model = DomainModel(
    name="pascal",
    types={pascal_Pascal, pascal_program, pascal_var_block, pascal_block, pascal_EObject, pascal_var_decl, pascal_var_list, pascal_statement, pascal_atrib, pascal_expression, expression, pascal_repetitive_arit_expression, pascal_rel_expression, pascal_arit_expression, type},
    associations={head0, declarations1, scope3, var_statements5, statements7, atrib_block9, exp11, exp13, exp15},
    generalizations={gen_pascal_arit_expression_expression, gen_pascal_rel_expression_expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)