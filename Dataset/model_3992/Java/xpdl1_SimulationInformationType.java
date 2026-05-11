





import java.util.List;
import java.util.ArrayList;

public class xpdl1_SimulationInformationType  {

    private String instantiation;
    private String cost;





    private xpdl1_ActivityType xpdl1_activitytype;


    public xpdl1_SimulationInformationType(
        String instantiation,        String cost    ) {
        this.instantiation = instantiation;
        this.cost = cost;
    }


    public String getInstantiation() {
        return instantiation;
    }

    public void setInstantiation(String instantiation) {
        this.instantiation = instantiation;
    }
    public String getCost() {
        return cost;
    }

    public void setCost(String cost) {
        this.cost = cost;
    }

    public xpdl1_ActivityType getXpdl1_activitytype() {
        return xpdl1_activitytype;
    }

    public void setXpdl1_activitytype(xpdl1_ActivityType xpdl1_activitytype) {
        this.xpdl1_activitytype = xpdl1_activitytype;
    }

}