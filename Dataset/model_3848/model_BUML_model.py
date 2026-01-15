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
model_Select = Class(name="model::Select")
model_Column = Class(name="model::Column")
model_From = Class(name="model::From")
model_Where = Class(name="model::Where")
model_Union = Class(name="model::Union")
model_ColumnAlias = Class(name="model::ColumnAlias")
model_Table = Class(name="model::Table")
model_TableAlias = Class(name="model::TableAlias")
model_Condition = Class(name="model::Condition", is_abstract=True)
model_BooleanOperation = Class(name="model::BooleanOperation", is_abstract=True)
model_ComparisonOperator = Class(name="model::ComparisonOperator", is_abstract=True)
model_Equals = Class(name="model::Equals")
ComparisonOperator = Class(name="ComparisonOperator")
model_GreaterThan = Class(name="model::GreaterThan")
model_LessThan = Class(name="model::LessThan")
model_Existence = Class(name="model::Existence", is_abstract=True)
model_NotEquals = Class(name="model::NotEquals")
model_And = Class(name="model::And")
BooleanOperation = Class(name="BooleanOperation")
model_Or = Class(name="model::Or")
model_Comparison = Class(name="model::Comparison")
Condition = Class(name="Condition")
model_Exists = Class(name="model::Exists")
Existence = Class(name="Existence")
model_NotExists = Class(name="model::NotExists")

# model_Select class attributes and methods

# model_Column class attributes and methods
model_Column_name: Property = Property(name="name", type=StringType)
model_Column.attributes={model_Column_name}

# model_From class attributes and methods

# model_Where class attributes and methods

# model_Union class attributes and methods

# model_ColumnAlias class attributes and methods
model_ColumnAlias_name: Property = Property(name="name", type=StringType)
model_ColumnAlias.attributes={model_ColumnAlias_name}

# model_Table class attributes and methods
model_Table_name: Property = Property(name="name", type=StringType)
model_Table.attributes={model_Table_name}

# model_TableAlias class attributes and methods
model_TableAlias_name: Property = Property(name="name", type=StringType)
model_TableAlias.attributes={model_TableAlias_name}

# model_Condition class attributes and methods

# model_BooleanOperation class attributes and methods

# model_ComparisonOperator class attributes and methods

# model_Equals class attributes and methods

# ComparisonOperator class attributes and methods

# model_GreaterThan class attributes and methods

# model_LessThan class attributes and methods

# model_Existence class attributes and methods

# model_NotEquals class attributes and methods

# model_And class attributes and methods

# BooleanOperation class attributes and methods

# model_Or class attributes and methods

# model_Comparison class attributes and methods
model_Comparison_lhs: Property = Property(name="lhs", type=StringType)
model_Comparison_rhs: Property = Property(name="rhs", type=StringType)
model_Comparison.attributes={model_Comparison_lhs, model_Comparison_rhs}

# Condition class attributes and methods

# model_Exists class attributes and methods

# Existence class attributes and methods

# model_NotExists class attributes and methods

# Relationships
column0: BinaryAssociation = BinaryAssociation(
    name="column0",
    ends={
        Property(name="model_Column", type=model_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Select", type=model_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
from1: BinaryAssociation = BinaryAssociation(
    name="from1",
    ends={
        Property(name="model_From", type=model_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Select2", type=model_From, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
where3: BinaryAssociation = BinaryAssociation(
    name="where3",
    ends={
        Property(name="model_Where", type=model_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Select4", type=model_Where, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
union5: BinaryAssociation = BinaryAssociation(
    name="union5",
    ends={
        Property(name="model_Union", type=model_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Select6", type=model_Union, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnalias7: BinaryAssociation = BinaryAssociation(
    name="columnalias7",
    ends={
        Property(name="model_ColumnAlias", type=model_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Column8", type=model_ColumnAlias, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table9: BinaryAssociation = BinaryAssociation(
    name="table9",
    ends={
        Property(name="model_Table", type=model_From, multiplicity=Multiplicity(1, 1)),
        Property(name="model_From10", type=model_Table, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tablealias11: BinaryAssociation = BinaryAssociation(
    name="tablealias11",
    ends={
        Property(name="model_TableAlias", type=model_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Table12", type=model_TableAlias, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition13: BinaryAssociation = BinaryAssociation(
    name="condition13",
    ends={
        Property(name="model_Condition", type=model_Where, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Where14", type=model_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition15: BinaryAssociation = BinaryAssociation(
    name="condition15",
    ends={
        Property(name="model_Condition16", type=model_BooleanOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BooleanOperation", type=model_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
select17: BinaryAssociation = BinaryAssociation(
    name="select17",
    ends={
        Property(name="model_Select19", type=model_Union, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Union18", type=model_Select, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
booleanoperation20: BinaryAssociation = BinaryAssociation(
    name="booleanoperation20",
    ends={
        Property(name="model_BooleanOperation22", type=model_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Condition21", type=model_BooleanOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comparisonoperator23: BinaryAssociation = BinaryAssociation(
    name="comparisonoperator23",
    ends={
        Property(name="model_ComparisonOperator", type=model_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Comparison", type=model_ComparisonOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
select24: BinaryAssociation = BinaryAssociation(
    name="select24",
    ends={
        Property(name="model_Select25", type=model_Existence, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Existence", type=model_Select, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_model_Equals_ComparisonOperator = Generalization(general=ComparisonOperator, specific=model_Equals)
gen_model_GreaterThan_ComparisonOperator = Generalization(general=ComparisonOperator, specific=model_GreaterThan)
gen_model_LessThan_ComparisonOperator = Generalization(general=ComparisonOperator, specific=model_LessThan)
gen_model_NotEquals_ComparisonOperator = Generalization(general=ComparisonOperator, specific=model_NotEquals)
gen_model_And_BooleanOperation = Generalization(general=BooleanOperation, specific=model_And)
gen_model_Or_BooleanOperation = Generalization(general=BooleanOperation, specific=model_Or)
gen_model_Comparison_Condition = Generalization(general=Condition, specific=model_Comparison)
gen_model_Existence_Condition = Generalization(general=Condition, specific=model_Existence)
gen_model_Exists_Existence = Generalization(general=Existence, specific=model_Exists)
gen_model_NotExists_Existence = Generalization(general=Existence, specific=model_NotExists)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Select, model_Column, model_From, model_Where, model_Union, model_ColumnAlias, model_Table, model_TableAlias, model_Condition, model_BooleanOperation, model_ComparisonOperator, model_Equals, ComparisonOperator, model_GreaterThan, model_LessThan, model_Existence, model_NotEquals, model_And, BooleanOperation, model_Or, model_Comparison, Condition, model_Exists, Existence, model_NotExists},
    associations={column0, from1, where3, union5, columnalias7, table9, tablealias11, condition13, condition15, select17, booleanoperation20, comparisonoperator23, select24},
    generalizations={gen_model_Equals_ComparisonOperator, gen_model_GreaterThan_ComparisonOperator, gen_model_LessThan_ComparisonOperator, gen_model_NotEquals_ComparisonOperator, gen_model_And_BooleanOperation, gen_model_Or_BooleanOperation, gen_model_Comparison_Condition, gen_model_Existence_Condition, gen_model_Exists_Existence, gen_model_NotExists_Existence},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)