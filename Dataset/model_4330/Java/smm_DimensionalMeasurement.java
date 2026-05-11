





import java.util.List;
import java.util.ArrayList;

public class smm_DimensionalMeasurement extends Measurement {

    private float value;





    private smm_AggregatedMeasurement smm_aggregatedmeasurement;


    public smm_DimensionalMeasurement(
        float value    ) {
        super(
        );
        this.value = value;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }

    public smm_AggregatedMeasurement getSmm_aggregatedmeasurement() {
        return smm_aggregatedmeasurement;
    }

    public void setSmm_aggregatedmeasurement(smm_AggregatedMeasurement smm_aggregatedmeasurement) {
        this.smm_aggregatedmeasurement = smm_aggregatedmeasurement;
    }

}