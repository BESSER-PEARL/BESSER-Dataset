from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractAction:

    pass
class ClassicalExpression_BinaryIntegerExpression:

    pass
class FSMModel_IntegerAssignement(AbstractAction, ClassicalExpression_BinaryIntegerExpression):

    pass
class ClockExpressionAndRelation_BindableEntity:

    pass
class AbstractTrigger:

    pass
class ClassicalExpression_ClassicalExpression:

    pass
class ClockExpressionAndRelation_ConcreteEntity:

    pass
class FSMModel_Trigger(AbstractTrigger):

    pass
class ClassicalExpression_BooleanExpression:

    pass
class AbstractGuard:

    pass
class FSMModel_Guard(AbstractGuard):

    pass
class FSMModel_AbstractTrigger(ABC):

    pass
class FSMModel_AbstractGuard(ABC):

    pass
class FSMModel_DeclarationBlock:

    pass
class FSMModel_AbstractAction(ABC):

    pass
class NamedElement:

    pass
class FSMModel_StateMachineDefinition(NamedElement):

    pass
class FSMModel_Transition(NamedElement):

    pass
class FSMModel_State(NamedElement):

    pass