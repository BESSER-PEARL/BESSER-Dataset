





import java.util.List;
import java.util.ArrayList;

public class bpmn2_PartnerEntity extends RootElement {






    private bpmn2_DocumentRoot bpmn2_documentroot;




    private List<bpmn2_Participant> bpmn2_participants;


    public bpmn2_PartnerEntity(
    ) {
        super(
        );
        this.bpmn2_participants = new ArrayList<>();
    }

    public bpmn2_PartnerEntity(
        ArrayList<bpmn2_Participant> bpmn2_participants    ) {
        this.bpmn2_participants = bpmn2_participants;
    }


    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public List<bpmn2_Participant> getBpmn2_participants() {
        return bpmn2_participants;
    }

    public void addBpmn2_participant(Bpmn2_participant bpmn2_participant) {
        this.bpmn2_participants.add(bpmn2_participant);
    }

}