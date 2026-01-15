from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"


############################################
# Definition of Classes
############################################

class Node:

    pass
class UML2_Device(Node):

    pass
class EncapsulatedClassifier:

    pass
class CentralBufferNode:

    pass
class UML2_DataStoreNode(CentralBufferNode):

    pass
class BehavioredClassifier:

    pass
class UML2_Class(BehavioredClassifier, EncapsulatedClassifier):

    pass
class UML2_UseCase(BehavioredClassifier):

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class Type:

    pass
class UML2_Classifier(Type):

    pass
class OpaqueExpression:

    pass
class UML2_Expression(OpaqueExpression):

    pass
class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class DataType:

    pass
class UML2_Enumeration(DataType):

    pass
class ValueSpecification:

    pass
class UML2_TimeExpression(ValueSpecification):

    pass
class UML2_Interval(ValueSpecification):

    pass
class UML2_OpaqueExpression(ValueSpecification):

    pass
class LiteralSpecification:

    pass
class UML2_LiteralNull(LiteralSpecification):

    pass
class UML2_LiteralString(LiteralSpecification):

    pass
class UML2_LiteralUnlimitedNatural(LiteralSpecification):

    pass
class UML2_LiteralBoolean(LiteralSpecification):

    pass
class Interval:

    pass
class UML2_DurationInterval(Interval):

    pass
class UML2_TimeInterval(Interval):

    pass
class Behavior:

    pass
class UML2_Activity(Behavior):

    pass
class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class StructuralFeature:

    pass
class UML2_Property(StructuralFeature):

    pass
class UML2_Type:

    pass
class UML2_TypedElement:

    pass
class UML2_Duration(ValueSpecification):

    pass
class Property:

    pass
class UML2_Port(Property):

    pass
class UML2_ExtensionEnd(Property):

    pass
class UML2_LiteralInteger(LiteralSpecification):

    pass
class UML2_PrimitiveType(DataType):

    pass
class StructuredClassifier:

    pass
class UML2_Collaboration(StructuredClassifier, BehavioredClassifier):

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class UML2_Interaction(Behavior):

    pass
class InputPin:

    pass
class UML2_ValuePin(InputPin):

    pass
class Pin:

    pass
class UML2_InputPin(Pin):

    pass
class UML2_OutputPin(Pin):

    pass
class UML2_LiteralSpecification(ValueSpecification):

    pass
class UML2_InstanceValue(ValueSpecification):

    pass
class UML2_StateMachine(Behavior):

    pass
class Association:

    pass
class UML2_CommunicationPath(Association):

    pass
class UML2_Extension(Association):

    pass
class Class:

    pass
class UML2_Component(Class):

    pass
class UML2_Behavior(Class):

    pass
class UML2_Stereotype(Class):

    pass
class UML2_AssociationClass(Association, Class):

    pass
class UML2_Node(Class):

    pass
class ObjectNode:

    pass
class UML2_ExpansionNode(ObjectNode):

    pass
class UML2_Pin(ObjectNode):

    pass
class UML2_CentralBufferNode(ObjectNode):

    pass
class UML2_ActivityParameterNode(ObjectNode):

    pass
class Classifier:

    pass
class UML2_Signal(Classifier):

    pass
class UML2_Actor(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_DataType(Classifier):

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_Artifact(Classifier):

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class UML2_Association(Classifier):

    pass
class UML2_Interface(Classifier):

    pass
class TypedElement:

    pass
class UML2_Operation(TypedElement):

    pass
class UML2_Variable(TypedElement):

    pass
class UML2_ObjectNode(TypedElement):

    pass
class UML2_ValueSpecification(TypedElement):

    pass
class UML2_StructuralFeature(TypedElement):

    pass
class UML2_Parameter(TypedElement):

    def __init__(self, direction: str, UML2_Parameter: "UML2_Operation" = None):
        self.direction = direction
        self.UML2_Parameter = UML2_Parameter
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def UML2_Parameter(self):
        return self.__UML2_Parameter

    @UML2_Parameter.setter
    def UML2_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__UML2_Parameter", None)
        self.__UML2_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Operation"):
                opp_val = getattr(old_value, "UML2_Operation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Operation"):
                opp_val = getattr(value, "UML2_Operation", None)
                if opp_val is None:
                    setattr(value, "UML2_Operation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
