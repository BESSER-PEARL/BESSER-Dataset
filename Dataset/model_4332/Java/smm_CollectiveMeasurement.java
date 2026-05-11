





import java.util.List;
import java.util.ArrayList;

public class smm_CollectiveMeasurement extends DimensionalMeasurement {

    private boolean isBaseSupplied;
    private String accumulator;





    private List<smm_DimensionalMeasurement> smm_dimensionalmeasurements;


    public smm_CollectiveMeasurement(
        boolean isBaseSupplied,        String accumulator    ) {
        super(
        );
        this.isBaseSupplied = isBaseSupplied;
        this.accumulator = accumulator;
        this.smm_dimensionalmeasurements = new ArrayList<>();
    }

    public smm_CollectiveMeasurement(
        boolean isBaseSupplied,        String accumulator        ArrayList<smm_DimensionalMeasurement> smm_dimensionalmeasurements    ) {
        this.isBaseSupplied = isBaseSupplied;
        this.accumulator = accumulator;
        this.smm_dimensionalmeasurements = smm_dimensionalmeasurements;
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

    public List<smm_DimensionalMeasurement> getSmm_dimensionalmeasurements() {
        return smm_dimensionalmeasurements;
    }

    public void addSmm_dimensionalmeasurement(Smm_dimensionalmeasurement smm_dimensionalmeasurement) {
        this.smm_dimensionalmeasurements.add(smm_dimensionalmeasurement);
    }

}