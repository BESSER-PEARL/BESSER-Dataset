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
Operators: Enumeration = Enumeration(
    name="Operators",
    literals={
            EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="lessThan"),
			EnumerationLiteral(name="moreThan"),
			EnumerationLiteral(name="lessEqualThan"),
			EnumerationLiteral(name="moreEqualThan"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="between"),
			EnumerationLiteral(name="in"),
			EnumerationLiteral(name="not"),
			EnumerationLiteral(name="notIn"),
			EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="multiplication"),
			EnumerationLiteral(name="isnot")
    }
)

# Classes
esper_Domainmodel = Class(name="esper::Domainmodel")
esper_RuleParts = Class(name="esper::RuleParts")
esper_Event = Class(name="esper::Event")
KindOfEvent = Class(name="KindOfEvent")
esper_Attributes = Class(name="esper::Attributes")
esper_AttributesDefinition = Class(name="esper::AttributesDefinition")
esper_Name = Class(name="esper::Name")
esper_Insert = Class(name="esper::Insert")
esper_Priority = Class(name="esper::Priority")
esper_Select = Class(name="esper::Select")
esper_From = Class(name="esper::From")
esper_GroupBy = Class(name="esper::GroupBy")
esper_Having = Class(name="esper::Having")
esper_SelectAttributesDefinition = Class(name="esper::SelectAttributesDefinition")
esper_KindSelectAttributesDefinition = Class(name="esper::KindSelectAttributesDefinition")
esper_SingleSelectDefinition = Class(name="esper::SingleSelectDefinition")
esper_DefaultMethods = Class(name="esper::DefaultMethods")
esper_SingleDefinition = Class(name="esper::SingleDefinition")
esper_Anything = Class(name="esper::Anything")
esper_Pattern = Class(name="esper::Pattern")
esper_JoinFollowBy = Class(name="esper::JoinFollowBy")
esper_Win = Class(name="esper::Win")
esper_AbstractFollowBy = Class(name="esper::AbstractFollowBy")
esper_FollowBy = Class(name="esper::FollowBy")
esper_FollowByWhere = Class(name="esper::FollowByWhere")
esper_TerminalExpression = Class(name="esper::TerminalExpression")
esper_KindOfEvent = Class(name="esper::KindOfEvent")
esper_Timer = Class(name="esper::Timer")
ExtraParenthesisRule = Class(name="ExtraParenthesisRule")
esper_ExtraParenthesisRule = Class(name="esper::ExtraParenthesisRule")

# esper_Domainmodel class attributes and methods

# esper_RuleParts class attributes and methods

# esper_Event class attributes and methods

# KindOfEvent class attributes and methods

# esper_Attributes class attributes and methods

# esper_AttributesDefinition class attributes and methods
esper_AttributesDefinition_name: Property = Property(name="name", type=StringType)
esper_AttributesDefinition_type: Property = Property(name="type", type=StringType)
esper_AttributesDefinition.attributes={esper_AttributesDefinition_name, esper_AttributesDefinition_type}

# esper_Name class attributes and methods
esper_Name_name: Property = Property(name="name", type=StringType)
esper_Name.attributes={esper_Name_name}

# esper_Insert class attributes and methods

# esper_Priority class attributes and methods
esper_Priority_priorityInt: Property = Property(name="priorityInt", type=IntegerType)
esper_Priority.attributes={esper_Priority_priorityInt}

# esper_Select class attributes and methods
esper_Select_alias: Property = Property(name="alias", type=StringType)
esper_Select_asterisk: Property = Property(name="asterisk", type=BooleanType)
esper_Select.attributes={esper_Select_alias, esper_Select_asterisk}

# esper_From class attributes and methods

# esper_GroupBy class attributes and methods

# esper_Having class attributes and methods
esper_Having_operator: Property = Property(name="operator", type=StringType)
esper_Having.attributes={esper_Having_operator}

# esper_SelectAttributesDefinition class attributes and methods
esper_SelectAttributesDefinition_operator: Property = Property(name="operator", type=StringType)
esper_SelectAttributesDefinition.attributes={esper_SelectAttributesDefinition_operator}

# esper_KindSelectAttributesDefinition class attributes and methods
esper_KindSelectAttributesDefinition_int: Property = Property(name="int", type=IntegerType)
esper_KindSelectAttributesDefinition_string: Property = Property(name="string", type=StringType)
esper_KindSelectAttributesDefinition.attributes={esper_KindSelectAttributesDefinition_int, esper_KindSelectAttributesDefinition_string}

# esper_SingleSelectDefinition class attributes and methods
esper_SingleSelectDefinition_attribute: Property = Property(name="attribute", type=StringType)
esper_SingleSelectDefinition.attributes={esper_SingleSelectDefinition_attribute}

# esper_DefaultMethods class attributes and methods
esper_DefaultMethods_name: Property = Property(name="name", type=StringType)
esper_DefaultMethods.attributes={esper_DefaultMethods_name}

# esper_SingleDefinition class attributes and methods
esper_SingleDefinition_name: Property = Property(name="name", type=StringType)
esper_SingleDefinition.attributes={esper_SingleDefinition_name}

# esper_Anything class attributes and methods
esper_Anything_operator: Property = Property(name="operator", type=StringType)
esper_Anything.attributes={esper_Anything_operator}

# esper_Pattern class attributes and methods

# esper_JoinFollowBy class attributes and methods
esper_JoinFollowBy_operator: Property = Property(name="operator", type=StringType)
esper_JoinFollowBy.attributes={esper_JoinFollowBy_operator}

# esper_Win class attributes and methods

# esper_AbstractFollowBy class attributes and methods

# esper_FollowBy class attributes and methods

# esper_FollowByWhere class attributes and methods

# esper_TerminalExpression class attributes and methods
esper_TerminalExpression_every: Property = Property(name="every", type=BooleanType)
esper_TerminalExpression_parenthesis: Property = Property(name="parenthesis", type=BooleanType)
esper_TerminalExpression.attributes={esper_TerminalExpression_every, esper_TerminalExpression_parenthesis}

# esper_KindOfEvent class attributes and methods
esper_KindOfEvent_name: Property = Property(name="name", type=StringType)
esper_KindOfEvent.attributes={esper_KindOfEvent_name}

# esper_Timer class attributes and methods

# ExtraParenthesisRule class attributes and methods

# esper_ExtraParenthesisRule class attributes and methods

# Relationships
rules0: BinaryAssociation = BinaryAssociation(
    name="rules0",
    ends={
        Property(name="esper_RuleParts", type=esper_Domainmodel, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_Domainmodel", type=esper_RuleParts, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="esper_Event", type=esper_Domainmodel, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_Domainmodel2", type=esper_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventattributes3: BinaryAssociation = BinaryAssociation(
    name="eventattributes3",
    ends={
        Property(name="esper_Attributes", type=esper_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_Event4", type=esper_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute5: BinaryAssociation = BinaryAssociation(
    name="attribute5",
    ends={
        Property(name="esper_AttributesDefinition", type=esper_Attributes, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_Attributes6", type=esper_AttributesDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nameRule7: BinaryAssociation = BinaryAssociation(
    name="nameRule7",
    ends={
        Property(name="esper_Name", type=esper_RuleParts, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_RuleParts8", type=esper_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
insert9: BinaryAssociation = BinaryAssociation(
    name="insert9",
    ends={
        Property(name="esper_Insert", type=esper_RuleParts, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_RuleParts10", type=esper_Insert, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
priority11: BinaryAssociation = BinaryAssociation(
    name="priority11",
    ends={
        Property(name="esper_Priority", type=esper_RuleParts, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_RuleParts12", type=esper_Priority, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectRule13: BinaryAssociation = BinaryAssociation(
    name="selectRule13",
    ends={
        Property(name="esper_Select", type=esper_RuleParts, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_RuleParts14", type=esper_Select, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromRule15: BinaryAssociation = BinaryAssociation(
    name="fromRule15",
    ends={
        Property(name="esper_From", type=esper_RuleParts, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_RuleParts16", type=esper_From, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupBy17: BinaryAssociation = BinaryAssociation(
    name="groupBy17",
    ends={
        Property(name="esper_GroupBy", type=esper_RuleParts, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_RuleParts18", type=esper_GroupBy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
having19: BinaryAssociation = BinaryAssociation(
    name="having19",
    ends={
        Property(name="esper_Having", type=esper_RuleParts, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_RuleParts20", type=esper_Having, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectAttributes21: BinaryAssociation = BinaryAssociation(
    name="selectAttributes21",
    ends={
        Property(name="esper_SelectAttributesDefinition", type=esper_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_Select22", type=esper_SelectAttributesDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
singleSelectDefinition23: BinaryAssociation = BinaryAssociation(
    name="singleSelectDefinition23",
    ends={
        Property(name="esper_SingleSelectDefinition", type=esper_KindSelectAttributesDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_KindSelectAttributesDefinition", type=esper_SingleSelectDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultMethod24: BinaryAssociation = BinaryAssociation(
    name="defaultMethod24",
    ends={
        Property(name="esper_DefaultMethods", type=esper_KindSelectAttributesDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_KindSelectAttributesDefinition25", type=esper_DefaultMethods, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightSide26: BinaryAssociation = BinaryAssociation(
    name="rightSide26",
    ends={
        Property(name="esper_KindSelectAttributesDefinition28", type=esper_SelectAttributesDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_SelectAttributesDefinition27", type=esper_KindSelectAttributesDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftSide29: BinaryAssociation = BinaryAssociation(
    name="leftSide29",
    ends={
        Property(name="esper_KindSelectAttributesDefinition31", type=esper_SelectAttributesDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_SelectAttributesDefinition30", type=esper_KindSelectAttributesDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event32: BinaryAssociation = BinaryAssociation(
    name="event32",
    ends={
        Property(name="esper_SingleDefinition", type=esper_SingleSelectDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_SingleSelectDefinition33", type=esper_SingleDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
event34: BinaryAssociation = BinaryAssociation(
    name="event34",
    ends={
        Property(name="esper_Event36", type=esper_From, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_From35", type=esper_Event, multiplicity=Multiplicity(0, 1))
    }
)
anything37: BinaryAssociation = BinaryAssociation(
    name="anything37",
    ends={
        Property(name="esper_Anything", type=esper_From, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_From38", type=esper_Anything, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pattern39: BinaryAssociation = BinaryAssociation(
    name="pattern39",
    ends={
        Property(name="esper_Pattern", type=esper_From, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_From40", type=esper_Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
joinFollowBy41: BinaryAssociation = BinaryAssociation(
    name="joinFollowBy41",
    ends={
        Property(name="esper_JoinFollowBy", type=esper_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_Pattern42", type=esper_JoinFollowBy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
win43: BinaryAssociation = BinaryAssociation(
    name="win43",
    ends={
        Property(name="esper_Win", type=esper_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_Pattern44", type=esper_Win, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
followsByJoinList45: BinaryAssociation = BinaryAssociation(
    name="followsByJoinList45",
    ends={
        Property(name="esper_AbstractFollowBy", type=esper_JoinFollowBy, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_JoinFollowBy46", type=esper_AbstractFollowBy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
followBy47: BinaryAssociation = BinaryAssociation(
    name="followBy47",
    ends={
        Property(name="esper_FollowBy", type=esper_AbstractFollowBy, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_AbstractFollowBy48", type=esper_FollowBy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wherePart49: BinaryAssociation = BinaryAssociation(
    name="wherePart49",
    ends={
        Property(name="esper_FollowByWhere", type=esper_AbstractFollowBy, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_AbstractFollowBy50", type=esper_FollowByWhere, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftSide51: BinaryAssociation = BinaryAssociation(
    name="leftSide51",
    ends={
        Property(name="esper_TerminalExpression", type=esper_FollowBy, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_FollowBy52", type=esper_TerminalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightSide53: BinaryAssociation = BinaryAssociation(
    name="rightSide53",
    ends={
        Property(name="esper_TerminalExpression55", type=esper_FollowBy, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_FollowBy54", type=esper_TerminalExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
everyExpression56: BinaryAssociation = BinaryAssociation(
    name="everyExpression56",
    ends={
        Property(name="esper_FollowBy58", type=esper_TerminalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_TerminalExpression57", type=esper_FollowBy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
betweenParenthesis59: BinaryAssociation = BinaryAssociation(
    name="betweenParenthesis59",
    ends={
        Property(name="esper_FollowBy61", type=esper_TerminalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_TerminalExpression60", type=esper_FollowBy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
singleDefinition62: BinaryAssociation = BinaryAssociation(
    name="singleDefinition62",
    ends={
        Property(name="esper_SingleDefinition64", type=esper_TerminalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_TerminalExpression63", type=esper_SingleDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleEvents65: BinaryAssociation = BinaryAssociation(
    name="simpleEvents65",
    ends={
        Property(name="esper_KindOfEvent", type=esper_SingleDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_SingleDefinition66", type=esper_KindOfEvent, multiplicity=Multiplicity(0, 1))
    }
)
anything67: BinaryAssociation = BinaryAssociation(
    name="anything67",
    ends={
        Property(name="esper_Anything69", type=esper_SingleDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_SingleDefinition68", type=esper_Anything, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultMethod70: BinaryAssociation = BinaryAssociation(
    name="defaultMethod70",
    ends={
        Property(name="esper_DefaultMethods72", type=esper_Win, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_Win71", type=esper_DefaultMethods, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timer73: BinaryAssociation = BinaryAssociation(
    name="timer73",
    ends={
        Property(name="esper_Timer", type=esper_FollowByWhere, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_FollowByWhere74", type=esper_Timer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultMethod75: BinaryAssociation = BinaryAssociation(
    name="defaultMethod75",
    ends={
        Property(name="esper_DefaultMethods77", type=esper_Timer, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_Timer76", type=esper_DefaultMethods, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anything78: BinaryAssociation = BinaryAssociation(
    name="anything78",
    ends={
        Property(name="esper_Anything80", type=esper_GroupBy, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_GroupBy79", type=esper_Anything, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultMethod81: BinaryAssociation = BinaryAssociation(
    name="defaultMethod81",
    ends={
        Property(name="esper_DefaultMethods83", type=esper_Having, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_Having82", type=esper_DefaultMethods, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anything84: BinaryAssociation = BinaryAssociation(
    name="anything84",
    ends={
        Property(name="esper_Anything86", type=esper_Having, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_Having85", type=esper_Anything, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anything87: BinaryAssociation = BinaryAssociation(
    name="anything87",
    ends={
        Property(name="esper_Anything89", type=esper_DefaultMethods, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_DefaultMethods88", type=esper_Anything, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extraParenthesis90: BinaryAssociation = BinaryAssociation(
    name="extraParenthesis90",
    ends={
        Property(name="esper_ExtraParenthesisRule", type=esper_Anything, multiplicity=Multiplicity(1, 1)),
        Property(name="esper_Anything91", type=esper_ExtraParenthesisRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_esper_Event_KindOfEvent = Generalization(general=KindOfEvent, specific=esper_Event)
gen_esper_Insert_KindOfEvent = Generalization(general=KindOfEvent, specific=esper_Insert)
gen_esper_Anything_ExtraParenthesisRule = Generalization(general=ExtraParenthesisRule, specific=esper_Anything)

# Domain Model
domain_model = DomainModel(
    name="esper",
    types={esper_Domainmodel, esper_RuleParts, esper_Event, KindOfEvent, esper_Attributes, esper_AttributesDefinition, esper_Name, esper_Insert, esper_Priority, esper_Select, esper_From, esper_GroupBy, esper_Having, esper_SelectAttributesDefinition, esper_KindSelectAttributesDefinition, esper_SingleSelectDefinition, esper_DefaultMethods, esper_SingleDefinition, esper_Anything, esper_Pattern, esper_JoinFollowBy, esper_Win, esper_AbstractFollowBy, esper_FollowBy, esper_FollowByWhere, esper_TerminalExpression, esper_KindOfEvent, esper_Timer, ExtraParenthesisRule, esper_ExtraParenthesisRule, Operators},
    associations={rules0, events1, eventattributes3, attribute5, nameRule7, insert9, priority11, selectRule13, fromRule15, groupBy17, having19, selectAttributes21, singleSelectDefinition23, defaultMethod24, rightSide26, leftSide29, event32, event34, anything37, pattern39, joinFollowBy41, win43, followsByJoinList45, followBy47, wherePart49, leftSide51, rightSide53, everyExpression56, betweenParenthesis59, singleDefinition62, simpleEvents65, anything67, defaultMethod70, timer73, defaultMethod75, anything78, defaultMethod81, anything84, anything87, extraParenthesis90},
    generalizations={gen_esper_Event_KindOfEvent, gen_esper_Insert_KindOfEvent, gen_esper_Anything_ExtraParenthesisRule},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)