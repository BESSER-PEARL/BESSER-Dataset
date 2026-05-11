





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ActivitiesType  {






    private xpdl1_ActivitySetType xpdl1_activitysettype;




    private List<xpdl1_ActivityType> xpdl1_activitytypes;


    public xpdl1_ActivitiesType(
    ) {
        this.xpdl1_activitytypes = new ArrayList<>();
    }

    public xpdl1_ActivitiesType(
        ArrayList<xpdl1_ActivityType> xpdl1_activitytypes    ) {
        this.xpdl1_activitytypes = xpdl1_activitytypes;
    }


    public xpdl1_ActivitySetType getXpdl1_activitysettype() {
        return xpdl1_activitysettype;
    }

    public void setXpdl1_activitysettype(xpdl1_ActivitySetType xpdl1_activitysettype) {
        this.xpdl1_activitysettype = xpdl1_activitysettype;
    }
    public List<xpdl1_ActivityType> getXpdl1_activitytypes() {
        return xpdl1_activitytypes;
    }

    public void addXpdl1_activitytype(Xpdl1_activitytype xpdl1_activitytype) {
        this.xpdl1_activitytypes.add(xpdl1_activitytype);
    }

}