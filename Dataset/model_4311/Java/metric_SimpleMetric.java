





import java.util.List;
import java.util.ArrayList;

public class metric_SimpleMetric extends Metric {

    private String value;



    public metric_SimpleMetric(
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