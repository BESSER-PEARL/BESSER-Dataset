





import java.util.List;
import java.util.ArrayList;

public class metrics_Metric extends Base {

    private String measurementKind;
    private String measurementPoint;
    private String description;
    private String name;





    private metrics_MetricSource metrics_metricsource;




    private List<metrics_Metric> metrics_metrics;




    private metrics_ValueDataKind metrics_valuedatakind;


    public metrics_Metric(
        String measurementKind,        String measurementPoint,        String description,        String name    ) {
        super(
        );
        this.measurementKind = measurementKind;
        this.measurementPoint = measurementPoint;
        this.description = description;
        this.name = name;
        this.metrics_metrics = new ArrayList<>();
    }

    public metrics_Metric(
        String measurementKind,        String measurementPoint,        String description,        String name        ArrayList<metrics_Metric> metrics_metrics    ) {
        this.measurementKind = measurementKind;
        this.measurementPoint = measurementPoint;
        this.description = description;
        this.name = name;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metrics_MetricSource getMetrics_metricsource() {
        return metrics_metricsource;
    }

    public void setMetrics_metricsource(metrics_MetricSource metrics_metricsource) {
        this.metrics_metricsource = metrics_metricsource;
    }
    public List<metrics_Metric> getMetrics_metrics() {
        return metrics_metrics;
    }

    public void addMetrics_metric(Metrics_metric metrics_metric) {
        this.metrics_metrics.add(metrics_metric);
    }
    public metrics_ValueDataKind getMetrics_valuedatakind() {
        return metrics_valuedatakind;
    }

    public void setMetrics_valuedatakind(metrics_ValueDataKind metrics_valuedatakind) {
        this.metrics_valuedatakind = metrics_valuedatakind;
    }

}