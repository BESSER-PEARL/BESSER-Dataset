





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricLibrary  {

    private String name;





    private List<metrics_MetricSource> metrics_metricsources;


    public metrics_MetricLibrary(
        String name    ) {
        this.name = name;
        this.metrics_metricsources = new ArrayList<>();
    }

    public metrics_MetricLibrary(
        String name        ArrayList<metrics_MetricSource> metrics_metricsources    ) {
        this.name = name;
        this.metrics_metricsources = metrics_metricsources;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<metrics_MetricSource> getMetrics_metricsources() {
        return metrics_metricsources;
    }

    public void addMetrics_metricsource(Metrics_metricsource metrics_metricsource) {
        this.metrics_metricsources.add(metrics_metricsource);
    }

}