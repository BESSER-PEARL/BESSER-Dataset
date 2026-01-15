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
cgimodel_StateModels = Class(name="cgimodel::StateModels")
cgimodel_StateModel = Class(name="cgimodel::StateModel")
cgimodel_BaseState = Class(name="cgimodel::BaseState", is_abstract=True)
cgimodel_Transition = Class(name="cgimodel::Transition")
cgimodel_State = Class(name="cgimodel::State")
BaseState = Class(name="BaseState")
cgimodel_Expr = Class(name="cgimodel::Expr")
cgimodel_OrState = Class(name="cgimodel::OrState")

# cgimodel_StateModels class attributes and methods

# cgimodel_StateModel class attributes and methods
cgimodel_StateModel_name: Property = Property(name="name", type=StringType)
cgimodel_StateModel.attributes={cgimodel_StateModel_name}

# cgimodel_BaseState class attributes and methods
cgimodel_BaseState_name: Property = Property(name="name", type=StringType)
cgimodel_BaseState_m_isSet: Method = Method(name="isSet", parameters={}, type=BooleanType)
cgimodel_BaseState.attributes={cgimodel_BaseState_name}
cgimodel_BaseState.methods={cgimodel_BaseState_m_isSet}

# cgimodel_Transition class attributes and methods

# cgimodel_State class attributes and methods
cgimodel_State_set: Property = Property(name="set", type=BooleanType)
cgimodel_State.attributes={cgimodel_State_set}

# BaseState class attributes and methods

# cgimodel_Expr class attributes and methods
cgimodel_Expr_value: Property = Property(name="value", type=StringType)
cgimodel_Expr.attributes={cgimodel_Expr_value}

# cgimodel_OrState class attributes and methods

# Relationships
stateModels15: BinaryAssociation = BinaryAssociation(
    name="stateModels15",
    ends={
        Property(name="cgimodel_StateModel16", type=cgimodel_StateModels, multiplicity=Multiplicity(1, 1)),
        Property(name="cgimodel_StateModels", type=cgimodel_StateModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="cgimodel_BaseState", type=cgimodel_StateModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cgimodel_StateModel", type=cgimodel_BaseState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="cgimodel_Transition", type=cgimodel_StateModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cgimodel_StateModel2", type=cgimodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr3: BinaryAssociation = BinaryAssociation(
    name="expr3",
    ends={
        Property(name="cgimodel_Expr", type=cgimodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cgimodel_State", type=cgimodel_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states4: BinaryAssociation = BinaryAssociation(
    name="states4",
    ends={
        Property(name="cgimodel_BaseState5", type=cgimodel_OrState, multiplicity=Multiplicity(1, 1)),
        Property(name="cgimodel_OrState", type=cgimodel_BaseState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="cgimodel_BaseState8", type=cgimodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cgimodel_Transition7", type=cgimodel_BaseState, multiplicity=Multiplicity(0, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="cgimodel_State11", type=cgimodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cgimodel_Transition10", type=cgimodel_State, multiplicity=Multiplicity(0, 1))
    }
)
condition12: BinaryAssociation = BinaryAssociation(
    name="condition12",
    ends={
        Property(name="cgimodel_Expr14", type=cgimodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cgimodel_Transition13", type=cgimodel_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_cgimodel_State_BaseState = Generalization(general=BaseState, specific=cgimodel_State)
gen_cgimodel_OrState_BaseState = Generalization(general=BaseState, specific=cgimodel_OrState)

# Domain Model
domain_model = DomainModel(
    name="cgimodel",
    types={cgimodel_StateModels, cgimodel_StateModel, cgimodel_BaseState, cgimodel_Transition, cgimodel_State, BaseState, cgimodel_Expr, cgimodel_OrState},
    associations={stateModels15, states0, transitions1, expr3, states4, source6, target9, condition12},
    generalizations={gen_cgimodel_State_BaseState, gen_cgimodel_OrState_BaseState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)