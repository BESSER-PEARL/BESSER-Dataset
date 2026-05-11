





import java.util.List;
import java.util.ArrayList;

public class smm_CollectiveMeasurement extends DimensionalMeasurement {

    private String accumulator;
    private boolean isBaseSupplied;





    private List<smm_DimensionalMeasurement> smm_dimensionalmeasurements;


    public smm_CollectiveMeasurement(
        String accumulator,        boolean isBaseSupplied    ) {
        super(
        );
        this.accumulator = accumulator;
        this.isBaseSupplied = isBaseSupplied;
        this.smm_dimensionalmeasurements = new ArrayList<>();
    }

    public smm_CollectiveMeasurement(
        String accumulator,        boolean isBaseSupplied        ArrayList<smm_DimensionalMeasurement> smm_dimensionalmeasurements    ) {
        this.accumulator = accumulator;
        this.isBaseSupplied = isBaseSupplied;
        this.smm_dimensionalmeasurements = smm_dimensionalmeasurements;
    }

    public String getAccumulator() {
        return accumulator;
    }

    public void setAccumulator(String accumulator) {
        this.accumulator = accumulator;
    }
    public boolean getIsbasesupplied() {
        return isBaseSupplied;
    }

    public void setIsbasesupplied(boolean isBaseSupplied) {
        this.isBaseSupplied = isBaseSupplied;
    }

    public List<smm_DimensionalMeasurement> getSmm_dimensionalmeasurements() {
        return smm_dimensionalmeasurements;
    }

    public void addSmm_dimensionalmeasurement(Smm_dimensionalmeasurement smm_dimensionalmeasurement) {
        this.smm_dimensionalmeasurements.add(smm_dimensionalmeasurement);
    }

}