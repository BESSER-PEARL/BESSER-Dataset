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
dsl_ServiceMetaData = Class(name="dsl::ServiceMetaData")
dsl_Metadata = Class(name="dsl::Metadata")
dsl_State = Class(name="dsl::State")
dsl_Resource = Class(name="dsl::Resource")
Metadata = Class(name="Metadata")
dsl_Specification = Class(name="dsl::Specification")
dsl_Trigger = Class(name="dsl::Trigger")
dsl_IfDoSpec = Class(name="dsl::IfDoSpec")
dsl_ElseIfDoSpec = Class(name="dsl::ElseIfDoSpec")
dsl_ElseDoSpec = Class(name="dsl::ElseDoSpec")
dsl_Element = Class(name="dsl::Element")
dsl_Action = Class(name="dsl::Action")
dsl_OrElement = Class(name="dsl::OrElement")
Element = Class(name="Element")
dsl_AndElement = Class(name="dsl::AndElement")
dsl_DiffElement = Class(name="dsl::DiffElement")
dsl_EqualElement = Class(name="dsl::EqualElement")
dsl_LargerElement = Class(name="dsl::LargerElement")
dsl_LargerEqualElement = Class(name="dsl::LargerEqualElement")
dsl_SmallerElement = Class(name="dsl::SmallerElement")
dsl_Resource_Object = Class(name="dsl::Resource::Object")
dsl_SmallerEqualElement = Class(name="dsl::SmallerEqualElement")
dsl_PlusElement = Class(name="dsl::PlusElement")
dsl_MinusElement = Class(name="dsl::MinusElement")
dsl_MultiplicationElement = Class(name="dsl::MultiplicationElement")
dsl_DivisionElement = Class(name="dsl::DivisionElement")
dsl_ModuloElement = Class(name="dsl::ModuloElement")
dsl_Number_Object = Class(name="dsl::Number::Object")
dsl_Boolean_Object = Class(name="dsl::Boolean::Object")
dsl_State_Object = Class(name="dsl::State::Object")
dsl_NegateElement = Class(name="dsl::NegateElement")

# dsl_RunTimeModel class attributes and methods

# dsl_EnvironmentMetaData class attributes and methods

# dsl_AppMetaData class attributes and methods
dsl_AppMetaData_appID: Property = Property(name="appID", type=StringType)
dsl_AppMetaData.attributes={dsl_AppMetaData_appID}

# dsl_ServiceMetaData class attributes and methods
dsl_ServiceMetaData_serviceID: Property = Property(name="serviceID", type=StringType)
dsl_ServiceMetaData.attributes={dsl_ServiceMetaData_serviceID}

# dsl_Metadata class attributes and methods

# dsl_State class attributes and methods
dsl_State_name: Property = Property(name="name", type=StringType)
dsl_State.attributes={dsl_State_name}

# dsl_Resource class attributes and methods
dsl_Resource_name: Property = Property(name="name", type=StringType)
dsl_Resource.attributes={dsl_Resource_name}

# Metadata class attributes and methods

# dsl_Specification class attributes and methods
dsl_Specification_specID: Property = Property(name="specID", type=StringType)
dsl_Specification_priority: Property = Property(name="priority", type=IntegerType)
dsl_Specification.attributes={dsl_Specification_specID, dsl_Specification_priority}

# dsl_Trigger class attributes and methods

# dsl_IfDoSpec class attributes and methods

# dsl_ElseIfDoSpec class attributes and methods

# dsl_ElseDoSpec class attributes and methods

# dsl_Element class attributes and methods

# dsl_Action class attributes and methods

# dsl_OrElement class attributes and methods

# Element class attributes and methods

# dsl_AndElement class attributes and methods

# dsl_DiffElement class attributes and methods

# dsl_EqualElement class attributes and methods

# dsl_LargerElement class attributes and methods

# dsl_LargerEqualElement class attributes and methods

# dsl_SmallerElement class attributes and methods

# dsl_Resource_Object class attributes and methods

# dsl_SmallerEqualElement class attributes and methods

# dsl_PlusElement class attributes and methods

# dsl_MinusElement class attributes and methods

# dsl_MultiplicationElement class attributes and methods

# dsl_DivisionElement class attributes and methods

# dsl_ModuloElement class attributes and methods

# dsl_Number_Object class attributes and methods
dsl_Number_Object_value: Property = Property(name="value", type=StringType)
dsl_Number_Object.attributes={dsl_Number_Object_value}

# dsl_Boolean_Object class attributes and methods
dsl_Boolean_Object_value: Property = Property(name="value", type=BooleanType)
dsl_Boolean_Object.attributes={dsl_Boolean_Object_value}

# dsl_State_Object class attributes and methods

# dsl_NegateElement class attributes and methods

# Relationships
resources35: BinaryAssociation = BinaryAssociation(
    name="resources35",
    ends={
        Property(name="dsl_Resource37", type=dsl_EnvironmentMetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_EnvironmentMetaData36", type=dsl_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
appData1: BinaryAssociation = BinaryAssociation(
    name="appData1",
    ends={
        Property(name="dsl_AppMetaData", type=dsl_RunTimeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_RunTimeModel2", type=dsl_AppMetaData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
servicesData3: BinaryAssociation = BinaryAssociation(
    name="servicesData3",
    ends={
        Property(name="dsl_ServiceMetaData", type=dsl_RunTimeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_RunTimeModel4", type=dsl_ServiceMetaData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states5: BinaryAssociation = BinaryAssociation(
    name="states5",
    ends={
        Property(name="dsl_State", type=dsl_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Resource", type=dsl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specifications6: BinaryAssociation = BinaryAssociation(
    name="specifications6",
    ends={
        Property(name="dsl_Specification", type=dsl_AppMetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AppMetaData7", type=dsl_Specification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger8: BinaryAssociation = BinaryAssociation(
    name="trigger8",
    ends={
        Property(name="dsl_Trigger", type=dsl_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Specification9", type=dsl_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifdo10: BinaryAssociation = BinaryAssociation(
    name="ifdo10",
    ends={
        Property(name="dsl_IfDoSpec", type=dsl_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Specification11", type=dsl_IfDoSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIfDo12: BinaryAssociation = BinaryAssociation(
    name="elseIfDo12",
    ends={
        Property(name="dsl_ElseIfDoSpec", type=dsl_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Specification13", type=dsl_ElseIfDoSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseDo14: BinaryAssociation = BinaryAssociation(
    name="elseDo14",
    ends={
        Property(name="dsl_ElseDoSpec", type=dsl_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Specification15", type=dsl_ElseDoSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resource16: BinaryAssociation = BinaryAssociation(
    name="resource16",
    ends={
        Property(name="dsl_Resource18", type=dsl_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Trigger17", type=dsl_Resource, multiplicity=Multiplicity(0, 1))
    }
)
state19: BinaryAssociation = BinaryAssociation(
    name="state19",
    ends={
        Property(name="dsl_State21", type=dsl_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Trigger20", type=dsl_State, multiplicity=Multiplicity(0, 1))
    }
)
condition22: BinaryAssociation = BinaryAssociation(
    name="condition22",
    ends={
        Property(name="dsl_Element", type=dsl_IfDoSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_IfDoSpec23", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action24: BinaryAssociation = BinaryAssociation(
    name="action24",
    ends={
        Property(name="dsl_Action", type=dsl_IfDoSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_IfDoSpec25", type=dsl_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition26: BinaryAssociation = BinaryAssociation(
    name="condition26",
    ends={
        Property(name="dsl_Element28", type=dsl_ElseIfDoSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ElseIfDoSpec27", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action29: BinaryAssociation = BinaryAssociation(
    name="action29",
    ends={
        Property(name="dsl_Action31", type=dsl_ElseIfDoSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ElseIfDoSpec30", type=dsl_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action32: BinaryAssociation = BinaryAssociation(
    name="action32",
    ends={
        Property(name="dsl_Action34", type=dsl_ElseDoSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ElseDoSpec33", type=dsl_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
envData0: BinaryAssociation = BinaryAssociation(
    name="envData0",
    ends={
        Property(name="dsl_EnvironmentMetaData", type=dsl_RunTimeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_RunTimeModel", type=dsl_EnvironmentMetaData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left74: BinaryAssociation = BinaryAssociation(
    name="left74",
    ends={
        Property(name="dsl_Element75", type=dsl_SmallerElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SmallerElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right76: BinaryAssociation = BinaryAssociation(
    name="right76",
    ends={
        Property(name="dsl_Element78", type=dsl_SmallerElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SmallerElement77", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resource38: BinaryAssociation = BinaryAssociation(
    name="resource38",
    ends={
        Property(name="dsl_Resource40", type=dsl_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Action39", type=dsl_Resource, multiplicity=Multiplicity(0, 1))
    }
)
state41: BinaryAssociation = BinaryAssociation(
    name="state41",
    ends={
        Property(name="dsl_State43", type=dsl_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Action42", type=dsl_State, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left44: BinaryAssociation = BinaryAssociation(
    name="left44",
    ends={
        Property(name="dsl_Element45", type=dsl_OrElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_OrElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right46: BinaryAssociation = BinaryAssociation(
    name="right46",
    ends={
        Property(name="dsl_Element48", type=dsl_OrElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_OrElement47", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left49: BinaryAssociation = BinaryAssociation(
    name="left49",
    ends={
        Property(name="dsl_Element50", type=dsl_AndElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AndElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right51: BinaryAssociation = BinaryAssociation(
    name="right51",
    ends={
        Property(name="dsl_Element53", type=dsl_AndElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AndElement52", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left54: BinaryAssociation = BinaryAssociation(
    name="left54",
    ends={
        Property(name="dsl_Element55", type=dsl_DiffElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_DiffElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right56: BinaryAssociation = BinaryAssociation(
    name="right56",
    ends={
        Property(name="dsl_Element58", type=dsl_DiffElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_DiffElement57", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left59: BinaryAssociation = BinaryAssociation(
    name="left59",
    ends={
        Property(name="dsl_Element60", type=dsl_EqualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_EqualElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right61: BinaryAssociation = BinaryAssociation(
    name="right61",
    ends={
        Property(name="dsl_Element63", type=dsl_EqualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_EqualElement62", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left64: BinaryAssociation = BinaryAssociation(
    name="left64",
    ends={
        Property(name="dsl_Element65", type=dsl_LargerElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LargerElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right66: BinaryAssociation = BinaryAssociation(
    name="right66",
    ends={
        Property(name="dsl_Element68", type=dsl_LargerElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LargerElement67", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left69: BinaryAssociation = BinaryAssociation(
    name="left69",
    ends={
        Property(name="dsl_Element70", type=dsl_LargerEqualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LargerEqualElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right71: BinaryAssociation = BinaryAssociation(
    name="right71",
    ends={
        Property(name="dsl_Element73", type=dsl_LargerEqualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LargerEqualElement72", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value109: BinaryAssociation = BinaryAssociation(
    name="value109",
    ends={
        Property(name="dsl_Resource110", type=dsl_Resource_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Resource_Object", type=dsl_Resource, multiplicity=Multiplicity(0, 1))
    }
)
left79: BinaryAssociation = BinaryAssociation(
    name="left79",
    ends={
        Property(name="dsl_Element80", type=dsl_SmallerEqualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SmallerEqualElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right81: BinaryAssociation = BinaryAssociation(
    name="right81",
    ends={
        Property(name="dsl_Element83", type=dsl_SmallerEqualElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SmallerEqualElement82", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left84: BinaryAssociation = BinaryAssociation(
    name="left84",
    ends={
        Property(name="dsl_Element85", type=dsl_PlusElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PlusElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right86: BinaryAssociation = BinaryAssociation(
    name="right86",
    ends={
        Property(name="dsl_Element88", type=dsl_PlusElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PlusElement87", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left89: BinaryAssociation = BinaryAssociation(
    name="left89",
    ends={
        Property(name="dsl_Element90", type=dsl_MinusElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MinusElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right91: BinaryAssociation = BinaryAssociation(
    name="right91",
    ends={
        Property(name="dsl_Element93", type=dsl_MinusElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MinusElement92", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left94: BinaryAssociation = BinaryAssociation(
    name="left94",
    ends={
        Property(name="dsl_Element95", type=dsl_MultiplicationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MultiplicationElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right96: BinaryAssociation = BinaryAssociation(
    name="right96",
    ends={
        Property(name="dsl_Element98", type=dsl_MultiplicationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MultiplicationElement97", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left99: BinaryAssociation = BinaryAssociation(
    name="left99",
    ends={
        Property(name="dsl_Element100", type=dsl_DivisionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_DivisionElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right101: BinaryAssociation = BinaryAssociation(
    name="right101",
    ends={
        Property(name="dsl_Element103", type=dsl_DivisionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_DivisionElement102", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left104: BinaryAssociation = BinaryAssociation(
    name="left104",
    ends={
        Property(name="dsl_Element105", type=dsl_ModuloElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ModuloElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right106: BinaryAssociation = BinaryAssociation(
    name="right106",
    ends={
        Property(name="dsl_Element108", type=dsl_ModuloElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ModuloElement107", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value111: BinaryAssociation = BinaryAssociation(
    name="value111",
    ends={
        Property(name="dsl_State112", type=dsl_State_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_State_Object", type=dsl_State, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp113: BinaryAssociation = BinaryAssociation(
    name="exp113",
    ends={
        Property(name="dsl_Element114", type=dsl_NegateElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_NegateElement", type=dsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dsl_ServiceMetaData_Metadata = Generalization(general=Metadata, specific=dsl_ServiceMetaData)
gen_dsl_AppMetaData_Metadata = Generalization(general=Metadata, specific=dsl_AppMetaData)
gen_dsl_EnvironmentMetaData_Metadata = Generalization(general=Metadata, specific=dsl_EnvironmentMetaData)
gen_dsl_OrElement_Element = Generalization(general=Element, specific=dsl_OrElement)
gen_dsl_AndElement_Element = Generalization(general=Element, specific=dsl_AndElement)
gen_dsl_DiffElement_Element = Generalization(general=Element, specific=dsl_DiffElement)
gen_dsl_EqualElement_Element = Generalization(general=Element, specific=dsl_EqualElement)
gen_dsl_LargerElement_Element = Generalization(general=Element, specific=dsl_LargerElement)
gen_dsl_LargerEqualElement_Element = Generalization(general=Element, specific=dsl_LargerEqualElement)
gen_dsl_SmallerElement_Element = Generalization(general=Element, specific=dsl_SmallerElement)
gen_dsl_Resource_Object_Element = Generalization(general=Element, specific=dsl_Resource_Object)
gen_dsl_SmallerEqualElement_Element = Generalization(general=Element, specific=dsl_SmallerEqualElement)
gen_dsl_PlusElement_Element = Generalization(general=Element, specific=dsl_PlusElement)
gen_dsl_MinusElement_Element = Generalization(general=Element, specific=dsl_MinusElement)
gen_dsl_MultiplicationElement_Element = Generalization(general=Element, specific=dsl_MultiplicationElement)
gen_dsl_DivisionElement_Element = Generalization(general=Element, specific=dsl_DivisionElement)
gen_dsl_ModuloElement_Element = Generalization(general=Element, specific=dsl_ModuloElement)
gen_dsl_Number_Object_Element = Generalization(general=Element, specific=dsl_Number_Object)
gen_dsl_Boolean_Object_Element = Generalization(general=Element, specific=dsl_Boolean_Object)
gen_dsl_State_Object_Element = Generalization(general=Element, specific=dsl_State_Object)
gen_dsl_NegateElement_Element = Generalization(general=Element, specific=dsl_NegateElement)

# Domain Model
domain_model = DomainModel(
    name="dsl",
    types={dsl_RunTimeModel, dsl_EnvironmentMetaData, dsl_AppMetaData, dsl_ServiceMetaData, dsl_Metadata, dsl_State, dsl_Resource, Metadata, dsl_Specification, dsl_Trigger, dsl_IfDoSpec, dsl_ElseIfDoSpec, dsl_ElseDoSpec, dsl_Element, dsl_Action, dsl_OrElement, Element, dsl_AndElement, dsl_DiffElement, dsl_EqualElement, dsl_LargerElement, dsl_LargerEqualElement, dsl_SmallerElement, dsl_Resource_Object, dsl_SmallerEqualElement, dsl_PlusElement, dsl_MinusElement, dsl_MultiplicationElement, dsl_DivisionElement, dsl_ModuloElement, dsl_Number_Object, dsl_Boolean_Object, dsl_State_Object, dsl_NegateElement},
    associations={resources35, appData1, servicesData3, states5, specifications6, trigger8, ifdo10, elseIfDo12, elseDo14, resource16, state19, condition22, action24, condition26, action29, action32, envData0, left74, right76, resource38, state41, left44, right46, left49, right51, left54, right56, left59, right61, left64, right66, left69, right71, value109, left79, right81, left84, right86, left89, right91, left94, right96, left99, right101, left104, right106, value111, exp113},
    generalizations={gen_dsl_ServiceMetaData_Metadata, gen_dsl_AppMetaData_Metadata, gen_dsl_EnvironmentMetaData_Metadata, gen_dsl_OrElement_Element, gen_dsl_AndElement_Element, gen_dsl_DiffElement_Element, gen_dsl_EqualElement_Element, gen_dsl_LargerElement_Element, gen_dsl_LargerEqualElement_Element, gen_dsl_SmallerElement_Element, gen_dsl_Resource_Object_Element, gen_dsl_SmallerEqualElement_Element, gen_dsl_PlusElement_Element, gen_dsl_MinusElement_Element, gen_dsl_MultiplicationElement_Element, gen_dsl_DivisionElement_Element, gen_dsl_ModuloElement_Element, gen_dsl_Number_Object_Element, gen_dsl_Boolean_Object_Element, gen_dsl_State_Object_Element, gen_dsl_NegateElement_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)