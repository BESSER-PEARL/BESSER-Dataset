





import java.util.List;
import java.util.ArrayList;

public class Metrics_StringMetricValue extends MetricValue {

    private String value;



    public Metrics_StringMetricValue(
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