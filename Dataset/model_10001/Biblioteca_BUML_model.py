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
Genero: Enumeration = Enumeration(
    name="Genero",
    literals={
            EnumerationLiteral(name="Lirico"),
			EnumerationLiteral(name="Epico"),
			EnumerationLiteral(name="Narrativo"),
			EnumerationLiteral(name="Dramatico"),
			EnumerationLiteral(name="Didactico"),
			EnumerationLiteral(name="Terror")
    }
)

Estado: Enumeration = Enumeration(
    name="Estado",
    literals={
            EnumerationLiteral(name="Bueno"),
			EnumerationLiteral(name="Malo")
    }
)

# Classes
Biblioteca_Biblioteca = Class(name="Biblioteca_Biblioteca")
Biblioteca_Libro = Class(name="Biblioteca_Libro")
Biblioteca_Autor = Class(name="Biblioteca_Autor")
Biblioteca_Socio = Class(name="Biblioteca_Socio")
Biblioteca_Prestamo = Class(name="Biblioteca_Prestamo")
Biblioteca_Ejemplar = Class(name="Biblioteca_Ejemplar")
Biblioteca_Multa = Class(name="Biblioteca_Multa")

# Biblioteca_Biblioteca class attributes and methods
Biblioteca_Biblioteca_direccion: Property = Property(name="direccion", type=StringType)
Biblioteca_Biblioteca.attributes={Biblioteca_Biblioteca_direccion}

# Biblioteca_Libro class attributes and methods
Biblioteca_Libro_ISBN: Property = Property(name="ISBN", type=StringType)
Biblioteca_Libro_titulo: Property = Property(name="titulo", type=StringType)
Biblioteca_Libro_editorial: Property = Property(name="editorial", type=StringType)
Biblioteca_Libro_anioDeEdicion: Property = Property(name="anioDeEdicion", type=IntegerType)
Biblioteca_Libro_genero: Property = Property(name="genero", type=StringType)
Biblioteca_Libro_activo: Property = Property(name="activo", type=BooleanType)
Biblioteca_Libro.attributes={Biblioteca_Libro_genero, Biblioteca_Libro_ISBN, Biblioteca_Libro_editorial, Biblioteca_Libro_anioDeEdicion, Biblioteca_Libro_titulo, Biblioteca_Libro_activo}

# Biblioteca_Autor class attributes and methods
Biblioteca_Autor_nombreCompleto: Property = Property(name="nombreCompleto", type=StringType)
Biblioteca_Autor_nacionalidad: Property = Property(name="nacionalidad", type=StringType)
Biblioteca_Autor_fechaDeNacimiento: Property = Property(name="fechaDeNacimiento", type=DateType)
Biblioteca_Autor.attributes={Biblioteca_Autor_nacionalidad, Biblioteca_Autor_nombreCompleto, Biblioteca_Autor_fechaDeNacimiento}

# Biblioteca_Socio class attributes and methods
Biblioteca_Socio_numeroDeSocio: Property = Property(name="numeroDeSocio", type=IntegerType)
Biblioteca_Socio_nombreCompleto: Property = Property(name="nombreCompleto", type=StringType)
Biblioteca_Socio_telefono: Property = Property(name="telefono", type=StringType)
Biblioteca_Socio_direccion: Property = Property(name="direccion", type=StringType)
Biblioteca_Socio_edad: Property = Property(name="edad", type=IntegerType)
Biblioteca_Socio_fechaDeNacimiento: Property = Property(name="fechaDeNacimiento", type=DateType)
Biblioteca_Socio_m_existeSocio: Method = Method(name="existeSocio", parameters={Parameter(name='Biblioteca_nombreDeSocio', type=StringType)}, type=StringType)
Biblioteca_Socio_m_solicitarEjemplar: Method = Method(name="solicitarEjemplar", parameters={Parameter(name='Biblioteca_codigo', type=StringType)}, type=StringType)
Biblioteca_Socio_m_devolverEjemplar: Method = Method(name="devolverEjemplar", parameters={Parameter(name='Biblioteca_fechaActual', type=StringType), Parameter(name='Biblioteca_codigo', type=StringType)}, type=StringType)
Biblioteca_Socio_m_generarMulta: Method = Method(name="generarMulta", parameters={Parameter(name='Biblioteca_prestamo', type=StringType)}, type=StringType)
Biblioteca_Socio_m_uniqueID: Method = Method(name="uniqueID", parameters={})
Biblioteca_Socio.attributes={Biblioteca_Socio_telefono, Biblioteca_Socio_nombreCompleto, Biblioteca_Socio_fechaDeNacimiento, Biblioteca_Socio_numeroDeSocio, Biblioteca_Socio_edad, Biblioteca_Socio_direccion}
Biblioteca_Socio.methods={Biblioteca_Socio_m_uniqueID, Biblioteca_Socio_m_devolverEjemplar, Biblioteca_Socio_m_generarMulta, Biblioteca_Socio_m_existeSocio, Biblioteca_Socio_m_solicitarEjemplar}

# Biblioteca_Prestamo class attributes and methods
Biblioteca_Prestamo_fechaDeInicio: Property = Property(name="fechaDeInicio", type=DateType)
Biblioteca_Prestamo_fechaDeFin: Property = Property(name="fechaDeFin", type=DateType)
Biblioteca_Prestamo_fechaDeDevolucion: Property = Property(name="fechaDeDevolucion", type=DateType)
Biblioteca_Prestamo.attributes={Biblioteca_Prestamo_fechaDeInicio, Biblioteca_Prestamo_fechaDeFin, Biblioteca_Prestamo_fechaDeDevolucion}

# Biblioteca_Ejemplar class attributes and methods
Biblioteca_Ejemplar_numeroDeEjemplar: Property = Property(name="numeroDeEjemplar", type=IntegerType)
Biblioteca_Ejemplar_estado: Property = Property(name="estado", type=StringType)
Biblioteca_Ejemplar.attributes={Biblioteca_Ejemplar_numeroDeEjemplar, Biblioteca_Ejemplar_estado}

# Biblioteca_Multa class attributes and methods
Biblioteca_Multa_fecha: Property = Property(name="fecha", type=DateType)
Biblioteca_Multa_monto: Property = Property(name="monto", type=IntegerType)
Biblioteca_Multa_diasExcedidos: Property = Property(name="diasExcedidos", type=IntegerType)
Biblioteca_Multa_fechaDePago: Property = Property(name="fechaDePago", type=DateType)
Biblioteca_Multa.attributes={Biblioteca_Multa_monto, Biblioteca_Multa_diasExcedidos, Biblioteca_Multa_fecha, Biblioteca_Multa_fechaDePago}

# Relationships
libros0: BinaryAssociation = BinaryAssociation(
    name="libros0",
    ends={
        Property(name="Biblioteca_Libro", type=Biblioteca_Biblioteca, multiplicity=Multiplicity(1, 1)),
        Property(name="Biblioteca_Biblioteca", type=Biblioteca_Libro, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
autores1: BinaryAssociation = BinaryAssociation(
    name="autores1",
    ends={
        Property(name="Biblioteca_Autor", type=Biblioteca_Biblioteca, multiplicity=Multiplicity(1, 1)),
        Property(name="Biblioteca_Biblioteca2", type=Biblioteca_Autor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
socios3: BinaryAssociation = BinaryAssociation(
    name="socios3",
    ends={
        Property(name="Biblioteca_Socio", type=Biblioteca_Biblioteca, multiplicity=Multiplicity(1, 1)),
        Property(name="Biblioteca_Biblioteca4", type=Biblioteca_Socio, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
autor5: BinaryAssociation = BinaryAssociation(
    name="autor5",
    ends={
        Property(name="Biblioteca_Autor7", type=Biblioteca_Libro, multiplicity=Multiplicity(1, 1)),
        Property(name="Biblioteca_Libro6", type=Biblioteca_Autor, multiplicity=Multiplicity(1, 1))
    }
)
ejemplar8: BinaryAssociation = BinaryAssociation(
    name="ejemplar8",
    ends={
        Property(name="Biblioteca_Ejemplar", type=Biblioteca_Prestamo, multiplicity=Multiplicity(1, 1)),
        Property(name="Biblioteca_Prestamo", type=Biblioteca_Ejemplar, multiplicity=Multiplicity(1, 1))
    }
)
socio9: BinaryAssociation = BinaryAssociation(
    name="socio9",
    ends={
        Property(name="Biblioteca_Socio11", type=Biblioteca_Prestamo, multiplicity=Multiplicity(1, 1)),
        Property(name="Biblioteca_Prestamo10", type=Biblioteca_Socio, multiplicity=Multiplicity(1, 1))
    }
)
obras12: BinaryAssociation = BinaryAssociation(
    name="obras12",
    ends={
        Property(name="Biblioteca_Libro14", type=Biblioteca_Autor, multiplicity=Multiplicity(1, 1)),
        Property(name="Biblioteca_Autor13", type=Biblioteca_Libro, multiplicity=Multiplicity(1, 9999))
    }
)
multas15: BinaryAssociation = BinaryAssociation(
    name="multas15",
    ends={
        Property(name="Biblioteca_Multa", type=Biblioteca_Socio, multiplicity=Multiplicity(1, 1)),
        Property(name="Biblioteca_Socio16", type=Biblioteca_Multa, multiplicity=Multiplicity(0, 9999))
    }
)
prestamos17: BinaryAssociation = BinaryAssociation(
    name="prestamos17",
    ends={
        Property(name="Biblioteca_Prestamo19", type=Biblioteca_Socio, multiplicity=Multiplicity(1, 1)),
        Property(name="Biblioteca_Socio18", type=Biblioteca_Prestamo, multiplicity=Multiplicity(0, 3))
    }
)
prestamo20: BinaryAssociation = BinaryAssociation(
    name="prestamo20",
    ends={
        Property(name="Biblioteca_Prestamo22", type=Biblioteca_Multa, multiplicity=Multiplicity(1, 1)),
        Property(name="Biblioteca_Multa21", type=Biblioteca_Prestamo, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Biblioteca",
    types={Biblioteca_Biblioteca, Biblioteca_Libro, Biblioteca_Autor, Biblioteca_Socio, Biblioteca_Prestamo, Biblioteca_Ejemplar, Biblioteca_Multa, Genero, Estado},
    associations={libros0, autores1, socios3, autor5, ejemplar8, socio9, obras12, multas15, prestamos17, prestamo20},
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