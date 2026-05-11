





import java.util.List;
import java.util.ArrayList;

public class metrics_Metric  {

    private String metricCalculation;
    private String description;
    private String measurementKind;
    private String measurementPoint;
    private String name;
    private String unitRef;





    private metrics_Metric metrics_metric;


    public metrics_Metric(
        String metricCalculation,        String description,        String measurementKind,        String measurementPoint,        String name,        String unitRef    ) {
        this.metricCalculation = metricCalculation;
        this.description = description;
        this.measurementKind = measurementKind;
        this.measurementPoint = measurementPoint;
        this.name = name;
        this.unitRef = unitRef;
    }


    public String getMetriccalculation() {
        return metricCalculation;
    }

    public void setMetriccalculation(String metricCalculation) {
        this.metricCalculation = metricCalculation;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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
    public String getUnitref() {
        return unitRef;
    }

    public void setUnitref(String unitRef) {
        this.unitRef = unitRef;
    }

    public metrics_Metric getMetrics_metric() {
        return metrics_metric;
    }

    public void setMetrics_metric(metrics_Metric metrics_metric) {
        this.metrics_metric = metrics_metric;
    }

}