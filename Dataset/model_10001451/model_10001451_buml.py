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
Figura = Class(name="Figura")
Canvas = Class(name="Canvas")
Cuadrado = Class(name="Cuadrado")
JFrame = Class(name="JFrame")
Ventana = Class(name="Ventana")

# Figura class attributes and methods
Figura_estado: Property = Property(name="estado", type=BooleanType)
Figura_valor: Property = Property(name="valor", type=IntegerType)
Figura.attributes={Figura_valor, Figura_estado}

# Canvas class attributes and methods

# Cuadrado class attributes and methods
Cuadrado_v1: Property = Property(name="v1", type=IntegerType)
Cuadrado_v2: Property = Property(name="v2", type=IntegerType)
Cuadrado_img: Property = Property(name="img", type=StringType)
Cuadrado.attributes={Cuadrado_v1, Cuadrado_img, Cuadrado_v2}

# JFrame class attributes and methods

# Ventana class attributes and methods
Ventana_c1: Property = Property(name="c1", type=Cuadrado)
Ventana_c2: Property = Property(name="c2", type=Cuadrado)
Ventana_c3: Property = Property(name="c3", type=Cuadrado)
Ventana_fig: Property = Property(name="fig", type=Figura)
Ventana_l1: Property = Property(name="l1", type=IntegerType)
Ventana_l2: Property = Property(name="l2", type=IntegerType)
Ventana_etiqueta: Property = Property(name="etiqueta", type=StringType)
Ventana.attributes={Ventana_c2, Ventana_fig, Ventana_c1, Ventana_l2, Ventana_etiqueta, Ventana_c3, Ventana_l1}

# Domain Model
domain_model = DomainModel(
    name="_7BlOgOSdEeiyGtLb2crGgA",
    types={Figura, Canvas, Cuadrado, JFrame, Ventana},
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