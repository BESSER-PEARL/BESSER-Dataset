





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_NumericalDataType extends PredefinedDataType {

    private int precision;



    public sqlmodel_datatypes_NumericalDataType(
        int precision    ) {
        super(
        );
        this.precision = precision;
    }


    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }


}