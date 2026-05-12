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
NuRightAnswer: Enumeration = Enumeration(
    name="NuRightAnswer",
    literals={
            
    }
)

OtherAnswer: Enumeration = Enumeration(
    name="OtherAnswer",
    literals={
            
    }
)

# Classes
ConcreteRightAnswers = Class(name="ConcreteRightAnswers")
Answers = Class(name="Answers")
Choices = Class(name="Choices")
ConcreteOtherAnswers = Class(name="ConcreteOtherAnswers")
AnswerdBuilder = Class(name="AnswerdBuilder")
MultipleChoicesAnswers = Class(name="MultipleChoicesAnswers")
MCRightAnswer = Class(name="MCRightAnswer")
NumericAnswers = Class(name="NumericAnswers")

# ConcreteRightAnswers class attributes and methods
ConcreteRightAnswers_address: Property = Property(name="address", type=StringType)
ConcreteRightAnswers_phone: Property = Property(name="phone", type=StringType)
ConcreteRightAnswers_email: Property = Property(name="email", type=StringType)
ConcreteRightAnswers.attributes={ConcreteRightAnswers_email, ConcreteRightAnswers_phone, ConcreteRightAnswers_address}

# Answers class attributes and methods
Answers_paidDate: Property = Property(name="paidDate", type=DateType)
Answers_total: Property = Property(name="total", type=FloatType)
Answers_details: Property = Property(name="details", type=StringType)
Answers.attributes={Answers_paidDate, Answers_details, Answers_total}

# Choices class attributes and methods
Choices_creationDate: Property = Property(name="creationDate", type=DateType)
Choices.attributes={Choices_creationDate}

# ConcreteOtherAnswers class attributes and methods
ConcreteOtherAnswers_billingAddress: Property = Property(name="billingAddress", type=StringType)
ConcreteOtherAnswers_open: Property = Property(name="open", type=DateType)
ConcreteOtherAnswers_closed: Property = Property(name="closed", type=DateType)
ConcreteOtherAnswers_isClosed: Property = Property(name="isClosed", type=BooleanType)
ConcreteOtherAnswers.attributes={ConcreteOtherAnswers_isClosed, ConcreteOtherAnswers_closed, ConcreteOtherAnswers_billingAddress, ConcreteOtherAnswers_open}

# AnswerdBuilder class attributes and methods
AnswerdBuilder_login: Property = Property(name="login", type=StringType)
AnswerdBuilder_password: Property = Property(name="password", type=StringType)
AnswerdBuilder_state: Property = Property(name="state", type=NuRightAnswer)
AnswerdBuilder.attributes={AnswerdBuilder_state, AnswerdBuilder_login, AnswerdBuilder_password}

# MultipleChoicesAnswers class attributes and methods
MultipleChoicesAnswers_number: Property = Property(name="number", type=IntegerType)
MultipleChoicesAnswers_ordered: Property = Property(name="ordered", type=DateType)
MultipleChoicesAnswers_shipped: Property = Property(name="shipped", type=BooleanType)
MultipleChoicesAnswers_shipTo: Property = Property(name="shipTo", type=StringType)
MultipleChoicesAnswers_total: Property = Property(name="total", type=FloatType)
MultipleChoicesAnswers_status: Property = Property(name="status", type=OtherAnswer)
MultipleChoicesAnswers.attributes={MultipleChoicesAnswers_status, MultipleChoicesAnswers_number, MultipleChoicesAnswers_total, MultipleChoicesAnswers_shipTo, MultipleChoicesAnswers_ordered, MultipleChoicesAnswers_shipped}

# MCRightAnswer class attributes and methods
MCRightAnswer_quantity: Property = Property(name="quantity", type=IntegerType)
MCRightAnswer_price: Property = Property(name="price", type=FloatType)
MCRightAnswer.attributes={MCRightAnswer_quantity, MCRightAnswer_price}

# NumericAnswers class attributes and methods
NumericAnswers_name: Property = Property(name="name", type=StringType)
NumericAnswers_description: Property = Property(name="description", type=StringType)
NumericAnswers.attributes={NumericAnswers_description, NumericAnswers_name}

# Relationships
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="customer0", type=ConcreteRightAnswers, multiplicity=Multiplicity(1, 1)),
        Property(name="webUser1", type=AnswerdBuilder, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="account2", type=ConcreteOtherAnswers, multiplicity=Multiplicity(1, 1)),
        Property(name="customer3", type=AnswerdBuilder, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9c48f098_5614_406a_92eb_9f7b2b7c3554",
    types={ConcreteRightAnswers, Answers, Choices, ConcreteOtherAnswers, AnswerdBuilder, MultipleChoicesAnswers, MCRightAnswer, NumericAnswers, NuRightAnswer, OtherAnswer},
    associations={WebUser_Customer, Customer_Account},
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