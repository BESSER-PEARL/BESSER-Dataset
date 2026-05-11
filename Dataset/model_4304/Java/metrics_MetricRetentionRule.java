





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricRetentionRule  {

    private String intervalHint;
    private String period;
    private String name;





    private metrics_Expression metrics_expression;


    public metrics_MetricRetentionRule(
        String intervalHint,        String period,        String name    ) {
        this.intervalHint = intervalHint;
        this.period = period;
        this.name = name;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metrics_Expression getMetrics_expression() {
        return metrics_expression;
    }

    public void setMetrics_expression(metrics_Expression metrics_expression) {
        this.metrics_expression = metrics_expression;
    }

}