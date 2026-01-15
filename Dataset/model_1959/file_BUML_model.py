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
FileEncoding: Enumeration = Enumeration(
    name="FileEncoding",
    literals={
            EnumerationLiteral(name="US_ASCII"),
			EnumerationLiteral(name="ISO_8859_1"),
			EnumerationLiteral(name="UTF_8"),
			EnumerationLiteral(name="UTF_16"),
			EnumerationLiteral(name="UTF_16BE"),
			EnumerationLiteral(name="UTF_16LE")
    }
)

# Classes
file_File = Class(name="file::File", is_abstract=True)
file_FileLocal = Class(name="file::FileLocal")
ByteFile = Class(name="ByteFile")
file_FileRemote = Class(name="file::FileRemote")
file_FileInMemory = Class(name="file::FileInMemory")
File = Class(name="File")
file_FileReaderWriter = Class(name="file::FileReaderWriter", is_abstract=True)
FileHandler = Class(name="FileHandler")
file_FileHandler = Class(name="file::FileHandler", is_abstract=True)
FileOwner = Class(name="FileOwner")
file_Files = Class(name="file::Files")
file_ByteFile = Class(name="file::ByteFile", is_abstract=True)
file_FileOutput = Class(name="file::FileOutput", is_abstract=True)
file_FileOwner = Class(name="file::FileOwner", is_abstract=True)

# file_File class attributes and methods
file_File_Name: Property = Property(name="Name", type=StringType)
file_File.attributes={file_File_Name}

# file_FileLocal class attributes and methods
file_FileLocal_FilePath: Property = Property(name="FilePath", type=StringType)
file_FileLocal.attributes={file_FileLocal_FilePath}

# ByteFile class attributes and methods

# file_FileRemote class attributes and methods
file_FileRemote_URL: Property = Property(name="URL", type=StringType)
file_FileRemote.attributes={file_FileRemote_URL}

# file_FileInMemory class attributes and methods
file_FileInMemory_Content: Property = Property(name="Content", type=StringType)
file_FileInMemory.attributes={file_FileInMemory_Content}

# File class attributes and methods

# file_FileReaderWriter class attributes and methods
file_FileReaderWriter_ReadFeedback: Property = Property(name="ReadFeedback", type=StringType)
file_FileReaderWriter_WriteFeedback: Property = Property(name="WriteFeedback", type=StringType)
file_FileReaderWriter_CloseFeedback: Property = Property(name="CloseFeedback", type=StringType)
file_FileReaderWriter_Open: Property = Property(name="Open", type=BooleanType)
file_FileReaderWriter_m_getReadFeedback: Method = Method(name="getReadFeedback", parameters={Parameter(name='file')}, type=StringType)
file_FileReaderWriter_m_getWriteFeedback: Method = Method(name="getWriteFeedback", parameters={Parameter(name='file')}, type=StringType)
file_FileReaderWriter_m_readFile: Method = Method(name="readFile", parameters={})
file_FileReaderWriter_m_writeFile: Method = Method(name="writeFile", parameters={})
file_FileReaderWriter_m_close: Method = Method(name="close", parameters={})
file_FileReaderWriter_m_readFile: Method = Method(name="readFile", parameters={Parameter(name='file')})
file_FileReaderWriter_m_writeFile: Method = Method(name="writeFile", parameters={Parameter(name='file')})
file_FileReaderWriter.attributes={file_FileReaderWriter_Open, file_FileReaderWriter_ReadFeedback, file_FileReaderWriter_CloseFeedback, file_FileReaderWriter_WriteFeedback}
file_FileReaderWriter.methods={file_FileReaderWriter_m_getReadFeedback, file_FileReaderWriter_m_readFile, file_FileReaderWriter_m_writeFile, file_FileReaderWriter_m_writeFile, file_FileReaderWriter_m_readFile, file_FileReaderWriter_m_close, file_FileReaderWriter_m_getWriteFeedback}

# FileHandler class attributes and methods

# file_FileHandler class attributes and methods

# FileOwner class attributes and methods

# file_Files class attributes and methods
file_Files_Name: Property = Property(name="Name", type=StringType)
file_Files.attributes={file_Files_Name}

# file_ByteFile class attributes and methods
file_ByteFile_Encoding: Property = Property(name="Encoding", type=StringType)
file_ByteFile.attributes={file_ByteFile_Encoding}

# file_FileOutput class attributes and methods

# file_FileOwner class attributes and methods

# Relationships
SelectedFile0: BinaryAssociation = BinaryAssociation(
    name="SelectedFile0",
    ends={
        Property(name="file_File", type=file_FileHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="file_FileHandler", type=file_File, multiplicity=Multiplicity(0, 1))
    }
)
HandledFile1: BinaryAssociation = BinaryAssociation(
    name="HandledFile1",
    ends={
        Property(name="file_File3", type=file_FileHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="file_FileHandler2", type=file_File, multiplicity=Multiplicity(0, 1))
    }
)
OutputFile6: BinaryAssociation = BinaryAssociation(
    name="OutputFile6",
    ends={
        Property(name="file_File7", type=file_FileOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="file_FileOutput", type=file_File, multiplicity=Multiplicity(0, 1))
    }
)
Files4: BinaryAssociation = BinaryAssociation(
    name="Files4",
    ends={
        Property(name="file_File5", type=file_FileOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="file_FileOwner", type=file_File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_file_FileLocal_ByteFile = Generalization(general=ByteFile, specific=file_FileLocal)
gen_file_FileRemote_ByteFile = Generalization(general=ByteFile, specific=file_FileRemote)
gen_file_FileInMemory_File = Generalization(general=File, specific=file_FileInMemory)
gen_file_FileReaderWriter_FileHandler = Generalization(general=FileHandler, specific=file_FileReaderWriter)
gen_file_FileHandler_FileOwner = Generalization(general=FileOwner, specific=file_FileHandler)
gen_file_Files_FileOwner = Generalization(general=FileOwner, specific=file_Files)
gen_file_ByteFile_File = Generalization(general=File, specific=file_ByteFile)
gen_file_FileOutput_FileOwner = Generalization(general=FileOwner, specific=file_FileOutput)

# Domain Model
domain_model = DomainModel(
    name="file",
    types={file_File, file_FileLocal, ByteFile, file_FileRemote, file_FileInMemory, File, file_FileReaderWriter, FileHandler, file_FileHandler, FileOwner, file_Files, file_ByteFile, file_FileOutput, file_FileOwner, FileEncoding},
    associations={SelectedFile0, HandledFile1, OutputFile6, Files4},
    generalizations={gen_file_FileLocal_ByteFile, gen_file_FileRemote_ByteFile, gen_file_FileInMemory_File, gen_file_FileReaderWriter_FileHandler, gen_file_FileHandler_FileOwner, gen_file_Files_FileOwner, gen_file_ByteFile_File, gen_file_FileOutput_FileOwner},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)