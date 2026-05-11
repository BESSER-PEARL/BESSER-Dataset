





import java.util.List;
import java.util.ArrayList;

public class smm_ObservedMeasure extends SmmElement {






    private List<smm_Argument> smm_arguments;




    private List<smm_Measurement> smm_measurements;




    private smm_Argument smm_argument;




    private smm_Observation smm_observation;




    private smm_Measurement smm_measurement;


    public smm_ObservedMeasure(
    ) {
        super(
        );
        this.smm_arguments = new ArrayList<>();
        this.smm_measurements = new ArrayList<>();
    }

    public smm_ObservedMeasure(
        ArrayList<smm_Argument> smm_arguments,        ArrayList<smm_Measurement> smm_measurements    ) {
        this.smm_arguments = smm_arguments;
        this.smm_measurements = smm_measurements;
    }


    public List<smm_Argument> getSmm_arguments() {
        return smm_arguments;
    }

    public void addSmm_argument(Smm_argument smm_argument) {
        this.smm_arguments.add(smm_argument);
    }
    public List<smm_Measurement> getSmm_measurements() {
        return smm_measurements;
    }

    public void addSmm_measurement(Smm_measurement smm_measurement) {
        this.smm_measurements.add(smm_measurement);
    }
    public smm_Argument getSmm_argument() {
        return smm_argument;
    }

    public void setSmm_argument(smm_Argument smm_argument) {
        this.smm_argument = smm_argument;
    }
    public smm_Observation getSmm_observation() {
        return smm_observation;
    }

    public void setSmm_observation(smm_Observation smm_observation) {
        this.smm_observation = smm_observation;
    }
    public smm_Measurement getSmm_measurement() {
        return smm_measurement;
    }

    public void setSmm_measurement(smm_Measurement smm_measurement) {
        this.smm_measurement = smm_measurement;
    }

}