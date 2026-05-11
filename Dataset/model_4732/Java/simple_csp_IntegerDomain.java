





import java.util.List;
import java.util.ArrayList;

public class simple_csp_IntegerDomain extends Domain {

    private String maxValue;
    private String minValue;



    public simple_csp_IntegerDomain(
        String maxValue,        String minValue    ) {
        super(
        );
        this.maxValue = maxValue;
        this.minValue = minValue;
    }


    public String getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(String maxValue) {
        this.maxValue = maxValue;
    }
    public String getMinvalue() {
        return minValue;
    }

    public void setMinvalue(String minValue) {
        this.minValue = minValue;
    }


}