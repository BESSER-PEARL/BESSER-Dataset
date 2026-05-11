





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricRetentionRule  {

    private String name;
    private String period;
    private String intervalHint;





    private metrics_Expression metrics_expression;


    public metrics_MetricRetentionRule(
        String name,        String period,        String intervalHint    ) {
        this.name = name;
        this.period = period;
        this.intervalHint = intervalHint;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public metrics_Expression getMetrics_expression() {
        return metrics_expression;
    }

    public void setMetrics_expression(metrics_Expression metrics_expression) {
        this.metrics_expression = metrics_expression;
    }

}