





import java.util.List;
import java.util.ArrayList;

public class smm_Measurement extends SmmElement {

    private String error;





    private smm_Measure smm_measure;




    private smm_Observation smm_observation;




    private smm_MeasurementRelationship smm_measurementrelationship;




    private List<smm_MeasurementRelationship> smm_measurementrelationships;




    private List<smm_MeasurementRelationship> smm_measurementrelationships;




    private smm_MeasurementRelationship smm_measurementrelationship;




    private smm_Measure smm_measure;


    public smm_Measurement(
        String error    ) {
        super(
        );
        this.error = error;
        this.smm_measurementrelationships = new ArrayList<>();
        this.smm_measurementrelationships = new ArrayList<>();
    }

    public smm_Measurement(
        String error        ArrayList<smm_MeasurementRelationship> smm_measurementrelationships,        ArrayList<smm_MeasurementRelationship> smm_measurementrelationships    ) {
        this.error = error;
        this.smm_measurementrelationships = smm_measurementrelationships;
        this.smm_measurementrelationships = smm_measurementrelationships;
    }

    public String getError() {
        return error;
    }

    public void setError(String error) {
        this.error = error;
    }

    public smm_Measure getSmm_measure() {
        return smm_measure;
    }

    public void setSmm_measure(smm_Measure smm_measure) {
        this.smm_measure = smm_measure;
    }
    public smm_Observation getSmm_observation() {
        return smm_observation;
    }

    public void setSmm_observation(smm_Observation smm_observation) {
        this.smm_observation = smm_observation;
    }
    public smm_MeasurementRelationship getSmm_measurementrelationship() {
        return smm_measurementrelationship;
    }

    public void setSmm_measurementrelationship(smm_MeasurementRelationship smm_measurementrelationship) {
        this.smm_measurementrelationship = smm_measurementrelationship;
    }
    public List<smm_MeasurementRelationship> getSmm_measurementrelationships() {
        return smm_measurementrelationships;
    }

    public void addSmm_measurementrelationship(Smm_measurementrelationship smm_measurementrelationship) {
        this.smm_measurementrelationships.add(smm_measurementrelationship);
    }
    public List<smm_MeasurementRelationship> getSmm_measurementrelationships() {
        return smm_measurementrelationships;
    }

    public void addSmm_measurementrelationship(Smm_measurementrelationship smm_measurementrelationship) {
        this.smm_measurementrelationships.add(smm_measurementrelationship);
    }
    public smm_MeasurementRelationship getSmm_measurementrelationship() {
        return smm_measurementrelationship;
    }

    public void setSmm_measurementrelationship(smm_MeasurementRelationship smm_measurementrelationship) {
        this.smm_measurementrelationship = smm_measurementrelationship;
    }
    public smm_Measure getSmm_measure() {
        return smm_measure;
    }

    public void setSmm_measure(smm_Measure smm_measure) {
        this.smm_measure = smm_measure;
    }

}