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
ArrayOperator: Enumeration = Enumeration(
    name="ArrayOperator",
    literals={
            EnumerationLiteral(name="mongo_all"),
			EnumerationLiteral(name="mongo_in"),
			EnumerationLiteral(name="sql_in"),
			EnumerationLiteral(name="mongo_nin"),
			EnumerationLiteral(name="sql_notIn")
    }
)

Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="lessThen"),
			EnumerationLiteral(name="greaterThen"),
			EnumerationLiteral(name="lessEqual"),
			EnumerationLiteral(name="greaterEqual"),
			EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="notEqual"),
			EnumerationLiteral(name="like"),
			EnumerationLiteral(name="notLike"),
			EnumerationLiteral(name="notIn"),
			EnumerationLiteral(name="in_")
    }
)

# Classes
query_Model = Class(name="query_Model")
query_Database = Class(name="query_Database")
query_WhereEntry = Class(name="query_WhereEntry")
query_ExpressionWhereEntry = Class(name="query_ExpressionWhereEntry")
WhereEntry = Class(name="WhereEntry")
query_SingleExpressionWhereEntry = Class(name="query_SingleExpressionWhereEntry")
ExpressionWhereEntry = Class(name="ExpressionWhereEntry")
query_Expression = Class(name="query_Expression")
query_ReplacableValue = Class(name="query_ReplacableValue")
Expression = Class(name="Expression")
query_DoubleExpression = Class(name="query_DoubleExpression")
query_LongExpression = Class(name="query_LongExpression")
query_StringExpression = Class(name="query_StringExpression")
query_NullExpression = Class(name="query_NullExpression")
query_DateExpression = Class(name="query_DateExpression")
query_BooleanExpression = Class(name="query_BooleanExpression")
query_MultiExpressionWhereEntry = Class(name="query_MultiExpressionWhereEntry")
query_ArrayExpression = Class(name="query_ArrayExpression")
query_DoubleArrayExpression = Class(name="query_DoubleArrayExpression")
ArrayExpression = Class(name="ArrayExpression")
query_LongArrayExpression = Class(name="query_LongArrayExpression")
query_StringArrayExpression = Class(name="query_StringArrayExpression")
query_NullArrayExpression = Class(name="query_NullArrayExpression")
query_DateArrayExpression = Class(name="query_DateArrayExpression")
query_BooleanArrayExpression = Class(name="query_BooleanArrayExpression")
query_OrWhereEntry = Class(name="query_OrWhereEntry")
query_AndWhereEntry = Class(name="query_AndWhereEntry")

# query_Model class attributes and methods
query_Model_attrs: Property = Property(name="attrs", type=StringType)
query_Model.attributes={query_Model_attrs}

# query_Database class attributes and methods
query_Database_url: Property = Property(name="url", type=StringType)
query_Database_port: Property = Property(name="port", type=StringType)
query_Database_dbName: Property = Property(name="dbName", type=StringType)
query_Database_name: Property = Property(name="name", type=StringType)
query_Database.attributes={query_Database_port, query_Database_name, query_Database_dbName, query_Database_url}

# query_WhereEntry class attributes and methods

# query_ExpressionWhereEntry class attributes and methods
query_ExpressionWhereEntry_name: Property = Property(name="name", type=StringType)
query_ExpressionWhereEntry.attributes={query_ExpressionWhereEntry_name}

# WhereEntry class attributes and methods

# query_SingleExpressionWhereEntry class attributes and methods
query_SingleExpressionWhereEntry_operator: Property = Property(name="operator", type=StringType)
query_SingleExpressionWhereEntry.attributes={query_SingleExpressionWhereEntry_operator}

# ExpressionWhereEntry class attributes and methods

# query_Expression class attributes and methods

# query_ReplacableValue class attributes and methods
query_ReplacableValue_value: Property = Property(name="value", type=StringType)
query_ReplacableValue.attributes={query_ReplacableValue_value}

# Expression class attributes and methods

# query_DoubleExpression class attributes and methods
query_DoubleExpression_value: Property = Property(name="value", type=FloatType)
query_DoubleExpression.attributes={query_DoubleExpression_value}

# query_LongExpression class attributes and methods
query_LongExpression_value: Property = Property(name="value", type=StringType)
query_LongExpression.attributes={query_LongExpression_value}

# query_StringExpression class attributes and methods
query_StringExpression_value: Property = Property(name="value", type=StringType)
query_StringExpression.attributes={query_StringExpression_value}

# query_NullExpression class attributes and methods
query_NullExpression_value: Property = Property(name="value", type=StringType)
query_NullExpression.attributes={query_NullExpression_value}

# query_DateExpression class attributes and methods
query_DateExpression_value: Property = Property(name="value", type=DateType)
query_DateExpression.attributes={query_DateExpression_value}

# query_BooleanExpression class attributes and methods
query_BooleanExpression_true: Property = Property(name="true", type=StringType)
query_BooleanExpression.attributes={query_BooleanExpression_true}

# query_MultiExpressionWhereEntry class attributes and methods
query_MultiExpressionWhereEntry_operator: Property = Property(name="operator", type=StringType)
query_MultiExpressionWhereEntry.attributes={query_MultiExpressionWhereEntry_operator}

# query_ArrayExpression class attributes and methods

# query_DoubleArrayExpression class attributes and methods
query_DoubleArrayExpression_values: Property = Property(name="values", type=FloatType)
query_DoubleArrayExpression.attributes={query_DoubleArrayExpression_values}

# ArrayExpression class attributes and methods

# query_LongArrayExpression class attributes and methods
query_LongArrayExpression_values: Property = Property(name="values", type=StringType)
query_LongArrayExpression.attributes={query_LongArrayExpression_values}

# query_StringArrayExpression class attributes and methods
query_StringArrayExpression_values: Property = Property(name="values", type=StringType)
query_StringArrayExpression.attributes={query_StringArrayExpression_values}

# query_NullArrayExpression class attributes and methods
query_NullArrayExpression_values: Property = Property(name="values", type=StringType)
query_NullArrayExpression.attributes={query_NullArrayExpression_values}

# query_DateArrayExpression class attributes and methods
query_DateArrayExpression_values: Property = Property(name="values", type=DateType)
query_DateArrayExpression.attributes={query_DateArrayExpression_values}

# query_BooleanArrayExpression class attributes and methods
query_BooleanArrayExpression_values: Property = Property(name="values", type=StringType)
query_BooleanArrayExpression.attributes={query_BooleanArrayExpression_values}

# query_OrWhereEntry class attributes and methods

# query_AndWhereEntry class attributes and methods

# Relationships
db0: BinaryAssociation = BinaryAssociation(
    name="db0",
    ends={
        Property(name="query_Database", type=query_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="query_Model", type=query_Database, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs4: BinaryAssociation = BinaryAssociation(
    name="rhs4",
    ends={
        Property(name="query_ArrayExpression", type=query_MultiExpressionWhereEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="query_MultiExpressionWhereEntry", type=query_ArrayExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereEntry1: BinaryAssociation = BinaryAssociation(
    name="whereEntry1",
    ends={
        Property(name="query_WhereEntry", type=query_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="query_Model2", type=query_WhereEntry, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs3: BinaryAssociation = BinaryAssociation(
    name="rhs3",
    ends={
        Property(name="query_Expression", type=query_SingleExpressionWhereEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="query_SingleExpressionWhereEntry", type=query_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries7: BinaryAssociation = BinaryAssociation(
    name="entries7",
    ends={
        Property(name="query_WhereEntry8", type=query_AndWhereEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="query_AndWhereEntry", type=query_WhereEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries5: BinaryAssociation = BinaryAssociation(
    name="entries5",
    ends={
        Property(name="query_WhereEntry6", type=query_OrWhereEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="query_OrWhereEntry", type=query_WhereEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_query_ExpressionWhereEntry_WhereEntry = Generalization(general=WhereEntry, specific=query_ExpressionWhereEntry)
gen_query_SingleExpressionWhereEntry_ExpressionWhereEntry = Generalization(general=ExpressionWhereEntry, specific=query_SingleExpressionWhereEntry)
gen_query_ReplacableValue_Expression = Generalization(general=Expression, specific=query_ReplacableValue)
gen_query_DoubleExpression_Expression = Generalization(general=Expression, specific=query_DoubleExpression)
gen_query_LongExpression_Expression = Generalization(general=Expression, specific=query_LongExpression)
gen_query_StringExpression_Expression = Generalization(general=Expression, specific=query_StringExpression)
gen_query_NullExpression_Expression = Generalization(general=Expression, specific=query_NullExpression)
gen_query_DateExpression_Expression = Generalization(general=Expression, specific=query_DateExpression)
gen_query_BooleanExpression_Expression = Generalization(general=Expression, specific=query_BooleanExpression)
gen_query_MultiExpressionWhereEntry_ExpressionWhereEntry = Generalization(general=ExpressionWhereEntry, specific=query_MultiExpressionWhereEntry)
gen_query_DoubleArrayExpression_ArrayExpression = Generalization(general=ArrayExpression, specific=query_DoubleArrayExpression)
gen_query_LongArrayExpression_ArrayExpression = Generalization(general=ArrayExpression, specific=query_LongArrayExpression)
gen_query_StringArrayExpression_ArrayExpression = Generalization(general=ArrayExpression, specific=query_StringArrayExpression)
gen_query_NullArrayExpression_ArrayExpression = Generalization(general=ArrayExpression, specific=query_NullArrayExpression)
gen_query_DateArrayExpression_ArrayExpression = Generalization(general=ArrayExpression, specific=query_DateArrayExpression)
gen_query_BooleanArrayExpression_ArrayExpression = Generalization(general=ArrayExpression, specific=query_BooleanArrayExpression)
gen_query_OrWhereEntry_WhereEntry = Generalization(general=WhereEntry, specific=query_OrWhereEntry)
gen_query_AndWhereEntry_WhereEntry = Generalization(general=WhereEntry, specific=query_AndWhereEntry)

# Domain Model
domain_model = DomainModel(
    name="query",
    types={query_Model, query_Database, query_WhereEntry, query_ExpressionWhereEntry, WhereEntry, query_SingleExpressionWhereEntry, ExpressionWhereEntry, query_Expression, query_ReplacableValue, Expression, query_DoubleExpression, query_LongExpression, query_StringExpression, query_NullExpression, query_DateExpression, query_BooleanExpression, query_MultiExpressionWhereEntry, query_ArrayExpression, query_DoubleArrayExpression, ArrayExpression, query_LongArrayExpression, query_StringArrayExpression, query_NullArrayExpression, query_DateArrayExpression, query_BooleanArrayExpression, query_OrWhereEntry, query_AndWhereEntry, ArrayOperator, Operator},
    associations={db0, rhs4, whereEntry1, rhs3, entries7, entries5},
    generalizations={gen_query_ExpressionWhereEntry_WhereEntry, gen_query_SingleExpressionWhereEntry_ExpressionWhereEntry, gen_query_ReplacableValue_Expression, gen_query_DoubleExpression_Expression, gen_query_LongExpression_Expression, gen_query_StringExpression_Expression, gen_query_NullExpression_Expression, gen_query_DateExpression_Expression, gen_query_BooleanExpression_Expression, gen_query_MultiExpressionWhereEntry_ExpressionWhereEntry, gen_query_DoubleArrayExpression_ArrayExpression, gen_query_LongArrayExpression_ArrayExpression, gen_query_StringArrayExpression_ArrayExpression, gen_query_NullArrayExpression_ArrayExpression, gen_query_DateArrayExpression_ArrayExpression, gen_query_BooleanArrayExpression_ArrayExpression, gen_query_OrWhereEntry_WhereEntry, gen_query_AndWhereEntry_WhereEntry},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)