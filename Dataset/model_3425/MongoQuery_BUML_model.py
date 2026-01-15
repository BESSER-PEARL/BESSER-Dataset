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
mongoQuery_Selector = Class(name="mongoQuery::Selector")
mongoQuery_JsonDate = Class(name="mongoQuery::JsonDate")
mongoQuery_Array = Class(name="mongoQuery::Array")
mongoQuery_QueryObject = Class(name="mongoQuery::QueryObject")
Query = Class(name="Query")
mongoQuery_Query = Class(name="mongoQuery::Query")
mongoQuery_Selection = Class(name="mongoQuery::Selection")
mongoQuery_FieldSelection = Class(name="mongoQuery::FieldSelection")

# mongoQuery_Selector class attributes and methods

# mongoQuery_JsonDate class attributes and methods
mongoQuery_JsonDate_milliseconds: Property = Property(name="milliseconds", type=IntegerType)
mongoQuery_JsonDate_dateString: Property = Property(name="dateString", type=StringType)
mongoQuery_JsonDate_year: Property = Property(name="year", type=IntegerType)
mongoQuery_JsonDate_month: Property = Property(name="month", type=IntegerType)
mongoQuery_JsonDate_day: Property = Property(name="day", type=IntegerType)
mongoQuery_JsonDate_hour: Property = Property(name="hour", type=IntegerType)
mongoQuery_JsonDate_minute: Property = Property(name="minute", type=IntegerType)
mongoQuery_JsonDate_second: Property = Property(name="second", type=IntegerType)
mongoQuery_JsonDate_millisecond: Property = Property(name="millisecond", type=IntegerType)
mongoQuery_JsonDate.attributes={mongoQuery_JsonDate_hour, mongoQuery_JsonDate_milliseconds, mongoQuery_JsonDate_day, mongoQuery_JsonDate_year, mongoQuery_JsonDate_month, mongoQuery_JsonDate_millisecond, mongoQuery_JsonDate_dateString, mongoQuery_JsonDate_second, mongoQuery_JsonDate_minute}

# mongoQuery_Array class attributes and methods

# mongoQuery_QueryObject class attributes and methods

# Query class attributes and methods

# mongoQuery_Query class attributes and methods
mongoQuery_Query_key: Property = Property(name="key", type=StringType)
mongoQuery_Query_stringValue: Property = Property(name="stringValue", type=StringType)
mongoQuery_Query_numberValue: Property = Property(name="numberValue", type=FloatType)
mongoQuery_Query_integerValue: Property = Property(name="integerValue", type=IntegerType)
mongoQuery_Query.attributes={mongoQuery_Query_stringValue, mongoQuery_Query_key, mongoQuery_Query_numberValue, mongoQuery_Query_integerValue}

# mongoQuery_Selection class attributes and methods

# mongoQuery_FieldSelection class attributes and methods
mongoQuery_FieldSelection_enabled: Property = Property(name="enabled", type=IntegerType)
mongoQuery_FieldSelection_key: Property = Property(name="key", type=StringType)
mongoQuery_FieldSelection.attributes={mongoQuery_FieldSelection_key, mongoQuery_FieldSelection_enabled}

# Relationships
value6: BinaryAssociation = BinaryAssociation(
    name="value6",
    ends={
        Property(name="mongoQuery_Query7", type=mongoQuery_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="mongoQuery_Query5", type=mongoQuery_Query, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dateValue8: BinaryAssociation = BinaryAssociation(
    name="dateValue8",
    ends={
        Property(name="mongoQuery_JsonDate", type=mongoQuery_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="mongoQuery_Query9", type=mongoQuery_JsonDate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayValue10: BinaryAssociation = BinaryAssociation(
    name="arrayValue10",
    ends={
        Property(name="mongoQuery_Array", type=mongoQuery_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="mongoQuery_Query11", type=mongoQuery_Array, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objectValue13: BinaryAssociation = BinaryAssociation(
    name="objectValue13",
    ends={
        Property(name="mongoQuery_Query14", type=mongoQuery_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="mongoQuery_Query12", type=mongoQuery_Query, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values15: BinaryAssociation = BinaryAssociation(
    name="values15",
    ends={
        Property(name="mongoQuery_Query17", type=mongoQuery_Array, multiplicity=Multiplicity(1, 1)),
        Property(name="mongoQuery_Array16", type=mongoQuery_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members18: BinaryAssociation = BinaryAssociation(
    name="members18",
    ends={
        Property(name="mongoQuery_Query19", type=mongoQuery_QueryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="mongoQuery_QueryObject", type=mongoQuery_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query0: BinaryAssociation = BinaryAssociation(
    name="query0",
    ends={
        Property(name="mongoQuery_Query", type=mongoQuery_Selector, multiplicity=Multiplicity(1, 1)),
        Property(name="mongoQuery_Selector", type=mongoQuery_Query, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selection1: BinaryAssociation = BinaryAssociation(
    name="selection1",
    ends={
        Property(name="mongoQuery_Selection", type=mongoQuery_Selector, multiplicity=Multiplicity(1, 1)),
        Property(name="mongoQuery_Selector2", type=mongoQuery_Selection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields3: BinaryAssociation = BinaryAssociation(
    name="fields3",
    ends={
        Property(name="mongoQuery_FieldSelection", type=mongoQuery_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="mongoQuery_Selection4", type=mongoQuery_FieldSelection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_mongoQuery_QueryObject_Query = Generalization(general=Query, specific=mongoQuery_QueryObject)

# Domain Model
domain_model = DomainModel(
    name="mongoQuery",
    types={mongoQuery_Selector, mongoQuery_JsonDate, mongoQuery_Array, mongoQuery_QueryObject, Query, mongoQuery_Query, mongoQuery_Selection, mongoQuery_FieldSelection},
    associations={value6, dateValue8, arrayValue10, objectValue13, values15, members18, query0, selection1, fields3},
    generalizations={gen_mongoQuery_QueryObject_Query},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)