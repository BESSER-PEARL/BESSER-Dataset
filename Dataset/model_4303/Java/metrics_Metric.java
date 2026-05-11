





import java.util.List;
import java.util.ArrayList;

public class metrics_Metric extends Base {

    private String measurementKind;
    private String measurementPoint;
    private String name;
    private String description;





    private metrics_ValueDataKind metrics_valuedatakind;




    private List<metrics_Metric> metrics_metrics;


    public metrics_Metric(
        String measurementKind,        String measurementPoint,        String name,        String description    ) {
        super(
        );
        this.measurementKind = measurementKind;
        this.measurementPoint = measurementPoint;
        this.name = name;
        this.description = description;
        this.metrics_metrics = new ArrayList<>();
    }

    public metrics_Metric(
        String measurementKind,        String measurementPoint,        String name,        String description        ArrayList<metrics_Metric> metrics_metrics    ) {
        this.measurementKind = measurementKind;
        this.measurementPoint = measurementPoint;
        this.name = name;
        this.description = description;
        this.metrics_metrics = metrics_metrics;
    }

    public String getMeasurementkind() {
        return measurementKind;
    }

    public void setMeasurementkind(String measurementKind) {
        this.measurementKind = measurementKind;
    }
    public String getMeasurementpoint() {
        return measurementPoint;
    }

    public void setMeasurementpoint(String measurementPoint) {
        this.measurementPoint = measurementPoint;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public metrics_ValueDataKind getMetrics_valuedatakind() {
        return metrics_valuedatakind;
    }

    public void setMetrics_valuedatakind(metrics_ValueDataKind metrics_valuedatakind) {
        this.metrics_valuedatakind = metrics_valuedatakind;
    }
    public List<metrics_Metric> getMetrics_metrics() {
        return metrics_metrics;
    }

    public void addMetrics_metric(Metrics_metric metrics_metric) {
        this.metrics_metrics.add(metrics_metric);
    }

}