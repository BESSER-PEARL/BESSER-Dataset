





import java.util.List;
import java.util.ArrayList;

public class connection_SAPFunctionParameterColumn extends AbstractMetadataObject {

    private String StructureOrTableName;
    private String Length;
    private String Value;
    private String ParameterType;
    private String DataType;





    private connection_SAPFunctionParameterTable connection_sapfunctionparametertable;




    private connection_SAPFunctionParameterTable connection_sapfunctionparametertable;


    public connection_SAPFunctionParameterColumn(
        String StructureOrTableName,        String Length,        String Value,        String ParameterType,        String DataType    ) {
        super(
        );
        this.StructureOrTableName = StructureOrTableName;
        this.Length = Length;
        this.Value = Value;
        this.ParameterType = ParameterType;
        this.DataType = DataType;
    }


    public String getStructureortablename() {
        return StructureOrTableName;
    }

    public void setStructureortablename(String StructureOrTableName) {
        this.StructureOrTableName = StructureOrTableName;
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
    public String getParametertype() {
        return ParameterType;
    }

    public void setParametertype(String ParameterType) {
        this.ParameterType = ParameterType;
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