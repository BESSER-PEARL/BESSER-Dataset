





import java.util.List;
import java.util.ArrayList;

public class Metrics_IntegerMetricValue extends MetricValue {

    private String value;



    public Metrics_IntegerMetricValue(
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