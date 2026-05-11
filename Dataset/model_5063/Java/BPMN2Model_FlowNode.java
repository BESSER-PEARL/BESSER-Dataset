





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_FlowNode extends FlowElement {






    private List<BPMN2Model_SequenceFlow> bpmn2model_sequenceflows;




    private List<BPMN2Model_Lane> bpmn2model_lanes;




    private BPMN2Model_SequenceFlow bpmn2model_sequenceflow;




    private BPMN2Model_SequenceFlow bpmn2model_sequenceflow;




    private BPMN2Model_Lane bpmn2model_lane;




    private List<BPMN2Model_SequenceFlow> bpmn2model_sequenceflows;


    public BPMN2Model_FlowNode(
    ) {
        super(
        );
        this.bpmn2model_sequenceflows = new ArrayList<>();
        this.bpmn2model_lanes = new ArrayList<>();
        this.bpmn2model_sequenceflows = new ArrayList<>();
    }

    public BPMN2Model_FlowNode(
        ArrayList<BPMN2Model_SequenceFlow> bpmn2model_sequenceflows,        ArrayList<BPMN2Model_Lane> bpmn2model_lanes,        ArrayList<BPMN2Model_SequenceFlow> bpmn2model_sequenceflows    ) {
        this.bpmn2model_sequenceflows = bpmn2model_sequenceflows;
        this.bpmn2model_lanes = bpmn2model_lanes;
        this.bpmn2model_sequenceflows = bpmn2model_sequenceflows;
    }


    public List<BPMN2Model_SequenceFlow> getBpmn2model_sequenceflows() {
        return bpmn2model_sequenceflows;
    }

    public void addBpmn2model_sequenceflow(Bpmn2model_sequenceflow bpmn2model_sequenceflow) {
        this.bpmn2model_sequenceflows.add(bpmn2model_sequenceflow);
    }
    public List<BPMN2Model_Lane> getBpmn2model_lanes() {
        return bpmn2model_lanes;
    }

    public void addBpmn2model_lane(Bpmn2model_lane bpmn2model_lane) {
        this.bpmn2model_lanes.add(bpmn2model_lane);
    }
    public BPMN2Model_SequenceFlow getBpmn2model_sequenceflow() {
        return bpmn2model_sequenceflow;
    }

    public void setBpmn2model_sequenceflow(BPMN2Model_SequenceFlow bpmn2model_sequenceflow) {
        this.bpmn2model_sequenceflow = bpmn2model_sequenceflow;
    }
    public BPMN2Model_SequenceFlow getBpmn2model_sequenceflow() {
        return bpmn2model_sequenceflow;
    }

    public void setBpmn2model_sequenceflow(BPMN2Model_SequenceFlow bpmn2model_sequenceflow) {
        this.bpmn2model_sequenceflow = bpmn2model_sequenceflow;
    }
    public BPMN2Model_Lane getBpmn2model_lane() {
        return bpmn2model_lane;
    }

    public void setBpmn2model_lane(BPMN2Model_Lane bpmn2model_lane) {
        this.bpmn2model_lane = bpmn2model_lane;
    }
    public List<BPMN2Model_SequenceFlow> getBpmn2model_sequenceflows() {
        return bpmn2model_sequenceflows;
    }

    public void addBpmn2model_sequenceflow(Bpmn2model_sequenceflow bpmn2model_sequenceflow) {
        this.bpmn2model_sequenceflows.add(bpmn2model_sequenceflow);
    }

}