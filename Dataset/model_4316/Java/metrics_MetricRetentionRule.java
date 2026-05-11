





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricRetentionRule extends Rule {

    private String intervalHint;
    private String period;





    private metrics_MetricRetentionRules metrics_metricretentionrules;


    public metrics_MetricRetentionRule(
        String intervalHint,        String period    ) {
        super(
        );
        this.intervalHint = intervalHint;
        this.period = period;
    }


    public String getIntervalhint() {
        return intervalHint;
    }

    public void setIntervalhint(String intervalHint) {
        this.intervalHint = intervalHint;
    }
    public String getPeriod() {
        return period;
    }

    public void setPeriod(String period) {
        this.period = period;
    }

    public metrics_MetricRetentionRules getMetrics_metricretentionrules() {
        return metrics_metricretentionrules;
    }

    public void setMetrics_metricretentionrules(metrics_MetricRetentionRules metrics_metricretentionrules) {
        this.metrics_metricretentionrules = metrics_metricretentionrules;
    }

}