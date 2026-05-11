





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_ChoreographyTask extends ChoreographyActivity {






    private List<BPMN2Model_MessageFlow> bpmn2model_messageflows;


    public BPMN2Model_ChoreographyTask(
    ) {
        super(
        );
        this.bpmn2model_messageflows = new ArrayList<>();
    }

    public BPMN2Model_ChoreographyTask(
        ArrayList<BPMN2Model_MessageFlow> bpmn2model_messageflows    ) {
        this.bpmn2model_messageflows = bpmn2model_messageflows;
    }


    public List<BPMN2Model_MessageFlow> getBpmn2model_messageflows() {
        return bpmn2model_messageflows;
    }

    public void addBpmn2model_messageflow(Bpmn2model_messageflow bpmn2model_messageflow) {
        this.bpmn2model_messageflows.add(bpmn2model_messageflow);
    }

}