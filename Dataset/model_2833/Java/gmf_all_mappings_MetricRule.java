





import java.util.List;
import java.util.ArrayList;

public class gmf_all_mappings_MetricRule extends RuleBase {

    private String key;
    private String lowLimit;
    private String highLimit;





    private ValueExpression valueexpression;




    private MetricContainer metriccontainer;


    public gmf_all_mappings_MetricRule(
        String key,        String lowLimit,        String highLimit    ) {
        super(
        );
        this.key = key;
        this.lowLimit = lowLimit;
        this.highLimit = highLimit;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getLowlimit() {
        return lowLimit;
    }

    public void setLowlimit(String lowLimit) {
        this.lowLimit = lowLimit;
    }
    public String getHighlimit() {
        return highLimit;
    }

    public void setHighlimit(String highLimit) {
        this.highLimit = highLimit;
    }

    public ValueExpression getValueexpression() {
        return valueexpression;
    }

    public void setValueexpression(ValueExpression valueexpression) {
        this.valueexpression = valueexpression;
    }
    public MetricContainer getMetriccontainer() {
        return metriccontainer;
    }

    public void setMetriccontainer(MetricContainer metriccontainer) {
        this.metriccontainer = metriccontainer;
    }

}