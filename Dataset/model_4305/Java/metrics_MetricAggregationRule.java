





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricAggregationRule extends Rule {






    private metrics_MetricAggregationRules metrics_metricaggregationrules;




    private metrics_Expression metrics_expression;


    public metrics_MetricAggregationRule(
    ) {
        super(
        );
    }



    public metrics_MetricAggregationRules getMetrics_metricaggregationrules() {
        return metrics_metricaggregationrules;
    }

    public void setMetrics_metricaggregationrules(metrics_MetricAggregationRules metrics_metricaggregationrules) {
        this.metrics_metricaggregationrules = metrics_metricaggregationrules;
    }
    public metrics_Expression getMetrics_expression() {
        return metrics_expression;
    }

    public void setMetrics_expression(metrics_Expression metrics_expression) {
        this.metrics_expression = metrics_expression;
    }

}