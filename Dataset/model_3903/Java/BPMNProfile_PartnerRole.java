





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_PartnerRole extends RootElement {






    private BPMNProfile_Participant bpmnprofile_participant;




    private List<BPMNProfile_Participant> bpmnprofile_participants;




    private BPMNProfile_Class bpmnprofile_class;


    public BPMNProfile_PartnerRole(
    ) {
        super(
        );
        this.bpmnprofile_participants = new ArrayList<>();
    }

    public BPMNProfile_PartnerRole(
        ArrayList<BPMNProfile_Participant> bpmnprofile_participants    ) {
        this.bpmnprofile_participants = bpmnprofile_participants;
    }


    public BPMNProfile_Participant getBpmnprofile_participant() {
        return bpmnprofile_participant;
    }

    public void setBpmnprofile_participant(BPMNProfile_Participant bpmnprofile_participant) {
        this.bpmnprofile_participant = bpmnprofile_participant;
    }
    public List<BPMNProfile_Participant> getBpmnprofile_participants() {
        return bpmnprofile_participants;
    }

    public void addBpmnprofile_participant(Bpmnprofile_participant bpmnprofile_participant) {
        this.bpmnprofile_participants.add(bpmnprofile_participant);
    }
    public BPMNProfile_Class getBpmnprofile_class() {
        return bpmnprofile_class;
    }

    public void setBpmnprofile_class(BPMNProfile_Class bpmnprofile_class) {
        this.bpmnprofile_class = bpmnprofile_class;
    }

}