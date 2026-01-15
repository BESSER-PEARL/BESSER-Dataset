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
DataTypes: Enumeration = Enumeration(
    name="DataTypes",
    literals={
            EnumerationLiteral(name="double"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="number"),
			EnumerationLiteral(name="Date")
    }
)

Cardinality: Enumeration = Enumeration(
    name="Cardinality",
    literals={
            EnumerationLiteral(name="CEROTOMANY"),
			EnumerationLiteral(name="CEROTOONE")
    }
)

LogicalCononnector: Enumeration = Enumeration(
    name="LogicalCononnector",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

AddOper: Enumeration = Enumeration(
    name="AddOper",
    literals={
            EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="MINUS")
    }
)

RelationType: Enumeration = Enumeration(
    name="RelationType",
    literals={
            EnumerationLiteral(name="COMPOSITION"),
			EnumerationLiteral(name="REFERENCE")
    }
)

LogicalOperator: Enumeration = Enumeration(
    name="LogicalOperator",
    literals={
            EnumerationLiteral(name="LESSTHAN"),
			EnumerationLiteral(name="EQUALTO"),
			EnumerationLiteral(name="DIFFERENT")
    }
)

MultOper: Enumeration = Enumeration(
    name="MultOper",
    literals={
            EnumerationLiteral(name="MULT"),
			EnumerationLiteral(name="DIV")
    }
)

# Classes
PagosPim_Application = Class(name="PagosPim::Application")
PagosPim_DataLayerComponent = Class(name="PagosPim::DataLayerComponent")
PagosPim_DaoComponent = Class(name="PagosPim::DaoComponent")
PagosPim_ViewComponent = Class(name="PagosPim::ViewComponent")
PagosPim_Control = Class(name="PagosPim::Control")
PagosPim_Input = Class(name="PagosPim::Input")
Control = Class(name="Control")
Attribute = Class(name="Attribute")
PagosPim_FrontService = Class(name="PagosPim::FrontService")
PagosPim_Output = Class(name="PagosPim::Output")
PagosPim_LogicComponent = Class(name="PagosPim::LogicComponent")
PagosPim_ServerService = Class(name="PagosPim::ServerService")
Operation = Class(name="Operation")
GenericComponent = Class(name="GenericComponent")
PagosPim_SubComponent = Class(name="PagosPim::SubComponent")
PagosPim_Relation = Class(name="PagosPim::Relation")
PagosPim_Operation = Class(name="PagosPim::Operation")
AttributeDefinition = Class(name="AttributeDefinition")
PagosPim_Expression = Class(name="PagosPim::Expression")
PagosPim_ParameterList = Class(name="PagosPim::ParameterList")
PagosPim_Body = Class(name="PagosPim::Body")
PagosPim_GenericComponent = Class(name="PagosPim::GenericComponent")
PagosPim_Attribute = Class(name="PagosPim::Attribute")
PagosPim_Parameter = Class(name="PagosPim::Parameter")
PagosPim_AttributeDefinition = Class(name="PagosPim::AttributeDefinition", is_abstract=True)
PagosPim_EObject = Class(name="PagosPim::EObject")
PagosPim_Return = Class(name="PagosPim::Return")
PagosPim_IfCondition = Class(name="PagosPim::IfCondition")
PagosPim_ElseSegment = Class(name="PagosPim::ElseSegment")
PagosPim_ProgramIfExpression = Class(name="PagosPim::ProgramIfExpression")
PagosPim_LogicalExpression = Class(name="PagosPim::LogicalExpression")
PagosPim_IfBlock = Class(name="PagosPim::IfBlock")
PagosPim_TerminalValue = Class(name="PagosPim::TerminalValue")
Expression = Class(name="Expression")
PagosPim_NewEClass21 = Class(name="PagosPim::NewEClass21")
PagosPim_Add = Class(name="PagosPim::Add")
PagosPim_Mult = Class(name="PagosPim::Mult")
PagosPim_Action = Class(name="PagosPim::Action")
PagosPim_Field = Class(name="PagosPim::Field")
Relation = Class(name="Relation")

# PagosPim_Application class attributes and methods
PagosPim_Application_name: Property = Property(name="name", type=StringType)
PagosPim_Application.attributes={PagosPim_Application_name}

# PagosPim_DataLayerComponent class attributes and methods

# PagosPim_DaoComponent class attributes and methods

# PagosPim_ViewComponent class attributes and methods
PagosPim_ViewComponent_title: Property = Property(name="title", type=StringType)
PagosPim_ViewComponent.attributes={PagosPim_ViewComponent_title}

# PagosPim_Control class attributes and methods
PagosPim_Control_label: Property = Property(name="label", type=StringType)
PagosPim_Control.attributes={PagosPim_Control_label}

# PagosPim_Input class attributes and methods

# Control class attributes and methods

# Attribute class attributes and methods

# PagosPim_FrontService class attributes and methods
PagosPim_FrontService_fullName: Property = Property(name="fullName", type=StringType)
PagosPim_FrontService.attributes={PagosPim_FrontService_fullName}

# PagosPim_Output class attributes and methods

# PagosPim_LogicComponent class attributes and methods
PagosPim_LogicComponent_persistible: Property = Property(name="persistible", type=BooleanType)
PagosPim_LogicComponent.attributes={PagosPim_LogicComponent_persistible}

# PagosPim_ServerService class attributes and methods

# Operation class attributes and methods

# GenericComponent class attributes and methods

# PagosPim_SubComponent class attributes and methods

# PagosPim_Relation class attributes and methods
PagosPim_Relation_type: Property = Property(name="type", type=StringType)
PagosPim_Relation_name: Property = Property(name="name", type=StringType)
PagosPim_Relation_cardinality: Property = Property(name="cardinality", type=StringType)
PagosPim_Relation.attributes={PagosPim_Relation_type, PagosPim_Relation_name, PagosPim_Relation_cardinality}

# PagosPim_Operation class attributes and methods
PagosPim_Operation_name: Property = Property(name="name", type=StringType)
PagosPim_Operation.attributes={PagosPim_Operation_name}

# AttributeDefinition class attributes and methods

# PagosPim_Expression class attributes and methods

# PagosPim_ParameterList class attributes and methods

# PagosPim_Body class attributes and methods

# PagosPim_GenericComponent class attributes and methods
PagosPim_GenericComponent_name: Property = Property(name="name", type=StringType)
PagosPim_GenericComponent.attributes={PagosPim_GenericComponent_name}

# PagosPim_Attribute class attributes and methods
PagosPim_Attribute_isIndex: Property = Property(name="isIndex", type=StringType)
PagosPim_Attribute.attributes={PagosPim_Attribute_isIndex}

# PagosPim_Parameter class attributes and methods

# PagosPim_AttributeDefinition class attributes and methods
PagosPim_AttributeDefinition_name: Property = Property(name="name", type=StringType)
PagosPim_AttributeDefinition_type: Property = Property(name="type", type=StringType)
PagosPim_AttributeDefinition.attributes={PagosPim_AttributeDefinition_name, PagosPim_AttributeDefinition_type}

# PagosPim_EObject class attributes and methods

# PagosPim_Return class attributes and methods
PagosPim_Return_type: Property = Property(name="type", type=StringType)
PagosPim_Return.attributes={PagosPim_Return_type}

# PagosPim_IfCondition class attributes and methods

# PagosPim_ElseSegment class attributes and methods

# PagosPim_ProgramIfExpression class attributes and methods

# PagosPim_LogicalExpression class attributes and methods
PagosPim_LogicalExpression_logicalOperator: Property = Property(name="logicalOperator", type=StringType)
PagosPim_LogicalExpression_literal: Property = Property(name="literal", type=StringType)
PagosPim_LogicalExpression_conOper: Property = Property(name="conOper", type=StringType)
PagosPim_LogicalExpression.attributes={PagosPim_LogicalExpression_conOper, PagosPim_LogicalExpression_literal, PagosPim_LogicalExpression_logicalOperator}

# PagosPim_IfBlock class attributes and methods

# PagosPim_TerminalValue class attributes and methods
PagosPim_TerminalValue_method: Property = Property(name="method", type=StringType)
PagosPim_TerminalValue_value: Property = Property(name="value", type=StringType)
PagosPim_TerminalValue.attributes={PagosPim_TerminalValue_value, PagosPim_TerminalValue_method}

# Expression class attributes and methods

# PagosPim_NewEClass21 class attributes and methods

# PagosPim_Add class attributes and methods
PagosPim_Add_operator: Property = Property(name="operator", type=StringType)
PagosPim_Add.attributes={PagosPim_Add_operator}

# PagosPim_Mult class attributes and methods
PagosPim_Mult_operator: Property = Property(name="operator", type=StringType)
PagosPim_Mult.attributes={PagosPim_Mult_operator}

# PagosPim_Action class attributes and methods

# PagosPim_Field class attributes and methods

# Relation class attributes and methods

# Relationships
serverservice1: BinaryAssociation = BinaryAssociation(
    name="serverservice1",
    ends={
        Property(name="PagosPim_Application2", type=PagosPim_ServerService, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="PagosPim_ServerService", type=PagosPim_Application, multiplicity=Multiplicity(1, 1))
    }
)
datalayercomponents3: BinaryAssociation = BinaryAssociation(
    name="datalayercomponents3",
    ends={
        Property(name="PagosPim_DataLayerComponent", type=PagosPim_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Application4", type=PagosPim_DataLayerComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daocomponent5: BinaryAssociation = BinaryAssociation(
    name="daocomponent5",
    ends={
        Property(name="PagosPim_DaoComponent", type=PagosPim_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Application6", type=PagosPim_DaoComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views7: BinaryAssociation = BinaryAssociation(
    name="views7",
    ends={
        Property(name="PagosPim_ViewComponent", type=PagosPim_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Application8", type=PagosPim_ViewComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
service9: BinaryAssociation = BinaryAssociation(
    name="service9",
    ends={
        Property(name="PagosPim_FrontService", type=PagosPim_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Input", type=PagosPim_FrontService, multiplicity=Multiplicity(0, 1))
    }
)
logicalComponents0: BinaryAssociation = BinaryAssociation(
    name="logicalComponents0",
    ends={
        Property(name="PagosPim_LogicComponent", type=PagosPim_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Application", type=PagosPim_LogicComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceCalls11: BinaryAssociation = BinaryAssociation(
    name="serviceCalls11",
    ends={
        Property(name="PagosPim_FrontService12", type=PagosPim_FrontService, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_FrontService10", type=PagosPim_FrontService, multiplicity=Multiplicity(0, 9999))
    }
)
serves13: BinaryAssociation = BinaryAssociation(
    name="serves13",
    ends={
        Property(name="PagosPim_ServerService15", type=PagosPim_FrontService, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_FrontService14", type=PagosPim_ServerService, multiplicity=Multiplicity(0, 1))
    }
)
subcomponents16: BinaryAssociation = BinaryAssociation(
    name="subcomponents16",
    ends={
        Property(name="PagosPim_SubComponent", type=PagosPim_ViewComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_ViewComponent17", type=PagosPim_SubComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controls18: BinaryAssociation = BinaryAssociation(
    name="controls18",
    ends={
        Property(name="PagosPim_Control", type=PagosPim_ViewComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_ViewComponent19", type=PagosPim_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
frontservices20: BinaryAssociation = BinaryAssociation(
    name="frontservices20",
    ends={
        Property(name="PagosPim_FrontService22", type=PagosPim_ViewComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_ViewComponent21", type=PagosPim_FrontService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations24: BinaryAssociation = BinaryAssociation(
    name="relations24",
    ends={
        Property(name="PagosPim_Relation", type=PagosPim_GenericComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_GenericComponent25", type=PagosPim_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations26: BinaryAssociation = BinaryAssociation(
    name="operations26",
    ends={
        Property(name="PagosPim_Operation", type=PagosPim_GenericComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_GenericComponent27", type=PagosPim_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression28: BinaryAssociation = BinaryAssociation(
    name="expression28",
    ends={
        Property(name="PagosPim_Expression", type=PagosPim_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Attribute29", type=PagosPim_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterList30: BinaryAssociation = BinaryAssociation(
    name="parameterList30",
    ends={
        Property(name="PagosPim_ParameterList", type=PagosPim_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Operation31", type=PagosPim_ParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body32: BinaryAssociation = BinaryAssociation(
    name="body32",
    ends={
        Property(name="PagosPim_Body", type=PagosPim_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Operation33", type=PagosPim_Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes23: BinaryAssociation = BinaryAssociation(
    name="attributes23",
    ends={
        Property(name="PagosPim_Attribute", type=PagosPim_GenericComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_GenericComponent", type=PagosPim_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters37: BinaryAssociation = BinaryAssociation(
    name="parameters37",
    ends={
        Property(name="PagosPim_Parameter", type=PagosPim_ParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_ParameterList38", type=PagosPim_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetComponent39: BinaryAssociation = BinaryAssociation(
    name="targetComponent39",
    ends={
        Property(name="PagosPim_GenericComponent41", type=PagosPim_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Relation40", type=PagosPim_GenericComponent, multiplicity=Multiplicity(0, 1))
    }
)
complexType42: BinaryAssociation = BinaryAssociation(
    name="complexType42",
    ends={
        Property(name="PagosPim_EObject", type=PagosPim_AttributeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_AttributeDefinition", type=PagosPim_EObject, multiplicity=Multiplicity(0, 1))
    }
)
attributes34: BinaryAssociation = BinaryAssociation(
    name="attributes34",
    ends={
        Property(name="PagosPim_Attribute36", type=PagosPim_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Operation35", type=PagosPim_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnExp47: BinaryAssociation = BinaryAssociation(
    name="returnExp47",
    ends={
        Property(name="PagosPim_Return49", type=PagosPim_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Body48", type=PagosPim_Return, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifcondition50: BinaryAssociation = BinaryAssociation(
    name="ifcondition50",
    ends={
        Property(name="PagosPim_IfCondition", type=PagosPim_IfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_IfBlock51", type=PagosPim_IfCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elsesegment52: BinaryAssociation = BinaryAssociation(
    name="elsesegment52",
    ends={
        Property(name="PagosPim_ElseSegment", type=PagosPim_IfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_IfBlock53", type=PagosPim_ElseSegment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifexpression54: BinaryAssociation = BinaryAssociation(
    name="ifexpression54",
    ends={
        Property(name="PagosPim_ProgramIfExpression", type=PagosPim_IfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_IfBlock55", type=PagosPim_ProgramIfExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logicalexpressions56: BinaryAssociation = BinaryAssociation(
    name="logicalexpressions56",
    ends={
        Property(name="PagosPim_LogicalExpression", type=PagosPim_IfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_IfCondition57", type=PagosPim_LogicalExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnBlock58: BinaryAssociation = BinaryAssociation(
    name="returnBlock58",
    ends={
        Property(name="PagosPim_Return60", type=PagosPim_IfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_IfCondition59", type=PagosPim_Return, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerIf61: BinaryAssociation = BinaryAssociation(
    name="innerIf61",
    ends={
        Property(name="PagosPim_IfBlock63", type=PagosPim_IfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_IfCondition62", type=PagosPim_IfBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression43: BinaryAssociation = BinaryAssociation(
    name="expression43",
    ends={
        Property(name="PagosPim_Expression44", type=PagosPim_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Return", type=PagosPim_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifblock45: BinaryAssociation = BinaryAssociation(
    name="ifblock45",
    ends={
        Property(name="PagosPim_IfBlock", type=PagosPim_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Body46", type=PagosPim_IfBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression67: BinaryAssociation = BinaryAssociation(
    name="expression67",
    ends={
        Property(name="PagosPim_Return69", type=PagosPim_ElseSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_ElseSegment68", type=PagosPim_Return, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftTerm70: BinaryAssociation = BinaryAssociation(
    name="leftTerm70",
    ends={
        Property(name="PagosPim_TerminalValue", type=PagosPim_LogicalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_LogicalExpression71", type=PagosPim_TerminalValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightTerm72: BinaryAssociation = BinaryAssociation(
    name="rightTerm72",
    ends={
        Property(name="PagosPim_TerminalValue74", type=PagosPim_LogicalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_LogicalExpression73", type=PagosPim_TerminalValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
moreExpressions76: BinaryAssociation = BinaryAssociation(
    name="moreExpressions76",
    ends={
        Property(name="PagosPim_LogicalExpression77", type=PagosPim_LogicalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_LogicalExpression75", type=PagosPim_LogicalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression78: BinaryAssociation = BinaryAssociation(
    name="expression78",
    ends={
        Property(name="PagosPim_Expression80", type=PagosPim_ProgramIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_ProgramIfExpression79", type=PagosPim_Expression, multiplicity=Multiplicity(0, 1))
    }
)
innerIfBlocks64: BinaryAssociation = BinaryAssociation(
    name="innerIfBlocks64",
    ends={
        Property(name="PagosPim_Body66", type=PagosPim_ElseSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_ElseSegment65", type=PagosPim_Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftExp87: BinaryAssociation = BinaryAssociation(
    name="leftExp87",
    ends={
        Property(name="PagosPim_Expression88", type=PagosPim_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Add", type=PagosPim_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightExp89: BinaryAssociation = BinaryAssociation(
    name="rightExp89",
    ends={
        Property(name="PagosPim_Expression91", type=PagosPim_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Add90", type=PagosPim_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightExp92: BinaryAssociation = BinaryAssociation(
    name="rightExp92",
    ends={
        Property(name="PagosPim_Expression93", type=PagosPim_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Mult", type=PagosPim_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftExp94: BinaryAssociation = BinaryAssociation(
    name="leftExp94",
    ends={
        Property(name="PagosPim_Expression96", type=PagosPim_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Mult95", type=PagosPim_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent81: BinaryAssociation = BinaryAssociation(
    name="parent81",
    ends={
        Property(name="PagosPim_EObject83", type=PagosPim_TerminalValue, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_TerminalValue82", type=PagosPim_EObject, multiplicity=Multiplicity(0, 1))
    }
)
attribute84: BinaryAssociation = BinaryAssociation(
    name="attribute84",
    ends={
        Property(name="PagosPim_Attribute86", type=PagosPim_TerminalValue, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_TerminalValue85", type=PagosPim_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
relatesTo97: BinaryAssociation = BinaryAssociation(
    name="relatesTo97",
    ends={
        Property(name="PagosPim_LogicComponent99", type=PagosPim_ServerService, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_ServerService98", type=PagosPim_LogicComponent, multiplicity=Multiplicity(0, 1))
    }
)
mapsTo100: BinaryAssociation = BinaryAssociation(
    name="mapsTo100",
    ends={
        Property(name="PagosPim_DataLayerComponent102", type=PagosPim_LogicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_LogicComponent101", type=PagosPim_DataLayerComponent, multiplicity=Multiplicity(0, 1))
    }
)
extendsData103: BinaryAssociation = BinaryAssociation(
    name="extendsData103",
    ends={
        Property(name="PagosPim_DaoComponent105", type=PagosPim_DataLayerComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_DataLayerComponent104", type=PagosPim_DaoComponent, multiplicity=Multiplicity(0, 1))
    }
)
service108: BinaryAssociation = BinaryAssociation(
    name="service108",
    ends={
        Property(name="PagosPim_FrontService109", type=PagosPim_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_Action", type=PagosPim_FrontService, multiplicity=Multiplicity(0, 1))
    }
)
fields106: BinaryAssociation = BinaryAssociation(
    name="fields106",
    ends={
        Property(name="PagosPim_Field", type=PagosPim_DataLayerComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="PagosPim_DataLayerComponent107", type=PagosPim_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_PagosPim_Input_Control = Generalization(general=Control, specific=PagosPim_Input)
gen_PagosPim_Input_Attribute = Generalization(general=Attribute, specific=PagosPim_Input)
gen_PagosPim_Output_Control = Generalization(general=Control, specific=PagosPim_Output)
gen_PagosPim_Output_Attribute = Generalization(general=Attribute, specific=PagosPim_Output)
gen_PagosPim_FrontService_Operation = Generalization(general=Operation, specific=PagosPim_FrontService)
gen_PagosPim_ViewComponent_GenericComponent = Generalization(general=GenericComponent, specific=PagosPim_ViewComponent)
gen_PagosPim_Attribute_AttributeDefinition = Generalization(general=AttributeDefinition, specific=PagosPim_Attribute)
gen_PagosPim_TerminalValue_Expression = Generalization(general=Expression, specific=PagosPim_TerminalValue)
gen_PagosPim_Add_Expression = Generalization(general=Expression, specific=PagosPim_Add)
gen_PagosPim_Mult_Expression = Generalization(general=Expression, specific=PagosPim_Mult)
gen_PagosPim_Parameter_AttributeDefinition = Generalization(general=AttributeDefinition, specific=PagosPim_Parameter)
gen_PagosPim_ServerService_GenericComponent = Generalization(general=GenericComponent, specific=PagosPim_ServerService)
gen_PagosPim_LogicComponent_GenericComponent = Generalization(general=GenericComponent, specific=PagosPim_LogicComponent)
gen_PagosPim_DataLayerComponent_GenericComponent = Generalization(general=GenericComponent, specific=PagosPim_DataLayerComponent)
gen_PagosPim_SubComponent_Relation = Generalization(general=Relation, specific=PagosPim_SubComponent)
gen_PagosPim_Action_Control = Generalization(general=Control, specific=PagosPim_Action)
gen_PagosPim_Action_Operation = Generalization(general=Operation, specific=PagosPim_Action)
gen_PagosPim_Field_Attribute = Generalization(general=Attribute, specific=PagosPim_Field)
gen_PagosPim_DaoComponent_GenericComponent = Generalization(general=GenericComponent, specific=PagosPim_DaoComponent)

# Domain Model
domain_model = DomainModel(
    name="PagosPim",
    types={PagosPim_Application, PagosPim_DataLayerComponent, PagosPim_DaoComponent, PagosPim_ViewComponent, PagosPim_Control, PagosPim_Input, Control, Attribute, PagosPim_FrontService, PagosPim_Output, PagosPim_LogicComponent, PagosPim_ServerService, Operation, GenericComponent, PagosPim_SubComponent, PagosPim_Relation, PagosPim_Operation, AttributeDefinition, PagosPim_Expression, PagosPim_ParameterList, PagosPim_Body, PagosPim_GenericComponent, PagosPim_Attribute, PagosPim_Parameter, PagosPim_AttributeDefinition, PagosPim_EObject, PagosPim_Return, PagosPim_IfCondition, PagosPim_ElseSegment, PagosPim_ProgramIfExpression, PagosPim_LogicalExpression, PagosPim_IfBlock, PagosPim_TerminalValue, Expression, PagosPim_NewEClass21, PagosPim_Add, PagosPim_Mult, PagosPim_Action, PagosPim_Field, Relation, DataTypes, Cardinality, LogicalCononnector, AddOper, RelationType, LogicalOperator, MultOper},
    associations={serverservice1, datalayercomponents3, daocomponent5, views7, service9, logicalComponents0, serviceCalls11, serves13, subcomponents16, controls18, frontservices20, relations24, operations26, expression28, parameterList30, body32, attributes23, parameters37, targetComponent39, complexType42, attributes34, returnExp47, ifcondition50, elsesegment52, ifexpression54, logicalexpressions56, returnBlock58, innerIf61, expression43, ifblock45, expression67, leftTerm70, rightTerm72, moreExpressions76, expression78, innerIfBlocks64, leftExp87, rightExp89, rightExp92, leftExp94, parent81, attribute84, relatesTo97, mapsTo100, extendsData103, service108, fields106},
    generalizations={gen_PagosPim_Input_Control, gen_PagosPim_Input_Attribute, gen_PagosPim_Output_Control, gen_PagosPim_Output_Attribute, gen_PagosPim_FrontService_Operation, gen_PagosPim_ViewComponent_GenericComponent, gen_PagosPim_Attribute_AttributeDefinition, gen_PagosPim_TerminalValue_Expression, gen_PagosPim_Add_Expression, gen_PagosPim_Mult_Expression, gen_PagosPim_Parameter_AttributeDefinition, gen_PagosPim_ServerService_GenericComponent, gen_PagosPim_LogicComponent_GenericComponent, gen_PagosPim_DataLayerComponent_GenericComponent, gen_PagosPim_SubComponent_Relation, gen_PagosPim_Action_Control, gen_PagosPim_Action_Operation, gen_PagosPim_Field_Attribute, gen_PagosPim_DaoComponent_GenericComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)