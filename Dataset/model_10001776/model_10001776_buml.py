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
Waiter_Actor = Class(name="Waiter_Actor")
Client_Actor = Class(name="Client_Actor")
Register_order_UseCase = Class(name="Register_order_UseCase")
View_prepared_orders_UseCase = Class(name="View_prepared_orders_UseCase")
Mark_order_as_served_UseCase = Class(name="Mark_order_as_served_UseCase")
Consult_menu_UseCase = Class(name="Consult_menu_UseCase")
Place_order_UseCase = Class(name="Place_order_UseCase")
Chef_Actor = Class(name="Chef_Actor")
View_current_orders_UseCase = Class(name="View_current_orders_UseCase")
Mark_order_as_prepared_UseCase = Class(name="Mark_order_as_prepared_UseCase")
Cashier_Actor = Class(name="Cashier_Actor")
View_price_of_served_orders_UseCase = Class(name="View_price_of_served_orders_UseCase")
Question = Class(name="Question")
Answer = Class(name="Answer")
QuestonOrAnswer = Class(name="QuestonOrAnswer")
User = Class(name="User")
Tag = Class(name="Tag")

# Waiter_Actor class attributes and methods

# Client_Actor class attributes and methods

# Register_order_UseCase class attributes and methods

# View_prepared_orders_UseCase class attributes and methods

# Mark_order_as_served_UseCase class attributes and methods

# Consult_menu_UseCase class attributes and methods

# Place_order_UseCase class attributes and methods

# Chef_Actor class attributes and methods

# View_current_orders_UseCase class attributes and methods

# Mark_order_as_prepared_UseCase class attributes and methods

# Cashier_Actor class attributes and methods

# View_price_of_served_orders_UseCase class attributes and methods

# Question class attributes and methods
Question_title: Property = Property(name="title", type=StringType)
Question.attributes={Question_title}

# Answer class attributes and methods

# QuestonOrAnswer class attributes and methods
QuestonOrAnswer_body: Property = Property(name="body", type=StringType)
QuestonOrAnswer.attributes={QuestonOrAnswer_body}

# User class attributes and methods

# Tag class attributes and methods

# Relationships
User_Waiter: BinaryAssociation = BinaryAssociation(
    name="User_Waiter",
    ends={
        Property(name="waiter0", type=Waiter_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=Client_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Waiter_Register_order: BinaryAssociation = BinaryAssociation(
    name="Waiter_Register_order",
    ends={
        Property(name="register_order2", type=Register_order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter3", type=Waiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Waiter_View_prepared_orders: BinaryAssociation = BinaryAssociation(
    name="Waiter_View_prepared_orders",
    ends={
        Property(name="view_prepared_orders4", type=View_prepared_orders_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter5", type=Waiter_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Client_Consult_menu: BinaryAssociation = BinaryAssociation(
    name="Client_Consult_menu",
    ends={
        Property(name="consult_menu6", type=Consult_menu_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client7", type=Client_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Client_Place_order: BinaryAssociation = BinaryAssociation(
    name="Client_Place_order",
    ends={
        Property(name="place_order8", type=Place_order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client9", type=Client_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Chef_View_current_orders: BinaryAssociation = BinaryAssociation(
    name="Chef_View_current_orders",
    ends={
        Property(name="view_current_orders10", type=View_current_orders_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="chef11", type=Chef_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Mark_order_as_prepared_Chef: BinaryAssociation = BinaryAssociation(
    name="Mark_order_as_prepared_Chef",
    ends={
        Property(name="chef12", type=Chef_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="mark_order_as_prepared13", type=Mark_order_as_prepared_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
View_price_of_served_orders_Cashier: BinaryAssociation = BinaryAssociation(
    name="View_price_of_served_orders_Cashier",
    ends={
        Property(name="cashier14", type=Cashier_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="view_price_of_served_orders15", type=View_price_of_served_orders_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
User_QuestonOrAnswer: BinaryAssociation = BinaryAssociation(
    name="User_QuestonOrAnswer",
    ends={
        Property(name="questonOrAnswer16", type=QuestonOrAnswer, multiplicity=Multiplicity(0, 9999)),
        Property(name="user17", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Tag_Question: BinaryAssociation = BinaryAssociation(
    name="Tag_Question",
    ends={
        Property(name="questions18", type=Question, multiplicity=Multiplicity(0, 9999)),
        Property(name="tags19", type=Tag, multiplicity=Multiplicity(0, 9999))
    }
)
Question_Question: BinaryAssociation = BinaryAssociation(
    name="Question_Question",
    ends={
        Property(name="question20", type=Question, multiplicity=Multiplicity(1, 1)),
        Property(name="similar21", type=Question, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_UqhLIMMVEeeWu_SLkciAbg",
    types={Waiter_Actor, Client_Actor, Register_order_UseCase, View_prepared_orders_UseCase, Mark_order_as_served_UseCase, Consult_menu_UseCase, Place_order_UseCase, Chef_Actor, View_current_orders_UseCase, Mark_order_as_prepared_UseCase, Cashier_Actor, View_price_of_served_orders_UseCase, Question, Answer, QuestonOrAnswer, User, Tag},
    associations={User_Waiter, Waiter_Register_order, Waiter_View_prepared_orders, Client_Consult_menu, Client_Place_order, Chef_View_current_orders, Mark_order_as_prepared_Chef, View_price_of_served_orders_Cashier, User_QuestonOrAnswer, Tag_Question, Question_Question},
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