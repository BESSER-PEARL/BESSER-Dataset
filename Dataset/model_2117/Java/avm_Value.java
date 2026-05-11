





import java.util.List;
import java.util.ArrayList;

public class avm_Value extends ValueNode {

    private String DataType;
    private String Dimensions;
    private String DimensionType;
    private String Unit;



    public avm_Value(
        String DataType,        String Dimensions,        String DimensionType,        String Unit    ) {
        super(
        );
        this.DataType = DataType;
        this.Dimensions = Dimensions;
        this.DimensionType = DimensionType;
        this.Unit = Unit;
    }


    public String getDatatype() {
        return DataType;
    }

    public void setDatatype(String DataType) {
        this.DataType = DataType;
    }
    public String getDimensions() {
        return Dimensions;
    }

    public void setDimensions(String Dimensions) {
        this.Dimensions = Dimensions;
    }
    public String getDimensiontype() {
        return DimensionType;
    }

    public void setDimensiontype(String DimensionType) {
        this.DimensionType = DimensionType;
    }
    public String getUnit() {
        return Unit;
    }

    public void setUnit(String Unit) {
        this.Unit = Unit;
    }


}