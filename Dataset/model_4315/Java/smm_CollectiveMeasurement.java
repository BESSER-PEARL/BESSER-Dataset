





import java.util.List;
import java.util.ArrayList;

public class smm_CollectiveMeasurement extends DimensionalMeasurement {

    private String isBaseSupplied;
    private String accumulator;





    private List<smm_BaseMeasurementRelationship> smm_basemeasurementrelationships;




    private smm_BaseMeasurementRelationship smm_basemeasurementrelationship;


    public smm_CollectiveMeasurement(
        String isBaseSupplied,        String accumulator    ) {
        super(
        );
        this.isBaseSupplied = isBaseSupplied;
        this.accumulator = accumulator;
        this.smm_basemeasurementrelationships = new ArrayList<>();
    }

    public smm_CollectiveMeasurement(
        String isBaseSupplied,        String accumulator        ArrayList<smm_BaseMeasurementRelationship> smm_basemeasurementrelationships    ) {
        this.isBaseSupplied = isBaseSupplied;
        this.accumulator = accumulator;
        this.smm_basemeasurementrelationships = smm_basemeasurementrelationships;
    }

    public String getIsbasesupplied() {
        return isBaseSupplied;
    }

    public void setIsbasesupplied(String isBaseSupplied) {
        this.isBaseSupplied = isBaseSupplied;
    }
    public String getAccumulator() {
        return accumulator;
    }

    public void setAccumulator(String accumulator) {
        this.accumulator = accumulator;
    }

    public List<smm_BaseMeasurementRelationship> getSmm_basemeasurementrelationships() {
        return smm_basemeasurementrelationships;
    }

    public void addSmm_basemeasurementrelationship(Smm_basemeasurementrelationship smm_basemeasurementrelationship) {
        this.smm_basemeasurementrelationships.add(smm_basemeasurementrelationship);
    }
    public smm_BaseMeasurementRelationship getSmm_basemeasurementrelationship() {
        return smm_basemeasurementrelationship;
    }

    public void setSmm_basemeasurementrelationship(smm_BaseMeasurementRelationship smm_basemeasurementrelationship) {
        this.smm_basemeasurementrelationship = smm_basemeasurementrelationship;
    }

}