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
BaseTypeEnum: Enumeration = Enumeration(
    name="BaseTypeEnum",
    literals={
            EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="BOOLEAN")
    }
)

Severity: Enumeration = Enumeration(
    name="Severity",
    literals={
            EnumerationLiteral(name="ERROR"),
			EnumerationLiteral(name="WARNING")
    }
)

# Classes
altarica_Model = Class(name="altarica::Model")
altarica_Error = Class(name="altarica::Error")
altarica_AbstractDeclaration = Class(name="altarica::AbstractDeclaration")
altarica_NamedElement = Class(name="altarica::NamedElement")
altarica_Declaration = Class(name="altarica::Declaration")
altarica_LabeledTransition = Class(name="altarica::LabeledTransition")
altarica_NameRef = Class(name="altarica::NameRef")
altarica_TransitionExpression = Class(name="altarica::TransitionExpression")
altarica_Instruction = Class(name="altarica::Instruction")
altarica_CaseExpression = Class(name="altarica::CaseExpression")
AbstractDeclaration = Class(name="AbstractDeclaration")
Declaration = Class(name="Declaration")
altarica_Type = Class(name="altarica::Type")
altarica_BaseType = Class(name="altarica::BaseType")
Type = Class(name="Type")
altarica_NamedType = Class(name="altarica::NamedType")
altarica_SwitchExpression = Class(name="altarica::SwitchExpression")
altarica_EObject = Class(name="altarica::EObject")
altarica_Expression = Class(name="altarica::Expression")
altarica_ARBoolean = Class(name="altarica::ARBoolean")
Expression = Class(name="Expression")
altarica_ARString = Class(name="altarica::ARString")
altarica_ARNumber = Class(name="altarica::ARNumber")
altarica_Node = Class(name="altarica::Node")
altarica_Variable = Class(name="altarica::Variable")
altarica_Domain = Class(name="altarica::Domain")
NamedElement = Class(name="NamedElement")
altarica_SymbolicConstant = Class(name="altarica::SymbolicConstant")
altarica_Observer = Class(name="altarica::Observer")
altarica_TransitionAnd = Class(name="altarica::TransitionAnd")
TransitionExpression = Class(name="TransitionExpression")
altarica_Attribute = Class(name="altarica::Attribute")
altarica_Event = Class(name="altarica::Event")
altarica_Parameter = Class(name="altarica::Parameter")
altarica_Skip = Class(name="altarica::Skip")
Instruction = Class(name="Instruction")
altarica_Assignment = Class(name="altarica::Assignment")
altarica_Block = Class(name="altarica::Block")
altarica_Conditional = Class(name="altarica::Conditional")
altarica_TransitionOr = Class(name="altarica::TransitionOr")
altarica_Transition = Class(name="altarica::Transition")
altarica_Equal = Class(name="altarica::Equal")
altarica_Addition = Class(name="altarica::Addition")
altarica_LogicalOr = Class(name="altarica::LogicalOr")
altarica_LogicalAnd = Class(name="altarica::LogicalAnd")
altarica_Not = Class(name="altarica::Not")
altarica_Minus = Class(name="altarica::Minus")
altarica_FunctionCall = Class(name="altarica::FunctionCall")
altarica_Multiplication = Class(name="altarica::Multiplication")

# altarica_Model class attributes and methods

# altarica_Error class attributes and methods
altarica_Error_severity: Property = Property(name="severity", type=StringType)
altarica_Error_message: Property = Property(name="message", type=StringType)
altarica_Error.attributes={altarica_Error_severity, altarica_Error_message}

# altarica_AbstractDeclaration class attributes and methods

# altarica_NamedElement class attributes and methods
altarica_NamedElement_name: Property = Property(name="name", type=StringType)
altarica_NamedElement.attributes={altarica_NamedElement_name}

# altarica_Declaration class attributes and methods

# altarica_LabeledTransition class attributes and methods

# altarica_NameRef class attributes and methods

# altarica_TransitionExpression class attributes and methods

# altarica_Instruction class attributes and methods

# altarica_CaseExpression class attributes and methods

# AbstractDeclaration class attributes and methods

# Declaration class attributes and methods

# altarica_Type class attributes and methods

# altarica_BaseType class attributes and methods
altarica_BaseType_name: Property = Property(name="name", type=StringType)
altarica_BaseType.attributes={altarica_BaseType_name}

# Type class attributes and methods

# altarica_NamedType class attributes and methods

# altarica_SwitchExpression class attributes and methods

# altarica_EObject class attributes and methods

# altarica_Expression class attributes and methods

# altarica_ARBoolean class attributes and methods
altarica_ARBoolean_value: Property = Property(name="value", type=StringType)
altarica_ARBoolean.attributes={altarica_ARBoolean_value}

# Expression class attributes and methods

# altarica_ARString class attributes and methods
altarica_ARString_value: Property = Property(name="value", type=StringType)
altarica_ARString.attributes={altarica_ARString_value}

# altarica_ARNumber class attributes and methods
altarica_ARNumber_value: Property = Property(name="value", type=FloatType)
altarica_ARNumber.attributes={altarica_ARNumber_value}

# altarica_Node class attributes and methods

# altarica_Variable class attributes and methods

# altarica_Domain class attributes and methods

# NamedElement class attributes and methods

# altarica_SymbolicConstant class attributes and methods

# altarica_Observer class attributes and methods

# altarica_TransitionAnd class attributes and methods

# TransitionExpression class attributes and methods

# altarica_Attribute class attributes and methods

# altarica_Event class attributes and methods

# altarica_Parameter class attributes and methods

# altarica_Skip class attributes and methods

# Instruction class attributes and methods

# altarica_Assignment class attributes and methods

# altarica_Block class attributes and methods

# altarica_Conditional class attributes and methods

# altarica_TransitionOr class attributes and methods

# altarica_Transition class attributes and methods

# altarica_Equal class attributes and methods
altarica_Equal_op: Property = Property(name="op", type=StringType)
altarica_Equal.attributes={altarica_Equal_op}

# altarica_Addition class attributes and methods
altarica_Addition_op: Property = Property(name="op", type=StringType)
altarica_Addition.attributes={altarica_Addition_op}

# altarica_LogicalOr class attributes and methods
altarica_LogicalOr_op: Property = Property(name="op", type=StringType)
altarica_LogicalOr.attributes={altarica_LogicalOr_op}

# altarica_LogicalAnd class attributes and methods
altarica_LogicalAnd_op: Property = Property(name="op", type=StringType)
altarica_LogicalAnd.attributes={altarica_LogicalAnd_op}

# altarica_Not class attributes and methods

# altarica_Minus class attributes and methods

# altarica_FunctionCall class attributes and methods
altarica_FunctionCall_name: Property = Property(name="name", type=StringType)
altarica_FunctionCall.attributes={altarica_FunctionCall_name}

# altarica_Multiplication class attributes and methods
altarica_Multiplication_op: Property = Property(name="op", type=StringType)
altarica_Multiplication.attributes={altarica_Multiplication_op}

# Relationships
errors0: BinaryAssociation = BinaryAssociation(
    name="errors0",
    ends={
        Property(name="altarica_Error", type=altarica_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Model", type=altarica_Error, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations1: BinaryAssociation = BinaryAssociation(
    name="declarations1",
    ends={
        Property(name="altarica_AbstractDeclaration", type=altarica_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Model2", type=altarica_AbstractDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event4: BinaryAssociation = BinaryAssociation(
    name="event4",
    ends={
        Property(name="altarica_NameRef", type=altarica_LabeledTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_LabeledTransition", type=altarica_NameRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression5: BinaryAssociation = BinaryAssociation(
    name="expression5",
    ends={
        Property(name="altarica_TransitionExpression", type=altarica_LabeledTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_LabeledTransition6", type=altarica_TransitionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases7: BinaryAssociation = BinaryAssociation(
    name="cases7",
    ends={
        Property(name="altarica_CaseExpression", type=altarica_Instruction, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Instruction", type=altarica_CaseExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nested14: BinaryAssociation = BinaryAssociation(
    name="nested14",
    ends={
        Property(name="altarica_NameRef15", type=altarica_NameRef, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_NameRef13", type=altarica_NameRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref3: BinaryAssociation = BinaryAssociation(
    name="ref3",
    ends={
        Property(name="altarica_NamedElement", type=altarica_NamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_NamedType", type=altarica_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
cases16: BinaryAssociation = BinaryAssociation(
    name="cases16",
    ends={
        Property(name="altarica_CaseExpression17", type=altarica_SwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_SwitchExpression", type=altarica_CaseExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default18: BinaryAssociation = BinaryAssociation(
    name="default18",
    ends={
        Property(name="altarica_Expression", type=altarica_SwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_SwitchExpression19", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition20: BinaryAssociation = BinaryAssociation(
    name="condition20",
    ends={
        Property(name="altarica_Expression22", type=altarica_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_CaseExpression21", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else8: BinaryAssociation = BinaryAssociation(
    name="else8",
    ends={
        Property(name="altarica_EObject", type=altarica_Instruction, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Instruction9", type=altarica_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable10: BinaryAssociation = BinaryAssociation(
    name="variable10",
    ends={
        Property(name="altarica_NamedElement12", type=altarica_NameRef, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_NameRef11", type=altarica_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
declarations28: BinaryAssociation = BinaryAssociation(
    name="declarations28",
    ends={
        Property(name="altarica_Declaration", type=altarica_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Node", type=altarica_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions29: BinaryAssociation = BinaryAssociation(
    name="transitions29",
    ends={
        Property(name="altarica_LabeledTransition31", type=altarica_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Node30", type=altarica_LabeledTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assertions32: BinaryAssociation = BinaryAssociation(
    name="assertions32",
    ends={
        Property(name="altarica_Instruction34", type=altarica_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Node33", type=altarica_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
case23: BinaryAssociation = BinaryAssociation(
    name="case23",
    ends={
        Property(name="altarica_Expression25", type=altarica_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_CaseExpression24", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constants26: BinaryAssociation = BinaryAssociation(
    name="constants26",
    ends={
        Property(name="altarica_NamedElement27", type=altarica_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Domain", type=altarica_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type43: BinaryAssociation = BinaryAssociation(
    name="type43",
    ends={
        Property(name="altarica_Parameter", type=altarica_Type, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="altarica_Type44", type=altarica_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
value45: BinaryAssociation = BinaryAssociation(
    name="value45",
    ends={
        Property(name="altarica_Expression47", type=altarica_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Parameter46", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type48: BinaryAssociation = BinaryAssociation(
    name="type48",
    ends={
        Property(name="altarica_Type49", type=altarica_Observer, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Observer", type=altarica_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value50: BinaryAssociation = BinaryAssociation(
    name="value50",
    ends={
        Property(name="altarica_Expression52", type=altarica_Observer, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Observer51", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type35: BinaryAssociation = BinaryAssociation(
    name="type35",
    ends={
        Property(name="altarica_Type", type=altarica_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Variable", type=altarica_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes36: BinaryAssociation = BinaryAssociation(
    name="attributes36",
    ends={
        Property(name="altarica_NamedElement38", type=altarica_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Variable37", type=altarica_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value39: BinaryAssociation = BinaryAssociation(
    name="value39",
    ends={
        Property(name="altarica_Expression40", type=altarica_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Attribute", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes41: BinaryAssociation = BinaryAssociation(
    name="attributes41",
    ends={
        Property(name="altarica_NamedElement42", type=altarica_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Event", type=altarica_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable68: BinaryAssociation = BinaryAssociation(
    name="variable68",
    ends={
        Property(name="altarica_NameRef69", type=altarica_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Assignment", type=altarica_NameRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value70: BinaryAssociation = BinaryAssociation(
    name="value70",
    ends={
        Property(name="altarica_Expression72", type=altarica_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Assignment71", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instructions73: BinaryAssociation = BinaryAssociation(
    name="instructions73",
    ends={
        Property(name="altarica_Instruction74", type=altarica_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Block", type=altarica_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left53: BinaryAssociation = BinaryAssociation(
    name="left53",
    ends={
        Property(name="altarica_TransitionExpression54", type=altarica_TransitionAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_TransitionAnd", type=altarica_TransitionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right55: BinaryAssociation = BinaryAssociation(
    name="right55",
    ends={
        Property(name="altarica_TransitionExpression57", type=altarica_TransitionAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_TransitionAnd56", type=altarica_TransitionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition75: BinaryAssociation = BinaryAssociation(
    name="condition75",
    ends={
        Property(name="altarica_Expression76", type=altarica_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Conditional", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left58: BinaryAssociation = BinaryAssociation(
    name="left58",
    ends={
        Property(name="altarica_TransitionExpression59", type=altarica_TransitionOr, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_TransitionOr", type=altarica_TransitionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right60: BinaryAssociation = BinaryAssociation(
    name="right60",
    ends={
        Property(name="altarica_TransitionExpression62", type=altarica_TransitionOr, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_TransitionOr61", type=altarica_TransitionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard63: BinaryAssociation = BinaryAssociation(
    name="guard63",
    ends={
        Property(name="altarica_Expression64", type=altarica_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Transition", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action65: BinaryAssociation = BinaryAssociation(
    name="action65",
    ends={
        Property(name="altarica_Instruction67", type=altarica_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Transition66", type=altarica_Instruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left85: BinaryAssociation = BinaryAssociation(
    name="left85",
    ends={
        Property(name="altarica_Expression86", type=altarica_LogicalAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_LogicalAnd", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right87: BinaryAssociation = BinaryAssociation(
    name="right87",
    ends={
        Property(name="altarica_Expression89", type=altarica_LogicalAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_LogicalAnd88", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left90: BinaryAssociation = BinaryAssociation(
    name="left90",
    ends={
        Property(name="altarica_Expression91", type=altarica_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Equal", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right92: BinaryAssociation = BinaryAssociation(
    name="right92",
    ends={
        Property(name="altarica_Expression94", type=altarica_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Equal93", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then77: BinaryAssociation = BinaryAssociation(
    name="then77",
    ends={
        Property(name="altarica_Instruction79", type=altarica_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Conditional78", type=altarica_Instruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left80: BinaryAssociation = BinaryAssociation(
    name="left80",
    ends={
        Property(name="altarica_Expression81", type=altarica_LogicalOr, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_LogicalOr", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right82: BinaryAssociation = BinaryAssociation(
    name="right82",
    ends={
        Property(name="altarica_Expression84", type=altarica_LogicalOr, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_LogicalOr83", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right102: BinaryAssociation = BinaryAssociation(
    name="right102",
    ends={
        Property(name="altarica_Expression104", type=altarica_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Multiplication103", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression105: BinaryAssociation = BinaryAssociation(
    name="expression105",
    ends={
        Property(name="altarica_Expression106", type=altarica_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Not", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression107: BinaryAssociation = BinaryAssociation(
    name="expression107",
    ends={
        Property(name="altarica_Expression108", type=altarica_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Minus", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters109: BinaryAssociation = BinaryAssociation(
    name="parameters109",
    ends={
        Property(name="altarica_Expression110", type=altarica_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_FunctionCall", type=altarica_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left95: BinaryAssociation = BinaryAssociation(
    name="left95",
    ends={
        Property(name="altarica_Expression96", type=altarica_Addition, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Addition", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right97: BinaryAssociation = BinaryAssociation(
    name="right97",
    ends={
        Property(name="altarica_Expression99", type=altarica_Addition, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Addition98", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left100: BinaryAssociation = BinaryAssociation(
    name="left100",
    ends={
        Property(name="altarica_Expression101", type=altarica_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Multiplication", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_altarica_NamedElement_AbstractDeclaration = Generalization(general=AbstractDeclaration, specific=altarica_NamedElement)
gen_altarica_NamedElement_Declaration = Generalization(general=Declaration, specific=altarica_NamedElement)
gen_altarica_BaseType_Type = Generalization(general=Type, specific=altarica_BaseType)
gen_altarica_NamedType_Type = Generalization(general=Type, specific=altarica_NamedType)
gen_altarica_SwitchExpression_Expression = Generalization(general=Expression, specific=altarica_SwitchExpression)
gen_altarica_ARBoolean_Expression = Generalization(general=Expression, specific=altarica_ARBoolean)
gen_altarica_ARString_Expression = Generalization(general=Expression, specific=altarica_ARString)
gen_altarica_ARNumber_Expression = Generalization(general=Expression, specific=altarica_ARNumber)
gen_altarica_NameRef_Expression = Generalization(general=Expression, specific=altarica_NameRef)
gen_altarica_Node_NamedElement = Generalization(general=NamedElement, specific=altarica_Node)
gen_altarica_Domain_NamedElement = Generalization(general=NamedElement, specific=altarica_Domain)
gen_altarica_SymbolicConstant_NamedElement = Generalization(general=NamedElement, specific=altarica_SymbolicConstant)
gen_altarica_Observer_NamedElement = Generalization(general=NamedElement, specific=altarica_Observer)
gen_altarica_TransitionAnd_TransitionExpression = Generalization(general=TransitionExpression, specific=altarica_TransitionAnd)
gen_altarica_Variable_NamedElement = Generalization(general=NamedElement, specific=altarica_Variable)
gen_altarica_Attribute_NamedElement = Generalization(general=NamedElement, specific=altarica_Attribute)
gen_altarica_Event_NamedElement = Generalization(general=NamedElement, specific=altarica_Event)
gen_altarica_Parameter_NamedElement = Generalization(general=NamedElement, specific=altarica_Parameter)
gen_altarica_Skip_Instruction = Generalization(general=Instruction, specific=altarica_Skip)
gen_altarica_Assignment_Instruction = Generalization(general=Instruction, specific=altarica_Assignment)
gen_altarica_Block_Instruction = Generalization(general=Instruction, specific=altarica_Block)
gen_altarica_Conditional_Instruction = Generalization(general=Instruction, specific=altarica_Conditional)
gen_altarica_TransitionOr_TransitionExpression = Generalization(general=TransitionExpression, specific=altarica_TransitionOr)
gen_altarica_Transition_TransitionExpression = Generalization(general=TransitionExpression, specific=altarica_Transition)
gen_altarica_Equal_Expression = Generalization(general=Expression, specific=altarica_Equal)
gen_altarica_Addition_Expression = Generalization(general=Expression, specific=altarica_Addition)
gen_altarica_LogicalOr_Expression = Generalization(general=Expression, specific=altarica_LogicalOr)
gen_altarica_LogicalAnd_Expression = Generalization(general=Expression, specific=altarica_LogicalAnd)
gen_altarica_Not_Expression = Generalization(general=Expression, specific=altarica_Not)
gen_altarica_Minus_Expression = Generalization(general=Expression, specific=altarica_Minus)
gen_altarica_FunctionCall_Expression = Generalization(general=Expression, specific=altarica_FunctionCall)
gen_altarica_Multiplication_Expression = Generalization(general=Expression, specific=altarica_Multiplication)

# Domain Model
domain_model = DomainModel(
    name="altarica",
    types={altarica_Model, altarica_Error, altarica_AbstractDeclaration, altarica_NamedElement, altarica_Declaration, altarica_LabeledTransition, altarica_NameRef, altarica_TransitionExpression, altarica_Instruction, altarica_CaseExpression, AbstractDeclaration, Declaration, altarica_Type, altarica_BaseType, Type, altarica_NamedType, altarica_SwitchExpression, altarica_EObject, altarica_Expression, altarica_ARBoolean, Expression, altarica_ARString, altarica_ARNumber, altarica_Node, altarica_Variable, altarica_Domain, NamedElement, altarica_SymbolicConstant, altarica_Observer, altarica_TransitionAnd, TransitionExpression, altarica_Attribute, altarica_Event, altarica_Parameter, altarica_Skip, Instruction, altarica_Assignment, altarica_Block, altarica_Conditional, altarica_TransitionOr, altarica_Transition, altarica_Equal, altarica_Addition, altarica_LogicalOr, altarica_LogicalAnd, altarica_Not, altarica_Minus, altarica_FunctionCall, altarica_Multiplication, BaseTypeEnum, Severity},
    associations={errors0, declarations1, event4, expression5, cases7, nested14, ref3, cases16, default18, condition20, else8, variable10, declarations28, transitions29, assertions32, case23, constants26, type43, value45, type48, value50, type35, attributes36, value39, attributes41, variable68, value70, instructions73, left53, right55, condition75, left58, right60, guard63, action65, left85, right87, left90, right92, then77, left80, right82, right102, expression105, expression107, parameters109, left95, right97, left100},
    generalizations={gen_altarica_NamedElement_AbstractDeclaration, gen_altarica_NamedElement_Declaration, gen_altarica_BaseType_Type, gen_altarica_NamedType_Type, gen_altarica_SwitchExpression_Expression, gen_altarica_ARBoolean_Expression, gen_altarica_ARString_Expression, gen_altarica_ARNumber_Expression, gen_altarica_NameRef_Expression, gen_altarica_Node_NamedElement, gen_altarica_Domain_NamedElement, gen_altarica_SymbolicConstant_NamedElement, gen_altarica_Observer_NamedElement, gen_altarica_TransitionAnd_TransitionExpression, gen_altarica_Variable_NamedElement, gen_altarica_Attribute_NamedElement, gen_altarica_Event_NamedElement, gen_altarica_Parameter_NamedElement, gen_altarica_Skip_Instruction, gen_altarica_Assignment_Instruction, gen_altarica_Block_Instruction, gen_altarica_Conditional_Instruction, gen_altarica_TransitionOr_TransitionExpression, gen_altarica_Transition_TransitionExpression, gen_altarica_Equal_Expression, gen_altarica_Addition_Expression, gen_altarica_LogicalOr_Expression, gen_altarica_LogicalAnd_Expression, gen_altarica_Not_Expression, gen_altarica_Minus_Expression, gen_altarica_FunctionCall_Expression, gen_altarica_Multiplication_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)