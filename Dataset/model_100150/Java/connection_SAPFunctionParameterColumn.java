





import java.util.List;
import java.util.ArrayList;

public class connection_SAPFunctionParameterColumn extends AbstractMetadataObject {

    private String Name;
    private String DataType;
    private String Description;
    private String ParameterType;
    private String Length;
    private String Value;
    private String StructureOrTableName;





    private connection_SAPFunctionParameterTable connection_sapfunctionparametertable;




    private connection_SAPFunctionParameterTable connection_sapfunctionparametertable;


    public connection_SAPFunctionParameterColumn(
        String Name,        String DataType,        String Description,        String ParameterType,        String Length,        String Value,        String StructureOrTableName    ) {
        super(
        );
        this.Name = Name;
        this.DataType = DataType;
        this.Description = Description;
        this.ParameterType = ParameterType;
        this.Length = Length;
        this.Value = Value;
        this.StructureOrTableName = StructureOrTableName;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDatatype() {
        return DataType;
    }

    public void setDatatype(String DataType) {
        this.DataType = DataType;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
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
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getStructureortablename() {
        return StructureOrTableName;
    }

    public void setStructureortablename(String StructureOrTableName) {
        this.StructureOrTableName = StructureOrTableName;
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