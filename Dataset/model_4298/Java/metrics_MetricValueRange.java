





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricValueRange  {

    private String name;
    private String periodHint;
    private String kindHint;





    private List<metrics_Value> metrics_values;


    public metrics_MetricValueRange(
        String name,        String periodHint,        String kindHint    ) {
        this.name = name;
        this.periodHint = periodHint;
        this.kindHint = kindHint;
        this.metrics_values = new ArrayList<>();
    }

    public metrics_MetricValueRange(
        String name,        String periodHint,        String kindHint        ArrayList<metrics_Value> metrics_values    ) {
        this.name = name;
        this.periodHint = periodHint;
        this.kindHint = kindHint;
        this.metrics_values = metrics_values;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPeriodhint() {
        return periodHint;
    }

    public void setPeriodhint(String periodHint) {
        this.periodHint = periodHint;
    }
    public String getKindhint() {
        return kindHint;
    }

    public void setKindhint(String kindHint) {
        this.kindHint = kindHint;
    }

    public List<metrics_Value> getMetrics_values() {
        return metrics_values;
    }

    public void addMetrics_value(Metrics_value metrics_value) {
        this.metrics_values.add(metrics_value);
    }

}