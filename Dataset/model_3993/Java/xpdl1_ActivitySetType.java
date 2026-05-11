





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ActivitySetType  {

    private String id;





    private xpdl1_ActivitySetsType xpdl1_activitysetstype;




    private xpdl1_ActivitiesType xpdl1_activitiestype;


    public xpdl1_ActivitySetType(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public xpdl1_ActivitySetsType getXpdl1_activitysetstype() {
        return xpdl1_activitysetstype;
    }

    public void setXpdl1_activitysetstype(xpdl1_ActivitySetsType xpdl1_activitysetstype) {
        this.xpdl1_activitysetstype = xpdl1_activitysetstype;
    }
    public xpdl1_ActivitiesType getXpdl1_activitiestype() {
        return xpdl1_activitiestype;
    }

    public void setXpdl1_activitiestype(xpdl1_ActivitiesType xpdl1_activitiestype) {
        this.xpdl1_activitiestype = xpdl1_activitiestype;
    }

}