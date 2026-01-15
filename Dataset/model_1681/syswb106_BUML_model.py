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
syswb106_System = Class(name="syswb106::System")
syswb106_FunctionProperty = Class(name="syswb106::FunctionProperty")
syswb106_Workbench = Class(name="syswb106::Workbench")
syswb106_Thing = Class(name="syswb106::Thing")
syswb106_Thoughts = Class(name="syswb106::Thoughts")
syswb106_PatternCatalog = Class(name="syswb106::PatternCatalog")
syswb106_RelatedTo = Class(name="syswb106::RelatedTo")
syswb106_Component = Class(name="syswb106::Component")
syswb106_Function = Class(name="syswb106::Function")

# syswb106_System class attributes and methods

# syswb106_FunctionProperty class attributes and methods
syswb106_FunctionProperty_description: Property = Property(name="description", type=StringType)
syswb106_FunctionProperty.attributes={syswb106_FunctionProperty_description}

# syswb106_Workbench class attributes and methods
syswb106_Workbench_aprop: Property = Property(name="aprop", type=StringType)
syswb106_Workbench.attributes={syswb106_Workbench_aprop}

# syswb106_Thing class attributes and methods
syswb106_Thing_id: Property = Property(name="id", type=IntegerType)
syswb106_Thing.attributes={syswb106_Thing_id}

# syswb106_Thoughts class attributes and methods

# syswb106_PatternCatalog class attributes and methods
syswb106_PatternCatalog_id: Property = Property(name="id", type=StringType)
syswb106_PatternCatalog.attributes={syswb106_PatternCatalog_id}

# syswb106_RelatedTo class attributes and methods
syswb106_RelatedTo_since: Property = Property(name="since", type=StringType)
syswb106_RelatedTo.attributes={syswb106_RelatedTo_since}

# syswb106_Component class attributes and methods

# syswb106_Function class attributes and methods

# Relationships
systemView3: BinaryAssociation = BinaryAssociation(
    name="systemView3",
    ends={
        Property(name="syswb106_System", type=syswb106_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_Workbench4", type=syswb106_System, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="syswb106_Thing", type=syswb106_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_Workbench", type=syswb106_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thoughts1: BinaryAssociation = BinaryAssociation(
    name="thoughts1",
    ends={
        Property(name="syswb106_Thoughts", type=syswb106_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_Workbench2", type=syswb106_Thoughts, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedTo13: BinaryAssociation = BinaryAssociation(
    name="relatedTo13",
    ends={
        Property(name="syswb106_Thing15", type=syswb106_Thoughts, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_Thoughts14", type=syswb106_Thing, multiplicity=Multiplicity(0, 9999))
    }
)
functionProperties5: BinaryAssociation = BinaryAssociation(
    name="functionProperties5",
    ends={
        Property(name="syswb106_FunctionProperty", type=syswb106_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_Workbench6", type=syswb106_FunctionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catalog7: BinaryAssociation = BinaryAssociation(
    name="catalog7",
    ends={
        Property(name="syswb106_PatternCatalog", type=syswb106_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_Workbench8", type=syswb106_PatternCatalog, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations9: BinaryAssociation = BinaryAssociation(
    name="relations9",
    ends={
        Property(name="RelatedTo", type=syswb106_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=syswb106_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing10: BinaryAssociation = BinaryAssociation(
    name="fromThing10",
    ends={
        Property(name="Thing", type=syswb106_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=syswb106_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing11: BinaryAssociation = BinaryAssociation(
    name="toThing11",
    ends={
        Property(name="syswb106_Thing12", type=syswb106_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_RelatedTo", type=syswb106_Thing, multiplicity=Multiplicity(0, 1))
    }
)
parent17: BinaryAssociation = BinaryAssociation(
    name="parent17",
    ends={
        Property(name="syswb106_FunctionProperty18", type=syswb106_FunctionProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_FunctionProperty16", type=syswb106_FunctionProperty, multiplicity=Multiplicity(0, 1))
    }
)
decompositions20: BinaryAssociation = BinaryAssociation(
    name="decompositions20",
    ends={
        Property(name="syswb106_Component", type=syswb106_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_Component19", type=syswb106_Component, multiplicity=Multiplicity(0, 9999))
    }
)
associations22: BinaryAssociation = BinaryAssociation(
    name="associations22",
    ends={
        Property(name="syswb106_Component23", type=syswb106_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_Component21", type=syswb106_Component, multiplicity=Multiplicity(0, 9999))
    }
)
performs24: BinaryAssociation = BinaryAssociation(
    name="performs24",
    ends={
        Property(name="syswb106_Function", type=syswb106_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_Component25", type=syswb106_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decompositions27: BinaryAssociation = BinaryAssociation(
    name="decompositions27",
    ends={
        Property(name="syswb106_Function28", type=syswb106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_Function26", type=syswb106_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property29: BinaryAssociation = BinaryAssociation(
    name="property29",
    ends={
        Property(name="syswb106_FunctionProperty31", type=syswb106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_Function30", type=syswb106_FunctionProperty, multiplicity=Multiplicity(0, 9999))
    }
)
associations33: BinaryAssociation = BinaryAssociation(
    name="associations33",
    ends={
        Property(name="syswb106_Function34", type=syswb106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_Function32", type=syswb106_Function, multiplicity=Multiplicity(0, 1))
    }
)
allocatedTo35: BinaryAssociation = BinaryAssociation(
    name="allocatedTo35",
    ends={
        Property(name="syswb106_Component37", type=syswb106_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_Function36", type=syswb106_Component, multiplicity=Multiplicity(0, 1))
    }
)
functionalArchitecture38: BinaryAssociation = BinaryAssociation(
    name="functionalArchitecture38",
    ends={
        Property(name="syswb106_Function40", type=syswb106_System, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_System39", type=syswb106_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
physicalArchitecture41: BinaryAssociation = BinaryAssociation(
    name="physicalArchitecture41",
    ends={
        Property(name="syswb106_Component43", type=syswb106_System, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_System42", type=syswb106_Component, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
patterns44: BinaryAssociation = BinaryAssociation(
    name="patterns44",
    ends={
        Property(name="syswb106_Function46", type=syswb106_PatternCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="syswb106_PatternCatalog45", type=syswb106_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="syswb106",
    types={syswb106_System, syswb106_FunctionProperty, syswb106_Workbench, syswb106_Thing, syswb106_Thoughts, syswb106_PatternCatalog, syswb106_RelatedTo, syswb106_Component, syswb106_Function},
    associations={systemView3, things0, thoughts1, relatedTo13, functionProperties5, catalog7, relations9, fromThing10, toThing11, parent17, decompositions20, associations22, performs24, decompositions27, property29, associations33, allocatedTo35, functionalArchitecture38, physicalArchitecture41, patterns44},
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