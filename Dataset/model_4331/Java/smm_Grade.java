





import java.util.List;
import java.util.ArrayList;

public class smm_Grade extends Measurement {

    private boolean isBaseSupplied;
    private String value;





    private smm_DimensionalMeasurement smm_dimensionalmeasurement;


    public smm_Grade(
        boolean isBaseSupplied,        String value    ) {
        super(
        );
        this.isBaseSupplied = isBaseSupplied;
        this.value = value;
    }


    public boolean getIsbasesupplied() {
        return isBaseSupplied;
    }

    public void setIsbasesupplied(boolean isBaseSupplied) {
        this.isBaseSupplied = isBaseSupplied;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public smm_DimensionalMeasurement getSmm_dimensionalmeasurement() {
        return smm_dimensionalmeasurement;
    }

    public void setSmm_dimensionalmeasurement(smm_DimensionalMeasurement smm_dimensionalmeasurement) {
        this.smm_dimensionalmeasurement = smm_dimensionalmeasurement;
    }

}