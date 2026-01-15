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
entity_Package = Class(name="entity::Package")
NamedElement = Class(name="NamedElement")
entity_Type = Class(name="entity::Type", is_abstract=True)
entity_Entity = Class(name="entity::Entity")
Type = Class(name="Type")
entity_Member = Class(name="entity::Member", is_abstract=True)
entity_Field = Class(name="entity::Field")
Member = Class(name="Member")
entity_Method = Class(name="entity::Method")
entity_Service = Class(name="entity::Service")
entity_NamedElement = Class(name="entity::NamedElement", is_abstract=True)

# entity_Package class attributes and methods

# NamedElement class attributes and methods

# entity_Type class attributes and methods

# entity_Entity class attributes and methods

# Type class attributes and methods

# entity_Member class attributes and methods

# entity_Field class attributes and methods

# Member class attributes and methods

# entity_Method class attributes and methods
entity_Method_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
entity_Method.attributes={entity_Method_isAbstract}

# entity_Service class attributes and methods

# entity_NamedElement class attributes and methods
entity_NamedElement_name: Property = Property(name="name", type=StringType)
entity_NamedElement.attributes={entity_NamedElement_name}

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="entity_Type", type=entity_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Package", type=entity_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members1: BinaryAssociation = BinaryAssociation(
    name="members1",
    ends={
        Property(name="entity_Member", type=entity_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Entity", type=entity_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods2: BinaryAssociation = BinaryAssociation(
    name="methods2",
    ends={
        Property(name="entity_Method", type=entity_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="entity_Service", type=entity_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_entity_Package_NamedElement = Generalization(general=NamedElement, specific=entity_Package)
gen_entity_Entity_Type = Generalization(general=Type, specific=entity_Entity)
gen_entity_Member_NamedElement = Generalization(general=NamedElement, specific=entity_Member)
gen_entity_Field_Member = Generalization(general=Member, specific=entity_Field)
gen_entity_Method_Member = Generalization(general=Member, specific=entity_Method)
gen_entity_Service_Type = Generalization(general=Type, specific=entity_Service)
gen_entity_Type_NamedElement = Generalization(general=NamedElement, specific=entity_Type)

# Domain Model
domain_model = DomainModel(
    name="entity",
    types={entity_Package, NamedElement, entity_Type, entity_Entity, Type, entity_Member, entity_Field, Member, entity_Method, entity_Service, entity_NamedElement},
    associations={types0, members1, methods2},
    generalizations={gen_entity_Package_NamedElement, gen_entity_Entity_Type, gen_entity_Member_NamedElement, gen_entity_Field_Member, gen_entity_Method_Member, gen_entity_Service_Type, gen_entity_Type_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)