





import java.util.List;
import java.util.ArrayList;

public class smm_BinaryMeasurement extends DimensionalMeasurement {

    private boolean isBaseSupplied;



    public smm_BinaryMeasurement(
        boolean isBaseSupplied    ) {
        super(
        );
        this.isBaseSupplied = isBaseSupplied;
    }


    public boolean getIsbasesupplied() {
        return isBaseSupplied;
    }

    public void setIsbasesupplied(boolean isBaseSupplied) {
        this.isBaseSupplied = isBaseSupplied;
    }


}