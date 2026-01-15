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
dsl_RunTimeModel = Class(name="dsl::RunTimeModel")
dsl_EnvironmentMetaData = Class(name="dsl::EnvironmentMetaData")
dsl_AppMetaData = Class(name="dsl::AppMetaData")
dsl_State = Class(name="dsl::State")
dsl_Resource = Class(name="dsl::Resource")
dsl_Specification = Class(name="dsl::Specification")
dsl_Element = Class(name="dsl::Element")
dsl_Action = Class(name="dsl::Action")
dsl_OrElement = Class(name="dsl::OrElement")
Element = Class(name="Element")
dsl_AndElement = Class(name="dsl::AndElement")
dsl_Trigger = Class(name="dsl::Trigger")
dsl_IfDoSpec = Class(name="dsl::IfDoSpec")
dsl_ElseIfDoSpec = Class(name="dsl::ElseIfDoSpec")
dsl_ElseDoSpec = Class(name="dsl::ElseDoSpec")
dsl_LargerElement = Class(name="dsl::LargerElement")
dsl_LargerEqualElement = Class(name="dsl::LargerEqualElement")
dsl_SmallerElement = Class(name="dsl::SmallerElement")
dsl_SmallerEqualElement = Class(name="dsl::SmallerEqualElement")
dsl_PlusElement = Class(name="dsl::PlusElement")
dsl_DiffElement = Class(name="dsl::DiffElement")
dsl_EqualElement = Class(name="dsl::EqualElement")
dsl_DivisionElement = Class(name="dsl::DivisionElement")
dsl_ModuloElement = Class(name="dsl::ModuloElement")
dsl_Number_Object = Class(name="dsl::Number::Object")
dsl_Boolean_Object = Class(name="dsl::Boolean::Object")
dsl_Resource_Object = Class(name="dsl::Resource::Object")
dsl_State_Object = Class(name="dsl::State::Object")
dsl_NegateElement = Class(name="dsl::NegateElement")
dsl_MinusElement = Class(name="dsl::MinusElement")
dsl_MultiplicationElement = Class(name="dsl::MultiplicationElement")

# dsl_RunTimeModel class attributes and methods

# dsl_EnvironmentMetaData class attributes and methods

# dsl_AppMetaData class attributes and methods
dsl_AppMetaData_appID: Property = Property(name="appID", type=StringType)
dsl_AppMetaData.attributes={dsl_AppMetaData_appID}

# dsl_State class attributes and methods
dsl_State_name: Property = Property(name="name", type=StringType)
dsl_State.attributes={dsl_State_name}

# dsl_Resource class attributes and methods
dsl_Resource_name: Property = Property(name="name", type=StringType)
dsl_Resource.attributes={dsl_Resource_name}

# dsl_Specification class attributes and methods
dsl_Specification_specID: Property = Property(name="specID", type=StringType)
dsl_Specification_priority: Property = Property(name="priority", type=IntegerType)
dsl_Specification.attributes={dsl_Specification_specID, dsl_Specification_priority}

# dsl_Element class attributes and methods

# dsl_Action class attributes and methods

# dsl_OrElement class attributes and methods

# Element class attributes and methods

# dsl_AndElement class attributes and methods

# dsl_Trigger class attributes and methods

# dsl_IfDoSpec class attributes and methods

# dsl_ElseIfDoSpec class attributes and methods

# dsl_ElseDoSpec class attributes and methods

# dsl_LargerElement class attributes and methods

# dsl_LargerEqualElement class attributes and methods

# dsl_SmallerElement class attributes and methods

# dsl_SmallerEqualElement class attributes and methods

# dsl_PlusElement class attributes and methods

# dsl_DiffElement class attributes and methods

# dsl_EqualElement class attributes and methods

# dsl_DivisionElement class attributes and methods

# dsl_ModuloElement class attributes and methods

# dsl_Number_Object class attributes and methods
dsl_Number_Object_value: Property = Property(name="value", type=StringType)
dsl_Number_Object.attributes={dsl_Number_Object_value}

# dsl_Boolean_Object class attributes and methods
dsl_Boolean_Object_value: Property = Property(name="value", type=BooleanType)
dsl_Boolean_Object.attributes={dsl_Boolean_Object_value}

# dsl_Resource_Object class attributes and methods

# dsl_State_Object class attributes and methods

# dsl_NegateElement class attributes and methods

# dsl_MinusElement class attributes and methods

# dsl_MultiplicationElement class attributes and methods

# Relationships
envData0: BinaryAssociation = BinaryAssociation(
    name="envData0",
    ends={
        Property(name="dsl_EnvironmentMetaData", type=dsl_RunTimeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_RunTimeModel", type=dsl_EnvironmentMetaData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
appData1: BinaryAssociation = BinaryAssociation(
    name="appData1",
    ends={
        Property(name="dsl_AppMetaData", type=dsl_RunTimeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_RunTimeModel2", type=dsl_AppMetaData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="dsl_State", type=dsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Resource", type=dsl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification4: BinaryAssociation = BinaryAssociation(
    name="specification4",
    ends={
        Property(name="dsl_Specification", type=dsl_AppMetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AppMetaData5", type=dsl_Specification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resource14: BinaryAssociation = BinaryAssociation(
    name="resource14",
    ends={
        Property(name="dsl_Resource16", type=dsl_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Trigger15", type=dsl_Resource, multiplicity=Multiplicity(0, 1))
    }
)
state17: BinaryAssociation = BinaryAssociation(
    name="state17",
    ends={
        Property(name="dsl_State19", type=dsl_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Trigger18", type=dsl_State, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition20: BinaryAssociation = BinaryAssociation(
    name="condition20",
    ends={
        Property(name="dsl_Element", type=dsl_IfDoSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_IfDoSpec21", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action22: BinaryAssociation = BinaryAssociation(
    name="action22",
    ends={
        Property(name="dsl_Action", type=dsl_IfDoSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_IfDoSpec23", type=dsl_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition24: BinaryAssociation = BinaryAssociation(
    name="condition24",
    ends={
        Property(name="dsl_Element26", type=dsl_ElseIfDoSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ElseIfDoSpec25", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action27: BinaryAssociation = BinaryAssociation(
    name="action27",
    ends={
        Property(name="dsl_Action29", type=dsl_ElseIfDoSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ElseIfDoSpec28", type=dsl_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action30: BinaryAssociation = BinaryAssociation(
    name="action30",
    ends={
        Property(name="dsl_Action32", type=dsl_ElseDoSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ElseDoSpec31", type=dsl_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources33: BinaryAssociation = BinaryAssociation(
    name="resources33",
    ends={
        Property(name="dsl_Resource35", type=dsl_EnvironmentMetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_EnvironmentMetaData34", type=dsl_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resource36: BinaryAssociation = BinaryAssociation(
    name="resource36",
    ends={
        Property(name="dsl_Resource38", type=dsl_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Action37", type=dsl_Resource, multiplicity=Multiplicity(0, 1))
    }
)
state39: BinaryAssociation = BinaryAssociation(
    name="state39",
    ends={
        Property(name="dsl_State41", type=dsl_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Action40", type=dsl_State, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left42: BinaryAssociation = BinaryAssociation(
    name="left42",
    ends={
        Property(name="dsl_Element43", type=dsl_OrElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_OrElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right44: BinaryAssociation = BinaryAssociation(
    name="right44",
    ends={
        Property(name="dsl_Element46", type=dsl_OrElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_OrElement45", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left47: BinaryAssociation = BinaryAssociation(
    name="left47",
    ends={
        Property(name="dsl_Element48", type=dsl_AndElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AndElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right49: BinaryAssociation = BinaryAssociation(
    name="right49",
    ends={
        Property(name="dsl_Element51", type=dsl_AndElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AndElement50", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger6: BinaryAssociation = BinaryAssociation(
    name="trigger6",
    ends={
        Property(name="dsl_Trigger", type=dsl_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Specification7", type=dsl_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifdo8: BinaryAssociation = BinaryAssociation(
    name="ifdo8",
    ends={
        Property(name="dsl_IfDoSpec", type=dsl_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Specification9", type=dsl_IfDoSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIfDo10: BinaryAssociation = BinaryAssociation(
    name="elseIfDo10",
    ends={
        Property(name="dsl_ElseIfDoSpec", type=dsl_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Specification11", type=dsl_ElseIfDoSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseDo12: BinaryAssociation = BinaryAssociation(
    name="elseDo12",
    ends={
        Property(name="dsl_ElseDoSpec", type=dsl_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Specification13", type=dsl_ElseDoSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left57: BinaryAssociation = BinaryAssociation(
    name="left57",
    ends={
        Property(name="dsl_Element58", type=dsl_EqualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_EqualElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right59: BinaryAssociation = BinaryAssociation(
    name="right59",
    ends={
        Property(name="dsl_Element61", type=dsl_EqualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_EqualElement60", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left62: BinaryAssociation = BinaryAssociation(
    name="left62",
    ends={
        Property(name="dsl_Element63", type=dsl_LargerElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LargerElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right64: BinaryAssociation = BinaryAssociation(
    name="right64",
    ends={
        Property(name="dsl_Element66", type=dsl_LargerElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LargerElement65", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left67: BinaryAssociation = BinaryAssociation(
    name="left67",
    ends={
        Property(name="dsl_Element68", type=dsl_LargerEqualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LargerEqualElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right69: BinaryAssociation = BinaryAssociation(
    name="right69",
    ends={
        Property(name="dsl_Element71", type=dsl_LargerEqualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LargerEqualElement70", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left72: BinaryAssociation = BinaryAssociation(
    name="left72",
    ends={
        Property(name="dsl_Element73", type=dsl_SmallerElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SmallerElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right74: BinaryAssociation = BinaryAssociation(
    name="right74",
    ends={
        Property(name="dsl_Element76", type=dsl_SmallerElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SmallerElement75", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left77: BinaryAssociation = BinaryAssociation(
    name="left77",
    ends={
        Property(name="dsl_Element78", type=dsl_SmallerEqualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SmallerEqualElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right79: BinaryAssociation = BinaryAssociation(
    name="right79",
    ends={
        Property(name="dsl_Element81", type=dsl_SmallerEqualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SmallerEqualElement80", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left82: BinaryAssociation = BinaryAssociation(
    name="left82",
    ends={
        Property(name="dsl_Element83", type=dsl_PlusElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PlusElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right84: BinaryAssociation = BinaryAssociation(
    name="right84",
    ends={
        Property(name="dsl_Element86", type=dsl_PlusElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PlusElement85", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left52: BinaryAssociation = BinaryAssociation(
    name="left52",
    ends={
        Property(name="dsl_Element53", type=dsl_DiffElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_DiffElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right54: BinaryAssociation = BinaryAssociation(
    name="right54",
    ends={
        Property(name="dsl_Element56", type=dsl_DiffElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_DiffElement55", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right94: BinaryAssociation = BinaryAssociation(
    name="right94",
    ends={
        Property(name="dsl_Element96", type=dsl_MultiplicationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MultiplicationElement95", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left97: BinaryAssociation = BinaryAssociation(
    name="left97",
    ends={
        Property(name="dsl_Element98", type=dsl_DivisionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_DivisionElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right99: BinaryAssociation = BinaryAssociation(
    name="right99",
    ends={
        Property(name="dsl_Element101", type=dsl_DivisionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_DivisionElement100", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left102: BinaryAssociation = BinaryAssociation(
    name="left102",
    ends={
        Property(name="dsl_Element103", type=dsl_ModuloElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ModuloElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right104: BinaryAssociation = BinaryAssociation(
    name="right104",
    ends={
        Property(name="dsl_Element106", type=dsl_ModuloElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ModuloElement105", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value107: BinaryAssociation = BinaryAssociation(
    name="value107",
    ends={
        Property(name="dsl_Resource108", type=dsl_Resource_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Resource_Object", type=dsl_Resource, multiplicity=Multiplicity(0, 1))
    }
)
value109: BinaryAssociation = BinaryAssociation(
    name="value109",
    ends={
        Property(name="dsl_State110", type=dsl_State_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_State_Object", type=dsl_State, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp111: BinaryAssociation = BinaryAssociation(
    name="exp111",
    ends={
        Property(name="dsl_Element112", type=dsl_NegateElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_NegateElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left87: BinaryAssociation = BinaryAssociation(
    name="left87",
    ends={
        Property(name="dsl_Element88", type=dsl_MinusElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MinusElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right89: BinaryAssociation = BinaryAssociation(
    name="right89",
    ends={
        Property(name="dsl_Element91", type=dsl_MinusElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MinusElement90", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left92: BinaryAssociation = BinaryAssociation(
    name="left92",
    ends={
        Property(name="dsl_Element93", type=dsl_MultiplicationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MultiplicationElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dsl_OrElement_Element = Generalization(general=Element, specific=dsl_OrElement)
gen_dsl_AndElement_Element = Generalization(general=Element, specific=dsl_AndElement)
gen_dsl_LargerElement_Element = Generalization(general=Element, specific=dsl_LargerElement)
gen_dsl_LargerEqualElement_Element = Generalization(general=Element, specific=dsl_LargerEqualElement)
gen_dsl_SmallerElement_Element = Generalization(general=Element, specific=dsl_SmallerElement)
gen_dsl_SmallerEqualElement_Element = Generalization(general=Element, specific=dsl_SmallerEqualElement)
gen_dsl_PlusElement_Element = Generalization(general=Element, specific=dsl_PlusElement)
gen_dsl_DiffElement_Element = Generalization(general=Element, specific=dsl_DiffElement)
gen_dsl_EqualElement_Element = Generalization(general=Element, specific=dsl_EqualElement)
gen_dsl_DivisionElement_Element = Generalization(general=Element, specific=dsl_DivisionElement)
gen_dsl_ModuloElement_Element = Generalization(general=Element, specific=dsl_ModuloElement)
gen_dsl_Number_Object_Element = Generalization(general=Element, specific=dsl_Number_Object)
gen_dsl_Boolean_Object_Element = Generalization(general=Element, specific=dsl_Boolean_Object)
gen_dsl_Resource_Object_Element = Generalization(general=Element, specific=dsl_Resource_Object)
gen_dsl_State_Object_Element = Generalization(general=Element, specific=dsl_State_Object)
gen_dsl_NegateElement_Element = Generalization(general=Element, specific=dsl_NegateElement)
gen_dsl_MinusElement_Element = Generalization(general=Element, specific=dsl_MinusElement)
gen_dsl_MultiplicationElement_Element = Generalization(general=Element, specific=dsl_MultiplicationElement)

# Domain Model
domain_model = DomainModel(
    name="dsl",
    types={dsl_RunTimeModel, dsl_EnvironmentMetaData, dsl_AppMetaData, dsl_State, dsl_Resource, dsl_Specification, dsl_Element, dsl_Action, dsl_OrElement, Element, dsl_AndElement, dsl_Trigger, dsl_IfDoSpec, dsl_ElseIfDoSpec, dsl_ElseDoSpec, dsl_LargerElement, dsl_LargerEqualElement, dsl_SmallerElement, dsl_SmallerEqualElement, dsl_PlusElement, dsl_DiffElement, dsl_EqualElement, dsl_DivisionElement, dsl_ModuloElement, dsl_Number_Object, dsl_Boolean_Object, dsl_Resource_Object, dsl_State_Object, dsl_NegateElement, dsl_MinusElement, dsl_MultiplicationElement},
    associations={envData0, appData1, states3, specification4, resource14, state17, condition20, action22, condition24, action27, action30, resources33, resource36, state39, left42, right44, left47, right49, trigger6, ifdo8, elseIfDo10, elseDo12, left57, right59, left62, right64, left67, right69, left72, right74, left77, right79, left82, right84, left52, right54, right94, left97, right99, left102, right104, value107, value109, exp111, left87, right89, left92},
    generalizations={gen_dsl_OrElement_Element, gen_dsl_AndElement_Element, gen_dsl_LargerElement_Element, gen_dsl_LargerEqualElement_Element, gen_dsl_SmallerElement_Element, gen_dsl_SmallerEqualElement_Element, gen_dsl_PlusElement_Element, gen_dsl_DiffElement_Element, gen_dsl_EqualElement_Element, gen_dsl_DivisionElement_Element, gen_dsl_ModuloElement_Element, gen_dsl_Number_Object_Element, gen_dsl_Boolean_Object_Element, gen_dsl_Resource_Object_Element, gen_dsl_State_Object_Element, gen_dsl_NegateElement_Element, gen_dsl_MinusElement_Element, gen_dsl_MultiplicationElement_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)