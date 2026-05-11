





import java.util.List;
import java.util.ArrayList;

public class dSLPolicies_StopCondition  {

    private int value;
    private String pathtype;
    private String percentage;



    public dSLPolicies_StopCondition(
        int value,        String pathtype,        String percentage    ) {
        this.value = value;
        this.pathtype = pathtype;
        this.percentage = percentage;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getPathtype() {
        return pathtype;
    }

    public void setPathtype(String pathtype) {
        this.pathtype = pathtype;
    }
    public String getPercentage() {
        return percentage;
    }

    public void setPercentage(String percentage) {
        this.percentage = percentage;
    }


}