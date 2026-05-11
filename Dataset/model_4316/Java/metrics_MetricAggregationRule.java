





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricAggregationRule extends Rule {

    private String period;
    private String intervalHint;





    private metrics_MetricAggregationRules metrics_metricaggregationrules;


    public metrics_MetricAggregationRule(
        String period,        String intervalHint    ) {
        super(
        );
        this.period = period;
        this.intervalHint = intervalHint;
    }


    public String getPeriod() {
        return period;
    }

    public void setPeriod(String period) {
        this.period = period;
    }
    public String getIntervalhint() {
        return intervalHint;
    }

    public void setIntervalhint(String intervalHint) {
        this.intervalHint = intervalHint;
    }

    public metrics_MetricAggregationRules getMetrics_metricaggregationrules() {
        return metrics_metricaggregationrules;
    }

    public void setMetrics_metricaggregationrules(metrics_MetricAggregationRules metrics_metricaggregationrules) {
        this.metrics_metricaggregationrules = metrics_metricaggregationrules;
    }

}