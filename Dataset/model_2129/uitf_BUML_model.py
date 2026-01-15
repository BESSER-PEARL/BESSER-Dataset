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
UserInstructionEnum: Enumeration = Enumeration(
    name="UserInstructionEnum",
    literals={
            EnumerationLiteral(name="SetUIValue"),
			EnumerationLiteral(name="SendUITrigger"),
			EnumerationLiteral(name="ManipulateUIControl"),
			EnumerationLiteral(name="AssertUIValue"),
			EnumerationLiteral(name="AssertUIState"),
			EnumerationLiteral(name="InstantiateUISUT")
    }
)

# Classes
uitf_TestCase = Class(name="uitf::TestCase")
uitf_Variable = Class(name="uitf::Variable")
Variable = Class(name="Variable")
uitf_UISUT = Class(name="uitf::UISUT")
uitf_Statement = Class(name="uitf::Statement")
uitf_TestSuite = Class(name="uitf::TestSuite")
uitf_AssertInState = Class(name="uitf::AssertInState")
Statement = Class(name="Statement")
uitf_UIControl = Class(name="uitf::UIControl")
uitf_UIControlVariable = Class(name="uitf::UIControlVariable")
uitf_TriggeredTransition = Class(name="uitf::TriggeredTransition")

# uitf_TestCase class attributes and methods
uitf_TestCase_id: Property = Property(name="id", type=StringType)
uitf_TestCase_m_start: Method = Method(name="start", parameters={})
uitf_TestCase_m_stop: Method = Method(name="stop", parameters={})
uitf_TestCase.attributes={uitf_TestCase_id}
uitf_TestCase.methods={uitf_TestCase_m_stop, uitf_TestCase_m_start}

# uitf_Variable class attributes and methods
uitf_Variable_id: Property = Property(name="id", type=StringType)
uitf_Variable_m_setValue: Method = Method(name="setValue", parameters={Parameter(name='val')})
uitf_Variable_m_getValue: Method = Method(name="getValue", parameters={}, type=StringType)
uitf_Variable_m_assertValue: Method = Method(name="assertValue", parameters={})
uitf_Variable.attributes={uitf_Variable_id}
uitf_Variable.methods={uitf_Variable_m_getValue, uitf_Variable_m_assertValue, uitf_Variable_m_setValue}

# Variable class attributes and methods

# uitf_UISUT class attributes and methods
uitf_UISUT_objectURI: Property = Property(name="objectURI", type=StringType)
uitf_UISUT_m_onUITrigger: Method = Method(name="onUITrigger", parameters={Parameter(name='trigger')})
uitf_UISUT_m_onManipulateUIControl: Method = Method(name="onManipulateUIControl", parameters={Parameter(name='manipulationKind'), Parameter(name='controlPath')})
uitf_UISUT_m_onManipulateUIControlData: Method = Method(name="onManipulateUIControlData", parameters={Parameter(name='controlPropertyKey'), Parameter(name='controlPath'), Parameter(name='controlPropertyVal')})
uitf_UISUT_m_assertInState: Method = Method(name="assertInState", parameters={})
uitf_UISUT.attributes={uitf_UISUT_objectURI}
uitf_UISUT.methods={uitf_UISUT_m_onManipulateUIControl, uitf_UISUT_m_assertInState, uitf_UISUT_m_onUITrigger, uitf_UISUT_m_onManipulateUIControlData}

# uitf_Statement class attributes and methods
uitf_Statement_description: Property = Property(name="description", type=StringType)
uitf_Statement_kind: Property = Property(name="kind", type=StringType)
uitf_Statement.attributes={uitf_Statement_description, uitf_Statement_kind}

# uitf_TestSuite class attributes and methods
uitf_TestSuite_id: Property = Property(name="id", type=StringType)
uitf_TestSuite_m_start: Method = Method(name="start", parameters={})
uitf_TestSuite_m_stop: Method = Method(name="stop", parameters={})
uitf_TestSuite.attributes={uitf_TestSuite_id}
uitf_TestSuite.methods={uitf_TestSuite_m_stop, uitf_TestSuite_m_start}

# uitf_AssertInState class attributes and methods
uitf_AssertInState_stateId: Property = Property(name="stateId", type=StringType)
uitf_AssertInState.attributes={uitf_AssertInState_stateId}

# Statement class attributes and methods

# uitf_UIControl class attributes and methods
uitf_UIControl_id: Property = Property(name="id", type=StringType)
uitf_UIControl.attributes={uitf_UIControl_id}

# uitf_UIControlVariable class attributes and methods

# uitf_TriggeredTransition class attributes and methods
uitf_TriggeredTransition_scriptStr: Property = Property(name="scriptStr", type=StringType)
uitf_TriggeredTransition_transitionId: Property = Property(name="transitionId", type=StringType)
uitf_TriggeredTransition.attributes={uitf_TriggeredTransition_scriptStr, uitf_TriggeredTransition_transitionId}

# Relationships
itsUISUT0: BinaryAssociation = BinaryAssociation(
    name="itsUISUT0",
    ends={
        Property(name="uitf_UISUT", type=uitf_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="uitf_TestCase", type=uitf_UISUT, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
itsStatement1: BinaryAssociation = BinaryAssociation(
    name="itsStatement1",
    ends={
        Property(name="uitf_Statement", type=uitf_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="uitf_TestCase2", type=uitf_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itsTestCase3: BinaryAssociation = BinaryAssociation(
    name="itsTestCase3",
    ends={
        Property(name="uitf_TestCase4", type=uitf_TestSuite, multiplicity=Multiplicity(1, 1)),
        Property(name="uitf_TestSuite", type=uitf_TestCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itsVariable12: BinaryAssociation = BinaryAssociation(
    name="itsVariable12",
    ends={
        Property(name="uitf_Variable14", type=uitf_UIControl, multiplicity=Multiplicity(1, 1)),
        Property(name="uitf_UIControl13", type=uitf_Variable, multiplicity=Multiplicity(0, 1))
    }
)
itsVariable5: BinaryAssociation = BinaryAssociation(
    name="itsVariable5",
    ends={
        Property(name="uitf_Variable", type=uitf_UISUT, multiplicity=Multiplicity(1, 1)),
        Property(name="uitf_UISUT6", type=uitf_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itsUICtrl7: BinaryAssociation = BinaryAssociation(
    name="itsUICtrl7",
    ends={
        Property(name="uitf_UIControl", type=uitf_UISUT, multiplicity=Multiplicity(1, 1)),
        Property(name="uitf_UISUT8", type=uitf_UIControl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itsVariable9: BinaryAssociation = BinaryAssociation(
    name="itsVariable9",
    ends={
        Property(name="uitf_Variable11", type=uitf_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="uitf_Statement10", type=uitf_Variable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_uitf_UISUT_Variable = Generalization(general=Variable, specific=uitf_UISUT)
gen_uitf_AssertInState_Statement = Generalization(general=Statement, specific=uitf_AssertInState)
gen_uitf_UIControlVariable_Variable = Generalization(general=Variable, specific=uitf_UIControlVariable)
gen_uitf_TriggeredTransition_Statement = Generalization(general=Statement, specific=uitf_TriggeredTransition)

# Domain Model
domain_model = DomainModel(
    name="uitf",
    types={uitf_TestCase, uitf_Variable, Variable, uitf_UISUT, uitf_Statement, uitf_TestSuite, uitf_AssertInState, Statement, uitf_UIControl, uitf_UIControlVariable, uitf_TriggeredTransition, UserInstructionEnum},
    associations={itsUISUT0, itsStatement1, itsTestCase3, itsVariable12, itsVariable5, itsUICtrl7, itsVariable9},
    generalizations={gen_uitf_UISUT_Variable, gen_uitf_AssertInState_Statement, gen_uitf_UIControlVariable_Variable, gen_uitf_TriggeredTransition_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)