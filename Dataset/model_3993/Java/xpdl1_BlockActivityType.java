





import java.util.List;
import java.util.ArrayList;

public class xpdl1_BlockActivityType  {

    private String blockId;





    private xpdl1_ActivityType xpdl1_activitytype;


    public xpdl1_BlockActivityType(
        String blockId    ) {
        this.blockId = blockId;
    }


    public String getBlockid() {
        return blockId;
    }

    public void setBlockid(String blockId) {
        this.blockId = blockId;
    }

    public xpdl1_ActivityType getXpdl1_activitytype() {
        return xpdl1_activitytype;
    }

    public void setXpdl1_activitytype(xpdl1_ActivityType xpdl1_activitytype) {
        this.xpdl1_activitytype = xpdl1_activitytype;
    }

}