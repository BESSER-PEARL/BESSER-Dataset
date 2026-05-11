





import java.util.List;
import java.util.ArrayList;

public class bpmn2_PartnerRole extends RootElement {

    private String name;





    private List<bpmn2_Participant> bpmn2_participants;


    public bpmn2_PartnerRole(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_participants = new ArrayList<>();
    }

    public bpmn2_PartnerRole(
        String name        ArrayList<bpmn2_Participant> bpmn2_participants    ) {
        this.name = name;
        this.bpmn2_participants = bpmn2_participants;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<bpmn2_Participant> getBpmn2_participants() {
        return bpmn2_participants;
    }

    public void addBpmn2_participant(Bpmn2_participant bpmn2_participant) {
        this.bpmn2_participants.add(bpmn2_participant);
    }

}