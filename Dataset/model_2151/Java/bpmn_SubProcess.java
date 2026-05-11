





import java.util.List;
import java.util.ArrayList;

public class bpmn_SubProcess extends Graph, Activity {

    private String isTransaction;





    private List<bpmn_Activity> bpmn_activitys;




    private bpmn_Activity bpmn_activity;


    public bpmn_SubProcess(
        String isTransaction    ) {
        super(
        );
        this.isTransaction = isTransaction;
        this.bpmn_activitys = new ArrayList<>();
    }

    public bpmn_SubProcess(
        String isTransaction        ArrayList<bpmn_Activity> bpmn_activitys    ) {
        this.isTransaction = isTransaction;
        this.bpmn_activitys = bpmn_activitys;
    }

    public String getIstransaction() {
        return isTransaction;
    }

    public void setIstransaction(String isTransaction) {
        this.isTransaction = isTransaction;
    }

    public List<bpmn_Activity> getBpmn_activitys() {
        return bpmn_activitys;
    }

    public void addBpmn_activity(Bpmn_activity bpmn_activity) {
        this.bpmn_activitys.add(bpmn_activity);
    }
    public bpmn_Activity getBpmn_activity() {
        return bpmn_activity;
    }

    public void setBpmn_activity(bpmn_Activity bpmn_activity) {
        this.bpmn_activity = bpmn_activity;
    }

}