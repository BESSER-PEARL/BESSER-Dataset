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
Transition = Class(name="Transition")
Module = Class(name="Module")
ea_automata_State = Class(name="ea_automata_State")
Automaton = Class(name="Automaton")
ea_automata_Transition = Class(name="ea_automata_Transition")
ea_automata_Module = Class(name="ea_automata_Module")
ea_extensions_IExtendible = Class(name="ea_extensions_IExtendible", is_abstract=True)
ea_automata_Automaton = Class(name="ea_automata_Automaton")
ExtendibleElement = Class(name="ExtendibleElement")
State = Class(name="State")
ea_extensions_ExtensionElement = Class(name="ea_extensions_ExtensionElement", is_abstract=True)
ea_extensions_IntegerExtension = Class(name="ea_extensions_IntegerExtension")
ExtensionElement = Class(name="ExtensionElement")
ea_extensions_StringExtension = Class(name="ea_extensions_StringExtension")
ea_extensions_StringListExtension = Class(name="ea_extensions_StringListExtension")
ea_extensions_BooleanExtension = Class(name="ea_extensions_BooleanExtension")
IExtension = Class(name="IExtension")
ea_extensions_IExtension = Class(name="ea_extensions_IExtension", is_abstract=True)
IExtendible = Class(name="IExtendible")
ea_extensions_ExtendibleElement = Class(name="ea_extensions_ExtendibleElement", is_abstract=True)

# Transition class attributes and methods

# Module class attributes and methods

# ea_automata_State class attributes and methods
ea_automata_State_id: Property = Property(name="id", type=StringType)
ea_automata_State_name: Property = Property(name="name", type=StringType)
ea_automata_State.attributes={ea_automata_State_name, ea_automata_State_id}

# Automaton class attributes and methods

# ea_automata_Transition class attributes and methods
ea_automata_Transition_id: Property = Property(name="id", type=StringType)
ea_automata_Transition.attributes={ea_automata_Transition_id}

# ea_automata_Module class attributes and methods

# ea_extensions_IExtendible class attributes and methods
ea_extensions_IExtendible_m_findExtension: Method = Method(name="findExtension", parameters={Parameter(name='ea_id', type=StringType)}, type=StringType)
ea_extensions_IExtendible_m_updateExtension: Method = Method(name="updateExtension", parameters={Parameter(name='ea_extension', type=StringType)})
ea_extensions_IExtendible.methods={ea_extensions_IExtendible_m_findExtension, ea_extensions_IExtendible_m_updateExtension}

# ea_automata_Automaton class attributes and methods
ea_automata_Automaton_name: Property = Property(name="name", type=StringType)
ea_automata_Automaton_usedExtensionIds: Property = Property(name="usedExtensionIds", type=StringType)
ea_automata_Automaton_id: Property = Property(name="id", type=StringType)
ea_automata_Automaton.attributes={ea_automata_Automaton_id, ea_automata_Automaton_name, ea_automata_Automaton_usedExtensionIds}

# ExtendibleElement class attributes and methods

# State class attributes and methods

# ea_extensions_ExtensionElement class attributes and methods

# ea_extensions_IntegerExtension class attributes and methods
ea_extensions_IntegerExtension_value: Property = Property(name="value", type=IntegerType)
ea_extensions_IntegerExtension.attributes={ea_extensions_IntegerExtension_value}

# ExtensionElement class attributes and methods

# ea_extensions_StringExtension class attributes and methods
ea_extensions_StringExtension_value: Property = Property(name="value", type=StringType)
ea_extensions_StringExtension.attributes={ea_extensions_StringExtension_value}

# ea_extensions_StringListExtension class attributes and methods
ea_extensions_StringListExtension_values: Property = Property(name="values", type=StringType)
ea_extensions_StringListExtension.attributes={ea_extensions_StringListExtension_values}

# ea_extensions_BooleanExtension class attributes and methods
ea_extensions_BooleanExtension_value: Property = Property(name="value", type=BooleanType)
ea_extensions_BooleanExtension.attributes={ea_extensions_BooleanExtension_value}

# IExtension class attributes and methods

# ea_extensions_IExtension class attributes and methods
ea_extensions_IExtension_id: Property = Property(name="id", type=StringType)
ea_extensions_IExtension.attributes={ea_extensions_IExtension_id}

# IExtendible class attributes and methods

# ea_extensions_ExtendibleElement class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="automaton", type=State, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="State", type=ea_automata_Automaton, multiplicity=Multiplicity(1, 1))
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=ea_automata_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton2", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module3: BinaryAssociation = BinaryAssociation(
    name="module3",
    ends={
        Property(name="Module", type=ea_automata_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automata", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
automaton4: BinaryAssociation = BinaryAssociation(
    name="automaton4",
    ends={
        Property(name="Automaton", type=ea_automata_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=Automaton, multiplicity=Multiplicity(0, 1))
    }
)
incoming5: BinaryAssociation = BinaryAssociation(
    name="incoming5",
    ends={
        Property(name="Transition6", type=ea_automata_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing7: BinaryAssociation = BinaryAssociation(
    name="outgoing7",
    ends={
        Property(name="Transition8", type=ea_automata_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
automaton9: BinaryAssociation = BinaryAssociation(
    name="automaton9",
    ends={
        Property(name="Automaton10", type=ea_automata_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=Automaton, multiplicity=Multiplicity(0, 1))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="State12", type=ea_automata_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=State, multiplicity=Multiplicity(0, 1))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="State14", type=ea_automata_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=State, multiplicity=Multiplicity(0, 1))
    }
)
automata15: BinaryAssociation = BinaryAssociation(
    name="automata15",
    ends={
        Property(name="Automaton16", type=ea_automata_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module", type=Automaton, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensions17: BinaryAssociation = BinaryAssociation(
    name="extensions17",
    ends={
        Property(name="IExtension", type=ea_extensions_IExtendible, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=IExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner18: BinaryAssociation = BinaryAssociation(
    name="owner18",
    ends={
        Property(name="IExtendible", type=ea_extensions_IExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="extensions", type=IExtendible, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ea_automata_State_ExtendibleElement = Generalization(general=ExtendibleElement, specific=ea_automata_State)
gen_ea_automata_Transition_ExtendibleElement = Generalization(general=ExtendibleElement, specific=ea_automata_Transition)
gen_ea_automata_Automaton_ExtendibleElement = Generalization(general=ExtendibleElement, specific=ea_automata_Automaton)
gen_ea_extensions_ExtensionElement_IExtension = Generalization(general=IExtension, specific=ea_extensions_ExtensionElement)
gen_ea_extensions_IntegerExtension_ExtensionElement = Generalization(general=ExtensionElement, specific=ea_extensions_IntegerExtension)
gen_ea_extensions_StringExtension_ExtensionElement = Generalization(general=ExtensionElement, specific=ea_extensions_StringExtension)
gen_ea_extensions_StringListExtension_ExtensionElement = Generalization(general=ExtensionElement, specific=ea_extensions_StringListExtension)
gen_ea_extensions_BooleanExtension_ExtensionElement = Generalization(general=ExtensionElement, specific=ea_extensions_BooleanExtension)
gen_ea_extensions_ExtendibleElement_IExtendible = Generalization(general=IExtendible, specific=ea_extensions_ExtendibleElement)

# Domain Model
domain_model = DomainModel(
    name="ea",
    types={Transition, Module, ea_automata_State, Automaton, ea_automata_Transition, ea_automata_Module, ea_extensions_IExtendible, ea_automata_Automaton, ExtendibleElement, State, ea_extensions_ExtensionElement, ea_extensions_IntegerExtension, ExtensionElement, ea_extensions_StringExtension, ea_extensions_StringListExtension, ea_extensions_BooleanExtension, IExtension, ea_extensions_IExtension, IExtendible, ea_extensions_ExtendibleElement},
    associations={states0, transitions1, module3, automaton4, incoming5, outgoing7, automaton9, source11, target13, automata15, extensions17, owner18},
    generalizations={gen_ea_automata_State_ExtendibleElement, gen_ea_automata_Transition_ExtendibleElement, gen_ea_automata_Automaton_ExtendibleElement, gen_ea_extensions_ExtensionElement_IExtension, gen_ea_extensions_IntegerExtension_ExtensionElement, gen_ea_extensions_StringExtension_ExtensionElement, gen_ea_extensions_StringListExtension_ExtensionElement, gen_ea_extensions_BooleanExtension_ExtensionElement, gen_ea_extensions_ExtendibleElement_IExtendible},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)