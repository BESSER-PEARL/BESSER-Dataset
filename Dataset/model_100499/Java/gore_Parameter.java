





import java.util.List;
import java.util.ArrayList;

public class gore_Parameter  {

    private String unit;
    private String metric;
    private String value;
    private String type;





    private gore_Configuration gore_configuration;




    private gore_Configuration gore_configuration;


    public gore_Parameter(
        String unit,        String metric,        String value,        String type    ) {
        this.unit = unit;
        this.metric = metric;
        this.value = value;
        this.type = type;
    }


    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
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

    public gore_Configuration getGore_configuration() {
        return gore_configuration;
    }

    public void setGore_configuration(gore_Configuration gore_configuration) {
        this.gore_configuration = gore_configuration;
    }
    public gore_Configuration getGore_configuration() {
        return gore_configuration;
    }

    public void setGore_configuration(gore_Configuration gore_configuration) {
        this.gore_configuration = gore_configuration;
    }

}