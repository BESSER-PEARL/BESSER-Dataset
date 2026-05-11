





import java.util.List;
import java.util.ArrayList;

public class cbpmn_DataObjectReference  {

    private int higherBound;
    private int lowerBound;
    private String name;





    private cbpmn_Activity cbpmn_activity;


    public cbpmn_DataObjectReference(
        int higherBound,        int lowerBound,        String name    ) {
        this.higherBound = higherBound;
        this.lowerBound = lowerBound;
        this.name = name;
    }


    public int getHigherbound() {
        return higherBound;
    }

    public void setHigherbound(int higherBound) {
        this.higherBound = higherBound;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cbpmn_Activity getCbpmn_activity() {
        return cbpmn_activity;
    }

    public void setCbpmn_activity(cbpmn_Activity cbpmn_activity) {
        this.cbpmn_activity = cbpmn_activity;
    }

}