from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class DataType:

    pass
class UML2_PrimitiveType(DataType):

    pass
class Association:

    pass
class UML2_CommunicationPath(Association):

    pass
class Class:

    pass
class UML2_Behavior(Class):

    pass
class Classifier:

    pass
class UML2_Actor(Classifier):

    pass
class UML2_Association(Classifier):

    pass
class UML2_Interface(Classifier):

    pass
class Node:

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_Artifact(Classifier):

    pass
class UML2_Enumeration(DataType):

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class UML2_Device(Node):

    pass
class UML2_AssociationClass(Class, Association):

    pass
class EncapsulatedClassifier:

    pass
class UML2_Stereotype(Class):

    pass
class UML2_Component(Class):

    pass
class Behavior:

    pass
class UML2_Interaction(Behavior):

    pass
class UML2_Activity(Behavior):

    pass
class UML2_StateMachine(Behavior):

    pass
class UML2_Extension(Association):

    pass
class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class UML2_Signal(Classifier):

    pass
class UML2_DataType(Classifier):

    pass
class UML2_Node(Class):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class UML2_CreateObjectAction:

    pass
class StructuredClassifier:

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class BehavioredClassifier:

    pass
class UML2_UseCase(BehavioredClassifier):

    pass
class UML2_Class(BehavioredClassifier, EncapsulatedClassifier):

    pass
class UML2_Collaboration(BehavioredClassifier, StructuredClassifier):

    pass
class UML2_Classifier:

    def __init__(self, isAbstract: bool, UML2_Classifier: "UML2_CreateObjectAction" = None):
        self.isAbstract = isAbstract
        self.UML2_Classifier = UML2_Classifier
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def UML2_Classifier(self):
        return self.__UML2_Classifier

    @UML2_Classifier.setter
    def UML2_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier", None)
        self.__UML2_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_CreateObjectAction"):
                opp_val = getattr(old_value, "UML2_CreateObjectAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2_CreateObjectAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_CreateObjectAction"):
                opp_val = getattr(value, "UML2_CreateObjectAction", None)
                setattr(value, "UML2_CreateObjectAction", self)
