





import java.util.List;
import java.util.ArrayList;

public class iot2_Trace  {






    private List<iot2_ActivityNode> iot2_activitynodes;


    public iot2_Trace(
    ) {
        this.iot2_activitynodes = new ArrayList<>();
    }

    public iot2_Trace(
        ArrayList<iot2_ActivityNode> iot2_activitynodes    ) {
        this.iot2_activitynodes = iot2_activitynodes;
    }


    public List<iot2_ActivityNode> getIot2_activitynodes() {
        return iot2_activitynodes;
    }

    public void addIot2_activitynode(Iot2_activitynode iot2_activitynode) {
        this.iot2_activitynodes.add(iot2_activitynode);
    }

}