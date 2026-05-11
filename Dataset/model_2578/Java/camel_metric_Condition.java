




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class camel_metric_Condition  {

    private String name;
    private String comparisonOperator;
    private float threshold;
    private LocalDate validity;



    public camel_metric_Condition(
        String name,        String comparisonOperator,        float threshold,        LocalDate validity    ) {
        this.name = name;
        this.comparisonOperator = comparisonOperator;
        this.threshold = threshold;
        this.validity = validity;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComparisonoperator() {
        return comparisonOperator;
    }

    public void setComparisonoperator(String comparisonOperator) {
        this.comparisonOperator = comparisonOperator;
    }
    public float getThreshold() {
        return threshold;
    }

    public void setThreshold(float threshold) {
        this.threshold = threshold;
    }
    public LocalDate getValidity() {
        return validity;
    }

    public void setValidity(LocalDate validity) {
        this.validity = validity;
    }


}