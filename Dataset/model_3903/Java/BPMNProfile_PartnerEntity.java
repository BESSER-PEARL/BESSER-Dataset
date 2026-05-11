





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_PartnerEntity extends RootElement {






    private List<BPMNProfile_Participant> bpmnprofile_participants;




    private BPMNProfile_Participant bpmnprofile_participant;


    public BPMNProfile_PartnerEntity(
    ) {
        super(
        );
        this.bpmnprofile_participants = new ArrayList<>();
    }

    public BPMNProfile_PartnerEntity(
        ArrayList<BPMNProfile_Participant> bpmnprofile_participants    ) {
        this.bpmnprofile_participants = bpmnprofile_participants;
    }


    public List<BPMNProfile_Participant> getBpmnprofile_participants() {
        return bpmnprofile_participants;
    }

    public void addBpmnprofile_participant(Bpmnprofile_participant bpmnprofile_participant) {
        this.bpmnprofile_participants.add(bpmnprofile_participant);
    }
    public BPMNProfile_Participant getBpmnprofile_participant() {
        return bpmnprofile_participant;
    }

    public void setBpmnprofile_participant(BPMNProfile_Participant bpmnprofile_participant) {
        this.bpmnprofile_participant = bpmnprofile_participant;
    }

}