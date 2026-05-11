





import java.util.List;
import java.util.ArrayList;

public class smm_ObservedMeasure extends SmmRelationship {






    private smm_Observation smm_observation;




    private List<smm_Measurement> smm_measurements;


    public smm_ObservedMeasure(
    ) {
        super(
        );
        this.smm_measurements = new ArrayList<>();
    }

    public smm_ObservedMeasure(
        ArrayList<smm_Measurement> smm_measurements    ) {
        this.smm_measurements = smm_measurements;
    }


    public smm_Observation getSmm_observation() {
        return smm_observation;
    }

    public void setSmm_observation(smm_Observation smm_observation) {
        this.smm_observation = smm_observation;
    }
    public List<smm_Measurement> getSmm_measurements() {
        return smm_measurements;
    }

    public void addSmm_measurement(Smm_measurement smm_measurement) {
        this.smm_measurements.add(smm_measurement);
    }

}