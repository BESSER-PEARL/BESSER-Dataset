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
actionpak1_InvokeSaflet2 = Class(name="actionpak1::InvokeSaflet2")
ParameterizedActionstep = Class(name="ParameterizedActionstep")
actionpak1_ActionstepTest = Class(name="actionpak1::ActionstepTest")
ActionStep = Class(name="ActionStep")
DynamicValue = Class(name="DynamicValue")
actionpak1_CustomInitiator = Class(name="actionpak1::CustomInitiator", is_abstract=True)
ParameterizedInitiator = Class(name="ParameterizedInitiator")
actionpak1_IncomingCall2 = Class(name="actionpak1::IncomingCall2", is_abstract=True)
actionstep_ParameterizedInitiator = Class(name="actionstep::ParameterizedInitiator")
call_CallSource1 = Class(name="call::CallSource1")
actionpak1_ScheduleSaflet = Class(name="actionpak1::ScheduleSaflet")
actionpak1_UnscheduleSaflet = Class(name="actionpak1::UnscheduleSaflet")

# actionpak1_InvokeSaflet2 class attributes and methods
actionpak1_InvokeSaflet2_labelText: Property = Property(name="labelText", type=StringType)
actionpak1_InvokeSaflet2.attributes={actionpak1_InvokeSaflet2_labelText}

# ParameterizedActionstep class attributes and methods

# actionpak1_ActionstepTest class attributes and methods

# ActionStep class attributes and methods

# DynamicValue class attributes and methods

# actionpak1_CustomInitiator class attributes and methods

# ParameterizedInitiator class attributes and methods

# actionpak1_IncomingCall2 class attributes and methods
actionpak1_IncomingCall2_callName: Property = Property(name="callName", type=StringType)
actionpak1_IncomingCall2.attributes={actionpak1_IncomingCall2_callName}

# actionstep_ParameterizedInitiator class attributes and methods

# call_CallSource1 class attributes and methods

# actionpak1_ScheduleSaflet class attributes and methods

# actionpak1_UnscheduleSaflet class attributes and methods

# Relationships
message0: BinaryAssociation = BinaryAssociation(
    name="message0",
    ends={
        Property(name="DynamicValue", type=actionpak1_ActionstepTest, multiplicity=Multiplicity(1, 1)),
        Property(name="actionpak1_ActionstepTest", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetSafletPath1: BinaryAssociation = BinaryAssociation(
    name="targetSafletPath1",
    ends={
        Property(name="DynamicValue2", type=actionpak1_InvokeSaflet2, multiplicity=Multiplicity(1, 1)),
        Property(name="actionpak1_InvokeSaflet2", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jobNamePrefix3: BinaryAssociation = BinaryAssociation(
    name="jobNamePrefix3",
    ends={
        Property(name="DynamicValue4", type=actionpak1_ScheduleSaflet, multiplicity=Multiplicity(1, 1)),
        Property(name="actionpak1_ScheduleSaflet", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetSafletPath5: BinaryAssociation = BinaryAssociation(
    name="targetSafletPath5",
    ends={
        Property(name="DynamicValue7", type=actionpak1_ScheduleSaflet, multiplicity=Multiplicity(1, 1)),
        Property(name="actionpak1_ScheduleSaflet6", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cronExpression8: BinaryAssociation = BinaryAssociation(
    name="cronExpression8",
    ends={
        Property(name="DynamicValue10", type=actionpak1_ScheduleSaflet, multiplicity=Multiplicity(1, 1)),
        Property(name="actionpak1_ScheduleSaflet9", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
startDateTime11: BinaryAssociation = BinaryAssociation(
    name="startDateTime11",
    ends={
        Property(name="DynamicValue13", type=actionpak1_ScheduleSaflet, multiplicity=Multiplicity(1, 1)),
        Property(name="actionpak1_ScheduleSaflet12", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endDateTime14: BinaryAssociation = BinaryAssociation(
    name="endDateTime14",
    ends={
        Property(name="DynamicValue16", type=actionpak1_ScheduleSaflet, multiplicity=Multiplicity(1, 1)),
        Property(name="actionpak1_ScheduleSaflet15", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
calendarName17: BinaryAssociation = BinaryAssociation(
    name="calendarName17",
    ends={
        Property(name="DynamicValue19", type=actionpak1_ScheduleSaflet, multiplicity=Multiplicity(1, 1)),
        Property(name="actionpak1_ScheduleSaflet18", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jobName20: BinaryAssociation = BinaryAssociation(
    name="jobName20",
    ends={
        Property(name="DynamicValue22", type=actionpak1_ScheduleSaflet, multiplicity=Multiplicity(1, 1)),
        Property(name="actionpak1_ScheduleSaflet21", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jobName23: BinaryAssociation = BinaryAssociation(
    name="jobName23",
    ends={
        Property(name="DynamicValue24", type=actionpak1_UnscheduleSaflet, multiplicity=Multiplicity(1, 1)),
        Property(name="actionpak1_UnscheduleSaflet", type=DynamicValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_actionpak1_ActionstepTest_ActionStep = Generalization(general=ActionStep, specific=actionpak1_ActionstepTest)
gen_actionpak1_CustomInitiator_ParameterizedInitiator = Generalization(general=ParameterizedInitiator, specific=actionpak1_CustomInitiator)
gen_actionpak1_IncomingCall2_actionstep_ParameterizedInitiator = Generalization(general=actionstep_ParameterizedInitiator, specific=actionpak1_IncomingCall2)
gen_actionpak1_IncomingCall2_call_CallSource1 = Generalization(general=call_CallSource1, specific=actionpak1_IncomingCall2)
gen_actionpak1_InvokeSaflet2_ParameterizedActionstep = Generalization(general=ParameterizedActionstep, specific=actionpak1_InvokeSaflet2)
gen_actionpak1_ScheduleSaflet_ParameterizedActionstep = Generalization(general=ParameterizedActionstep, specific=actionpak1_ScheduleSaflet)
gen_actionpak1_UnscheduleSaflet_ActionStep = Generalization(general=ActionStep, specific=actionpak1_UnscheduleSaflet)

# Domain Model
domain_model = DomainModel(
    name="actionpak1",
    types={actionpak1_InvokeSaflet2, ParameterizedActionstep, actionpak1_ActionstepTest, ActionStep, DynamicValue, actionpak1_CustomInitiator, ParameterizedInitiator, actionpak1_IncomingCall2, actionstep_ParameterizedInitiator, call_CallSource1, actionpak1_ScheduleSaflet, actionpak1_UnscheduleSaflet},
    associations={message0, targetSafletPath1, jobNamePrefix3, targetSafletPath5, cronExpression8, startDateTime11, endDateTime14, calendarName17, jobName20, jobName23},
    generalizations={gen_actionpak1_ActionstepTest_ActionStep, gen_actionpak1_CustomInitiator_ParameterizedInitiator, gen_actionpak1_IncomingCall2_actionstep_ParameterizedInitiator, gen_actionpak1_IncomingCall2_call_CallSource1, gen_actionpak1_InvokeSaflet2_ParameterizedActionstep, gen_actionpak1_ScheduleSaflet_ParameterizedActionstep, gen_actionpak1_UnscheduleSaflet_ActionStep},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)