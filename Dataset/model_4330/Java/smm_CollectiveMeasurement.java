





import java.util.List;
import java.util.ArrayList;

public class smm_CollectiveMeasurement extends DimensionalMeasurement {

    private boolean isBaseSupplied;
    private String accumulator;



    public smm_CollectiveMeasurement(
        boolean isBaseSupplied,        String accumulator    ) {
        super(
        );
        this.isBaseSupplied = isBaseSupplied;
        this.accumulator = accumulator;
    }


    public boolean getIsbasesupplied() {
        return isBaseSupplied;
    }

    public void setIsbasesupplied(boolean isBaseSupplied) {
        this.isBaseSupplied = isBaseSupplied;
    }
    public String getAccumulator() {
        return accumulator;
    }

    public void setAccumulator(String accumulator) {
        this.accumulator = accumulator;
    }


}