





import java.util.List;
import java.util.ArrayList;

public class Metrics_BooleanMetricValue extends MetricValue {

    private String value;



    public Metrics_BooleanMetricValue(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}