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
DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Complex")
    }
)

# Classes
sooml_Package = Class(name="sooml::Package")
NamedElement = Class(name="NamedElement")
sooml_Class = Class(name="sooml::Class")
sooml_NamedElement = Class(name="sooml::NamedElement", is_abstract=True)
sooml_StateMachine = Class(name="sooml::StateMachine")
sooml_Reference = Class(name="sooml::Reference")
sooml_Parameter = Class(name="sooml::Parameter")
sooml_Operation = Class(name="sooml::Operation")
sooml_StructuralFeature = Class(name="sooml::StructuralFeature", is_abstract=True)
sooml_Attribute = Class(name="sooml::Attribute")
StructuralFeature = Class(name="StructuralFeature")
sooml_Action = Class(name="sooml::Action", is_abstract=True)
sooml_Guard = Class(name="sooml::Guard", is_abstract=True)
sooml_Event = Class(name="sooml::Event")
sooml_CallOperationAction = Class(name="sooml::CallOperationAction", is_abstract=True)
Action = Class(name="Action")
sooml_State = Class(name="sooml::State")
sooml_Transition = Class(name="sooml::Transition")
sooml_EntryOperation = Class(name="sooml::EntryOperation")
sooml_ReferenceIsInStateCondition = Class(name="sooml::ReferenceIsInStateCondition")
IsInStateCondition = Class(name="IsInStateCondition")
sooml_ParameterIsInStateCondition = Class(name="sooml::ParameterIsInStateCondition")
sooml_CallReferenceOperationAction = Class(name="sooml::CallReferenceOperationAction")
CallOperationAction = Class(name="CallOperationAction")
sooml_CallParameterOperationAction = Class(name="sooml::CallParameterOperationAction")
sooml_ReferenceAssignmentAction = Class(name="sooml::ReferenceAssignmentAction")
sooml_ParameterBinding = Class(name="sooml::ParameterBinding")
sooml_IsInStateCondition = Class(name="sooml::IsInStateCondition", is_abstract=True)
Guard = Class(name="Guard")

# sooml_Package class attributes and methods

# NamedElement class attributes and methods

# sooml_Class class attributes and methods

# sooml_NamedElement class attributes and methods
sooml_NamedElement_name: Property = Property(name="name", type=StringType)
sooml_NamedElement.attributes={sooml_NamedElement_name}

# sooml_StateMachine class attributes and methods

# sooml_Reference class attributes and methods

# sooml_Parameter class attributes and methods
sooml_Parameter_dataType: Property = Property(name="dataType", type=StringType)
sooml_Parameter.attributes={sooml_Parameter_dataType}

# sooml_Operation class attributes and methods

# sooml_StructuralFeature class attributes and methods
sooml_StructuralFeature_upperBound: Property = Property(name="upperBound", type=IntegerType)
sooml_StructuralFeature_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
sooml_StructuralFeature.attributes={sooml_StructuralFeature_lowerBound, sooml_StructuralFeature_upperBound}

# sooml_Attribute class attributes and methods
sooml_Attribute_dataType: Property = Property(name="dataType", type=StringType)
sooml_Attribute.attributes={sooml_Attribute_dataType}

# StructuralFeature class attributes and methods

# sooml_Action class attributes and methods

# sooml_Guard class attributes and methods

# sooml_Event class attributes and methods

# sooml_CallOperationAction class attributes and methods

# Action class attributes and methods

# sooml_State class attributes and methods

# sooml_Transition class attributes and methods

# sooml_EntryOperation class attributes and methods

# sooml_ReferenceIsInStateCondition class attributes and methods

# IsInStateCondition class attributes and methods

# sooml_ParameterIsInStateCondition class attributes and methods

# sooml_CallReferenceOperationAction class attributes and methods

# CallOperationAction class attributes and methods

# sooml_CallParameterOperationAction class attributes and methods

# sooml_ReferenceAssignmentAction class attributes and methods

# sooml_ParameterBinding class attributes and methods

# sooml_IsInStateCondition class attributes and methods

# Guard class attributes and methods

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="sooml_Class", type=sooml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_Package", type=sooml_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages2: BinaryAssociation = BinaryAssociation(
    name="packages2",
    ends={
        Property(name="Package", type=sooml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="parentPackage", type=sooml_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentPackage4: BinaryAssociation = BinaryAssociation(
    name="parentPackage4",
    ends={
        Property(name="Package5", type=sooml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="packages", type=sooml_Package, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine6: BinaryAssociation = BinaryAssociation(
    name="stateMachine6",
    ends={
        Property(name="StateMachine", type=sooml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=sooml_StateMachine, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="sooml_Class12", type=sooml_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_Reference", type=sooml_Class, multiplicity=Multiplicity(1, 1))
    }
)
opposite14: BinaryAssociation = BinaryAssociation(
    name="opposite14",
    ends={
        Property(name="sooml_Reference15", type=sooml_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_Reference13", type=sooml_Reference, multiplicity=Multiplicity(0, 1))
    }
)
parameter16: BinaryAssociation = BinaryAssociation(
    name="parameter16",
    ends={
        Property(name="sooml_Parameter", type=sooml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_Operation17", type=sooml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class18: BinaryAssociation = BinaryAssociation(
    name="class18",
    ends={
        Property(name="Class", type=sooml_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=sooml_Class, multiplicity=Multiplicity(1, 1))
    }
)
operations7: BinaryAssociation = BinaryAssociation(
    name="operations7",
    ends={
        Property(name="sooml_Operation", type=sooml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_Class8", type=sooml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features9: BinaryAssociation = BinaryAssociation(
    name="features9",
    ends={
        Property(name="sooml_StructuralFeature", type=sooml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_Class10", type=sooml_StructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions27: BinaryAssociation = BinaryAssociation(
    name="actions27",
    ends={
        Property(name="sooml_Action", type=sooml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_Transition28", type=sooml_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard29: BinaryAssociation = BinaryAssociation(
    name="guard29",
    ends={
        Property(name="sooml_Guard", type=sooml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_Transition30", type=sooml_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event31: BinaryAssociation = BinaryAssociation(
    name="event31",
    ends={
        Property(name="sooml_Event", type=sooml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_Transition32", type=sooml_Event, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target33: BinaryAssociation = BinaryAssociation(
    name="target33",
    ends={
        Property(name="sooml_State35", type=sooml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_Transition34", type=sooml_State, multiplicity=Multiplicity(1, 1))
    }
)
operation36: BinaryAssociation = BinaryAssociation(
    name="operation36",
    ends={
        Property(name="sooml_Operation38", type=sooml_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_Event37", type=sooml_Operation, multiplicity=Multiplicity(1, 1))
    }
)
classType39: BinaryAssociation = BinaryAssociation(
    name="classType39",
    ends={
        Property(name="sooml_Class41", type=sooml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_Parameter40", type=sooml_Class, multiplicity=Multiplicity(0, 1))
    }
)
calledOperation42: BinaryAssociation = BinaryAssociation(
    name="calledOperation42",
    ends={
        Property(name="sooml_Operation43", type=sooml_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_CallOperationAction", type=sooml_Operation, multiplicity=Multiplicity(1, 1))
    }
)
states19: BinaryAssociation = BinaryAssociation(
    name="states19",
    ends={
        Property(name="sooml_State", type=sooml_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_StateMachine", type=sooml_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState20: BinaryAssociation = BinaryAssociation(
    name="initialState20",
    ends={
        Property(name="sooml_State22", type=sooml_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_StateMachine21", type=sooml_State, multiplicity=Multiplicity(1, 1))
    }
)
transitions23: BinaryAssociation = BinaryAssociation(
    name="transitions23",
    ends={
        Property(name="sooml_Transition", type=sooml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_State24", type=sooml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryOperation25: BinaryAssociation = BinaryAssociation(
    name="entryOperation25",
    ends={
        Property(name="sooml_EntryOperation", type=sooml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_State26", type=sooml_EntryOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reference57: BinaryAssociation = BinaryAssociation(
    name="reference57",
    ends={
        Property(name="sooml_Reference58", type=sooml_ReferenceIsInStateCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_ReferenceIsInStateCondition", type=sooml_Reference, multiplicity=Multiplicity(1, 1))
    }
)
parameter59: BinaryAssociation = BinaryAssociation(
    name="parameter59",
    ends={
        Property(name="sooml_Parameter60", type=sooml_ParameterIsInStateCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_ParameterIsInStateCondition", type=sooml_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
callObjectViaReference61: BinaryAssociation = BinaryAssociation(
    name="callObjectViaReference61",
    ends={
        Property(name="sooml_Reference62", type=sooml_CallReferenceOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_CallReferenceOperationAction", type=sooml_Reference, multiplicity=Multiplicity(0, 1))
    }
)
callObjectViaParameter63: BinaryAssociation = BinaryAssociation(
    name="callObjectViaParameter63",
    ends={
        Property(name="sooml_Parameter64", type=sooml_CallParameterOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_CallParameterOperationAction", type=sooml_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
parameter65: BinaryAssociation = BinaryAssociation(
    name="parameter65",
    ends={
        Property(name="sooml_Parameter66", type=sooml_ReferenceAssignmentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_ReferenceAssignmentAction", type=sooml_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
reference67: BinaryAssociation = BinaryAssociation(
    name="reference67",
    ends={
        Property(name="sooml_Reference69", type=sooml_ReferenceAssignmentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_ReferenceAssignmentAction68", type=sooml_Reference, multiplicity=Multiplicity(1, 1))
    }
)
parameter44: BinaryAssociation = BinaryAssociation(
    name="parameter44",
    ends={
        Property(name="sooml_ParameterBinding", type=sooml_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_CallOperationAction45", type=sooml_ParameterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuralFeatureBinding46: BinaryAssociation = BinaryAssociation(
    name="structuralFeatureBinding46",
    ends={
        Property(name="sooml_StructuralFeature48", type=sooml_ParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_ParameterBinding47", type=sooml_StructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
parameterBinding49: BinaryAssociation = BinaryAssociation(
    name="parameterBinding49",
    ends={
        Property(name="sooml_Parameter51", type=sooml_ParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_ParameterBinding50", type=sooml_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
inState52: BinaryAssociation = BinaryAssociation(
    name="inState52",
    ends={
        Property(name="sooml_State53", type=sooml_IsInStateCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_IsInStateCondition", type=sooml_State, multiplicity=Multiplicity(1, 1))
    }
)
calledOperation54: BinaryAssociation = BinaryAssociation(
    name="calledOperation54",
    ends={
        Property(name="sooml_Operation56", type=sooml_EntryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="sooml_EntryOperation55", type=sooml_Operation, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_sooml_Package_NamedElement = Generalization(general=NamedElement, specific=sooml_Package)
gen_sooml_Class_NamedElement = Generalization(general=NamedElement, specific=sooml_Class)
gen_sooml_Reference_StructuralFeature = Generalization(general=StructuralFeature, specific=sooml_Reference)
gen_sooml_Operation_NamedElement = Generalization(general=NamedElement, specific=sooml_Operation)
gen_sooml_StructuralFeature_NamedElement = Generalization(general=NamedElement, specific=sooml_StructuralFeature)
gen_sooml_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=sooml_Attribute)
gen_sooml_Parameter_NamedElement = Generalization(general=NamedElement, specific=sooml_Parameter)
gen_sooml_CallOperationAction_Action = Generalization(general=Action, specific=sooml_CallOperationAction)
gen_sooml_State_NamedElement = Generalization(general=NamedElement, specific=sooml_State)
gen_sooml_ReferenceIsInStateCondition_IsInStateCondition = Generalization(general=IsInStateCondition, specific=sooml_ReferenceIsInStateCondition)
gen_sooml_ParameterIsInStateCondition_IsInStateCondition = Generalization(general=IsInStateCondition, specific=sooml_ParameterIsInStateCondition)
gen_sooml_CallReferenceOperationAction_CallOperationAction = Generalization(general=CallOperationAction, specific=sooml_CallReferenceOperationAction)
gen_sooml_CallParameterOperationAction_CallOperationAction = Generalization(general=CallOperationAction, specific=sooml_CallParameterOperationAction)
gen_sooml_ReferenceAssignmentAction_Action = Generalization(general=Action, specific=sooml_ReferenceAssignmentAction)
gen_sooml_IsInStateCondition_Guard = Generalization(general=Guard, specific=sooml_IsInStateCondition)

# Domain Model
domain_model = DomainModel(
    name="sooml",
    types={sooml_Package, NamedElement, sooml_Class, sooml_NamedElement, sooml_StateMachine, sooml_Reference, sooml_Parameter, sooml_Operation, sooml_StructuralFeature, sooml_Attribute, StructuralFeature, sooml_Action, sooml_Guard, sooml_Event, sooml_CallOperationAction, Action, sooml_State, sooml_Transition, sooml_EntryOperation, sooml_ReferenceIsInStateCondition, IsInStateCondition, sooml_ParameterIsInStateCondition, sooml_CallReferenceOperationAction, CallOperationAction, sooml_CallParameterOperationAction, sooml_ReferenceAssignmentAction, sooml_ParameterBinding, sooml_IsInStateCondition, Guard, DataType},
    associations={classes0, packages2, parentPackage4, stateMachine6, type11, opposite14, parameter16, class18, operations7, features9, actions27, guard29, event31, target33, operation36, classType39, calledOperation42, states19, initialState20, transitions23, entryOperation25, reference57, parameter59, callObjectViaReference61, callObjectViaParameter63, parameter65, reference67, parameter44, structuralFeatureBinding46, parameterBinding49, inState52, calledOperation54},
    generalizations={gen_sooml_Package_NamedElement, gen_sooml_Class_NamedElement, gen_sooml_Reference_StructuralFeature, gen_sooml_Operation_NamedElement, gen_sooml_StructuralFeature_NamedElement, gen_sooml_Attribute_StructuralFeature, gen_sooml_Parameter_NamedElement, gen_sooml_CallOperationAction_Action, gen_sooml_State_NamedElement, gen_sooml_ReferenceIsInStateCondition_IsInStateCondition, gen_sooml_ParameterIsInStateCondition_IsInStateCondition, gen_sooml_CallReferenceOperationAction_CallOperationAction, gen_sooml_CallParameterOperationAction_CallOperationAction, gen_sooml_ReferenceAssignmentAction_Action, gen_sooml_IsInStateCondition_Guard},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)