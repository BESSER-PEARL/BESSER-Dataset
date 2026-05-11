





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_ChoreographyActivity extends FlowNode {

    private String loopType;





    private List<BPMN2Model_Participant> bpmn2model_participants;




    private BPMN2Model_Participant bpmn2model_participant;


    public BPMN2Model_ChoreographyActivity(
        String loopType    ) {
        super(
        );
        this.loopType = loopType;
        this.bpmn2model_participants = new ArrayList<>();
    }

    public BPMN2Model_ChoreographyActivity(
        String loopType        ArrayList<BPMN2Model_Participant> bpmn2model_participants    ) {
        this.loopType = loopType;
        this.bpmn2model_participants = bpmn2model_participants;
    }

    public String getLooptype() {
        return loopType;
    }

    public void setLooptype(String loopType) {
        this.loopType = loopType;
    }

    public List<BPMN2Model_Participant> getBpmn2model_participants() {
        return bpmn2model_participants;
    }

    public void addBpmn2model_participant(Bpmn2model_participant bpmn2model_participant) {
        this.bpmn2model_participants.add(bpmn2model_participant);
    }
    public BPMN2Model_Participant getBpmn2model_participant() {
        return bpmn2model_participant;
    }

    public void setBpmn2model_participant(BPMN2Model_Participant bpmn2model_participant) {
        this.bpmn2model_participant = bpmn2model_participant;
    }

}