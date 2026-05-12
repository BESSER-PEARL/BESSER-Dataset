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
Presenter = Class(name="Presenter")
Model_Session = Class(name="Model_Session")
Model_Transaction = Class(name="Model_Transaction")
Model_Queue = Class(name="Model_Queue")
Model_WithdrawTransaction = Class(name="Model_WithdrawTransaction")
Model_Communication = Class(name="Model_Communication")
Model_ISO = Class(name="Model_ISO")
Model_Init = Class(name="Model_Init")
Model_BalanceInquiryTransaction = Class(name="Model_BalanceInquiryTransaction")
Model_IDLE = Class(name="Model_IDLE")

# Presenter class attributes and methods
Presenter_currentView: Property = Property(name="currentView", type=StringType)
Presenter_session: Property = Property(name="session", type=StringType)
Presenter.attributes={Presenter_currentView, Presenter_session}

# Model_Session class attributes and methods
Model_Session_DeviceStatus: Property = Property(name="DeviceStatus", type=StringType)
Model_Session_pan: Property = Property(name="pan", type=IntegerType)
Model_Session_track2: Property = Property(name="track2", type=StringType)
Model_Session.attributes={Model_Session_pan, Model_Session_DeviceStatus, Model_Session_track2}

# Model_Transaction class attributes and methods
Model_Transaction_attribute: Property = Property(name="attribute", type=StringType)
Model_Transaction_presenter: Property = Property(name="presenter", type=Presenter)
Model_Transaction.attributes={Model_Transaction_presenter, Model_Transaction_attribute}

# Model_Queue class attributes and methods
Model_Queue_attribute: Property = Property(name="attribute", type=StringType)
Model_Queue.attributes={Model_Queue_attribute}

# Model_WithdrawTransaction class attributes and methods
Model_WithdrawTransaction_amount: Property = Property(name="amount", type=IntegerType)
Model_WithdrawTransaction.attributes={Model_WithdrawTransaction_amount}

# Model_Communication class attributes and methods

# Model_ISO class attributes and methods

# Model_Init class attributes and methods

# Model_BalanceInquiryTransaction class attributes and methods

# Model_IDLE class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_484652f6_e5a4_46ab_befb_dfb8f7641371",
    types={Presenter, Model_Session, Model_Transaction, Model_Queue, Model_WithdrawTransaction, Model_Communication, Model_ISO, Model_Init, Model_BalanceInquiryTransaction, Model_IDLE},
    associations={},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)