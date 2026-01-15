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
smalluml_Class = Class(name="smalluml::Class")
Type = Class(name="Type")
smalluml_Operation = Class(name="smalluml::Operation")
NamedElement = Class(name="NamedElement")
smalluml_Type = Class(name="smalluml::Type")
smalluml_NamedElement = Class(name="smalluml::NamedElement", is_abstract=True)
smalluml_TypeString = Class(name="smalluml::TypeString")
smalluml_TypeReal = Class(name="smalluml::TypeReal")
smalluml_Property = Class(name="smalluml::Property")
smalluml_TypeBoolean = Class(name="smalluml::TypeBoolean")
smalluml_Root = Class(name="smalluml::Root")
smalluml_TypeInteger = Class(name="smalluml::TypeInteger")
smalluml_TypeUnlimitedNatural = Class(name="smalluml::TypeUnlimitedNatural")

# smalluml_Class class attributes and methods

# Type class attributes and methods

# smalluml_Operation class attributes and methods

# NamedElement class attributes and methods

# smalluml_Type class attributes and methods

# smalluml_NamedElement class attributes and methods
smalluml_NamedElement_name: Property = Property(name="name", type=StringType)
smalluml_NamedElement.attributes={smalluml_NamedElement_name}

# smalluml_TypeString class attributes and methods
smalluml_TypeString_value: Property = Property(name="value", type=StringType)
smalluml_TypeString.attributes={smalluml_TypeString_value}

# smalluml_TypeReal class attributes and methods
smalluml_TypeReal_value: Property = Property(name="value", type=StringType)
smalluml_TypeReal.attributes={smalluml_TypeReal_value}

# smalluml_Property class attributes and methods
smalluml_Property_upperBound: Property = Property(name="upperBound", type=IntegerType)
smalluml_Property_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
smalluml_Property.attributes={smalluml_Property_upperBound, smalluml_Property_lowerBound}

# smalluml_TypeBoolean class attributes and methods
smalluml_TypeBoolean_value: Property = Property(name="value", type=StringType)
smalluml_TypeBoolean.attributes={smalluml_TypeBoolean_value}

# smalluml_Root class attributes and methods

# smalluml_TypeInteger class attributes and methods
smalluml_TypeInteger_value: Property = Property(name="value", type=StringType)
smalluml_TypeInteger.attributes={smalluml_TypeInteger_value}

# smalluml_TypeUnlimitedNatural class attributes and methods
smalluml_TypeUnlimitedNatural_value: Property = Property(name="value", type=StringType)
smalluml_TypeUnlimitedNatural.attributes={smalluml_TypeUnlimitedNatural_value}

# Relationships
ownedOperations0: BinaryAssociation = BinaryAssociation(
    name="ownedOperations0",
    ends={
        Property(name="smalluml_Operation", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class", type=smalluml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultType6: BinaryAssociation = BinaryAssociation(
    name="resultType6",
    ends={
        Property(name="smalluml_Type", type=smalluml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Operation7", type=smalluml_Type, multiplicity=Multiplicity(0, 1))
    }
)
params8: BinaryAssociation = BinaryAssociation(
    name="params8",
    ends={
        Property(name="smalluml_Type10", type=smalluml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Operation9", type=smalluml_Type, multiplicity=Multiplicity(0, 9999))
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="smalluml_Type13", type=smalluml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Property12", type=smalluml_Type, multiplicity=Multiplicity(1, 1))
    }
)
superClass2: BinaryAssociation = BinaryAssociation(
    name="superClass2",
    ends={
        Property(name="smalluml_Class3", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class1", type=smalluml_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedProperties4: BinaryAssociation = BinaryAssociation(
    name="ownedProperties4",
    ends={
        Property(name="smalluml_Property", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class5", type=smalluml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements14: BinaryAssociation = BinaryAssociation(
    name="elements14",
    ends={
        Property(name="smalluml_Class15", type=smalluml_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Root", type=smalluml_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveTypes16: BinaryAssociation = BinaryAssociation(
    name="primitiveTypes16",
    ends={
        Property(name="smalluml_Type18", type=smalluml_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Root17", type=smalluml_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_smalluml_Class_Type = Generalization(general=Type, specific=smalluml_Class)
gen_smalluml_Operation_NamedElement = Generalization(general=NamedElement, specific=smalluml_Operation)
gen_smalluml_Property_NamedElement = Generalization(general=NamedElement, specific=smalluml_Property)
gen_smalluml_Type_NamedElement = Generalization(general=NamedElement, specific=smalluml_Type)
gen_smalluml_TypeString_Type = Generalization(general=Type, specific=smalluml_TypeString)
gen_smalluml_TypeBoolean_Type = Generalization(general=Type, specific=smalluml_TypeBoolean)
gen_smalluml_TypeReal_Type = Generalization(general=Type, specific=smalluml_TypeReal)
gen_smalluml_TypeInteger_Type = Generalization(general=Type, specific=smalluml_TypeInteger)
gen_smalluml_TypeUnlimitedNatural_Type = Generalization(general=Type, specific=smalluml_TypeUnlimitedNatural)

# Domain Model
domain_model = DomainModel(
    name="smalluml",
    types={smalluml_Class, Type, smalluml_Operation, NamedElement, smalluml_Type, smalluml_NamedElement, smalluml_TypeString, smalluml_TypeReal, smalluml_Property, smalluml_TypeBoolean, smalluml_Root, smalluml_TypeInteger, smalluml_TypeUnlimitedNatural},
    associations={ownedOperations0, resultType6, params8, type11, superClass2, ownedProperties4, elements14, primitiveTypes16},
    generalizations={gen_smalluml_Class_Type, gen_smalluml_Operation_NamedElement, gen_smalluml_Property_NamedElement, gen_smalluml_Type_NamedElement, gen_smalluml_TypeString_Type, gen_smalluml_TypeBoolean_Type, gen_smalluml_TypeReal_Type, gen_smalluml_TypeInteger_Type, gen_smalluml_TypeUnlimitedNatural_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)