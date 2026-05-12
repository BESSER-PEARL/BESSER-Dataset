





import java.util.List;
import java.util.ArrayList;

public class connection_SAPFunctionParameterColumn extends AbstractMetadataObject {

    private String ParameterType;
    private String Length;
    private String Name;
    private String Description;
    private String StructureOrTableName;
    private String Value;
    private String DataType;





    private connection_SAPFunctionParameterTable connection_sapfunctionparametertable;




    private connection_SAPFunctionParameterTable connection_sapfunctionparametertable;


    public connection_SAPFunctionParameterColumn(
        String ParameterType,        String Length,        String Name,        String Description,        String StructureOrTableName,        String Value,        String DataType    ) {
        super(
        );
        this.ParameterType = ParameterType;
        this.Length = Length;
        this.Name = Name;
        this.Description = Description;
        this.StructureOrTableName = StructureOrTableName;
        this.Value = Value;
        this.DataType = DataType;
    }


    public String getParametertype() {
        return ParameterType;
    }

    public void setParametertype(String ParameterType) {
        this.ParameterType = ParameterType;
    }
    public String getLength() {
        return Length;
    }

    public void setLength(String Length) {
        this.Length = Length;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getStructureortablename() {
        return StructureOrTableName;
    }

    public void setStructureortablename(String StructureOrTableName) {
        this.StructureOrTableName = StructureOrTableName;
    }
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getDatatype() {
        return DataType;
    }

    public void setDatatype(String DataType) {
        this.DataType = DataType;
    }

    public connection_SAPFunctionParameterTable getConnection_sapfunctionparametertable() {
        return connection_sapfunctionparametertable;
    }

    public void setConnection_sapfunctionparametertable(connection_SAPFunctionParameterTable connection_sapfunctionparametertable) {
        this.connection_sapfunctionparametertable = connection_sapfunctionparametertable;
    }
    public connection_SAPFunctionParameterTable getConnection_sapfunctionparametertable() {
        return connection_sapfunctionparametertable;
    }

    public void setConnection_sapfunctionparametertable(connection_SAPFunctionParameterTable connection_sapfunctionparametertable) {
        this.connection_sapfunctionparametertable = connection_sapfunctionparametertable;
    }

}