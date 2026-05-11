





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ChoreographyTask extends ChoreographyActivity {






    private List<bpmn2_MessageFlow> bpmn2_messageflows;


    public bpmn2_ChoreographyTask(
    ) {
        super(
        );
        this.bpmn2_messageflows = new ArrayList<>();
    }

    public bpmn2_ChoreographyTask(
        ArrayList<bpmn2_MessageFlow> bpmn2_messageflows    ) {
        this.bpmn2_messageflows = bpmn2_messageflows;
    }


    public List<bpmn2_MessageFlow> getBpmn2_messageflows() {
        return bpmn2_messageflows;
    }

    public void addBpmn2_messageflow(Bpmn2_messageflow bpmn2_messageflow) {
        this.bpmn2_messageflows.add(bpmn2_messageflow);
    }

}