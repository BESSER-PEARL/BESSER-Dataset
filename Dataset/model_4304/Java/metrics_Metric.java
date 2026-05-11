





import java.util.List;
import java.util.ArrayList;

public class metrics_Metric extends Base {

    private String measurementPoint;
    private String measurementKind;
    private String description;
    private String name;





    private metrics_MetricSource metrics_metricsource;




    private metrics_ValueDataKind metrics_valuedatakind;




    private List<metrics_Metric> metrics_metrics;


    public metrics_Metric(
        String measurementPoint,        String measurementKind,        String description,        String name    ) {
        super(
        );
        this.measurementPoint = measurementPoint;
        this.measurementKind = measurementKind;
        this.description = description;
        this.name = name;
        this.metrics_metrics = new ArrayList<>();
    }

    public metrics_Metric(
        String measurementPoint,        String measurementKind,        String description,        String name        ArrayList<metrics_Metric> metrics_metrics    ) {
        this.measurementPoint = measurementPoint;
        this.measurementKind = measurementKind;
        this.description = description;
        this.name = name;
        this.metrics_metrics = metrics_metrics;
    }

    public String getMeasurementpoint() {
        return measurementPoint;
    }

    public void setMeasurementpoint(String measurementPoint) {
        this.measurementPoint = measurementPoint;
    }
    public String getMeasurementkind() {
        return measurementKind;
    }

    public void setMeasurementkind(String measurementKind) {
        this.measurementKind = measurementKind;
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