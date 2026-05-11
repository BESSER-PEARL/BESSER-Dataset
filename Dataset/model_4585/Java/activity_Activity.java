





import java.util.List;
import java.util.ArrayList;

public class activity_Activity  {






    private List<activity_ActivityNode> activity_activitynodes;


    public activity_Activity(
    ) {
        this.activity_activitynodes = new ArrayList<>();
    }

    public activity_Activity(
        ArrayList<activity_ActivityNode> activity_activitynodes    ) {
        this.activity_activitynodes = activity_activitynodes;
    }


    public List<activity_ActivityNode> getActivity_activitynodes() {
        return activity_activitynodes;
    }

    public void addActivity_activitynode(Activity_activitynode activity_activitynode) {
        this.activity_activitynodes.add(activity_activitynode);
    }

}