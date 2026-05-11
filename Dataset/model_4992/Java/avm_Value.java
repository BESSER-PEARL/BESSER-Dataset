





import java.util.List;
import java.util.ArrayList;

public class avm_Value extends ValueNode {

    private String DimensionType;
    private String DataType;
    private String Unit;
    private String Dimensions;



    public avm_Value(
        String DimensionType,        String DataType,        String Unit,        String Dimensions    ) {
        super(
        );
        this.DimensionType = DimensionType;
        this.DataType = DataType;
        this.Unit = Unit;
        this.Dimensions = Dimensions;
    }


    public String getDimensiontype() {
        return DimensionType;
    }

    public void setDimensiontype(String DimensionType) {
        this.DimensionType = DimensionType;
    }
    public String getDatatype() {
        return DataType;
    }

    public void setDatatype(String DataType) {
        this.DataType = DataType;
    }
    public String getUnit() {
        return Unit;
    }

    public void setUnit(String Unit) {
        this.Unit = Unit;
    }
    public String getDimensions() {
        return Dimensions;
    }

    public void setDimensions(String Dimensions) {
        this.Dimensions = Dimensions;
    }


}