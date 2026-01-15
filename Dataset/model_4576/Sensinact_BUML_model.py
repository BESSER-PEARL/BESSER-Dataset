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
sensinact_DSL_IfDo = Class(name="sensinact::DSL::IfDo")
sensinact_DSL_ElseIfDo = Class(name="sensinact::DSL::ElseIfDo")
sensinact_DSL_ElseDo = Class(name="sensinact::DSL::ElseDo")
sensinact_DSL_Expression = Class(name="sensinact::DSL::Expression")
sensinact_DSL_ListActions = Class(name="sensinact::DSL::ListActions")
sensinact_Sensinact = Class(name="sensinact::Sensinact")
sensinact_DSL_SENSINACT = Class(name="sensinact::DSL::SENSINACT")
sensinact_DSL_FLAG_AUTOSTART = Class(name="sensinact::DSL::FLAG::AUTOSTART")
sensinact_DSL_Resource = Class(name="sensinact::DSL::Resource")
sensinact_DSL_CEP_STATEMENT = Class(name="sensinact::DSL::CEP::STATEMENT")
sensinact_DSL_On = Class(name="sensinact::DSL::On")
sensinact_DSL_ECA_STATEMENT = Class(name="sensinact::DSL::ECA::STATEMENT")
DSL_REF = Class(name="DSL::REF")
sensinact_DSL_REF_CONDITION = Class(name="sensinact::DSL::REF::CONDITION")
sensinact_DSL_CEP_COINCIDE = Class(name="sensinact::DSL::CEP::COINCIDE")
sensinact_DSL_CEP_MIN = Class(name="sensinact::DSL::CEP::MIN")
sensinact_DSL_CEP_MAX = Class(name="sensinact::DSL::CEP::MAX")
sensinact_DSL_REF = Class(name="sensinact::DSL::REF")
sensinact_EObject = Class(name="sensinact::EObject")
sensinact_DSL_CEP_AFTER = Class(name="sensinact::DSL::CEP::AFTER")
sensinact_DSL_CEP_DURATION = Class(name="sensinact::DSL::CEP::DURATION")
sensinact_DSL_CEP_BEFORE = Class(name="sensinact::DSL::CEP::BEFORE")
sensinact_DSL_Expression_Or = Class(name="sensinact::DSL::Expression::Or")
DSL_Expression = Class(name="DSL::Expression")
sensinact_DSL_Expression_And = Class(name="sensinact::DSL::Expression::And")
sensinact_DSL_Expression_Diff = Class(name="sensinact::DSL::Expression::Diff")
sensinact_DSL_CEP_AVG = Class(name="sensinact::DSL::CEP::AVG")
sensinact_DSL_CEP_SUM = Class(name="sensinact::DSL::CEP::SUM")
sensinact_DSL_CEP_COUNT = Class(name="sensinact::DSL::CEP::COUNT")
sensinact_DSL_CEP_DURATION_MIN = Class(name="sensinact::DSL::CEP::DURATION::MIN")
sensinact_DSL_CEP_DURATION_SEC = Class(name="sensinact::DSL::CEP::DURATION::SEC")
sensinact_DSL_ResourceAction = Class(name="sensinact::DSL::ResourceAction")
sensinact_DSL_ListParam = Class(name="sensinact::DSL::ListParam")
sensinact_DSL_Expression_Plus = Class(name="sensinact::DSL::Expression::Plus")
sensinact_DSL_Expression_Minus = Class(name="sensinact::DSL::Expression::Minus")
sensinact_DSL_Expression_Multiplication = Class(name="sensinact::DSL::Expression::Multiplication")
sensinact_DSL_Expression_Equal = Class(name="sensinact::DSL::Expression::Equal")
sensinact_DSL_Expression_Larger = Class(name="sensinact::DSL::Expression::Larger")
sensinact_DSL_Expression_Larger_Equal = Class(name="sensinact::DSL::Expression::Larger::Equal")
sensinact_DSL_Expression_Smaller = Class(name="sensinact::DSL::Expression::Smaller")
sensinact_DSL_Expression_Smaller_Equal = Class(name="sensinact::DSL::Expression::Smaller::Equal")
sensinact_DSL_Expression_Division = Class(name="sensinact::DSL::Expression::Division")
sensinact_DSL_Expression_Modulo = Class(name="sensinact::DSL::Expression::Modulo")
sensinact_DSL_Object_Number = Class(name="sensinact::DSL::Object::Number")
sensinact_DSL_Object_String = Class(name="sensinact::DSL::Object::String")
sensinact_DSL_Object_Boolean = Class(name="sensinact::DSL::Object::Boolean")
sensinact_DSL_Object_Ref = Class(name="sensinact::DSL::Object::Ref")
sensinact_DSL_Expression_Negate = Class(name="sensinact::DSL::Expression::Negate")

# sensinact_DSL_IfDo class attributes and methods

# sensinact_DSL_ElseIfDo class attributes and methods

# sensinact_DSL_ElseDo class attributes and methods

# sensinact_DSL_Expression class attributes and methods

# sensinact_DSL_ListActions class attributes and methods

# sensinact_Sensinact class attributes and methods

# sensinact_DSL_SENSINACT class attributes and methods

# sensinact_DSL_FLAG_AUTOSTART class attributes and methods
sensinact_DSL_FLAG_AUTOSTART_activated: Property = Property(name="activated", type=BooleanType)
sensinact_DSL_FLAG_AUTOSTART.attributes={sensinact_DSL_FLAG_AUTOSTART_activated}

# sensinact_DSL_Resource class attributes and methods
sensinact_DSL_Resource_gatewayID: Property = Property(name="gatewayID", type=StringType)
sensinact_DSL_Resource_deviceID: Property = Property(name="deviceID", type=StringType)
sensinact_DSL_Resource_serviceID: Property = Property(name="serviceID", type=StringType)
sensinact_DSL_Resource_resourceID: Property = Property(name="resourceID", type=StringType)
sensinact_DSL_Resource.attributes={sensinact_DSL_Resource_gatewayID, sensinact_DSL_Resource_resourceID, sensinact_DSL_Resource_deviceID, sensinact_DSL_Resource_serviceID}

# sensinact_DSL_CEP_STATEMENT class attributes and methods

# sensinact_DSL_On class attributes and methods

# sensinact_DSL_ECA_STATEMENT class attributes and methods

# DSL_REF class attributes and methods

# sensinact_DSL_REF_CONDITION class attributes and methods

# sensinact_DSL_CEP_COINCIDE class attributes and methods

# sensinact_DSL_CEP_MIN class attributes and methods

# sensinact_DSL_CEP_MAX class attributes and methods

# sensinact_DSL_REF class attributes and methods
sensinact_DSL_REF_name: Property = Property(name="name", type=StringType)
sensinact_DSL_REF.attributes={sensinact_DSL_REF_name}

# sensinact_EObject class attributes and methods

# sensinact_DSL_CEP_AFTER class attributes and methods

# sensinact_DSL_CEP_DURATION class attributes and methods

# sensinact_DSL_CEP_BEFORE class attributes and methods

# sensinact_DSL_Expression_Or class attributes and methods

# DSL_Expression class attributes and methods

# sensinact_DSL_Expression_And class attributes and methods

# sensinact_DSL_Expression_Diff class attributes and methods

# sensinact_DSL_CEP_AVG class attributes and methods

# sensinact_DSL_CEP_SUM class attributes and methods

# sensinact_DSL_CEP_COUNT class attributes and methods

# sensinact_DSL_CEP_DURATION_MIN class attributes and methods
sensinact_DSL_CEP_DURATION_MIN_min: Property = Property(name="min", type=StringType)
sensinact_DSL_CEP_DURATION_MIN.attributes={sensinact_DSL_CEP_DURATION_MIN_min}

# sensinact_DSL_CEP_DURATION_SEC class attributes and methods
sensinact_DSL_CEP_DURATION_SEC_sec: Property = Property(name="sec", type=StringType)
sensinact_DSL_CEP_DURATION_SEC.attributes={sensinact_DSL_CEP_DURATION_SEC_sec}

# sensinact_DSL_ResourceAction class attributes and methods
sensinact_DSL_ResourceAction_variable: Property = Property(name="variable", type=StringType)
sensinact_DSL_ResourceAction_actiontype: Property = Property(name="actiontype", type=StringType)
sensinact_DSL_ResourceAction.attributes={sensinact_DSL_ResourceAction_variable, sensinact_DSL_ResourceAction_actiontype}

# sensinact_DSL_ListParam class attributes and methods

# sensinact_DSL_Expression_Plus class attributes and methods

# sensinact_DSL_Expression_Minus class attributes and methods

# sensinact_DSL_Expression_Multiplication class attributes and methods

# sensinact_DSL_Expression_Equal class attributes and methods

# sensinact_DSL_Expression_Larger class attributes and methods

# sensinact_DSL_Expression_Larger_Equal class attributes and methods

# sensinact_DSL_Expression_Smaller class attributes and methods

# sensinact_DSL_Expression_Smaller_Equal class attributes and methods

# sensinact_DSL_Expression_Division class attributes and methods

# sensinact_DSL_Expression_Modulo class attributes and methods

# sensinact_DSL_Object_Number class attributes and methods
sensinact_DSL_Object_Number_value: Property = Property(name="value", type=StringType)
sensinact_DSL_Object_Number.attributes={sensinact_DSL_Object_Number_value}

# sensinact_DSL_Object_String class attributes and methods
sensinact_DSL_Object_String_value: Property = Property(name="value", type=StringType)
sensinact_DSL_Object_String.attributes={sensinact_DSL_Object_String_value}

# sensinact_DSL_Object_Boolean class attributes and methods
sensinact_DSL_Object_Boolean_value: Property = Property(name="value", type=BooleanType)
sensinact_DSL_Object_Boolean.attributes={sensinact_DSL_Object_Boolean_value}

# sensinact_DSL_Object_Ref class attributes and methods

# sensinact_DSL_Expression_Negate class attributes and methods

# Relationships
ifdo13: BinaryAssociation = BinaryAssociation(
    name="ifdo13",
    ends={
        Property(name="sensinact_DSL_IfDo", type=sensinact_DSL_ECA_STATEMENT, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_ECA_STATEMENT14", type=sensinact_DSL_IfDo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIfdo15: BinaryAssociation = BinaryAssociation(
    name="elseIfdo15",
    ends={
        Property(name="sensinact_DSL_ElseIfDo", type=sensinact_DSL_ECA_STATEMENT, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_ECA_STATEMENT16", type=sensinact_DSL_ElseIfDo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsedo17: BinaryAssociation = BinaryAssociation(
    name="elsedo17",
    ends={
        Property(name="sensinact_DSL_ElseDo", type=sensinact_DSL_ECA_STATEMENT, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_ECA_STATEMENT18", type=sensinact_DSL_ElseDo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition19: BinaryAssociation = BinaryAssociation(
    name="condition19",
    ends={
        Property(name="sensinact_DSL_Expression", type=sensinact_DSL_IfDo, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_IfDo20", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions21: BinaryAssociation = BinaryAssociation(
    name="actions21",
    ends={
        Property(name="sensinact_DSL_ListActions", type=sensinact_DSL_IfDo, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_IfDo22", type=sensinact_DSL_ListActions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition23: BinaryAssociation = BinaryAssociation(
    name="condition23",
    ends={
        Property(name="sensinact_DSL_Expression25", type=sensinact_DSL_ElseIfDo, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_ElseIfDo24", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions26: BinaryAssociation = BinaryAssociation(
    name="actions26",
    ends={
        Property(name="sensinact_DSL_ListActions28", type=sensinact_DSL_ElseIfDo, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_ElseIfDo27", type=sensinact_DSL_ListActions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eca0: BinaryAssociation = BinaryAssociation(
    name="eca0",
    ends={
        Property(name="sensinact_DSL_SENSINACT", type=sensinact_Sensinact, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_Sensinact", type=sensinact_DSL_SENSINACT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
autostart1: BinaryAssociation = BinaryAssociation(
    name="autostart1",
    ends={
        Property(name="sensinact_DSL_FLAG_AUTOSTART", type=sensinact_DSL_SENSINACT, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_SENSINACT2", type=sensinact_DSL_FLAG_AUTOSTART, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resources3: BinaryAssociation = BinaryAssociation(
    name="resources3",
    ends={
        Property(name="sensinact_DSL_Resource", type=sensinact_DSL_SENSINACT, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_SENSINACT4", type=sensinact_DSL_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cep5: BinaryAssociation = BinaryAssociation(
    name="cep5",
    ends={
        Property(name="sensinact_DSL_CEP_STATEMENT", type=sensinact_DSL_SENSINACT, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_SENSINACT6", type=sensinact_DSL_CEP_STATEMENT, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
on7: BinaryAssociation = BinaryAssociation(
    name="on7",
    ends={
        Property(name="sensinact_DSL_On", type=sensinact_DSL_SENSINACT, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_SENSINACT8", type=sensinact_DSL_On, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eca9: BinaryAssociation = BinaryAssociation(
    name="eca9",
    ends={
        Property(name="sensinact_DSL_ECA_STATEMENT", type=sensinact_DSL_SENSINACT, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_SENSINACT10", type=sensinact_DSL_ECA_STATEMENT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggers11: BinaryAssociation = BinaryAssociation(
    name="triggers11",
    ends={
        Property(name="sensinact_DSL_REF_CONDITION", type=sensinact_DSL_On, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_On12", type=sensinact_DSL_REF_CONDITION, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
end54: BinaryAssociation = BinaryAssociation(
    name="end54",
    ends={
        Property(name="sensinact_DSL_CEP_DURATION56", type=sensinact_DSL_CEP_BEFORE, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_BEFORE55", type=sensinact_DSL_CEP_DURATION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref157: BinaryAssociation = BinaryAssociation(
    name="ref157",
    ends={
        Property(name="sensinact_DSL_REF_CONDITION58", type=sensinact_DSL_CEP_COINCIDE, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_COINCIDE", type=sensinact_DSL_REF_CONDITION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref259: BinaryAssociation = BinaryAssociation(
    name="ref259",
    ends={
        Property(name="sensinact_DSL_REF_CONDITION61", type=sensinact_DSL_CEP_COINCIDE, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_COINCIDE60", type=sensinact_DSL_REF_CONDITION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
window62: BinaryAssociation = BinaryAssociation(
    name="window62",
    ends={
        Property(name="sensinact_DSL_CEP_DURATION64", type=sensinact_DSL_CEP_COINCIDE, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_COINCIDE63", type=sensinact_DSL_CEP_DURATION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref65: BinaryAssociation = BinaryAssociation(
    name="ref65",
    ends={
        Property(name="sensinact_DSL_REF_CONDITION66", type=sensinact_DSL_CEP_MIN, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_MIN", type=sensinact_DSL_REF_CONDITION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
window67: BinaryAssociation = BinaryAssociation(
    name="window67",
    ends={
        Property(name="sensinact_DSL_CEP_DURATION69", type=sensinact_DSL_CEP_MIN, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_MIN68", type=sensinact_DSL_CEP_DURATION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref70: BinaryAssociation = BinaryAssociation(
    name="ref70",
    ends={
        Property(name="sensinact_DSL_REF_CONDITION71", type=sensinact_DSL_CEP_MAX, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_MAX", type=sensinact_DSL_REF_CONDITION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
window72: BinaryAssociation = BinaryAssociation(
    name="window72",
    ends={
        Property(name="sensinact_DSL_CEP_DURATION74", type=sensinact_DSL_CEP_MAX, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_MAX73", type=sensinact_DSL_CEP_DURATION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions29: BinaryAssociation = BinaryAssociation(
    name="actions29",
    ends={
        Property(name="sensinact_DSL_ListActions31", type=sensinact_DSL_ElseDo, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_ElseDo30", type=sensinact_DSL_ListActions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref32: BinaryAssociation = BinaryAssociation(
    name="ref32",
    ends={
        Property(name="sensinact_DSL_REF", type=sensinact_DSL_REF_CONDITION, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_REF_CONDITION33", type=sensinact_DSL_REF, multiplicity=Multiplicity(0, 1))
    }
)
operation34: BinaryAssociation = BinaryAssociation(
    name="operation34",
    ends={
        Property(name="sensinact_EObject", type=sensinact_DSL_CEP_STATEMENT, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_STATEMENT35", type=sensinact_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref136: BinaryAssociation = BinaryAssociation(
    name="ref136",
    ends={
        Property(name="sensinact_DSL_REF_CONDITION37", type=sensinact_DSL_CEP_AFTER, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_AFTER", type=sensinact_DSL_REF_CONDITION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref238: BinaryAssociation = BinaryAssociation(
    name="ref238",
    ends={
        Property(name="sensinact_DSL_REF_CONDITION40", type=sensinact_DSL_CEP_AFTER, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_AFTER39", type=sensinact_DSL_REF_CONDITION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start41: BinaryAssociation = BinaryAssociation(
    name="start41",
    ends={
        Property(name="sensinact_DSL_CEP_DURATION", type=sensinact_DSL_CEP_AFTER, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_AFTER42", type=sensinact_DSL_CEP_DURATION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end43: BinaryAssociation = BinaryAssociation(
    name="end43",
    ends={
        Property(name="sensinact_DSL_CEP_DURATION45", type=sensinact_DSL_CEP_AFTER, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_AFTER44", type=sensinact_DSL_CEP_DURATION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref146: BinaryAssociation = BinaryAssociation(
    name="ref146",
    ends={
        Property(name="sensinact_DSL_REF_CONDITION47", type=sensinact_DSL_CEP_BEFORE, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_BEFORE", type=sensinact_DSL_REF_CONDITION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref248: BinaryAssociation = BinaryAssociation(
    name="ref248",
    ends={
        Property(name="sensinact_DSL_REF_CONDITION50", type=sensinact_DSL_CEP_BEFORE, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_BEFORE49", type=sensinact_DSL_REF_CONDITION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start51: BinaryAssociation = BinaryAssociation(
    name="start51",
    ends={
        Property(name="sensinact_DSL_CEP_DURATION53", type=sensinact_DSL_CEP_BEFORE, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_BEFORE52", type=sensinact_DSL_CEP_DURATION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
listParam98: BinaryAssociation = BinaryAssociation(
    name="listParam98",
    ends={
        Property(name="sensinact_DSL_ListParam", type=sensinact_DSL_ResourceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_ResourceAction99", type=sensinact_DSL_ListParam, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param100: BinaryAssociation = BinaryAssociation(
    name="param100",
    ends={
        Property(name="sensinact_DSL_Expression102", type=sensinact_DSL_ListParam, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_ListParam101", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left103: BinaryAssociation = BinaryAssociation(
    name="left103",
    ends={
        Property(name="sensinact_DSL_Expression104", type=sensinact_DSL_Expression_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Or", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right105: BinaryAssociation = BinaryAssociation(
    name="right105",
    ends={
        Property(name="sensinact_DSL_Expression107", type=sensinact_DSL_Expression_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Or106", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left108: BinaryAssociation = BinaryAssociation(
    name="left108",
    ends={
        Property(name="sensinact_DSL_Expression109", type=sensinact_DSL_Expression_And, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_And", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right110: BinaryAssociation = BinaryAssociation(
    name="right110",
    ends={
        Property(name="sensinact_DSL_Expression112", type=sensinact_DSL_Expression_And, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_And111", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left113: BinaryAssociation = BinaryAssociation(
    name="left113",
    ends={
        Property(name="sensinact_DSL_Expression114", type=sensinact_DSL_Expression_Diff, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Diff", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref75: BinaryAssociation = BinaryAssociation(
    name="ref75",
    ends={
        Property(name="sensinact_DSL_REF_CONDITION76", type=sensinact_DSL_CEP_AVG, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_AVG", type=sensinact_DSL_REF_CONDITION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
window77: BinaryAssociation = BinaryAssociation(
    name="window77",
    ends={
        Property(name="sensinact_DSL_CEP_DURATION79", type=sensinact_DSL_CEP_AVG, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_AVG78", type=sensinact_DSL_CEP_DURATION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref80: BinaryAssociation = BinaryAssociation(
    name="ref80",
    ends={
        Property(name="sensinact_DSL_REF_CONDITION81", type=sensinact_DSL_CEP_SUM, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_SUM", type=sensinact_DSL_REF_CONDITION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
window82: BinaryAssociation = BinaryAssociation(
    name="window82",
    ends={
        Property(name="sensinact_DSL_CEP_DURATION84", type=sensinact_DSL_CEP_SUM, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_SUM83", type=sensinact_DSL_CEP_DURATION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref85: BinaryAssociation = BinaryAssociation(
    name="ref85",
    ends={
        Property(name="sensinact_DSL_REF_CONDITION86", type=sensinact_DSL_CEP_COUNT, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_COUNT", type=sensinact_DSL_REF_CONDITION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
window87: BinaryAssociation = BinaryAssociation(
    name="window87",
    ends={
        Property(name="sensinact_DSL_CEP_DURATION89", type=sensinact_DSL_CEP_COUNT, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_COUNT88", type=sensinact_DSL_CEP_DURATION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
units90: BinaryAssociation = BinaryAssociation(
    name="units90",
    ends={
        Property(name="sensinact_EObject92", type=sensinact_DSL_CEP_DURATION, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_CEP_DURATION91", type=sensinact_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionList93: BinaryAssociation = BinaryAssociation(
    name="actionList93",
    ends={
        Property(name="sensinact_DSL_ResourceAction", type=sensinact_DSL_ListActions, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_ListActions94", type=sensinact_DSL_ResourceAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref95: BinaryAssociation = BinaryAssociation(
    name="ref95",
    ends={
        Property(name="sensinact_DSL_REF97", type=sensinact_DSL_ResourceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_ResourceAction96", type=sensinact_DSL_REF, multiplicity=Multiplicity(0, 1))
    }
)
right140: BinaryAssociation = BinaryAssociation(
    name="right140",
    ends={
        Property(name="sensinact_DSL_Expression142", type=sensinact_DSL_Expression_Smaller_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Smaller_Equal141", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left143: BinaryAssociation = BinaryAssociation(
    name="left143",
    ends={
        Property(name="sensinact_DSL_Expression144", type=sensinact_DSL_Expression_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Plus", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right145: BinaryAssociation = BinaryAssociation(
    name="right145",
    ends={
        Property(name="sensinact_DSL_Expression147", type=sensinact_DSL_Expression_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Plus146", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left148: BinaryAssociation = BinaryAssociation(
    name="left148",
    ends={
        Property(name="sensinact_DSL_Expression149", type=sensinact_DSL_Expression_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Minus", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right150: BinaryAssociation = BinaryAssociation(
    name="right150",
    ends={
        Property(name="sensinact_DSL_Expression152", type=sensinact_DSL_Expression_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Minus151", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left153: BinaryAssociation = BinaryAssociation(
    name="left153",
    ends={
        Property(name="sensinact_DSL_Expression154", type=sensinact_DSL_Expression_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Multiplication", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right115: BinaryAssociation = BinaryAssociation(
    name="right115",
    ends={
        Property(name="sensinact_DSL_Expression117", type=sensinact_DSL_Expression_Diff, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Diff116", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left118: BinaryAssociation = BinaryAssociation(
    name="left118",
    ends={
        Property(name="sensinact_DSL_Expression119", type=sensinact_DSL_Expression_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Equal", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right120: BinaryAssociation = BinaryAssociation(
    name="right120",
    ends={
        Property(name="sensinact_DSL_Expression122", type=sensinact_DSL_Expression_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Equal121", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left123: BinaryAssociation = BinaryAssociation(
    name="left123",
    ends={
        Property(name="sensinact_DSL_Expression124", type=sensinact_DSL_Expression_Larger, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Larger", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right125: BinaryAssociation = BinaryAssociation(
    name="right125",
    ends={
        Property(name="sensinact_DSL_Expression127", type=sensinact_DSL_Expression_Larger, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Larger126", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left128: BinaryAssociation = BinaryAssociation(
    name="left128",
    ends={
        Property(name="sensinact_DSL_Expression129", type=sensinact_DSL_Expression_Larger_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Larger_Equal", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right130: BinaryAssociation = BinaryAssociation(
    name="right130",
    ends={
        Property(name="sensinact_DSL_Expression132", type=sensinact_DSL_Expression_Larger_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Larger_Equal131", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left133: BinaryAssociation = BinaryAssociation(
    name="left133",
    ends={
        Property(name="sensinact_DSL_Expression134", type=sensinact_DSL_Expression_Smaller, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Smaller", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right135: BinaryAssociation = BinaryAssociation(
    name="right135",
    ends={
        Property(name="sensinact_DSL_Expression137", type=sensinact_DSL_Expression_Smaller, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Smaller136", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left138: BinaryAssociation = BinaryAssociation(
    name="left138",
    ends={
        Property(name="sensinact_DSL_Expression139", type=sensinact_DSL_Expression_Smaller_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Smaller_Equal", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right155: BinaryAssociation = BinaryAssociation(
    name="right155",
    ends={
        Property(name="sensinact_DSL_Expression157", type=sensinact_DSL_Expression_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Multiplication156", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left158: BinaryAssociation = BinaryAssociation(
    name="left158",
    ends={
        Property(name="sensinact_DSL_Expression159", type=sensinact_DSL_Expression_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Division", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right160: BinaryAssociation = BinaryAssociation(
    name="right160",
    ends={
        Property(name="sensinact_DSL_Expression162", type=sensinact_DSL_Expression_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Division161", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left163: BinaryAssociation = BinaryAssociation(
    name="left163",
    ends={
        Property(name="sensinact_DSL_Expression164", type=sensinact_DSL_Expression_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Modulo", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right165: BinaryAssociation = BinaryAssociation(
    name="right165",
    ends={
        Property(name="sensinact_DSL_Expression167", type=sensinact_DSL_Expression_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Modulo166", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value168: BinaryAssociation = BinaryAssociation(
    name="value168",
    ends={
        Property(name="sensinact_DSL_REF169", type=sensinact_DSL_Object_Ref, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Object_Ref", type=sensinact_DSL_REF, multiplicity=Multiplicity(0, 1))
    }
)
exp170: BinaryAssociation = BinaryAssociation(
    name="exp170",
    ends={
        Property(name="sensinact_DSL_Expression171", type=sensinact_DSL_Expression_Negate, multiplicity=Multiplicity(1, 1)),
        Property(name="sensinact_DSL_Expression_Negate", type=sensinact_DSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_sensinact_DSL_Resource_DSL_REF = Generalization(general=DSL_REF, specific=sensinact_DSL_Resource)
gen_sensinact_DSL_CEP_STATEMENT_DSL_REF = Generalization(general=DSL_REF, specific=sensinact_DSL_CEP_STATEMENT)
gen_sensinact_DSL_Expression_Or_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Expression_Or)
gen_sensinact_DSL_Expression_And_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Expression_And)
gen_sensinact_DSL_Expression_Diff_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Expression_Diff)
gen_sensinact_DSL_Expression_Plus_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Expression_Plus)
gen_sensinact_DSL_Expression_Minus_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Expression_Minus)
gen_sensinact_DSL_Expression_Multiplication_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Expression_Multiplication)
gen_sensinact_DSL_Expression_Equal_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Expression_Equal)
gen_sensinact_DSL_Expression_Larger_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Expression_Larger)
gen_sensinact_DSL_Expression_Larger_Equal_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Expression_Larger_Equal)
gen_sensinact_DSL_Expression_Smaller_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Expression_Smaller)
gen_sensinact_DSL_Expression_Smaller_Equal_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Expression_Smaller_Equal)
gen_sensinact_DSL_Expression_Division_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Expression_Division)
gen_sensinact_DSL_Expression_Modulo_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Expression_Modulo)
gen_sensinact_DSL_Object_Number_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Object_Number)
gen_sensinact_DSL_Object_String_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Object_String)
gen_sensinact_DSL_Object_Boolean_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Object_Boolean)
gen_sensinact_DSL_Object_Ref_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Object_Ref)
gen_sensinact_DSL_Expression_Negate_DSL_Expression = Generalization(general=DSL_Expression, specific=sensinact_DSL_Expression_Negate)

# Domain Model
domain_model = DomainModel(
    name="sensinact",
    types={sensinact_DSL_IfDo, sensinact_DSL_ElseIfDo, sensinact_DSL_ElseDo, sensinact_DSL_Expression, sensinact_DSL_ListActions, sensinact_Sensinact, sensinact_DSL_SENSINACT, sensinact_DSL_FLAG_AUTOSTART, sensinact_DSL_Resource, sensinact_DSL_CEP_STATEMENT, sensinact_DSL_On, sensinact_DSL_ECA_STATEMENT, DSL_REF, sensinact_DSL_REF_CONDITION, sensinact_DSL_CEP_COINCIDE, sensinact_DSL_CEP_MIN, sensinact_DSL_CEP_MAX, sensinact_DSL_REF, sensinact_EObject, sensinact_DSL_CEP_AFTER, sensinact_DSL_CEP_DURATION, sensinact_DSL_CEP_BEFORE, sensinact_DSL_Expression_Or, DSL_Expression, sensinact_DSL_Expression_And, sensinact_DSL_Expression_Diff, sensinact_DSL_CEP_AVG, sensinact_DSL_CEP_SUM, sensinact_DSL_CEP_COUNT, sensinact_DSL_CEP_DURATION_MIN, sensinact_DSL_CEP_DURATION_SEC, sensinact_DSL_ResourceAction, sensinact_DSL_ListParam, sensinact_DSL_Expression_Plus, sensinact_DSL_Expression_Minus, sensinact_DSL_Expression_Multiplication, sensinact_DSL_Expression_Equal, sensinact_DSL_Expression_Larger, sensinact_DSL_Expression_Larger_Equal, sensinact_DSL_Expression_Smaller, sensinact_DSL_Expression_Smaller_Equal, sensinact_DSL_Expression_Division, sensinact_DSL_Expression_Modulo, sensinact_DSL_Object_Number, sensinact_DSL_Object_String, sensinact_DSL_Object_Boolean, sensinact_DSL_Object_Ref, sensinact_DSL_Expression_Negate},
    associations={ifdo13, elseIfdo15, elsedo17, condition19, actions21, condition23, actions26, eca0, autostart1, resources3, cep5, on7, eca9, triggers11, end54, ref157, ref259, window62, ref65, window67, ref70, window72, actions29, ref32, operation34, ref136, ref238, start41, end43, ref146, ref248, start51, listParam98, param100, left103, right105, left108, right110, left113, ref75, window77, ref80, window82, ref85, window87, units90, actionList93, ref95, right140, left143, right145, left148, right150, left153, right115, left118, right120, left123, right125, left128, right130, left133, right135, left138, right155, left158, right160, left163, right165, value168, exp170},
    generalizations={gen_sensinact_DSL_Resource_DSL_REF, gen_sensinact_DSL_CEP_STATEMENT_DSL_REF, gen_sensinact_DSL_Expression_Or_DSL_Expression, gen_sensinact_DSL_Expression_And_DSL_Expression, gen_sensinact_DSL_Expression_Diff_DSL_Expression, gen_sensinact_DSL_Expression_Plus_DSL_Expression, gen_sensinact_DSL_Expression_Minus_DSL_Expression, gen_sensinact_DSL_Expression_Multiplication_DSL_Expression, gen_sensinact_DSL_Expression_Equal_DSL_Expression, gen_sensinact_DSL_Expression_Larger_DSL_Expression, gen_sensinact_DSL_Expression_Larger_Equal_DSL_Expression, gen_sensinact_DSL_Expression_Smaller_DSL_Expression, gen_sensinact_DSL_Expression_Smaller_Equal_DSL_Expression, gen_sensinact_DSL_Expression_Division_DSL_Expression, gen_sensinact_DSL_Expression_Modulo_DSL_Expression, gen_sensinact_DSL_Object_Number_DSL_Expression, gen_sensinact_DSL_Object_String_DSL_Expression, gen_sensinact_DSL_Object_Boolean_DSL_Expression, gen_sensinact_DSL_Object_Ref_DSL_Expression, gen_sensinact_DSL_Expression_Negate_DSL_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)