





import java.util.List;
import java.util.ArrayList;

public class gore_Parameter  {

    private String metric;
    private String value;
    private String type;
    private String unit;



    public gore_Parameter(
        String metric,        String value,        String type,        String unit    ) {
        this.metric = metric;
        this.value = value;
        this.type = type;
        this.unit = unit;
    }


    public String getMetric() {
        return metric;
    }

    public void setMetric(String metric) {
        this.metric = metric;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}