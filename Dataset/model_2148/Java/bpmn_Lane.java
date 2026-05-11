





import java.util.List;
import java.util.ArrayList;

public class bpmn_Lane extends NamedBpmnObject, AssociationTarget {






    private bpmn_Pool bpmn_pool;




    private bpmn_Activity bpmn_activity;




    private bpmn_Pool bpmn_pool;




    private List<bpmn_Activity> bpmn_activitys;


    public bpmn_Lane(
    ) {
        super(
        );
        this.bpmn_activitys = new ArrayList<>();
    }

    public bpmn_Lane(
        ArrayList<bpmn_Activity> bpmn_activitys    ) {
        this.bpmn_activitys = bpmn_activitys;
    }


    public bpmn_Pool getBpmn_pool() {
        return bpmn_pool;
    }

    public void setBpmn_pool(bpmn_Pool bpmn_pool) {
        this.bpmn_pool = bpmn_pool;
    }
    public bpmn_Activity getBpmn_activity() {
        return bpmn_activity;
    }

    public void setBpmn_activity(bpmn_Activity bpmn_activity) {
        this.bpmn_activity = bpmn_activity;
    }
    public bpmn_Pool getBpmn_pool() {
        return bpmn_pool;
    }

    public void setBpmn_pool(bpmn_Pool bpmn_pool) {
        this.bpmn_pool = bpmn_pool;
    }
    public List<bpmn_Activity> getBpmn_activitys() {
        return bpmn_activitys;
    }

    public void addBpmn_activity(Bpmn_activity bpmn_activity) {
        this.bpmn_activitys.add(bpmn_activity);
    }

}