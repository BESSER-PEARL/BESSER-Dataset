





import java.util.List;
import java.util.ArrayList;

public class smm_AggregatedMeasurement extends DimensionalMeasurement {

    private boolean isBaseSuppled;





    private List<smm_DimensionalMeasurement> smm_dimensionalmeasurements;


    public smm_AggregatedMeasurement(
        boolean isBaseSuppled    ) {
        super(
        );
        this.isBaseSuppled = isBaseSuppled;
        this.smm_dimensionalmeasurements = new ArrayList<>();
    }

    public smm_AggregatedMeasurement(
        boolean isBaseSuppled        ArrayList<smm_DimensionalMeasurement> smm_dimensionalmeasurements    ) {
        this.isBaseSuppled = isBaseSuppled;
        this.smm_dimensionalmeasurements = smm_dimensionalmeasurements;
    }

    public boolean getIsbasesuppled() {
        return isBaseSuppled;
    }

    public void setIsbasesuppled(boolean isBaseSuppled) {
        this.isBaseSuppled = isBaseSuppled;
    }

    public List<smm_DimensionalMeasurement> getSmm_dimensionalmeasurements() {
        return smm_dimensionalmeasurements;
    }

    public void addSmm_dimensionalmeasurement(Smm_dimensionalmeasurement smm_dimensionalmeasurement) {
        this.smm_dimensionalmeasurements.add(smm_dimensionalmeasurement);
    }

}