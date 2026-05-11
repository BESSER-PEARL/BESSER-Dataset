





import java.util.List;
import java.util.ArrayList;

public class metrics_ComplexMeasurement extends Measurement {






    private List<metrics_Measurement> metrics_measurements;


    public metrics_ComplexMeasurement(
    ) {
        super(
        );
        this.metrics_measurements = new ArrayList<>();
    }

    public metrics_ComplexMeasurement(
        ArrayList<metrics_Measurement> metrics_measurements    ) {
        this.metrics_measurements = metrics_measurements;
    }


    public List<metrics_Measurement> getMetrics_measurements() {
        return metrics_measurements;
    }

    public void addMetrics_measurement(Metrics_measurement metrics_measurement) {
        this.metrics_measurements.add(metrics_measurement);
    }

}