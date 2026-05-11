





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_PartnerEntity extends RootElement {

    private String name;





    private List<BPMN2Model_Participant> bpmn2model_participants;


    public BPMN2Model_PartnerEntity(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2model_participants = new ArrayList<>();
    }

    public BPMN2Model_PartnerEntity(
        String name        ArrayList<BPMN2Model_Participant> bpmn2model_participants    ) {
        this.name = name;
        this.bpmn2model_participants = bpmn2model_participants;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<BPMN2Model_Participant> getBpmn2model_participants() {
        return bpmn2model_participants;
    }

    public void addBpmn2model_participant(Bpmn2model_participant bpmn2model_participant) {
        this.bpmn2model_participants.add(bpmn2model_participant);
    }

}