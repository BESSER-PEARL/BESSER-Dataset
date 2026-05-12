





import java.util.List;
import java.util.ArrayList;

public class connection_SAPFunctionParameterColumn extends AbstractMetadataObject {

    private String StructureOrTableName;
    private String DataType;
    private String Value;
    private String ParameterType;
    private String Length;



    public connection_SAPFunctionParameterColumn(
        String StructureOrTableName,        String DataType,        String Value,        String ParameterType,        String Length    ) {
        super(
        );
        this.StructureOrTableName = StructureOrTableName;
        this.DataType = DataType;
        this.Value = Value;
        this.ParameterType = ParameterType;
        this.Length = Length;
    }


    public String getStructureortablename() {
        return StructureOrTableName;
    }

    public void setStructureortablename(String StructureOrTableName) {
        this.StructureOrTableName = StructureOrTableName;
    }
    public String getDatatype() {
        return DataType;
    }

    public void setDatatype(String DataType) {
        this.DataType = DataType;
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
    public String getLength() {
        return Length;
    }

    public void setLength(String Length) {
        this.Length = Length;
    }


}