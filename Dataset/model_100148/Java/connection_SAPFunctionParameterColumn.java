





import java.util.List;
import java.util.ArrayList;

public class connection_SAPFunctionParameterColumn extends AbstractMetadataObject {

    private String Value;
    private String StructureOrTableName;
    private String DataType;
    private String Length;
    private String ParameterType;



    public connection_SAPFunctionParameterColumn(
        String Value,        String StructureOrTableName,        String DataType,        String Length,        String ParameterType    ) {
        super(
        );
        this.Value = Value;
        this.StructureOrTableName = StructureOrTableName;
        this.DataType = DataType;
        this.Length = Length;
        this.ParameterType = ParameterType;
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
    public String getDatatype() {
        return DataType;
    }

    public void setDatatype(String DataType) {
        this.DataType = DataType;
    }
    public String getLength() {
        return Length;
    }

    public void setLength(String Length) {
        this.Length = Length;
    }
    public String getParametertype() {
        return ParameterType;
    }

    public void setParametertype(String ParameterType) {
        this.ParameterType = ParameterType;
    }


}