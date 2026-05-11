





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricRetentionRule extends Rule {

    private String period;
    private String intervalHint;



    public metrics_MetricRetentionRule(
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


}