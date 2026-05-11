





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ChoreographyActivity extends FlowNode {

    private String loopType;





    private List<bpmn2_CorrelationKey> bpmn2_correlationkeys;




    private List<bpmn2_Participant> bpmn2_participants;




    private bpmn2_Participant bpmn2_participant;


    public bpmn2_ChoreographyActivity(
        String loopType    ) {
        super(
        );
        this.loopType = loopType;
        this.bpmn2_correlationkeys = new ArrayList<>();
        this.bpmn2_participants = new ArrayList<>();
    }

    public bpmn2_ChoreographyActivity(
        String loopType        ArrayList<bpmn2_CorrelationKey> bpmn2_correlationkeys,        ArrayList<bpmn2_Participant> bpmn2_participants    ) {
        this.loopType = loopType;
        this.bpmn2_correlationkeys = bpmn2_correlationkeys;
        this.bpmn2_participants = bpmn2_participants;
    }

    public String getLooptype() {
        return loopType;
    }

    public void setLooptype(String loopType) {
        this.loopType = loopType;
    }

    public List<bpmn2_CorrelationKey> getBpmn2_correlationkeys() {
        return bpmn2_correlationkeys;
    }

    public void addBpmn2_correlationkey(Bpmn2_correlationkey bpmn2_correlationkey) {
        this.bpmn2_correlationkeys.add(bpmn2_correlationkey);
    }
    public List<bpmn2_Participant> getBpmn2_participants() {
        return bpmn2_participants;
    }

    public void addBpmn2_participant(Bpmn2_participant bpmn2_participant) {
        this.bpmn2_participants.add(bpmn2_participant);
    }
    public bpmn2_Participant getBpmn2_participant() {
        return bpmn2_participant;
    }

    public void setBpmn2_participant(bpmn2_Participant bpmn2_participant) {
        this.bpmn2_participant = bpmn2_participant;
    }

}