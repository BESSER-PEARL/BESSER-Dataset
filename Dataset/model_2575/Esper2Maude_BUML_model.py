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
esper2Maude_Model = Class(name="esper2Maude::Model")
esper2Maude_Schema = Class(name="esper2Maude::Schema")
esper2Maude_Pattern = Class(name="esper2Maude::Pattern")
esper2Maude_EventProperty = Class(name="esper2Maude::EventProperty")
esper2Maude_FilterOperator = Class(name="esper2Maude::FilterOperator")
esper2Maude_FollowedBy = Class(name="esper2Maude::FollowedBy")
esper2Maude_LogicalOperator = Class(name="esper2Maude::LogicalOperator")
esper2Maude_SubFilterFollowedBy = Class(name="esper2Maude::SubFilterFollowedBy")
esper2Maude_Event = Class(name="esper2Maude::Event")
esper2Maude_NonLastSelectEntry = Class(name="esper2Maude::NonLastSelectEntry")
esper2Maude_LastSelectEntry = Class(name="esper2Maude::LastSelectEntry")
esper2Maude_FilterFrom = Class(name="esper2Maude::FilterFrom")
esper2Maude_Window = Class(name="esper2Maude::Window")
esper2Maude_WhereFilter = Class(name="esper2Maude::WhereFilter")
esper2Maude_FilterEvent = Class(name="esper2Maude::FilterEvent")
esper2Maude_ComparisonOperator = Class(name="esper2Maude::ComparisonOperator")
esper2Maude_SelectEntry = Class(name="esper2Maude::SelectEntry")
esper2Maude_Every = Class(name="esper2Maude::Every")
esper2Maude_FilterPart = Class(name="esper2Maude::FilterPart")
esper2Maude_Field = Class(name="esper2Maude::Field")

# esper2Maude_Model class attributes and methods

# esper2Maude_Schema class attributes and methods
esper2Maude_Schema_name: Property = Property(name="name", type=StringType)
esper2Maude_Schema.attributes={esper2Maude_Schema_name}

# esper2Maude_Pattern class attributes and methods
esper2Maude_Pattern_name: Property = Property(name="name", type=StringType)
esper2Maude_Pattern_num: Property = Property(name="num", type=IntegerType)
esper2Maude_Pattern.attributes={esper2Maude_Pattern_name, esper2Maude_Pattern_num}

# esper2Maude_EventProperty class attributes and methods
esper2Maude_EventProperty_name: Property = Property(name="name", type=StringType)
esper2Maude_EventProperty_type: Property = Property(name="type", type=StringType)
esper2Maude_EventProperty.attributes={esper2Maude_EventProperty_name, esper2Maude_EventProperty_type}

# esper2Maude_FilterOperator class attributes and methods

# esper2Maude_FollowedBy class attributes and methods

# esper2Maude_LogicalOperator class attributes and methods
esper2Maude_LogicalOperator_and: Property = Property(name="and", type=StringType)
esper2Maude_LogicalOperator_or: Property = Property(name="or", type=StringType)
esper2Maude_LogicalOperator.attributes={esper2Maude_LogicalOperator_and, esper2Maude_LogicalOperator_or}

# esper2Maude_SubFilterFollowedBy class attributes and methods
esper2Maude_SubFilterFollowedBy_eventVariable: Property = Property(name="eventVariable", type=StringType)
esper2Maude_SubFilterFollowedBy_eventName: Property = Property(name="eventName", type=StringType)
esper2Maude_SubFilterFollowedBy.attributes={esper2Maude_SubFilterFollowedBy_eventVariable, esper2Maude_SubFilterFollowedBy_eventName}

# esper2Maude_Event class attributes and methods
esper2Maude_Event_name: Property = Property(name="name", type=StringType)
esper2Maude_Event.attributes={esper2Maude_Event_name}

# esper2Maude_NonLastSelectEntry class attributes and methods

# esper2Maude_LastSelectEntry class attributes and methods

# esper2Maude_FilterFrom class attributes and methods
esper2Maude_FilterFrom_eventVariable: Property = Property(name="eventVariable", type=StringType)
esper2Maude_FilterFrom_eventName: Property = Property(name="eventName", type=StringType)
esper2Maude_FilterFrom.attributes={esper2Maude_FilterFrom_eventName, esper2Maude_FilterFrom_eventVariable}

# esper2Maude_Window class attributes and methods
esper2Maude_Window_typeTime: Property = Property(name="typeTime", type=StringType)
esper2Maude_Window_num: Property = Property(name="num", type=IntegerType)
esper2Maude_Window_typeBatch: Property = Property(name="typeBatch", type=StringType)
esper2Maude_Window.attributes={esper2Maude_Window_num, esper2Maude_Window_typeBatch, esper2Maude_Window_typeTime}

# esper2Maude_WhereFilter class attributes and methods
esper2Maude_WhereFilter_timer: Property = Property(name="timer", type=StringType)
esper2Maude_WhereFilter_num: Property = Property(name="num", type=IntegerType)
esper2Maude_WhereFilter.attributes={esper2Maude_WhereFilter_timer, esper2Maude_WhereFilter_num}

# esper2Maude_FilterEvent class attributes and methods

# esper2Maude_ComparisonOperator class attributes and methods
esper2Maude_ComparisonOperator_gt: Property = Property(name="gt", type=StringType)
esper2Maude_ComparisonOperator_ge: Property = Property(name="ge", type=StringType)
esper2Maude_ComparisonOperator_eq: Property = Property(name="eq", type=StringType)
esper2Maude_ComparisonOperator_neq: Property = Property(name="neq", type=StringType)
esper2Maude_ComparisonOperator_lt: Property = Property(name="lt", type=StringType)
esper2Maude_ComparisonOperator_le: Property = Property(name="le", type=StringType)
esper2Maude_ComparisonOperator.attributes={esper2Maude_ComparisonOperator_le, esper2Maude_ComparisonOperator_lt, esper2Maude_ComparisonOperator_gt, esper2Maude_ComparisonOperator_ge, esper2Maude_ComparisonOperator_eq, esper2Maude_ComparisonOperator_neq}

# esper2Maude_SelectEntry class attributes and methods
esper2Maude_SelectEntry_alias: Property = Property(name="alias", type=StringType)
esper2Maude_SelectEntry_groupOp: Property = Property(name="groupOp", type=StringType)
esper2Maude_SelectEntry.attributes={esper2Maude_SelectEntry_groupOp, esper2Maude_SelectEntry_alias}

# esper2Maude_Every class attributes and methods
esper2Maude_Every_eventVariable: Property = Property(name="eventVariable", type=StringType)
esper2Maude_Every_eventName: Property = Property(name="eventName", type=StringType)
esper2Maude_Every.attributes={esper2Maude_Every_eventVariable, esper2Maude_Every_eventName}

# esper2Maude_FilterPart class attributes and methods
esper2Maude_FilterPart_eventPropName: Property = Property(name="eventPropName", type=StringType)
esper2Maude_FilterPart_eventVariable: Property = Property(name="eventVariable", type=StringType)
esper2Maude_FilterPart_neg: Property = Property(name="neg", type=StringType)
esper2Maude_FilterPart_num: Property = Property(name="num", type=IntegerType)
esper2Maude_FilterPart_dec: Property = Property(name="dec", type=IntegerType)
esper2Maude_FilterPart_str: Property = Property(name="str", type=StringType)
esper2Maude_FilterPart_t: Property = Property(name="t", type=StringType)
esper2Maude_FilterPart_f: Property = Property(name="f", type=StringType)
esper2Maude_FilterPart.attributes={esper2Maude_FilterPart_eventPropName, esper2Maude_FilterPart_str, esper2Maude_FilterPart_f, esper2Maude_FilterPart_eventVariable, esper2Maude_FilterPart_dec, esper2Maude_FilterPart_neg, esper2Maude_FilterPart_t, esper2Maude_FilterPart_num}

# esper2Maude_Field class attributes and methods
esper2Maude_Field_star: Property = Property(name="star", type=StringType)
esper2Maude_Field_eventVariable: Property = Property(name="eventVariable", type=StringType)
esper2Maude_Field_eventPropName: Property = Property(name="eventPropName", type=StringType)
esper2Maude_Field.attributes={esper2Maude_Field_eventPropName, esper2Maude_Field_eventVariable, esper2Maude_Field_star}

# Relationships
schemas0: BinaryAssociation = BinaryAssociation(
    name="schemas0",
    ends={
        Property(name="esper2Maude_Schema", type=esper2Maude_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_Model", type=esper2Maude_Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
patterns1: BinaryAssociation = BinaryAssociation(
    name="patterns1",
    ends={
        Property(name="esper2Maude_Pattern", type=esper2Maude_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_Model2", type=esper2Maude_Pattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prop3: BinaryAssociation = BinaryAssociation(
    name="prop3",
    ends={
        Property(name="esper2Maude_EventProperty", type=esper2Maude_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_Schema4", type=esper2Maude_EventProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
props5: BinaryAssociation = BinaryAssociation(
    name="props5",
    ends={
        Property(name="esper2Maude_EventProperty7", type=esper2Maude_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_Schema6", type=esper2Maude_EventProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filterOpL19: BinaryAssociation = BinaryAssociation(
    name="filterOpL19",
    ends={
        Property(name="esper2Maude_FilterOperator", type=esper2Maude_WhereFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_WhereFilter20", type=esper2Maude_FilterOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filterOpR21: BinaryAssociation = BinaryAssociation(
    name="filterOpR21",
    ends={
        Property(name="esper2Maude_FilterOperator23", type=esper2Maude_WhereFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_WhereFilter22", type=esper2Maude_FilterOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filterEventR24: BinaryAssociation = BinaryAssociation(
    name="filterEventR24",
    ends={
        Property(name="esper2Maude_FilterEvent26", type=esper2Maude_WhereFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_WhereFilter25", type=esper2Maude_FilterEvent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
followedBy27: BinaryAssociation = BinaryAssociation(
    name="followedBy27",
    ends={
        Property(name="esper2Maude_FollowedBy", type=esper2Maude_FilterFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_FilterFrom28", type=esper2Maude_FollowedBy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left30: BinaryAssociation = BinaryAssociation(
    name="left30",
    ends={
        Property(name="esper2Maude_FilterFrom31", type=esper2Maude_FilterFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_FilterFrom29", type=esper2Maude_FilterFrom, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op32: BinaryAssociation = BinaryAssociation(
    name="op32",
    ends={
        Property(name="esper2Maude_LogicalOperator", type=esper2Maude_FilterFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_FilterFrom33", type=esper2Maude_LogicalOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right35: BinaryAssociation = BinaryAssociation(
    name="right35",
    ends={
        Property(name="esper2Maude_FilterFrom36", type=esper2Maude_FilterFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_FilterFrom34", type=esper2Maude_FilterFrom, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filter37: BinaryAssociation = BinaryAssociation(
    name="filter37",
    ends={
        Property(name="esper2Maude_FilterEvent39", type=esper2Maude_FilterFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_FilterFrom38", type=esper2Maude_FilterEvent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left40: BinaryAssociation = BinaryAssociation(
    name="left40",
    ends={
        Property(name="esper2Maude_SubFilterFollowedBy", type=esper2Maude_FollowedBy, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_FollowedBy41", type=esper2Maude_SubFilterFollowedBy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right42: BinaryAssociation = BinaryAssociation(
    name="right42",
    ends={
        Property(name="esper2Maude_SubFilterFollowedBy44", type=esper2Maude_FollowedBy, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_FollowedBy43", type=esper2Maude_SubFilterFollowedBy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whereFilter45: BinaryAssociation = BinaryAssociation(
    name="whereFilter45",
    ends={
        Property(name="esper2Maude_WhereFilter47", type=esper2Maude_FollowedBy, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_FollowedBy46", type=esper2Maude_WhereFilter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event8: BinaryAssociation = BinaryAssociation(
    name="event8",
    ends={
        Property(name="esper2Maude_Event", type=esper2Maude_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_Pattern9", type=esper2Maude_Event, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectEntries10: BinaryAssociation = BinaryAssociation(
    name="selectEntries10",
    ends={
        Property(name="esper2Maude_NonLastSelectEntry", type=esper2Maude_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_Pattern11", type=esper2Maude_NonLastSelectEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selectEntry12: BinaryAssociation = BinaryAssociation(
    name="selectEntry12",
    ends={
        Property(name="esper2Maude_LastSelectEntry", type=esper2Maude_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_Pattern13", type=esper2Maude_LastSelectEntry, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromFilter14: BinaryAssociation = BinaryAssociation(
    name="fromFilter14",
    ends={
        Property(name="esper2Maude_FilterFrom", type=esper2Maude_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_Pattern15", type=esper2Maude_FilterFrom, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
win16: BinaryAssociation = BinaryAssociation(
    name="win16",
    ends={
        Property(name="esper2Maude_Window", type=esper2Maude_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_Pattern17", type=esper2Maude_Window, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filterEventL18: BinaryAssociation = BinaryAssociation(
    name="filterEventL18",
    ends={
        Property(name="esper2Maude_FilterEvent", type=esper2Maude_WhereFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_WhereFilter", type=esper2Maude_FilterEvent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
comparison67: BinaryAssociation = BinaryAssociation(
    name="comparison67",
    ends={
        Property(name="esper2Maude_ComparisonOperator", type=esper2Maude_FilterOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_FilterOperator68", type=esper2Maude_ComparisonOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical69: BinaryAssociation = BinaryAssociation(
    name="logical69",
    ends={
        Property(name="esper2Maude_LogicalOperator71", type=esper2Maude_FilterOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_FilterOperator70", type=esper2Maude_LogicalOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry72: BinaryAssociation = BinaryAssociation(
    name="entry72",
    ends={
        Property(name="esper2Maude_SelectEntry", type=esper2Maude_NonLastSelectEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_NonLastSelectEntry73", type=esper2Maude_SelectEntry, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry74: BinaryAssociation = BinaryAssociation(
    name="entry74",
    ends={
        Property(name="esper2Maude_SelectEntry76", type=esper2Maude_LastSelectEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_LastSelectEntry75", type=esper2Maude_SelectEntry, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filter48: BinaryAssociation = BinaryAssociation(
    name="filter48",
    ends={
        Property(name="esper2Maude_FilterEvent50", type=esper2Maude_SubFilterFollowedBy, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_SubFilterFollowedBy49", type=esper2Maude_FilterEvent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
every51: BinaryAssociation = BinaryAssociation(
    name="every51",
    ends={
        Property(name="esper2Maude_Every", type=esper2Maude_SubFilterFollowedBy, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_SubFilterFollowedBy52", type=esper2Maude_Every, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filter53: BinaryAssociation = BinaryAssociation(
    name="filter53",
    ends={
        Property(name="esper2Maude_FilterEvent55", type=esper2Maude_Every, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_Every54", type=esper2Maude_FilterEvent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filterFrom56: BinaryAssociation = BinaryAssociation(
    name="filterFrom56",
    ends={
        Property(name="esper2Maude_FilterFrom58", type=esper2Maude_Every, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_Every57", type=esper2Maude_FilterFrom, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filterLeftHandSide59: BinaryAssociation = BinaryAssociation(
    name="filterLeftHandSide59",
    ends={
        Property(name="esper2Maude_FilterPart", type=esper2Maude_FilterEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_FilterEvent60", type=esper2Maude_FilterPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filterOp61: BinaryAssociation = BinaryAssociation(
    name="filterOp61",
    ends={
        Property(name="esper2Maude_FilterOperator63", type=esper2Maude_FilterEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_FilterEvent62", type=esper2Maude_FilterOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filterRightHandSide64: BinaryAssociation = BinaryAssociation(
    name="filterRightHandSide64",
    ends={
        Property(name="esper2Maude_FilterPart66", type=esper2Maude_FilterEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_FilterEvent65", type=esper2Maude_FilterPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field77: BinaryAssociation = BinaryAssociation(
    name="field77",
    ends={
        Property(name="esper2Maude_Field", type=esper2Maude_SelectEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="esper2Maude_SelectEntry78", type=esper2Maude_Field, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="esper2Maude",
    types={esper2Maude_Model, esper2Maude_Schema, esper2Maude_Pattern, esper2Maude_EventProperty, esper2Maude_FilterOperator, esper2Maude_FollowedBy, esper2Maude_LogicalOperator, esper2Maude_SubFilterFollowedBy, esper2Maude_Event, esper2Maude_NonLastSelectEntry, esper2Maude_LastSelectEntry, esper2Maude_FilterFrom, esper2Maude_Window, esper2Maude_WhereFilter, esper2Maude_FilterEvent, esper2Maude_ComparisonOperator, esper2Maude_SelectEntry, esper2Maude_Every, esper2Maude_FilterPart, esper2Maude_Field},
    associations={schemas0, patterns1, prop3, props5, filterOpL19, filterOpR21, filterEventR24, followedBy27, left30, op32, right35, filter37, left40, right42, whereFilter45, event8, selectEntries10, selectEntry12, fromFilter14, win16, filterEventL18, comparison67, logical69, entry72, entry74, filter48, every51, filter53, filterFrom56, filterLeftHandSide59, filterOp61, filterRightHandSide64, field77},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)