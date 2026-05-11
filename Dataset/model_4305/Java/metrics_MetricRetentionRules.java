





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricRetentionRules  {






    private List<metrics_MetricRetentionRule> metrics_metricretentionrules;


    public metrics_MetricRetentionRules(
    ) {
        this.metrics_metricretentionrules = new ArrayList<>();
    }

    public metrics_MetricRetentionRules(
        ArrayList<metrics_MetricRetentionRule> metrics_metricretentionrules    ) {
        this.metrics_metricretentionrules = metrics_metricretentionrules;
    }


    public List<metrics_MetricRetentionRule> getMetrics_metricretentionrules() {
        return metrics_metricretentionrules;
    }

    public void addMetrics_metricretentionrule(Metrics_metricretentionrule metrics_metricretentionrule) {
        this.metrics_metricretentionrules.add(metrics_metricretentionrule);
    }

}