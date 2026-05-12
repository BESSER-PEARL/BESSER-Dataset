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
RoyalAndLoyal_Service = Class(name="RoyalAndLoyal_Service")
RoyalAndLoyal_ProgramPartner = Class(name="RoyalAndLoyal_ProgramPartner")
RoyalAndLoyal_ServiceLevel = Class(name="RoyalAndLoyal_ServiceLevel")
RoyalAndLoyal_Customer = Class(name="RoyalAndLoyal_Customer")
RoyalAndLoyal_Container_RandL = Class(name="RoyalAndLoyal_Container_RandL")
RoyalAndLoyal_CustomerCard = Class(name="RoyalAndLoyal_CustomerCard")
RoyalAndLoyal_LoyaltyProgram = Class(name="RoyalAndLoyal_LoyaltyProgram")

# RoyalAndLoyal_Service class attributes and methods

# RoyalAndLoyal_ProgramPartner class attributes and methods
RoyalAndLoyal_ProgramPartner_numberOfCustomers: Property = Property(name="numberOfCustomers", type=IntegerType)
RoyalAndLoyal_ProgramPartner.attributes={RoyalAndLoyal_ProgramPartner_numberOfCustomers}

# RoyalAndLoyal_ServiceLevel class attributes and methods

# RoyalAndLoyal_Customer class attributes and methods

# RoyalAndLoyal_Container_RandL class attributes and methods

# RoyalAndLoyal_CustomerCard class attributes and methods
RoyalAndLoyal_CustomerCard_valid: Property = Property(name="valid", type=BooleanType)
RoyalAndLoyal_CustomerCard.attributes={RoyalAndLoyal_CustomerCard_valid}

# RoyalAndLoyal_LoyaltyProgram class attributes and methods
RoyalAndLoyal_LoyaltyProgram_m_addService: Method = Method(name="addService", parameters={Parameter(name='RoyalAndLoyal_s', type=StringType), Parameter(name='RoyalAndLoyal_p', type=StringType), Parameter(name='RoyalAndLoyal_l', type=StringType)})
RoyalAndLoyal_LoyaltyProgram_m_enroll: Method = Method(name="enroll", parameters={Parameter(name='RoyalAndLoyal_c', type=StringType)})
RoyalAndLoyal_LoyaltyProgram.methods={RoyalAndLoyal_LoyaltyProgram_m_addService, RoyalAndLoyal_LoyaltyProgram_m_enroll}

# Relationships
partners0: BinaryAssociation = BinaryAssociation(
    name="partners0",
    ends={
        Property(name="ProgramPartner", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="programs", type=RoyalAndLoyal_ProgramPartner, multiplicity=Multiplicity(1, 9999))
    }
)
levels1: BinaryAssociation = BinaryAssociation(
    name="levels1",
    ends={
        Property(name="ServiceLevel", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="program", type=RoyalAndLoyal_ServiceLevel, multiplicity=Multiplicity(1, 9999))
    }
)
participants2: BinaryAssociation = BinaryAssociation(
    name="participants2",
    ends={
        Property(name="Customer", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="programs3", type=RoyalAndLoyal_Customer, multiplicity=Multiplicity(0, 9999))
    }
)
program4: BinaryAssociation = BinaryAssociation(
    name="program4",
    ends={
        Property(name="LoyaltyProgram", type=RoyalAndLoyal_ServiceLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="levels", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(0, 1))
    }
)
availableServices5: BinaryAssociation = BinaryAssociation(
    name="availableServices5",
    ends={
        Property(name="RoyalAndLoyal_Service", type=RoyalAndLoyal_ServiceLevel, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_ServiceLevel", type=RoyalAndLoyal_Service, multiplicity=Multiplicity(0, 9999))
    }
)
ref_RandL_Customer6: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Customer6",
    ends={
        Property(name="RoyalAndLoyal_Customer", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL", type=RoyalAndLoyal_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_CustomerCard7: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_CustomerCard7",
    ends={
        Property(name="RoyalAndLoyal_CustomerCard", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL8", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_Service9: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Service9",
    ends={
        Property(name="RoyalAndLoyal_Service11", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL10", type=RoyalAndLoyal_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_LoyaltyProgram12: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_LoyaltyProgram12",
    ends={
        Property(name="RoyalAndLoyal_LoyaltyProgram", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL13", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_ServiceLevel14: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_ServiceLevel14",
    ends={
        Property(name="RoyalAndLoyal_ServiceLevel16", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL15", type=RoyalAndLoyal_ServiceLevel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref_RandL_ProgramPartner17: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_ProgramPartner17",
    ends={
        Property(name="RoyalAndLoyal_ProgramPartner", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL18", type=RoyalAndLoyal_ProgramPartner, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programs19: BinaryAssociation = BinaryAssociation(
    name="programs19",
    ends={
        Property(name="LoyaltyProgram20", type=RoyalAndLoyal_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="participants", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(0, 9999))
    }
)
cards21: BinaryAssociation = BinaryAssociation(
    name="cards21",
    ends={
        Property(name="CustomerCard", type=RoyalAndLoyal_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(0, 9999))
    }
)
owner25: BinaryAssociation = BinaryAssociation(
    name="owner25",
    ends={
        Property(name="Customer26", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(1, 1)),
        Property(name="cards", type=RoyalAndLoyal_Customer, multiplicity=Multiplicity(0, 1))
    }
)
deliveredServices27: BinaryAssociation = BinaryAssociation(
    name="deliveredServices27",
    ends={
        Property(name="RoyalAndLoyal_Service29", type=RoyalAndLoyal_ProgramPartner, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_ProgramPartner28", type=RoyalAndLoyal_Service, multiplicity=Multiplicity(0, 9999))
    }
)
programs30: BinaryAssociation = BinaryAssociation(
    name="programs30",
    ends={
        Property(name="LoyaltyProgram31", type=RoyalAndLoyal_ProgramPartner, multiplicity=Multiplicity(1, 1)),
        Property(name="partners", type=RoyalAndLoyal_LoyaltyProgram, multiplicity=Multiplicity(1, 9999))
    }
)
myLevel22: BinaryAssociation = BinaryAssociation(
    name="myLevel22",
    ends={
        Property(name="RoyalAndLoyal_ServiceLevel24", type=RoyalAndLoyal_CustomerCard, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_CustomerCard23", type=RoyalAndLoyal_ServiceLevel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)


# OCL Constraints
invariant_ProgramPartner1: Constraint = Constraint(
    name="invariant_ProgramPartner1",
    context=RoyalAndLoyal_ProgramPartner,
    expression="context ProgramPartner inv: self.programs->collect( i_LoyaltyProgram : LoyaltyProgram | i_LoyaltyProgram.partners )->select( p : ProgramPartner | p <> self )->isEmpty()",
    language="OCL"
)
invariant_ServiceLevel1: Constraint = Constraint(
    name="invariant_ServiceLevel1",
    context=RoyalAndLoyal_ServiceLevel,
    expression="context ServiceLevel inv: self.program.partners->isEmpty()",
    language="OCL"
)
invariant_Customer10: Constraint = Constraint(
    name="invariant_Customer10",
    context=RoyalAndLoyal_Customer,
    expression="context Customer inv: self.programs->collect( i_LoyaltyProgram : LoyaltyProgram | i_LoyaltyProgram.partners )->collectNested( i_ProgramPartner : ProgramPartner | i_ProgramPartner.deliveredServices )->isEmpty()",
    language="OCL"
)
invariant_sizesAgree: Constraint = Constraint(
    name="invariant_sizesAgree",
    context=RoyalAndLoyal_Customer,
    expression="context Customer inv: self.programs->size() = self.cards->select( i_CustomerCard : CustomerCard | i_CustomerCard.valid = true )->size()",
    language="OCL"
)
invariant_nrOfParticipants: Constraint = Constraint(
    name="invariant_nrOfParticipants",
    context=RoyalAndLoyal_ProgramPartner,
    expression="context ProgramPartner inv: self.numberOfCustomers = self.programs->collect( i_LoyaltyProgram : LoyaltyProgram | i_LoyaltyProgram.participants )->size()",
    language="OCL"
)
invariant_Customer1: Constraint = Constraint(
    name="invariant_Customer1",
    context=RoyalAndLoyal_Customer,
    expression="context Customer inv: (self.cards->select( i_CustomerCard : CustomerCard | i_CustomerCard.valid = true )->size()) > 1",
    language="OCL"
)
invariant_CustomerCard3: Constraint = Constraint(
    name="invariant_CustomerCard3",
    context=RoyalAndLoyal_CustomerCard,
    expression="context CustomerCard inv: self.owner.programs->size() > 0",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="RoyalAndLoyal",
    types={RoyalAndLoyal_Service, RoyalAndLoyal_ProgramPartner, RoyalAndLoyal_ServiceLevel, RoyalAndLoyal_Customer, RoyalAndLoyal_Container_RandL, RoyalAndLoyal_CustomerCard, RoyalAndLoyal_LoyaltyProgram},
    associations={partners0, levels1, participants2, program4, availableServices5, ref_RandL_Customer6, ref_RandL_CustomerCard7, ref_RandL_Service9, ref_RandL_LoyaltyProgram12, ref_RandL_ServiceLevel14, ref_RandL_ProgramPartner17, programs19, cards21, owner25, deliveredServices27, programs30, myLevel22},
    constraints={invariant_ProgramPartner1, invariant_ServiceLevel1, invariant_Customer10, invariant_sizesAgree, invariant_nrOfParticipants, invariant_Customer1, invariant_CustomerCard3},
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