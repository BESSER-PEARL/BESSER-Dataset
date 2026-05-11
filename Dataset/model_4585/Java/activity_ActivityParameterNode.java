





import java.util.List;
import java.util.ArrayList;

public class activity_ActivityParameterNode extends Activity {

    private String name;





    private List<activity_ActivityNode> activity_activitynodes;




    private activity_Activity activity_activity;


    public activity_ActivityParameterNode(
        String name    ) {
        super(
        );
        this.name = name;
        this.activity_activitynodes = new ArrayList<>();
    }

    public activity_ActivityParameterNode(
        String name        ArrayList<activity_ActivityNode> activity_activitynodes    ) {
        this.name = name;
        this.activity_activitynodes = activity_activitynodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<activity_ActivityNode> getActivity_activitynodes() {
        return activity_activitynodes;
    }

    public void addActivity_activitynode(Activity_activitynode activity_activitynode) {
        this.activity_activitynodes.add(activity_activitynode);
    }
    public activity_Activity getActivity_activity() {
        return activity_activity;
    }

    public void setActivity_activity(activity_Activity activity_activity) {
        this.activity_activity = activity_activity;
    }

}