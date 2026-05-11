





import java.util.List;
import java.util.ArrayList;

public class smm_RescaledMeasurement extends DimensionalMeasurement {

    private String isBaseSupplied;





    private smm_RescaleMeasurementRelationship smm_rescalemeasurementrelationship;




    private List<smm_RescaleMeasurementRelationship> smm_rescalemeasurementrelationships;


    public smm_RescaledMeasurement(
        String isBaseSupplied    ) {
        super(
        );
        this.isBaseSupplied = isBaseSupplied;
        this.smm_rescalemeasurementrelationships = new ArrayList<>();
    }

    public smm_RescaledMeasurement(
        String isBaseSupplied        ArrayList<smm_RescaleMeasurementRelationship> smm_rescalemeasurementrelationships    ) {
        this.isBaseSupplied = isBaseSupplied;
        this.smm_rescalemeasurementrelationships = smm_rescalemeasurementrelationships;
    }

    public String getIsbasesupplied() {
        return isBaseSupplied;
    }

    public void setIsbasesupplied(String isBaseSupplied) {
        this.isBaseSupplied = isBaseSupplied;
    }

    public smm_RescaleMeasurementRelationship getSmm_rescalemeasurementrelationship() {
        return smm_rescalemeasurementrelationship;
    }

    public void setSmm_rescalemeasurementrelationship(smm_RescaleMeasurementRelationship smm_rescalemeasurementrelationship) {
        this.smm_rescalemeasurementrelationship = smm_rescalemeasurementrelationship;
    }
    public List<smm_RescaleMeasurementRelationship> getSmm_rescalemeasurementrelationships() {
        return smm_rescalemeasurementrelationships;
    }

    public void addSmm_rescalemeasurementrelationship(Smm_rescalemeasurementrelationship smm_rescalemeasurementrelationship) {
        this.smm_rescalemeasurementrelationships.add(smm_rescalemeasurementrelationship);
    }

}